# SOP: Repository Layout, Navigation & Index Files

**Purpose**  
This SOP defines the standard structure, naming conventions, linking rules, and maintenance practices for the *Book of Secret Knowledge* fork (JK_Revisions branch). The goal is to keep the repo highly navigable on GitHub, consistent across folders, and easy to extend as new categories/tools are added.

**Last Updated**: March 2026  
**Applies to**: All folders, especially `tools/`, `documentation/`, and root-level files

## 1. Core Principles

- **Navigation-first design** — Every folder with >2 subfolders or >3 .md files should have an `INDEX.md` file.
- **Hyperlinks everywhere** — All references to files, folders, external sites, GitHub repos, and the schema must be clickable.
- **Consistency over perfection** — Use the same patterns (naming, table styles, link formats) across the repo.
- **GitHub rendering** — Prefer native markdown features (`<details>`, tables, relative links) over code blocks for interactive elements.
- **Tool tables only** — All tool/resource lists follow [TOOL-TABLE-SCHEMA.md](./TOOL-TABLE-SCHEMA.md) exactly.

## 2. Naming Conventions

| File/Folder Type          | Recommended Name       | Notes / Alternatives |
|---------------------------|------------------------|----------------------|
| Navigation / overview file| `INDEX.md`             | Uppercase `I`. Use this instead of `README.md` in content-heavy folders to distinguish from regular docs. GitHub renders it as folder preview. |
| Legacy / old index        | `_INDEX.md` or `00_index.md` | Rename → `INDEX.md` when possible for cleaner sorting and visibility. |
| Tool/resource list files  | Lowercase-with-dashes.md | e.g. `dns-tools.md`, `shell-one-liners.md` |
| Personal section          | `my-contributions.md`  | Keep at `tools/` root |
| Schema reference          | `TOOL-TABLE-SCHEMA.md` | Root level, never move |

**Rule**: Avoid spaces in file names (use `-` or `_`). Encode special characters in links if needed (e.g. `%20` for space, `%26` for &).

## 3. Folder-Level INDEX.md Structure (Minimum Template)

Every `INDEX.md` should include:

```markdown
# [Category Name] Index

Short 1–2 sentence purpose of this folder.

All tool tables follow → [TOOL-TABLE-SCHEMA.md](../TOOL-TABLE-SCHEMA.md)

## Sub-categories & Files

| Section / Topic              | Description                                      | Link |
|------------------------------|--------------------------------------------------|------|
| Example Subfolder            | What it contains                                 | [subfolder/INDEX.md](./subfolder/INDEX.md) |
| Example File                 | Brief note                                       | [example-file.md](./example-file.md) |

### Quick Links / Backlinks
- [↑ Back to Tools Overview](../_INDEX.md) (or ../INDEX.md)
- [↑ Back to Root README.md](../../README.md)
```

Use `<details>` for long lists if desired.

## 4. Top-Level README.md Requirements

Must contain (at minimum, near the top):

- Brief mission/fork statement
- `<details><summary>` collapsible directory structure (indented markdown list with hyperlinks)
- **Quick Access** table linking to major entry points
- Reference to this SOP and the TOOL-TABLE-SCHEMA

Example snippet (update paths as needed):

```markdown
<details>
<summary>Repository Structure (click to expand)</summary>

- **tools/** — ...
  - [_INDEX.md](./tools/_INDEX.md) — ...
- ...

</details>

### Quick Access
| Area          | Link                                 |
|---------------|--------------------------------------|
| Tools         | [tools/_INDEX.md](./tools/_INDEX.md) |
| ...           | ...                                  |
```

## 5. Linking Rules (Mandatory)

| Context                     | Format / Example                                                                 |
|-----------------------------|----------------------------------------------------------------------------------|
| Internal file               | `[shell-one-liners.md](./manuals-howtos-guides/shell-one-liners.md)`            |
| Internal folder             | `[diagnostics-troubleshooting/](./network-engineering/diagnostics-troubleshooting/)` |
| Schema reference            | `[TOOL-TABLE-SCHEMA.md](../TOOL-TABLE-SCHEMA.md)`                               |
| GitHub repo in tool table   | `[trimstray/multitool](https://github.com/trimstray/multitool)`                 |
| Official site in tool table | `[Official Site](https://example.com)` or `—`                                   |
| Upward navigation           | `[↑ Tools Overview](../_INDEX.md)` or `[↑ Root](../../README.md)`               |

## 6. Maintenance Checklist (When Adding/Editing)

- [ ] Create or update `INDEX.md` in the folder if missing or outdated
- [ ] Add relative hyperlinks to all mentioned files/folders
- [ ] Ensure tool tables match [TOOL-TABLE-SCHEMA.md](./TOOL-TABLE-SCHEMA.md) columns exactly
- [ ] Update parent INDEX.md and top-level README.md if structure changes significantly
- [ ] Use `<details>` for long collapsible sections
- [ ] Commit message includes affected areas, e.g. "Add INDEX.md to security/; update README quick links"

## 7. Future Improvements (Nice-to-Have)

- Rename `tools/_INDEX.md` → `tools/INDEX.md`
- Add file/tool counts to overview tables
- Create `all-tools.md` (A–Z consolidated list) if repo grows very large
- Add badges (stars, last commit) to README.md
- Consider GitHub wiki for very long guides (keep core content in repo)

Questions or deviations? Open an issue or PR referencing this SOP.

Happy building!

This SOP is self-contained, actionable, and reinforces the patterns we've established. Once added, link to it from the top-level README.md (e.g. in the Quick Access table or at the bottom: "See [SOP-Navigation-and-Layout.md](./SOP-Navigation-and-Layout.md) for layout standards").

Let me know if you'd like tweaks (shorter version, more examples, move to a different location), or if the next step is generating INDEX.md for a specific subfolder like `tools/security/` or `tools/sysadmin-devops/`.