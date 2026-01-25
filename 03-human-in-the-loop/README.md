# Human-in-the-Loop (HITL)

Patterns for integrating human decision-making into AI workflows. These examples show how to request human input, approval, and feedback during procedure execution.

## What You'll Learn

- Basic HITL primitives: `Human.approve()`, `Human.input()`, `Human.review()`
- Traditional hardcoded HITL workflows
- Agent-driven HITL with tool-wrapped primitives
- Dynamic vs. static human interaction patterns
- Multi-turn agent workflows with human approval

## Examples

### 01-basic-hitl.tac

Introduction to HITL primitives with direct procedure calls. This example demonstrates the traditional approach where the procedure code explicitly calls HITL primitives with hardcoded messages:
- `Human.approve()` - Yes/no decisions
- `Human.input()` - Text input with optional dropdown options
- `Human.review()` - Content review and feedback

**Best for**: Simple, predetermined workflows where you know exactly when and what to ask the human.

**Run it:**
```bash
tactus run 03-human-in-the-loop/01-basic-hitl.tac
```

### 02-agent-driven-approval.tac

An AI agent that dynamically decides when to request human approval and constructs context-aware approval messages. This demonstrates **agent-driven HITL** where the agent has tools that wrap HITL primitives and uses them intelligently based on context.

**Key Innovation**:
- **Traditional HITL** (example 01): Procedure directly calls `Human.approve({message: "..."})`
- **Agent-Driven HITL** (this example): Agent has `ask_approval` tool and decides when/how to use it

The agent analyzes the situation, constructs appropriate questions, and can adapt its behavior based on context. Much more flexible than hardcoded workflows.

**Use Cases**:
- Risk-based approval flows (agent only asks for high-risk operations)
- Dynamic questionnaires (agent adapts questions based on previous answers)
- Context-aware confirmations (agent explains WHY approval is needed)
- Multi-stage reviews (agent requests approvals from different stakeholders)

**Run it:**
```bash
tactus run 03-human-in-the-loop/02-agent-driven-approval.tac \
  --param app_name="MyApp" \
  --param environment="production"
```

**Note**: Both examples require the Tactus IDE or VSCode extension to display HITL modals. Running from CLI will execute but cannot display the interactive modals.
