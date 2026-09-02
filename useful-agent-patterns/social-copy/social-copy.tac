--[[
Social Copy — paste-ready posts for anth.us articles

Publicist invokes this procedure to draft three independent social posts from
article context. One stateful copywriter Agent takes three sequential turns on
the same conversation so each turn sees prior options.

Run:
  tactus run useful-agent-patterns/social-copy/social-copy.tac \
    --param url="https://anth.us/blog/bugonomics-cheap-exploits-2026/" \
    --param channel=x \
    --param card_title="Bugonomics" \
    --param card_dek="When breaking software gets as cheap as writing it, cheaper offense means more offense." \
    --param rejected_takes='["When breaking software gets as cheap as writing it..."]'

Test (CI):
  tactus test useful-agent-patterns/social-copy/social-copy.tac --mock
]]--

-- Copy rules live in the agent prompt (not as slogans the model can parrot).
local COPY_RULES = [[
You write social posts for Ryan Alyn Porter (anth.us): dry, specific, technical essays.
Plain English. Sounds like a person, not a brand.

Hard rules:
- The post must stand alone if the link preview never loads. The card already has title + dek; do not echo them.
- Do not restate the preview/dek or polish a failed take from the rejected list.
- No marketing jargon: cheap offense, privileged identity, blast radius, NHI, "the path."
- No riddles. If you name a product or incident, give strangers the chain they need.
- No "I wrote a piece about…" unless the caller explicitly asks for that frame.
- Each post is paste-ready: body text with the article URL once at the end.
- Return only the post text. No labels ("Option 1"), no preamble, no fourth alternative.
]]

copywriter = Agent {
    model = "openai/gpt-5-mini",
    model_type = "responses",
    max_tokens = 16000,
    reasoning_effort = "medium",
    system_prompt = COPY_RULES,
}

local function trim(text)
    if text == nil then
        return ""
    end
    return (tostring(text):gsub("^%s+", ""):gsub("%s+$", ""))
end

local function ensure_url(post, url)
    local body = trim(post)
    local link = trim(url)
    if body == "" or link == "" then
        return body
    end
    if body:find(link, 1, true) then
        return body
    end
    return body .. "\n\n" .. link
end

local function normalize_channel(channel)
    local value = trim(channel):lower()
    if value == "x" or value == "twitter" then
        return "x"
    end
    if value == "linkedin" then
        return "linkedin"
    end
    return nil
end

local function channel_hint(channel)
    if channel == "x" then
        return "Write for X: tight, one or two short paragraphs max. No thread numbering."
    end
    return "Write for LinkedIn: still concise; one or two short paragraphs, not a press release."
end

local function format_rejected(rejected)
    if rejected == nil or type(rejected) ~= "table" or #rejected == 0 then
        return "(none provided)"
    end
    local lines = {}
    for i = 1, #rejected do
        local take = trim(rejected[i])
        if take ~= "" then
            table.insert(lines, "- " .. take)
        end
    end
    if #lines == 0 then
        return "(none provided)"
    end
    return table.concat(lines, "\n")
end

local function article_block(excerpt, card_title, card_dek, url)
    local body = trim(excerpt)
    if body ~= "" then
        return body
    end
    return table.concat({
        "No article_excerpt was provided. Tactus cannot fetch the live URL in this procedure;",
        "work from the card metadata and your training knowledge only.",
        "Do not claim you read the page.",
        "URL for reference (append at end of post, do not summarize the URL itself): " .. trim(url),
        "Card title (do not echo): " .. trim(card_title),
        "Card dek (do not echo): " .. trim(card_dek),
    }, "\n")
end

local function extract_post(result)
    if result == nil then
        return ""
    end
    if type(result) == "string" then
        return trim(result)
    end
    if type(result) == "table" then
        if result.output ~= nil and tostring(result.output) ~= "" then
            return trim(result.output)
        end
        if result.response ~= nil and tostring(result.response) ~= "" then
            return trim(result.response)
        end
        if result.message ~= nil and tostring(result.message) ~= "" then
            return trim(result.message)
        end
    end
    return trim(tostring(result))
end

local function dek_echoes(post, dek)
    local normalized_post = trim(post):lower()
    local normalized_dek = trim(dek):lower()
    if normalized_dek == "" or normalized_post == "" then
        return false
    end
    if normalized_post:find(normalized_dek, 1, true) then
        return true
    end
    -- Flag long overlapping phrases from the dek (rough restatement check).
    local words = {}
    for word in normalized_dek:gmatch("%S+") do
        if #word > 4 then
            table.insert(words, word)
        end
    end
    if #words < 4 then
        return false
    end
    local chunk = table.concat(words, " ", 1, math.min(6, #words))
    return normalized_post:find(chunk, 1, true) ~= nil
end

local function collect_dropped_reasons(options, dek, rejected)
    local reasons = {}
    for i = 1, 3 do
        local post = options[i] or ""
        if post == "" then
            table.insert(reasons, "option_" .. i .. ": empty post from agent")
        end
        if dek_echoes(post, dek) then
            table.insert(reasons, "option_" .. i .. ": may echo card dek (manual review)")
        end
    end
    if rejected ~= nil and type(rejected) == "table" then
        for i = 1, #rejected do
            local bad = trim(rejected[i])
            if bad ~= "" then
                for j = 1, 3 do
                    local post = (options[j] or ""):lower()
                    if post:find(bad:lower(), 1, true) then
                        table.insert(reasons, "option_" .. j .. ": overlaps rejected_take")
                    end
                end
            end
        end
    end
    return reasons
end

Procedure {
    input = {
        url = field.string{required = true, description = "Article URL (appended once per post)"},
        channel = field.string{required = true, description = "x or linkedin"},
        card_title = field.string{required = true, description = "Link preview title (do not echo)"},
        card_dek = field.string{required = true, description = "Link preview dek (do not echo)"},
        article_excerpt = field.string{
            required = false,
            default = "",
            description = "Optional article body excerpt from Publicist",
        },
        rejected_takes = field.array{
            required = false,
            default = {},
            description = "Prior failed posts to avoid",
        },
    },
    output = {
        option_1 = field.string{required = true},
        option_2 = field.string{required = true},
        option_3 = field.string{required = true},
        dropped_reasons = field.array{required = false},
        source_note = field.string{required = false},
        model = field.string{required = false},
        turns = field.number{required = false},
    },
    function(input)
        local channel = normalize_channel(input.channel)
        if channel == nil then
            error("channel must be 'x' or 'linkedin', got: " .. tostring(input.channel))
        end

        local url = trim(input.url)
        local card_title = trim(input.card_title)
        local card_dek = trim(input.card_dek)
        local excerpt = trim(input.article_excerpt or "")
        local rejected = input.rejected_takes
        if rejected == nil or type(rejected) ~= "table" then
            rejected = {}
        end

        local source_note
        if excerpt ~= "" then
            source_note = "Used article_excerpt from caller."
        else
            source_note = "No article_excerpt; URL not fetched — card metadata only."
        end

        local article_context = article_block(excerpt, card_title, card_dek, url)
        local rejected_block = format_rejected(rejected)
        local channel_line = channel_hint(channel)

        Log.info("Social copy: starting three-turn copywriter session", {
            channel = channel,
            url = url,
            rejected_count = #rejected,
        })

        -- Turn 1: standalone fact or mechanism
        local turn1_message = table.concat({
            "Draft option 1 for " .. channel .. ".",
            channel_line,
            "",
            "ARTICLE CONTEXT:",
            article_context,
            "",
            "CARD METADATA (do not echo in the post):",
            "Title: " .. card_title,
            "Dek: " .. card_dek,
            "",
            "REJECTED TAKES (never repeat or lightly rephrase):",
            rejected_block,
            "",
            "Angle: one solid standalone take — lead with a concrete fact or mechanism from the essay.",
            "Append this URL once at the end: " .. url,
        }, "\n")

        local r1 = copywriter({message = turn1_message})
        local option_1 = ensure_url(extract_post(r1), url)

        -- Turn 2: different angle; conversation history includes turn 1
        local turn2_message = table.concat({
            "Draft option 2 for " .. channel .. ".",
            channel_line,
            "",
            "Requirements:",
            "- Genuinely different angle from option 1 in this conversation — not a restatement or polish.",
            "- Do not echo the card title or dek.",
            "- Same copy rules as your system prompt.",
            "Append this URL once at the end: " .. url,
        }, "\n")

        local r2 = copywriter({message = turn2_message})
        local option_2 = ensure_url(extract_post(r2), url)

        -- Turn 3: hotter take; creativity via prompt (no temperature — GPT-5 rejects it)
        local turn3_message = table.concat({
            "Draft option 3 for " .. channel .. ".",
            channel_line,
            "",
            "Requirements:",
            "- Hotter and more surprising than options 1 and 2 in this thread.",
            "- Do not repeat their angles. Surprise with a specific detail or implication, not slogans.",
            "- Still defensible from the article; plain English, not marketing voice.",
            "- Do not echo the card title or dek.",
            "- Be bold — the take you might hesitate to post, but can stand behind.",
            "Append this URL once at the end: " .. url,
        }, "\n")

        local r3 = copywriter({message = turn3_message})
        local option_3 = ensure_url(extract_post(r3), url)

        local options = {option_1, option_2, option_3}
        local dropped_reasons = collect_dropped_reasons(options, card_dek, rejected)

        state.turns_completed = 3

        return {
            option_1 = option_1,
            option_2 = option_2,
            option_3 = option_3,
            dropped_reasons = dropped_reasons,
            source_note = source_note,
            model = "openai/gpt-5-mini",
            turns = 3,
        }
    end
}

Specification([[
Feature: Social copy for anth.us articles
  Publicist gets three paste-ready posts from one multi-turn copywriter session

  Scenario: Three sequential copywriter turns produce options
    Given the procedure has started
    And the input url is "https://anth.us/blog/bugonomics-cheap-exploits-2026/"
    And the input channel is "x"
    And the input card_title is "Bugonomics"
    And the input card_dek is "When breaking software gets as cheap as writing it, cheaper offense means more offense."
    And the input article_excerpt is "Exploit discovery is now cheap enough that attackers run volume plays defenders still model as rare."
    And the agent "copywriter" responds with "Exploit discovery used to be a specialist job. Now it is a script kiddie with a budget."
    And the agent "copywriter" responds with "We still write incident response playbooks as if misconfig bugs are scarce. They are not."
    And the agent "copywriter" responds with "The scary shift is not zero-days. It is a thousand boring bugs nobody has time to fix."
    When the procedure runs
    Then the procedure should complete successfully
    And the output option_1 should exist
    And the output option_2 should exist
    And the output option_3 should exist
    And the output turns should be 3
    And the output model should be "openai/gpt-5-mini"
]])
