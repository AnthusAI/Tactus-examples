-- Composite Classification: Fuzzy Match First, LLM Fallback
--
-- Pattern:
--   1) Try fast fuzzy matching for obvious cases (no API calls).
--   2) If nothing matches, fall back to LLM classification for nuance.

-- SNIPPET START
Procedure {
  input = {
    message = field.string{required = true, description = "Incoming support message"}
  },
  output = {
    label = field.string{required = true, description = "One of: billing, account, bug, other"},
    path = field.string{required = true, description = "Which classifier decided: fuzzy or llm"}
  },
  function(input)
    local fuzzy = Classify {
      method = "fuzzy",
      classes = {"double charged", "refund", "invoice", "login", "password reset", "crash", "error"},
      threshold = 0.90,
      algorithm = "token_set_ratio"
    }

    local llm = Classify {
      name = "support_triage_llm_fallback",
      method = "llm",
      classes = {"billing", "account", "bug", "other"},
      prompt = "Classify this support message into one label: billing, account, bug, other.",
      model = "openai/gpt-4o-mini",
      temperature = 0,
      max_retries = 3
    }

    local fuzzy_result = fuzzy(input.message)
    if fuzzy_result.value ~= "NO_MATCH" then
      local v = fuzzy_result.value
      if v == "double charged" or v == "refund" or v == "invoice" then
        return {label = "billing", path = "fuzzy"}
      end
      if v == "login" or v == "password reset" then
        return {label = "account", path = "fuzzy"}
      end
      if v == "crash" or v == "error" then
        return {label = "bug", path = "fuzzy"}
      end
    end

    local llm_result = llm(input.message)
    return {label = llm_result.value, path = "llm"}
  end
}
-- SNIPPET END

-- Deterministic model response for CI-safe specs.
Mocks {
  support_triage_llm_fallback = {
    returns = {value = "bug", confidence = 0.93}
  }
}

Specification([[
Feature: Composite classification

  Scenario: Fuzzy path handles an obvious billing message
    Given the procedure has started
    And the input message is "double charged"
    When the procedure runs
    Then the output label should be "billing"
    And the output path should be "fuzzy"

  Scenario: LLM fallback handles the long tail
    Given the procedure has started
    And the input message is "After the last update, the app crashes whenever I click Save."
    When the procedure runs
    Then the output label should be "bug"
    And the output path should be "llm"
]])
