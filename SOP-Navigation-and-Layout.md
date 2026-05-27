### Revised SOP-Navigation-and-Layout.md (full suggested content)

# SOP: Repository Layout, Navigation & Index Files

**Purpose**  
This SOP defines the standard structure, naming conventions, linking rules, and maintenance practices for the *Book of Secret Knowledge* fork (JK_Revisions branch). The goal is to keep the repo highly navigable on GitHub, consistent across folders, and easy to extend as new categories/tools are added.

**Last Updated**: March 2026  
**Applies to**: All folders, especially `tools/`, `documentation/`, and root-level files

## 1. Core Principles (Updated)

- **Navigation-first design** — Every folder containing subfolders or >2–3 .md files **must** have an `INDEX.md`.
- **Recursive TOC in every INDEX.md** — Show the full subtree (nested folders + files) using indented, hyperlinked markdown lists. Use `<details>` + `<summary>` for collapsible deep sections to avoid overwhelming long pages.
- **Tabular lists preferred over full markdown tables** — For folder overviews / quick indexes use definition lists, bolded bullets, or simple indented pairs instead of | Name | Description | Link | tables.
- **Hyperlinks everywhere** — All files, folders, external sites, GitHub repos, and the schema must be clickable (relative links whenever possible).
- **Consistency over perfection** — Use the same patterns (naming, list styles, link formats) across the repo.
- **GitHub rendering** — Prefer native markdown (`<details>`, relative links, lists) over code blocks for interactive elements.
- **Tool tables only** — All tool/resource lists follow [TOOL-TABLE-SCHEMA.md](../TOOL-TABLE-SCHEMA.md) exactly (those remain proper tables).

## 2. Naming Conventions

- Navigation / overview file: **INDEX.md** (uppercase `I`) — preferred over README.md in content folders  
  Alternatives (legacy only): `_INDEX.md`, `00_index.md`
- Tool/resource list files: lowercase-with-dashes.md  
  e.g. `dns-tools.md`, `shell-one-liners.md`
- Personal section: `my-contributions.md` (keep at `tools/` root)
- Schema reference: `TOOL-TABLE-SCHEMA.md` (root level, never move)

**Rule**: No spaces in file/folder names (use `-` or `_`). Escape special characters in links when needed.

## 3. Folder-Level INDEX.md Structure (Recommended Template – Updated)

Every `INDEX.md` should follow this minimal layout:

# [Category Name] Index

Short 1–2 sentence purpose of this folder.

All tool tables in this section follow → [TOOL-TABLE-SCHEMA.md](../TOOL-TABLE-SCHEMA.md)

## Contents (Recursive Overview)

- **[Subfolder A](./subfolder-a/INDEX.md)** — brief one-line description of what it contains
  - [file-one.md](./subfolder-a/file-one.md) — short note
  - [file-two.md](./subfolder-a/file-two.md) — short note
  - **[Nested Subfolder](./subfolder-a/nested/INDEX.md)** — purpose
    - [deep-file.md](./subfolder-a/nested/deep-file.md)

- **[Subfolder B](./subfolder-b/INDEX.md)** — brief description
  - ...

- **Standalone Files**
  - [example-file.md](./example-file.md) — purpose / note
  - [another.md](./another.md)

## Quick Navigation
- ↑ [Back to Parent Index](tools/INDEX.md) (or `../_INDEX.md` for legacy)
- ↑ [Back to Tools Root](../_INDEX.md)  (adjust level as needed)
- ↑ [Repository Root](../../README.md)


**For deeper folders**, wrap large subtrees in:

```
<details>
<summary>Expand: Network Engineering subtree</summary>

- [diagnostics-troubleshooting/](./diagnostics-troubleshooting/INDEX.md)
  - ...
</details>
```

This creates a recursive, explorable map without forcing the reader to click into every folder.

## 4. Top-Level README.md Requirements (Updated)

Near the top, include:

- Brief mission/fork statement
- Collapsible recursive-ish directory structure (use indented list with key folders hyperlinked; full recursion optional here to avoid bloat)
- **Quick Access** section using a simple tabular list (not full table)

Example:

```markdown
<details>
<summary>Repository Structure (click to expand)</summary>

- **[tools/](./tools/INDEX.md)** — main tool & resource collections
  - [my-contributions.md](./tools/my-contributions.md)
  - **[network-engineering/](./tools/network-engineering/INDEX.md)**
  - **[security/](./tools/security/INDEX.md)**
  - ...
- **[documentation/](./documentation/INDEX.md)** — guides, cheat sheets, learning
- [TOOL-TABLE-SCHEMA.md](./TOOL-TABLE-SCHEMA.md) — mandatory table format
- [SOP-Navigation-and-Layout.md](./SOP-Navigation-and-Layout.md)

</details>

### Quick Access
- **Tools Overview** → [tools/_INDEX.md](./tools/_INDEX.md) (or INDEX.md once renamed)
- **Documentation & Guides** → [documentation/INDEX.md](./documentation/INDEX.md)
- **Schema Rules** → [TOOL-TABLE-SCHEMA.md](./TOOL-TABLE-SCHEMA.md)
- **This SOP** → [SOP-Navigation-and-Layout.md](./SOP-Navigation-and-Layout.md)
```

## 5. Linking Rules (Mandatory – no change)

- Internal file: `[shell-one-liners.md](./manuals-howtos-guides/shell-one-liners.md)`
- Internal folder: `[diagnostics-troubleshooting/](./network-engineering/diagnostics-troubleshooting/)`
- Schema: `[TOOL-TABLE-SCHEMA.md](../TOOL-TABLE-SCHEMA.md)`
- Upward: `↑ [Tools Overview](../_INDEX.md)` or `↑ [Root](../../README.md)`

## 6. Maintenance Checklist (When Adding/Editing – Updated)

- Create/update `INDEX.md` in every qualifying folder
- Build recursive contents list with relative hyperlinks
- Use tabular lists (bold bullets / definition style) instead of tables for index overviews
- Ensure tool-list .md files match [TOOL-TABLE-SCHEMA.md](../TOOL-TABLE-SCHEMA.md) exactly
- Update parent `INDEX.md` and root `README.md` when structure changes
- Use `<details>` liberally for deep recursion
- Commit message example: "feat: recursive INDEX.md for security/; tabular list conversion"

## 7. Future Improvements (Nice-to-Have)

- Rename `tools/_INDEX.md` → `tools/INDEX.md` for consistency
- Add item counts next to folders in recursive lists (e.g. `(12 tools)` )
- Consider a single `all-tools.md` A–Z list if repo becomes very large
- Explore GitHub Actions to auto-generate/update recursive INDEX files

Questions or deviations? Open an issue or PR referencing this SOP.

Happy building!
