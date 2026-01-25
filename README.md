# Tactus Examples

Educational examples for the Tactus programming language. This repository contains runnable, tested examples organized by topic to help you learn Tactus.

## Purpose

This repository is the single source of truth for educational Tactus examples. These examples are:
- **Educational**: Designed to teach Tactus concepts progressively
- **Tested**: Every example includes embedded BDD specifications
- **Runnable**: All examples can be executed directly with the Tactus CLI

This repository is separate from the CI-focused examples in the main Tactus repo. Examples here are specifically curated for learning and are ingested by the [Tactus website](https://github.com/AnthusAI/Tactus-web) for documentation.

## Organization

Examples are organized hierarchically using numbered prefixes for natural file ordering:

```
01-getting-started/
  01-hello-world.tac
  02-another-example.tac
  README.md
02-state-and-sessions/
  01-state-basics.tac
  02-complex-example/
    README.md
    example.tac
    helper.lua
  README.md
```

### Two Example Formats

1. **Simple `.tac` files**: Single-file examples for straightforward concepts
2. **Folders**: Multi-file examples for complex topics, each containing a README

### Documentation Hierarchy

- **Repository README** (this file): Overview and getting started
- **Chapter README**: Overview of examples in that chapter with paragraph descriptions
- **Example README**: Full explanation for folder-based examples only

## Running Examples

Execute any example with the Tactus CLI:

```bash
tactus run 01-getting-started/01-hello-world.tac
```

## Testing Examples

All examples include embedded BDD specifications. Test them with:

```bash
# Test with mocks (fast, no API calls)
tactus test 01-getting-started/01-hello-world.tac --mock

# Test against real APIs (requires API keys)
tactus test 01-getting-started/01-hello-world.tac
```

## Continuous Integration

This repository includes a test runner that validates all examples:

```bash
# Run all tests with mocks (default)
./scripts/test-all.sh

# Run all tests against real APIs
./scripts/test-all.sh --real
```

The CI system ensures all showcased examples remain runnable and pass their specifications.

## Chapters

### [01-getting-started](01-getting-started/)
Introduction to Tactus fundamentals: agents, specifications, and basic interactions. Start here if you're new to Tactus.

### [02-agents](02-agents/)
Working with AI agents: multiple providers, streaming, multi-agent workflows, and model switching.

### [03-standard-library](03-standard-library/)
Built-in utilities for state management, logging, file I/O, sessions, and checkpointing.

### [04-specifications](04-specifications/)
Behavior-driven development with Gherkin specifications, fuzzy matching, and comprehensive testing patterns.

### [05-evaluations](05-evaluations/)
Quantitative assessments: running evaluations over datasets, metrics, thresholds, and statistical analysis.

### [06-advanced-features](06-advanced-features/)
Advanced capabilities: tools, MCP integration, sub-procedures, and custom models. _Examples coming soon._

### [02-classification](02-classification/)
Real-world classification patterns: route messy text into explicit label sets using LLMs and fuzzy matching.

### [03-human-in-the-loop](03-human-in-the-loop/)
Patterns for integrating human decision-making into AI workflows, including agent-driven approval requests.

## For Tactus-web Integration

This repository is designed to be ingested by the Tactus-web build process. See [README-INGESTION.md](README-INGESTION.md) for details on the ingestion pipeline and frontmatter requirements.

## Contributing

When adding examples:
1. Use numbered prefixes (01-, 02-, etc.) for natural ordering
2. Include embedded `Specification([[...]])` blocks for testing
3. Update the chapter README with a paragraph description
4. For folder-based examples, include a detailed README

## Requirements

- Python 3.11+
- Tactus CLI: `pip install tactus`
- API keys (for running examples against real APIs): Set `OPENAI_API_KEY` environment variable

## Links

- [Tactus Main Repository](https://github.com/AnthusAI/Tactus)
- [Tactus Website](https://github.com/AnthusAI/Tactus-web)
- [Documentation](https://github.com/AnthusAI/Tactus/tree/main/docs)
