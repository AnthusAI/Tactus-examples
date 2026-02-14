World = Agent {
  model = "openai/gpt-4o-mini",
  system_prompt = "Your name is World."
}

Specification([[
Feature: Hello World

  Scenario: Greeter returns greeting
    Given the procedure has started
    And the message is "Hello, World!"
    And the agent "World" responds with "Hello! I'm World, nice to meet you!"
    When the procedure runs
    Then the output should fuzzy match any of ["Hello", "Hi", "Hey"] with threshold 0.9
]])

local result = World({message = "Hello, World!"})
return (result and (result.output or result)) or ""
