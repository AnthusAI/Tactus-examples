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

_Examples coming soon. This chapter will cover agent basics, multi-model support, streaming, and provider-specific features._

## Key Concepts

**Agent**: The primary abstraction for interacting with language models. Agents are defined with a provider, model, system prompt, and optional tools.

**Providers**: Tactus supports multiple LLM providers including OpenAI, Anthropic, AWS Bedrock, and Google Gemini. Each agent specifies its provider and model.

**System Prompts**: Instructions that define the agent's behavior and role. System prompts are set when creating an agent and persist across interactions.

**Streaming**: Real-time token-by-token responses from agents, useful for interactive applications and long-form generation.
