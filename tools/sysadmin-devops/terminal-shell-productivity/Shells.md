# 🐚 Shells & Prompting

Interactive shells, modern enhancers, customizable prompts, plugins, fuzzy finders, and directory jump tools for improved CLI productivity and workflow.

| Name              | Vendor/Webpage              | GitHub Repo                                          | Brief Description                                                                 | Tags                                      | Latest Commit    | Creation Date   | Stars                  |
|-------------------|-----------------------------|------------------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|------------------|-----------------|------------------------|
| GNU Bash         | https://www.gnu.org/software/bash/ | —                                                    | sh-compatible shell with ksh/csh-inspired features; the default on most Unix-like systems. | shell, bash, cli, scripting, gnu          | 2025-12         | 1989            | —                      |
| Zsh              | https://www.zsh.org/       | —                                                    | Advanced interactive shell and powerful scripting language with extensive completion. | shell, zsh, interactive, cli, scripting   | 2025-11         | 1990            | —                      |
| Starship         | https://starship.rs        | [starship/starship](https://github.com/starship/starship) | Fast, minimal, highly customizable cross-shell prompt written in Rust.            | prompt, rust, cross-shell, productivity, customizable | 2026-03-05      | 2019            | 54.6k as of 2026-03    |
| powerlevel10k    | —                          | [romkatv/powerlevel10k](https://github.com/romkatv/powerlevel10k) | Very fast Zsh theme with extensive customization and instant prompt wizard.       | zsh, theme, prompt, performance, fast     | 2026-01-28      | 2019-03         | ~40k as of 2026-03     |
| Oh My Zsh        | https://ohmyz.sh/          | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | Popular community framework for Zsh configuration with 300+ plugins and 140+ themes. | zsh, framework, plugins, productivity, themes | 2026-03-06      | 2009            | 185k as of 2026-03     |

## Shell Plugins

Frecency jumpers, fuzzy finders, autosuggestions, syntax highlighting, and other lightweight Zsh extensions.

| Name                       | Vendor/Webpage | GitHub Repo                                          | Brief Description                                                                 | Tags                                      | Latest Commit    | Creation Date   | Stars                  |
|----------------------------|----------------|------------------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|------------------|-----------------|------------------------|
| z                         | —             | [rupa/z](https://github.com/rupa/z)                  | Frecency-based directory jumper using cd history for fast navigation.             | navigation, jump, shell, zsh, bash        | 2023-12-09      | ~2010           | ~16k as of 2026-03     |
| fzf                       | —             | [junegunn/fzf](https://github.com/junegunn/fzf)      | General-purpose command-line fuzzy finder for files, commands, git, etc.          | fuzzy, finder, cli, productivity, go      | 2026-03-07      | 2015            | 78.4k as of 2026-03    |
| zsh-autosuggestions       | —             | [zsh-users/zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions) | Fish-style autosuggestions for Zsh based on history.                              | zsh, plugin, autosuggest, completion      | 2025-06         | 2014            | ~30k as of 2026-03     |
| zsh-syntax-highlighting   | —             | [zsh-users/zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting) | Fish-like syntax highlighting for Zsh commands in the terminal.                   | zsh, plugin, highlighting, syntax         | 2025-04         | 2012            | ~20k as of 2026-03     |

## Terminal & Multiplexing Utils

Fast modern replacements for classic CLI tools (grep/find/cat/diff) often used in shells/terminals; includes search, navigation, viewing, and diffing enhancers.

| Name      | Vendor/Webpage | GitHub Repo                                          | Brief Description                                                                 | Tags                                      | Latest Commit    | Creation Date   | Stars                  |
|-----------|----------------|------------------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|------------------|-----------------|------------------------|
| ripgrep  | —             | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) | Recursively searches directories very fast while respecting .gitignore (rg command). | search, grep-alternative, rust, cli       | 2026-02         | 2016-02-27      | 60.6k as of 2026-03    |
| fd       | —             | [sharkdp/fd](https://github.com/sharkdp/fd)          | Simple, fast, user-friendly alternative to find with colorized output and ignores. | find, filesystem, rust, cli               | 2026-01         | ~2017           | ~35k as of 2026-03     |
| bat      | —             | [sharkdp/bat](https://github.com/sharkdp/bat)        | cat clone with syntax highlighting, Git integration, and line numbers.            | syntax-highlighter, viewer, rust, cli     | 2026-03         | ~2017           | ~50k as of 2026-03     |
| delta    | —             | [dandavison/delta](https://github.com/dandavison/delta) | Beautiful syntax-highlighting pager for git diff and other tools.                 | diff, git, pager, rust, cli               | 2026-02         | ~2019           | ~25k as of 2026-03     |
