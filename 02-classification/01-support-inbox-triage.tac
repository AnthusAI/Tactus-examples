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

Specification([[
Feature: Support inbox triage

  Scenario: Invalid output triggers retry and still returns a valid label
    Given the procedure has started
    And the input message is "I was double charged this month. Please refund me."
    And the agent "support_triage_llm" responds with "Maybe"
    And the agent "support_triage_llm" responds with "billing\nThe message is about being charged twice and requesting a refund."
    When the procedure runs
    Then the procedure should complete successfully
    And the output label should be "billing"
    And the output retries should be 1
]])
