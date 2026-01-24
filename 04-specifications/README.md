# Specifications

This chapter covers behavior-driven development (BDD) with Tactus specifications - embedded tests that validate your AI workflows.

## What You'll Learn

- Writing BDD specifications using Gherkin syntax
- Common Gherkin steps and assertions
- Fuzzy matching for flexible output validation
- Testing agent behavior with specifications
- Mocking vs. real API calls in tests
- Running specifications with `tactus test`

## Examples

### 01-complete-specs.tac

A comprehensive demonstration of BDD testing features in Tactus. This example shows:
- Multiple test scenarios in a single specification
- Testing state changes and validations
- Assertions on procedure inputs, outputs, and state variables
- Testing agent interactions within procedures
- Numeric comparisons and boolean assertions
- Testing iteration counts and loop behavior

This example includes scenarios for setup verification, processing validation, state management, output validation, edge cases, and agent integration - providing a complete reference for writing thorough specifications.

### 02-passing-specs.tac

Demonstrates passing specifications that validate successful procedure execution. This example shows:
- Basic Given/When/Then structure
- Testing procedure completion
- Output existence and value assertions
- State variable validation
- Success criteria testing

This example focuses on positive test cases - verifying that procedures work correctly under normal conditions. It's a good starting point for understanding specification structure before adding edge cases.

### 03-fuzzy-matching.tac

Focused demonstration of fuzzy matching for AI output validation. This example shows:
- High-threshold fuzzy matching (0.95) for near-exact matches
- Medium-threshold fuzzy matching (0.45) for semantic similarity
- Default threshold behavior when not specified
- Using fuzzy matching to handle natural language variation

Fuzzy matching is essential for testing AI agents since their outputs may vary in wording while maintaining semantic meaning. This example demonstrates how to set appropriate thresholds for different validation requirements.

## Key Concepts

**Specification**: Embedded BDD tests defined using Gherkin syntax (Given/When/Then). Specifications are wrapped in `Specification([[...]])` blocks.

**Gherkin**: A domain-specific language for describing test scenarios. Uses keywords like Feature, Scenario, Given, When, Then, And, But.

**Fuzzy Matching**: Flexible assertion that checks if output is semantically similar to expected values. Useful for testing AI outputs that may vary in wording. Use `should fuzzy match` with a threshold (0.0-1.0).

**Mocking**: Running tests without actual API calls using `--mock` flag. Mocks provide deterministic responses for testing logic without incurring API costs.

**Custom Steps**: You can define custom Gherkin steps using the `step()` function for domain-specific assertions.
