# Research: Advanced Agent Rule-Sets & Cognitive Architectures

**Date**: 2025-12-14
**Objective**: Identify best practices for enhancing agent "Constitutions" (Rule-Sets) and Cognitive Architectures.

## Key Findings

### 1. Constitutional AI & System Prompts
*   **Concrete Rules > Abstract Goals**: Agents perform better with actionable, blocking rules (e.g., "Do not use X") rather than vague ethical goals.
*   **Positive Framing**: While negative constraints are useful, positive instructions ("Do X instead of Y") improve alignment.
*   **Structure**: Best-in-class prompts use strict segmentation (e.g., Markdown headers, XML tags) to separate "Context", "Instructions", and "Constraints".

### 2. Cognitive Architecture Components
Research suggests a robust agent requires explicit modules beyond just "Think-Act":
*   **Structured Reasoning (CoT)**: Mandating "Chain-of-Thought" or "Step-by-Step" reasoning for high-complexity tasks reduces error propagation.
*   **Memory Systems**:
    *   *Episodic*: Logs of past actions/errors.
    *   *Procedural*: Stored "skills" or "playbooks".
*   **Reflection Loops**: explicit steps where the agent must "Self-Criticize" its output before finalizing it.

### 3. Constraints-of-Thought
A novel pattern where agents must generate `(Intent, Constraint)` pairs before acting.
*   *Example*: "Intent: Update database. Constraint: Do not drop tables."

## Recommendations for Agents-MD

1.  **Enhance Cognitive Loop**:
    *   Upgrade `System of Thought` to include **Reflection** and **Constraint-Checking** steps explicitly.
2.  **Formalize the Constitution**:
    *   The `Engineering Manifesto` should be treated as the "Immutable Constitution".
    *   Add a "Safety Protocol" section that mandates "Constraints-of-Thought" for destructive actions.
3.  **Standardize Prompt Structure**:
    *   Adopt a strict `CONTEXT -> CONSTITUTION -> SPECIALIZATION -> MEMORY` flow in agent definitions.
