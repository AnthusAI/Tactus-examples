# Standard Library

This chapter explores Tactus's built-in standard library - utilities and primitives that make it easier to build robust AI workflows.

## What You'll Learn

- State management with `State` primitives
- Logging and debugging with `Log`
- File I/O operations (JSON, CSV, TSV, Parquet, HDF5, Excel, text files)
- Session management for stateful conversations
- Checkpointing for expensive operations
- Message history and conversation context
- Structured output validation

## Examples

_Examples coming soon. This chapter will cover built-in Tactus utilities for common workflow patterns._

## Key Concepts

**State**: Global state that persists across procedure executions. Use `state.key = value` to set and `state.key` to read. The `State` module provides utilities like `State.increment()` for atomic operations.

**Log**: Built-in logging utility with levels (debug, info, warn, error). Use `Log.info("message", {data})` to log structured data.

**File I/O**: Tactus provides native support for reading and writing common data formats. The file I/O API is designed to be simple and consistent across formats.

**Sessions**: Maintain conversation context across multiple agent interactions. Sessions track message history and state.

**Checkpoints**: Save and restore procedure state at specific points. Useful for expensive operations that you don't want to repeat on failure.
