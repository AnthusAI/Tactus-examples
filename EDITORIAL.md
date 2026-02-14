# Tactus Examples Editorial & Technical Guidelines

This document establishes the standards for all code and prose in the Tactus Examples repository. All contributors and agents must adhere to these guidelines to ensure consistency, quality, and accessibility.

## 1. Code Requirements

**The Golden Rule: Code Must Run.**

*   **Executability**: Example code must be fully functional. "Pseudocode" or "illustrative snippets" that do not compile or run are forbidden unless explicitly marked as a non-functional diagram.
*   **Dual-Target Testing**:
    1.  **CI Ready (Mocked)**: Every example must pass in our Continuous Integration environment. You must provide mocks for external AI services (OpenAI, Anthropic, etc.) so that tests pass without API keys.
    2.  **Production Ready (Real)**: The same code must work with *real* AI services when valid API keys are provided.
*   **Specifications**: Every example must include a corresponding specification (test file) that verifies its behavior. We use BDD-style tests (Cucumber/Gherkin) or standard unit tests where appropriate.
*   **Simplicity**: Prefer the simplest possible implementation that demonstrates the pattern.

## 2. Prose Guidelines

**Goal**: Accessible, magazine-quality technical writing.

### Target Audience
*   **Primary**: AI Engineers looking for practical patterns.
*   **Secondary**: Technical business leaders and product managers who want to understand *what is possible*.

### Tone & Style
*   **Accessible**: Avoid "mansplaining" or being pedantic, but do not assume deep familiarity with niche software engineering acronyms.
*   **Engaging**: Write in a narrative style. Guide the reader through the concept.
*   **Problem-First**: Always start with a **relatable real-world scenario** or problem that the pattern solves.
    *   *Bad*: "Here is how to implement a RAG pipeline using Tactus."
    *   *Good*: "Imagine you need to answer customer support questions based on a 500-page PDF manual, but the model's context window is too small..."

### Terminology & Jargon
*   **Allowed (No Definition Needed)**:
    *   AI (Artificial Intelligence)
    *   ML (Machine Learning)
    *   LLM (Large Language Model)
*   **Define on First Use**:
    *   RLHF (Reinforcement Learning from Human Feedback) - *spell it out*
    *   RAG (Retrieval-Augmented Generation)
    *   CI/CD (Continuous Integration/Continuous Deployment)
    *   RL (Reinforcement Learning)
*   **Avoid**:
    *   Unnecessary internal Google/Facebook jargon unless it's industry standard.
    *   Overly academic notation unless the example is specifically about implementing a paper.

## 3. Structure of an Example

1.  **The Hook**: The relatable problem.
2.  **The Pattern**: High-level explanation of the solution (The "What").
3.  **The Code**: The Tactus implementation (The "How").
    *   *Highlight*: Explicitly mention how much simpler this is in Tactus compared to Python/TypeScript/Go.
4.  **The Breakdown**: Walk through the key parts of the code.
5.  **Extensions**: How this could be extended (e.g., "In a real app, you might add a database here...").

## 4. Tactus Positioning

*   **Simplicity**: The core value proposition is that Tactus makes complex agent patterns *easy*.
*   **Readability**: Tactus code should be readable by non-programmers.
*   **Comparison**: Where appropriate, briefly contrast with the complexity of doing the same thing in traditional languages (e.g., "No need for complex async/await chains...").
