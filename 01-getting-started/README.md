# Getting Started

Welcome to Tactus! This chapter introduces the fundamental concepts of the Tactus programming language through simple, self-contained examples.

## What You'll Learn

- How to define AI agents with system prompts
- Basic agent interaction and responses
- Embedded BDD specifications for testing
- Fuzzy matching for flexible output validation

## Examples

### 01-hello-world.tac

A minimal Tactus program demonstrating the core workflow. This example shows how to:
- Define an agent with a provider and model
- Include an embedded BDD specification with Gherkin syntax
- Execute a simple agent interaction
- Use fuzzy matching to validate agent responses flexibly

This example uses the OpenAI GPT-4o-mini model and includes a specification that tests the agent's greeting behavior using fuzzy matching with a 0.9 threshold.

### 02-simple-logic.tac

A pure logic example that demonstrates Tactus procedures without using any AI agents. This example shows:
- How to define procedures with input and output schemas using field definitions
- State management with the `state` primitive
- Multiple BDD specifications testing different aspects of the procedure
- Basic Lua control flow (loops, conditionals)

This example requires no API keys since it doesn't call any LLM providers - perfect for learning the core Tactus programming model.

### 03-parameters.tac

Demonstrates how to work with procedure parameters (inputs) and use them throughout your workflow. This example shows:
- Defining input schemas with descriptions and default values
- Accessing input parameters within the procedure function
- Using parameters in loops and logic
- Logging with the Log utility
- State management with `State.increment()`
- Returning structured output that references input parameters

This example defines an agent but uses it minimally - focusing on parameter handling and state management.
