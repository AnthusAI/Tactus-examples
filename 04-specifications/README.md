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

_Examples coming soon. This chapter will demonstrate comprehensive BDD testing patterns for AI workflows._

## Key Concepts

**Specification**: Embedded BDD tests defined using Gherkin syntax (Given/When/Then). Specifications are wrapped in `Specification([[...]])` blocks.

**Gherkin**: A domain-specific language for describing test scenarios. Uses keywords like Feature, Scenario, Given, When, Then, And, But.

**Fuzzy Matching**: Flexible assertion that checks if output is semantically similar to expected values. Useful for testing AI outputs that may vary in wording. Use `should fuzzy match` with a threshold (0.0-1.0).

**Mocking**: Running tests without actual API calls using `--mock` flag. Mocks provide deterministic responses for testing logic without incurring API costs.

**Custom Steps**: You can define custom Gherkin steps using the `step()` function for domain-specific assertions.
