-- Human-in-the-Loop (HITL): the basics
--
-- This example demonstrates the core HITL primitives:
-- - Human.approve() for yes/no decisions
-- - Human.input() for collecting text input
-- - Human.review() for reviewing an artifact
--
-- Test mocked (CI-safe; HITL auto-responds with defaults):
--   ./scripts/test-all.sh
--   tactus test 03-human-in-the-loop/01-basic-hitl.tac --mock
--
-- Run for real (CLI prompts; IDE shows components):
--   tactus run 03-human-in-the-loop/01-basic-hitl.tac

Procedure {
  output = {
    completed = field.boolean{required = true},
    user_name = field.string{required = true},
    favorite_color = field.string{required = true},
    review_decision = field.string{required = true}
  },
  function(_)
    local should_continue = Human.approve({
      message = "Would you like to continue with the workflow?"
    })

    if not should_continue then
      return {
        completed = false,
        user_name = "",
        favorite_color = "",
        review_decision = "rejected"
      }
    end

    local user_name = Human.input({
      message = "What is your name?",
      placeholder = "Enter your name..."
    }) or ""

    local color = Human.input({
      message = "What is your favorite color?",
      options = {
        {label = "Red", value = "red"},
        {label = "Blue", value = "blue"},
        {label = "Green", value = "green"}
      }
    }) or ""

    local generated_text = "This is a sample document that was generated."
    local review_result = Human.review({
      message = "Please review this generated document",
      artifact = generated_text,
      artifact_type = "document"
    }) or {}

    local final_approval = Human.approve({
      message = "Complete the workflow and save results?",
      timeout = 60,
      default = false
    })

    return {
      completed = final_approval and true or false,
      user_name = user_name,
      favorite_color = color,
      review_decision = review_result.decision or ""
    }
  end
}

Specification([[
Feature: Human-in-the-loop basics

  Scenario: Workflow completes in mocked mode
    Given the procedure has started
    When the procedure runs
    Then the procedure should complete successfully
    And the output completed should be true
    And the output user_name should exist
    And the output review_decision should be "Approve"
]])

