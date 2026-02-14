# Classification

Real-world classification patterns: route messy text into a small, explicit set of labels.

These examples are designed to run in mock mode (fast, deterministic) and also in real mode (with API keys and/or optional ML dependencies) so you can iterate safely.

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

### model-primitive-sentiment

A minimal Model primitive example using a mock backend. Demonstrates:
- Stateless prediction via the Model primitive
- Input/output schemas on the model itself
- Deterministic specs that run in CI without API keys

### model-train-imdb-naive-bayes

Train a real (local) sentiment classifier using Naive Bayes + TF-IDF on the IMDB dataset, register it, then call it from a Procedure. Demonstrates:
- A single Model block that includes both runtime config and training config
- A real training + evaluation loop via the CLI (`tactus train`, `tactus models evaluate`)
- CI-safe specs that test your branching logic via `Mocks { ... }`

### model-train-imdb-hf-sequence-classifier

Train a Hugging Face sequence classifier (AutoModelForSequenceClassification) on IMDB and register it. Demonstrates:
- Using the same Model/Procedure pattern with a different training backend
- Hyperparameter control via a simple `hyperparameters` table
- How to keep specs deterministic (mocked) even when the real model is expensive to train
