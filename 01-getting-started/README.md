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

**Run it:**
```bash
tactus run 01-getting-started/01-hello-world.tac
```

**Test it:**
```bash
tactus test 01-getting-started/01-hello-world.tac --mock
```
