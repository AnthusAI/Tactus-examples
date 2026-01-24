# Advanced Features

This chapter covers advanced Tactus capabilities for building sophisticated AI workflows with tools, composition, and external integrations.

## What You'll Learn

- Tool definitions and tool calling
- MCP (Model Context Protocol) integration
- Toolsets and tool organization
- Sub-procedures and composition
- Recursive procedures
- Custom models (PyTorch, scikit-learn)
- Host tools and broker patterns
- Script mode for CLI workflows

## Examples

_Examples coming soon. This chapter will demonstrate advanced patterns for complex AI applications._

## Key Concepts

**Tools**: Functions that agents can call to interact with external systems. Tools are defined with schemas and can be written in Lua or provided via MCP servers.

**MCP (Model Context Protocol)**: A standard for connecting AI agents to external tools and data sources. Tactus supports MCP servers for tool provisioning.

**Toolsets**: Organized collections of related tools. Toolsets can be defined inline, imported from files, or provided by MCP servers.

**Sub-procedures**: Procedures that call other procedures. Enables composition and reusability. Sub-procedures can be called recursively for tree-structured problems.

**Custom Models**: Integration with non-LLM models like classifiers, regressors, or custom PyTorch models. Useful for hybrid AI workflows.

**Host Tools**: Tools that run on the host system (outside the sandbox). Accessed via a broker pattern for controlled execution.

**Script Mode**: Run Tactus procedures from the command line with input/output redirection. Useful for batch processing and integration with other tools.
