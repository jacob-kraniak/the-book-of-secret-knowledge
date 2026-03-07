# CLI Tools
Curated, high-quality command-line utilities across sysadmin, security, networking, productivity, and development workflows.

## Shells & Prompting
Interactive shells, enhancers, prompts, plugins, fuzzy finders/jump tools

|Name|Vendor/Webpage|GitHub Repo|Brief Description|Tags|Latest Commit|
|---|---|---|---|---|---|
|GNU Bash|[https://www.gnu.org/software/bash/](https://www.gnu.org/software/bash/)|—|sh-compatible shell with ksh/csh-inspired features.|shell, bash, cli, scripting|2025-12|
|Zsh|[https://www.zsh.org/](https://www.zsh.org/)|—|Advanced interactive shell and scripting language.|shell, zsh, interactive, cli|2025-11|
|Starship|[https://starship.rs](https://starship.rs/)|[starship/starship](https://github.com/starship/starship)|Fast, minimal, highly customizable cross-shell prompt.|prompt, rust, cross-shell, productivity|2026-03-05|
|powerlevel10k|—|[romkatv/powerlevel10k](https://github.com/romkatv/powerlevel10k)|Very fast Zsh theme with extensive customization.|zsh, theme, prompt, performance|2024-01-26|
|Oh My Zsh|[https://ohmyz.sh/](https://ohmyz.sh/)|[ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)|Popular framework for Zsh configuration and plugins.|zsh, framework, plugins, productivity|2026-02|

### Shell Plug-ins

|Name|Vendor/Webpage|GitHub Repo|Brief Description|Tags|Latest Commit|
|---|---|---|---|---|---|
|z|—|[rupa/z](https://github.com/rupa/z)|Frecency-based directory jumper using cd history.|navigation, jump, shell|2023-12-09|
|fzf|—|[junegunn/fzf](https://github.com/junegunn/fzf)|General-purpose fuzzy finder for command-line use.|fuzzy, finder, cli, productivity|2026-03|
|zsh-autosuggestions|—|[zsh-users/zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)|Fish-style autosuggestions for Zsh.|zsh, plugin, autosuggest|2025-06|
|zsh-syntax-highlighting|—|[zsh-users/zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)|Fish-like syntax highlighting for Zsh.|zsh, plugin, highlighting|2025-04|

## Terminal & Multiplexing
- Multiplexers (tmux/screen), terminal emulators/utils, session managers

|Name|Vendor/Webpage|GitHub Repo|Brief Description|Tags|Latest Commit|
|---|---|---|---|---|---|
|ripgrep|—|[BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)|Recursively searches directories very fast (rg).|search, grep-alternative, rust|2026-02|
|fd|—|[sharkdp/fd](https://github.com/sharkdp/fd)|Simple, fast, user-friendly alternative to find.|find, filesystem, rust|2026-01|
|bat|—|[sharkdp/bat](https://github.com/sharkdp/bat)|cat clone with syntax highlighting and Git integration.|syntax-highlighter, viewer, rust|2026-03|
|delta|—|[dandavison/delta](https://github.com/dandavison/delta)|Beautiful syntax-highlighting pager for git diff.|diff, git, pager, rust|2026-02|

## Text & File Manipulation
- Editors (vim/neovim/micro), viewers (bat, hexyl), finders (fd, ripgrep), fuzzy (fzf), diff/pretty (delta), file ops (exa/lsd, dust, duf, ncdu)

## Filesystem & Disk
- Disk usage/analyzers, mount/umount helpers, secure delete/wipe, inotify tools

## System Monitoring & Diagnostics
- Process (htop/btop, glances, bottom), memory/CPU (nvtop if GPU), logs (lnav, goaccess), debuggers (strace, ltrace), perf tools

## Networking & Recon
### Core Utilities
- curl, wget, httpie, aria2, transmission-cli

### Scanning & Discovery
- nmap, masscan, RustScan, naabu, zmap

### Traffic Capture & Analysis
- tcpdump, tshark, termshark, wireshark-cli equivalents

### DNS & Subdomain
- subfinder, amass, dnsx, dnstwist, fierce

### Proxy / Tunneling / TOR
- proxychains, redsocks, tor, torsocks, chisel, bore

## Security & Crypto
- openssl, gnupg/gpg, age/sops, hashcat/john (if CLI-focused), secure-delete tools, password managers (pass, bitwarden-cli)

## Databases & Data
- sqlite3 utils, jq/yq (JSON/YAML), miller (CSV/TSV), csvkit, duckdb CLI

## Development & Versioning
- git cli helpers/extras (gh, git-extras, lazygit), diff-so-fancy/delta, tig

## Productivity & Misc
- Task runners (task, just), note-taking (jrnl, taskwarrior), calendars (calcurse), chat/IRC (weechat, irssi), RSS (newsboat)

## Benchmarking & Performance
- wrk, hyperfine, fio, sysbench

