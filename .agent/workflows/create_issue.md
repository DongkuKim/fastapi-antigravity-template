---
description: Workflow for creating a new GitHub issue with proper context and conflict checking.
---

1.  **Get Current User**:
    -   Use `mcp_github_get_me` to identify the authenticated user (e.g., `DongkuKim`).

2.  **Search Context**:
    -   Use `mcp_github_search_issues` to check for existing issues that are similar, related, or conflicting.
    -   **Conflict Check**: If a conflicting issue exists (e.g., one proposing the opposite change), **STOP** and resolve the conflict before proceeding. Do not create a duplicate or contradictory issue.

3.  **Draft Issue Content**:
    -   **Goal/Problem**: Clearly state what needs to be achieved or what is broken.
    -   **Proposed Changes**: If known, specify which files or logic parts will be changed and how.
    -   **References**: List any related issue numbers found in step 2 (e.g., "Relates to #12").

4.  **Create Issue**:
    -   Use `mcp_github_issue_write` with `method='create'`.
    -   **Assign**: Set `assignees=['<username>']` using the username retrieved in step 1.
    -   **Body**: Ensure the body includes the sections drafted in step 3.
