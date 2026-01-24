# Agents

This chapter focuses on working with AI agents in Tactus - the core abstraction for interacting with language models.

## What You'll Learn

- Defining agents with different providers (OpenAI, Anthropic, Bedrock, Gemini)
- Configuring agent system prompts and initial messages
- Multi-agent workflows and coordination
- Streaming responses from agents
- Switching between models dynamically
- Agent conversation history and context management

## Examples

### 01-multi-model.tac

Demonstrates using multiple models in a single workflow - a researcher using GPT-4o and a summarizer using GPT-4o-mini. This example shows:
- Defining multiple agents with different models
- Sequential agent execution (research then summarize)
- Template strings in initial messages (`{input.topic}`, `{research}`)
- Passing results between agents
- Turn-limited loops for each agent phase
- Using the done tool to extract agent outputs

This example showcases Tactus's ability to compose workflows from different models based on task requirements - using a more capable model for research and a faster, cheaper model for summarization.

### 02-streaming.tac

Shows real-time streaming responses from an agent. This example demonstrates:
- Enabling streaming mode with `streaming = true`
- Processing token-by-token responses as they arrive
- Accumulating streamed content into a final result
- Using streaming for interactive or long-form generation

Streaming is useful for user-facing applications where you want to display partial responses as they're generated, or for monitoring long-running agent operations.

### 03-bedrock.tac

Demonstrates using AWS Bedrock as a provider with multiple Claude models. This example shows:
- Configuring the `bedrock` provider
- Using different Claude models (Claude 3.5 Sonnet, Claude 3 Haiku, Claude 3 Opus)
- AWS credential configuration requirements
- Provider-specific model identifiers
- Multi-agent workflows across different Bedrock models

This example requires AWS credentials to be configured (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`) and demonstrates Tactus's support for enterprise cloud providers.

## Key Concepts

**Agent**: The primary abstraction for interacting with language models. Agents are defined with a provider, model, system prompt, and optional tools.

**Providers**: Tactus supports multiple LLM providers including OpenAI, Anthropic, AWS Bedrock, and Google Gemini. Each agent specifies its provider and model.

**System Prompts**: Instructions that define the agent's behavior and role. System prompts are set when creating an agent and persist across interactions.

**Streaming**: Real-time token-by-token responses from agents, useful for interactive applications and long-form generation.
