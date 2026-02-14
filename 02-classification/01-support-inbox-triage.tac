-- Support Inbox Triage (LLM Classification)
--
-- Route an incoming support message into an explicit label set.
-- Demonstrates stdlib retry logic when the model returns an invalid label.

-- SNIPPET START
Procedure {
  input = {
    message = field.string{required = true, description = "Incoming support message"}
  },
  output = {
    label = field.string{required = true, description = "One of: billing, account, bug, other"},
    retries = field.number{required = true, description = "How many retries were needed"}
  },
  function(input)
    local triage = Classify {
      name = "support_triage_llm",
      method = "llm",
      classes = {"billing", "account", "bug", "other"},
      prompt = [[
You are a support triage assistant.
Return only one label from: billing, account, bug, other.
If the request is unclear, choose "other".
]],
      model = "openai/gpt-4o-mini",
      temperature = 0,
      max_retries = 3
    }

    local result = triage(input.message)
    return {label = result.value, retries = result.retry_count}
  end
}
-- SNIPPET END

-- Deterministic model responses for CI-safe specs.
--
-- The LLM classifier retries if the predicted value isn't in the allowed class set.
-- With temporal mocks, we can simulate an invalid first attempt followed by a valid one.
Mocks {
  support_triage_llm = {
    temporal = {
      {value = "Maybe", confidence = 0.2},
      {value = "billing", confidence = 0.91}
    }
  }
}

Specification([[
Feature: Support inbox triage

  Scenario: Invalid output triggers retry and still returns a valid label
    Given the procedure has started
    And the input message is "I was double charged this month. Please refund me."
    When the procedure runs
    Then the procedure should complete successfully
    And the output label should be "billing"
    And the output retries should be 1
]])
