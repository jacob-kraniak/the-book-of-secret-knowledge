# TOOL TABLE SCHEMA

Use this exact column order and formatting for all tool lists in the repository.

| Name | Vendor/Webpage | GitHub Repo | Brief Description | Tags | Latest Commit | Creation Date | Stars |

### Rules

- **Name**: plain text, consistent capitalization (match official project name / branding)
- **Vendor/Webpage**: official site URL or — (use — when primarily GitHub-based with no strong separate homepage)
- **GitHub Repo**: shortened markdown link in format `[owner/repo](https://github.com/owner/repo)` — only include if the project lives on GitHub
- **Brief Description**: exactly 1 sentence, <120 characters, ends with period.
- **Tags**: comma-separated lowercase tags in [brackets], 4–8 max; include functional + interface + scope + primary language(s) when relevant
- **Latest Commit**: `YYYY-MM-DD` preferred; or `~Month YYYY` (with optional note e.g. `(major release)` or `(security fix)`)
- **Creation Date** (new): repository creation date in `YYYY-MM-DD` format if GitHub-hosted; for very old / non-GitHub projects use earliest known public release year (e.g. `1991`) or approximate decade if exact date unavailable (e.g. `~mid-1990s`). Leave blank or use `—` if unknown/irrelevant.
- **Stars** (new): current GitHub star count in format `Xk` or `X.Yk` (e.g. `35.4k`, `812`) with optional "as of YYYY-MM" note if not very recent (e.g. `5.2k as of 2026-03`). Use `—` for non-GitHub projects.

### Guidance

- **Creation Date** is especially valuable for legacy / classic Unix tools, early security utilities, and projects from the 1990s–early 2000s to give historical perspective.
- **Stars** provides at-a-glance community adoption signal — useful for readers new to the field who want to prioritize widely trusted tools.
- When adding or updating entries, fetch Creation Date and Stars directly from the GitHub repo page or API if possible.
- For extremely old projects without GitHub presence (e.g. original tcpdump releases, early versions of OpenSSH), prefer the initial public release year in Creation Date and leave Stars as `—`.

### Example row (classic tool)

| Name | Vendor/Webpage | GitHub Repo | Brief Description | Tags | Latest Commit | Creation Date | Stars |
|------|----------------|-------------|-------------------|------|---------------|---------------|-------|
| Vim  | —              | [vim/vim](https://github.com/vim/vim) | Highly configurable text editor for efficiently creating and changing any kind of text. | editor, text, cli, sysadmin, c | 2026-03-01 (v9.1 patch) | 1991-11-02 | 35.4k |

This format keeps tables readable, adds meaningful context without clutter, and aligns with the goal of making the book more educational for beginners while respecting the heritage of many tools listed.
