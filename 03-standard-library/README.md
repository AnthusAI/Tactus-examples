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

### 01-state-management.tac

Demonstrates state operations in Tactus workflows. This example shows:
- Initializing state with metatable syntax (`state.key = value`)
- Using `State.increment()` for atomic counter operations
- Reading state values for output and validation
- Tracking workflow progress with state variables
- State assertions in specifications

State is essential for workflows that need to track progress, count iterations, or maintain values across procedure steps. This example shows the basics of state management without requiring any LLM calls.

### 02-file-io.tac

Comprehensive demonstration of file I/O operations across different formats. This example shows:
- Reading CSV files with automatic header handling
- Processing data with Lua table operations
- Writing results to multiple formats (CSV, JSON, text)
- Using `require()` to import I/O libraries (`tactus.io.csv`, `tactus.io.json`, `tactus.io.file`)
- Relative file paths from procedure directory
- Working with the gitignored `output/` folder

File I/O is crucial for workflows that process datasets, generate reports, or integrate with external systems. This example demonstrates the consistent API across different file formats.

### 03-message-history.tac

Shows how to manage conversation history with the MessageHistory primitive. This example demonstrates:
- Manually injecting system messages with `MessageHistory.inject_system()`
- Appending user messages with `MessageHistory.append()`
- Retrieving full conversation history with `MessageHistory.get()`
- Iterating through messages with `python.iter()`
- Tracking conversation length and message roles
- Clearing history when needed with `MessageHistory.clear()`

MessageHistory is aligned with pydantic-ai's message_history concept and is essential for building stateful chatbots and multi-turn conversations where context matters.

## Key Concepts

**State**: Global state that persists across procedure executions. Use `state.key = value` to set and `state.key` to read. The `State` module provides utilities like `State.increment()` for atomic operations.

**Log**: Built-in logging utility with levels (debug, info, warn, error). Use `Log.info("message", {data})` to log structured data.

**File I/O**: Tactus provides native support for reading and writing common data formats. The file I/O API is designed to be simple and consistent across formats.

**Sessions**: Maintain conversation context across multiple agent interactions. Sessions track message history and state.

**Checkpoints**: Save and restore procedure state at specific points. Useful for expensive operations that you don't want to repeat on failure.
