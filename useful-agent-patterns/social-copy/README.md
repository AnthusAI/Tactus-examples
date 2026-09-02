# Social Copy

Ryan Alyn Porter rarely posts to social because AI-generated copy tends to restate the link preview, stack slogans, or hide in-article riddles behind a URL. Publicist calls this procedure to draft three paste-ready posts for an anth.us article — each a distinct angle, none echoing the card dek.

## The pattern

One stateful `copywriter` Agent takes **three sequential turns** on the same conversation. Turn 2 sees turn 1; turn 3 sees turns 1 and 2. The orchestrator is plain Lua; intelligence stays in the Agent.

| Turn | Goal |
|------|------|
| 1 | Standalone take — concrete fact or mechanism |
| 2 | Different angle; explicitly not a restatement of option 1 |
| 3 | Hotter / more surprising (creativity via prompt nudge only) |

**GPT-5 note:** This procedure uses `openai/gpt-5-mini` with `model_type = "responses"`. Do not set `temperature` on the Agent or on individual turns — the GPT-5 family omits temperature because OpenAI rejects it. Turn 3 creativity is prompt-only.

**Article source:** Pass `article_excerpt` when Publicist has body text. The procedure does not fetch the live URL; without an excerpt it works from card metadata only and records that in `source_note`.

## Run

```bash
tactus run useful-agent-patterns/social-copy/social-copy.tac \
  --param url="https://anth.us/blog/bugonomics-cheap-exploits-2026/" \
  --param channel=x \
  --param card_title="Bugonomics" \
  --param card_dek="When breaking software gets as cheap as writing it, cheaper offense means more offense." \
  --param article_excerpt="Paste article body or key paragraphs here when available." \
  --param rejected_takes='["When breaking software gets as cheap as writing it, cheaper offense means more offense.","What got cheap was not breaking in. It was trying."]'
```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `url` | yes | Article URL — appended once at the end of each post |
| `channel` | yes | `x` or `linkedin` |
| `card_title` | yes | Link preview title (agent must not echo) |
| `card_dek` | yes | Link preview dek (agent must not echo) |
| `article_excerpt` | no | Body text from Publicist; preferred source of article facts |
| `rejected_takes` | no | JSON array of failed posts to avoid (default `[]`) |

### Outputs

| Field | Description |
|-------|-------------|
| `option_1` | Paste-ready post (URL at end) |
| `option_2` | Paste-ready post (URL at end) |
| `option_3` | Paste-ready post (URL at end) |
| `dropped_reasons` | Heuristic flags for manual review (dek echo, rejected overlap) |
| `source_note` | Whether excerpt or card-only context was used |
| `model` | Model id used |
| `turns` | Always `3` when complete |

## Test

```bash
tactus validate useful-agent-patterns/social-copy/social-copy.tac
tactus test useful-agent-patterns/social-copy/social-copy.tac --mock
```

## Copy rules (enforced in agent prompt)

Posts must stand alone if the card never loads. No dek echo, no slogan-stack jargon (`cheap offense`, `blast radius`, `NHI`, etc.), no in-article riddles without context, no "I wrote a piece about…" unless requested. Three survivors only — no fourth option.

## What Tactus did well here

- **Multi-turn Agent history** — three `copywriter({message = ...})` calls on one Agent; prior turns stay in context without manual session wiring.
- **Per-turn `message` override** — each turn gets a distinct instruction while sharing system prompt and history.
- **`reasoning_effort` on Agent config** — thinking depth without inventing new DSL.
- **Mock specs** — `tactus test --mock` runs the full orchestration in CI without API keys.

## Known limitations (workarounds in this example)

- **No URL fetch** — pass `article_excerpt` from Publicist; `source_note` records when only card metadata is available.
- **No per-turn `reasoning_effort`** — set once on the Agent; turn 3 uses prompt nudge for creativity instead.
- **Quality gate is heuristic** — `dropped_reasons` flags likely failures; Publicist or a human still approves before posting.
