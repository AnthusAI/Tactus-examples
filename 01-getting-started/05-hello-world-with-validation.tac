-- Hello World with Input/Output Validation
-- This example demonstrates the formal Procedure structure with schema validation

World = Agent {
  provider = "openai",
  model = "gpt-4o-mini",
  system_prompt = "Your name is World. Greet users in a friendly manner."
}

Procedure {
    input = {
        name = field.string{
            required = true, 
            description = "The name of the person to greet"
        },
        language = field.string{
            required = false,
            default = "English",
            description = "Language for the greeting"
        }
    },
    output = {
        greeting = field.string{
            required = true,
            description = "The greeting message from the agent"
        },
        language_used = field.string{
            required = true,
            description = "The language used for the greeting"
        }
    },
    function(input)
        Log.info("Greeting user", {name = input.name, language = input.language})
        
        -- Create a message for the agent
        local message = string.format(
            "Please greet %s in %s",
            input.name,
            input.language
        )
        
        -- Get the agent's response
        local response = World(message)
        
        return {
            greeting = response,
            language_used = input.language
        }
    end
}

Specification([[
Feature: Hello World with Validation

  Scenario: Greets user with validated inputs
    Given the procedure has started
    And the input name is "Alice"
    And the input language is "English"
    And the agent "World" responds with "Hello Alice! I'm World, nice to meet you!"
    When the procedure runs
    Then the procedure should complete successfully
    And the output greeting should exist
    And the output language_used should be "English"
    
  Scenario: Uses default language when not specified
    Given the procedure has started
    And the input name is "Bob"
    And the agent "World" responds with "Hi Bob! Welcome!"
    When the procedure runs
    Then the output language_used should be "English"
]])
