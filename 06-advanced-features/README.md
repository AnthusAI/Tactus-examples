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

## Examples

_Runnable examples coming soon. This chapter will demonstrate advanced patterns for complex AI applications._

### One Tool For Everything

Tactus can be used as a programmable integration surface. Instead of exposing a large MCP catalog as many separate tools, a host application can expose one tool that runs sandboxed Tactus snippets. The host injects an application module, so code can use `require("your_app")` and call a typed SDK-like surface for the host application's capabilities.

This is also a context-efficiency pattern: the MCP client starts with one self-documenting tool, then asks that tool for focused docs and examples only for the capability it needs.

Plexus is a real-world example of this pattern with `execute_tactus`; its runtime injects `plexus` so snippets can call Plexus APIs without repeating the import. The Tactus site describes the broader pattern here: [One Tool For Everything](https://tactus.anth.us/use-cases/one-tool-programmable-api/).

## Key Concepts

**Tools**: Functions that agents can call to interact with external systems. Tools are defined with schemas and can be written in Lua or provided via MCP servers.

**MCP (Model Context Protocol)**: A standard for connecting AI agents to external tools and data sources. Tactus supports MCP servers for tool provisioning.

**Toolsets**: Organized collections of related tools. Toolsets can be defined inline, imported from files, or provided by MCP servers.

**Sub-procedures**: Procedures that call other procedures. Enables composition and reusability. Sub-procedures can be called recursively for tree-structured problems.

**Custom Models**: Integration with non-LLM models like classifiers, regressors, or custom PyTorch models. Useful for hybrid AI workflows.

**Host Tools**: Tools that run on the host system (outside the sandbox). Accessed via a broker pattern for controlled execution.

**Host-Registered Modules**: Application-specific modules injected by an embedding host and imported from Tactus with `require(...)`. They let one programmable gateway expose a broad application surface without publishing every operation as a separate tool.
