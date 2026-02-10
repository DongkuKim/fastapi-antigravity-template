---
trigger: always_on
---

# User Rules

Define custom rules for the agent here.

## Package Management
## Package Management
- **ALWAYS** use `pnpm` for managing dependencies. Never use `npm` or `yarn` unless explicitly requested.

## Architecture
- Enforce clean separation business logic and others.

## Testing
- Require unit tests for all function.


## GitHub & Collaboration
- **Assignments**: Always assign the **current user** (self) to any Issue or Pull Request you create. Verify the current user with `get_me` if unsure.

## General Behavior
- **ALWAYS** adhere to the [stop-slop skill](.agent/skills/stop-slop/SKILL.md) for all coding tasks. Be concise, direct, and avoid over-engineering.