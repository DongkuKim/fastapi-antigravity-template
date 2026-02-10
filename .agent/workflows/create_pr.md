---
description: Workflow for creating a Pull Request on GitHub.
---

1.  **Pre-check**: Run `/check_lint` to ensure code quality.
2.  **Commit Changes**: Ensure all changes are committed with a clear message.
3.  **Push Branch**: Push the local branch to the remote repository using `git push origin <branch-name>`.
4.  **Create PR**: Use `mcp_github_create_pull_request` to open a PR.
    *   **Base**: `main`
    *   **Head**: current branch name
    *   **Title**: Brief summary of changes.
    *   **Body**: Include "Resolves #<number>" to link the issue.

5. **Assign User**:
    *   Get the `pullNumber` from the previous step output.
    *   Use `mcp_github_issue_write` with `method='update'`, `issue_number=pullNumber`.
    *   Set `assignees` to the current user (e.g., `['DongkuKim']`).
