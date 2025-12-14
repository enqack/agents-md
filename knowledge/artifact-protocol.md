# Artifact Protocol

This protocol enforces the **Artifact-First** philosophy. Agents do not just write code; they produce tangible outputs for every complex task.

## 1. Planning Artifacts

**When**: Before starting any complex coding task or architectural change.
**Naming**: `implementation_plan.md` or `plan_[task_name].md`.
**Content**:
- **Goal**: What are we solving?
- **Analysis**: "Deep Think" reasoning, tradeoffs, and edge cases.
- **Proposed Changes**: Specific files and logical steps.
- **Verification Strategy**: How will we know it worked?

## 2. Evidence Artifacts

**When**: During execution and verification.
**Naming**: `logs/[timestamp]_[command].log` or embedded in `walkthrough.md`.
**Content**:
- Raw terminal output.
- Test results (`pytest` output).
- Error traces.

## 3. Visual Artifacts

**When**: Modifying UI, Frontend, or generating diagrams.
**Naming**: `visuals/[name].[png|svg]`.
**Content**:
- Screenshots of the running application.
- Architecture diagrams (Mermaid).
- "Generates Artifact: Screenshot" must be in the tool description if automating.

## 4. Summary Artifacts

**When**: At the conclusion of a task.
**Naming**: `walkthrough.md`.
**Content**:
- **Changes**: Bulleted list of what was done.
- **Validation**: Proof that it works (links to evidence/visuals).
- **Next Steps**: Handover instructions.
