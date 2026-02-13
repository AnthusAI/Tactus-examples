# Useful Agent Patterns

A collection of high-value architectural patterns for AI agents, implemented in Tactus.

## The Patterns

### Foundations
*   **[Tool Use](./01-tool-use)**: Giving an agent a tool and having it use it reliably.
*   **[Context & Virtual Files](./02-context-io)**: Managing agent I/O with virtual files.
*   **[Guardrails](./03-guardrails)**: Using specs and tests to constrain agent behavior.

### Text Processing
*   **[Filtering](./04-filtering)**: Reducing long contexts before processing.
*   **[Classification](./05-classification)**: Deterministic and fuzzy classification.

### Advanced Flows
*   **[Blind RAG](./06-blind-rag)**: Retrieval without exposing the full corpus to the model.
*   **[Sub-agents](./07-sub-agents)**: Delegating tasks to specialized workers.
*   **[Multi-agent Teams](./08-teams)**: Orchestration of complex groups.
*   **[Feedback Loops](./09-feedback)**: Agents critiquing and improving other agents.
*   **[Progressive Disclosure](./10-progressive)**: UX patterns for complex interactions.

### Multimodal & Integration
*   **[Real-time Video](./11-video)**: Generating video assets on the fly.
*   **[System Integration](./12-system-integration)**: Connecting to external tools (Beads/JIRA).
*   **[Human-in-the-Loop](./13-hitl)**: Approval workflows and human oversight.

### Experimental
*   **[RaR RL](./14-rar-rl)**: Deriving rubrics from feedback.
*   **[Advanced RAG](./15-advanced-rag)**: HyDE, Reranking, Graph RAG.
