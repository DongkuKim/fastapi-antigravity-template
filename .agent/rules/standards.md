---
trigger: always_on
---

# Development Standards

## 1. Mandatory Testing
- **Execution**: Before completing any task or creating a Pull Request, you MUST run the test suite.
- **Commands**:
  - Unit tests: `uv run pytest`
- **Zero Tolerance**: Do not propose changes or finalize tasks if tests are failing.

## 2. Documentation
- **Flow**: Use Mermaid diagrams or detailed text descriptions to explain "Why" a specific logic path was chosen.
- **Auto-Update**: Follow the `.agent/workflows/update_docs.md` workflow to synchronously update documentation with every code change.
- **Docstrings**: Public APIs and core classes must have Google-style docstrings.
- **Reference**: Consult `.agent/skills/fastapi-best-practices/SKILL.md` for architectural guidelines.

## 3. Code Style & Quality
- **Linting & Formatting**: Codebase must be clean and formatted using `ruff`.
- **Pre-Commit**: Always run `uv run ruff check --fix` and `uv run ruff format` before committing.