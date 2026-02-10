---
trigger: always_on
---

# Development Standards

## 1. Mandatory Testing
- **Execution**: Before completing any task or creating a Pull Request, you MUST run the test suite.
- **Commands**:
  - Unit tests: `pnpm run test`
- **Zero Tolerance**: Do not propose changes or finalize tasks if tests are failing.

## 2. Documentation
- **Flow**: Use Mermaid diagrams or detailed text descriptions to explain "Why" a specific logic path was chosen.
- **Auto-Update**: Follow the `.agent/workflows/update_docs.md` workflow to synchronously update documentation with every code change.
- **Docstrings**: Public APIs and core classes must have JSDoc comments.

## 3. Code Style & Quality
- **Linting & Formatting**: Codebase must be clean and formatted using `eslint` and `prettier`.
- **Pre-Commit**: Always run `pnpm run lint` and `pnpm exec prettier --write .` before committing.