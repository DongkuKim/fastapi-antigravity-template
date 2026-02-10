---
description: Workflow for automatically updating documentation based on code changes
---

To ensure documentation stays in sync with implementation, follow these steps after completing a code change:

1. **Analyze Changes**:
   - Review all modified files and identify changes to public APIs, logic flow, or configuration.

2. **Identify Impacted Docs**:
   - **Public API change** -> Update `api.md` or the dedicated doc in 'docs/'.
   - **New directory in src** -> Create a new dedicated doc in `docs/` and link it in `README.md`.

3. **Perform Updates**:
   - Add "How to use" or "Why it works this way" explanations for new features.
   - **Important**: Follow the `stop-slop` skill (.agent/skills/stop-slop/SKILL.md) to ensure clean, direct, and non-repetitive writing.

4. **Verify Consistency**:
   - Read the updated documentation to ensure it accurately reflects the new state of the code.
   - Ensure all links between docs are valid.