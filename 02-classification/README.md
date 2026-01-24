# Classification

Real-world classification patterns: route messy text into a small, explicit set of labels.

These examples are designed to run in mock mode (fast, deterministic) and also in real mode (with API keys) so you can iterate safely.

## Examples

### support-inbox-triage

Route a support message into one of four queues. Demonstrates:
- LLM classification with an explicit label set
- Built-in retry loop when the model returns an invalid label
- Returning both the label and retry_count for observability

### composite-fuzzy-then-llm

Compose classifiers: use fuzzy matching for obvious cases first, then fall back to an LLM for the long tail. Demonstrates:
- Fuzzy matching (fast, offline) for known phrases/keywords
- LLM classification fallback
- Returning which path was used (fuzzy vs llm)

