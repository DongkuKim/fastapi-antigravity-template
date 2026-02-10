---
description: Workflow for managing python dependencies with uv.
---

# Manage Dependencies

1.  **Initialize Project**
    -   If starting fresh: `uv init`
    -   After cloning: `uv sync`

2.  **Add Dependencies**
    -   To add a package: `uv add <package_name>`
    -   Example: `uv add fastapi`
    -   For dev dependencies: `uv add --dev <package_name>`

3.  **Remove Dependencies**
    -   To remove a package: `uv remove <package_name>`

4.  **Sync Environment**
    -   To install dependencies from `pyproject.toml` / `uv.lock`:
    -   Command: `uv sync`
