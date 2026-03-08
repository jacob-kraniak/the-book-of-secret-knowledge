## Active Development Branch: JK_Revisions

**This branch is under heavy revision — do not merge to main yet.**

- All recent work (since fork on 2026-03-03) is by @jacob-kraniak
- Upstream history (pre-2026 commits) remains from original trimstray repo for credit & context

**See only my changes:**
- [Commits by me on this branch](https://github.com/jacob-kraniak/the-book-of-secret-knowledge/commits/JK_Revisions?author=jacob-kraniak)
- [Full branch compare (if main diverges later)](https://github.com/jacob-kraniak/the-book-of-secret-knowledge/compare/main...JK_Revisions)

When ready: Plan to squash-merge or rebase + clean history into main.

## Fork Attribution & My Contributions

**Forked on 2026-03-03** from [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) (MIT licensed, last major upstream activity ~2024).
## Repository Contents

<details>
<summary>Click to expand full directory structure</summary>

- **documentation/** — Guides, how-tos, one-liners, cheat sheets, learning material
  - [INDEX.md](./documentation/INDEX.md) — Documentation overview
  - **learning-resources/**
    - [daily-knowledge-news.md](./documentation/learning-resources/daily-knowledge-news.md)
  - **manuals-howtos-guides/**
    - [shell-one-liners.md](./documentation/manuals-howtos-guides/shell-one-liners.md)
    - [shell-tricks-functions.md](./documentation/manuals-howtos-guides/shell-tricks-functions.md)
  - [other-cheat-sheets.md](./documentation/other-cheat-sheets.md)
  - readme - to refactor.md *(legacy — planned for migration)*

- **tools/** — Curated collections of tools across security, networking, sysadmin & devops
  - [_INDEX.md](./tools/_INDEX.md) — Tools overview (recommended rename → INDEX.md)
  - [my-contributions.md](./tools/my-contributions.md) — Personally added / heavily used tools
  - [system-services.md](./tools/system-services.md)
  - **network-engineering/**
    - **diagnostics-troubleshooting/** — Bandwidth & performance, tracing, online utilities, protocols
    - **dns-dhc-ipam/**
      - [dns-tools.md](./tools/network-engineering/dns-dhc-ipam/dns-tools.md)
    - **routing-bgp-ospf/**
      - [BGP & Routing Tools.md](./tools/network-engineering/routing-bgp-ospf/BGP%20%26%20Routing%20Tools.md)
  - **security/**
    - [Untitled.md](./tools/security/Untitled.md) *(to be reviewed / renamed)*
    - **pentest-recon-enum/**
      - [Packet Capture & Analysis.md](./tools/security/pentest-recon-enum/Packet%20Capture%20%26%20Analysis.md)
      - [Port Scanners & Network Discovery.md](./tools/security/pentest-recon-enum/Port%20Scanners%20%26%20Network%20Discovery.md)
      - [Recon & Threat Reputation.md](./tools/security/pentest-recon-enum/Recon%20%26%20Threat%20Reputation.md)
    - [ssl-tls-web-security.md](./tools/security/ssl-tls-web-security.md)
    - **vuln-analysis-exploitation/**
      - [Packet Crafting & Manipulation.md](./tools/security/vuln-analysis-exploitation/Packet%20Crafting%20%26%20Manipulation.md)
      - [Vulnerability & Exploit Databases.md](./tools/security/vuln-analysis-exploitation/Vulnerability%20%26%20Exploit%20Databases.md)
  - **sysadmin-devops/**
    - [Remote Access + SSH Clients.md](./tools/sysadmin-devops/Remote%20Access%20%2B%20SSH%20Clients.md)
    - **https-web-services/**
      - **benchmark-load/**
      - **browsers/**
      - **clients-inspectors/**
      - **security-hardening/**
    - **system-monitoring-tracing/**
      - [Log Analyzers.md](./tools/sysadmin-devops/system-monitoring-tracing/Log%20Analyzers.md)
    - **terminal-shell-productivity/**
      - [Files & Directories.md](./tools/sysadmin-devops/terminal-shell-productivity/Files%20%26%20Directories.md)
      - [Shells.md](./tools/sysadmin-devops/terminal-shell-productivity/Shells.md)
      - [Terminal Emulators.md](./tools/sysadmin-devops/terminal-shell-productivity/Terminal%20Emulators.md)
      - [Text Editors.md](./tools/sysadmin-devops/terminal-shell-productivity/Text%20Editors.md)

- **Meta & Configuration**
  - [.github/](./.github/)
  - [.obsidian/](./.obsidian/) — optional personal vault settings
  - [.gitignore](./.gitignore)
  - [.markdownlint.json](./.markdownlint.json)
  - [.markdownlintignore](./.markdownlintignore)
  - [Contributing.md](./Contributing.md)
  - [LICENSE.md](./LICENSE.md)
  - [README.md](./README.md) ← you are here
  - [TOOL-TABLE-SCHEMA.md](./TOOL-TABLE-SCHEMA.md) — format standard for all tool tables

</details>

### Quick Access

| Area                        | Focus                                              | Main Entry Point                                                            |
|-----------------------------|----------------------------------------------------|-----------------------------------------------------------------------------|
| Tools – Overview            | All categories & personal contributions            | [_INDEX.md](./tools/_INDEX.md)                                              |
| Security Tools              | Recon, scanning, TLS/web security, exploits        | [tools/security/](./tools/security/)                                        |
| Network Engineering         | Diagnostics, DNS/IPAM, BGP/OSPF/routing            | [tools/network-engineering/](./tools/network-engineering/)                  |
| SysAdmin / DevOps           | SSH, web services, monitoring, shell productivity  | [tools/sysadmin-devops/](./tools/sysadmin-devops/)                          |
| Documentation & Guides      | One-liners, cheat sheets, daily learning           | [documentation/INDEX.md](./documentation/INDEX.md)                          |
| My Contributions            | Personally vetted / added tools & notes            | [tools/my-contributions.md](./tools/my-contributions.md)                    |
| Tool Table Format           | Schema used in every tool list                     | [TOOL-TABLE-SCHEMA.md](./TOOL-TABLE-SCHEMA.md)                              |

All tool-list markdown files follow the structure and linking rules defined in [TOOL-TABLE-SCHEMA.md](./TOOL-TABLE-SCHEMA.md).

##### :black_small_square: Security

<p>
&nbsp;&nbsp; <a href="https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/5/html/deployment_guide/ch-selinux"><b>SELinux</b></a> - provides a flexible Mandatory Access Control (MAC) system built into the Linux kernel.<br>
&nbsp;&nbsp; <a href="https://wiki.ubuntu.com/AppArmor"><b>AppArmor</b></a> - proactively protects the operating system and applications from external or internal threats.<br>
&nbsp;&nbsp; <a href="https://github.com/grapheneX/grapheneX"><b>grapheneX</b></a> - Automated System Hardening Framework.<br>
&nbsp;&nbsp; <a href="https://github.com/dev-sec/"><b>DevSec Hardening Framework</b></a> - Security + DevOps: Automatic Server Hardening.<br>
</p>

##### :black_small_square: Auditing Tools

<p>
&nbsp;&nbsp; <a href="https://www.ossec.net/"><b>ossec</b></a> - actively monitoring all aspects of system activity with file integrity monitoring.<br>
&nbsp;&nbsp; <a href="https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/chap-system_auditing"><b>auditd</b></a> - provides a way to track security-relevant information on your system.<br>
&nbsp;&nbsp; <a href="https://www.nongnu.org/tiger/"><b>Tiger</b></a> - is a security tool that can be use both as a security audit and intrusion detection system.<br>
&nbsp;&nbsp; <a href="https://cisofy.com/lynis/"><b>Lynis</b></a> - battle-tested security tool for systems running Linux, macOS, or Unix-based operating system.<br>
&nbsp;&nbsp; <a href="https://github.com/rebootuser/LinEnum"><b>LinEnum</b></a> - scripted Local Linux Enumeration & Privilege Escalation Checks.<br>
&nbsp;&nbsp; <a href="https://github.com/installation/rkhunter"><b>Rkhunter</b></a> - scanner tool for Linux systems that scans backdoors, rootkits and local exploits on your systems.<br>
&nbsp;&nbsp; <a href="https://github.com/hasherezade/pe-sieve"><b>PE-sieve</b></a> - is a light-weight tool that helps to detect malware running on the system.<br>
&nbsp;&nbsp; <a href="https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite"><b>PEASS</b></a> - privilege escalation tools for Windows and Linux/Unix and MacOS.<br>
</p>

##### :black_small_square: Databases

<p>
&nbsp;&nbsp; <a href="https://github.com/xo/usql"><b>usql</b></a> - universal command-line interface for SQL databases.<br>
&nbsp;&nbsp; <a href="https://github.com/dbcli/pgcli"><b>pgcli</b></a> - postgres CLI with autocompletion and syntax highlighting.<br>
&nbsp;&nbsp; <a href="https://github.com/dbcli/mycli"><b>mycli</b></a> - terminal client for MySQL with autocompletion and syntax highlighting.<br>
&nbsp;&nbsp; <a href="https://github.com/dbcli/litecli"><b>litecli</b></a> - SQLite CLI with autocompletion and syntax highlighting.<br>
  &nbsp;&nbsp; <a href="https://github.com/dbcli/mssql-cli"><b>mssql-cli</b></a> - SQL Server CLI with autocompletion and syntax highlighting.<br>
&nbsp;&nbsp; <a href="https://github.com/osquery/osquery"><b>OSQuery</b></a> - is a SQL powered operating system instrumentation, monitoring, and analytics framework.<br>
&nbsp;&nbsp; <a href="https://github.com/ankane/pgsync"><b>pgsync</b></a> - sync data from one Postgres database to another.<br>
&nbsp;&nbsp; <a href="https://github.com/laixintao/iredis"><b>iredis</b></a> - a terminal client for redis with autocompletion and syntax highlighting.<br>
&nbsp;&nbsp; <a href="https://www.schemacrawler.com/diagramming.html"><b>SchemaCrawler</b></a> - generates an E-R diagram of your database.<br>
</p>

##### :black_small_square: TOR

<p>
&nbsp;&nbsp; <a href="https://github.com/GouveaHeitor/nipe"><b>Nipe</b></a> - script to make Tor Network your default gateway.<br>
&nbsp;&nbsp; <a href="https://github.com/trimstray/multitor"><b>multitor</b></a> - a tool that lets you create multiple TOR instances with a load-balancing.<br>
</p>

##### :black_small_square: Messengers/IRC Clients

<p>
&nbsp;&nbsp; <a href="https://irssi.org"><b>Irssi</b></a> - is a free open source terminal based IRC client.<br>
&nbsp;&nbsp; <a href="https://weechat.org/"><b>WeeChat</b></a> - is an extremely extensible and lightweight IRC client.<br>
</p>

##### :black_small_square: Productivity

<p>
&nbsp;&nbsp; <a href="https://taskwarrior.org"><b>taskwarrior</b></a> - task management system, todo list <br>
</p>

##### :black_small_square: Other

<p>
&nbsp;&nbsp; <a href="https://github.com/skx/sysadmin-util"><b>sysadmin-util</b></a> - tools for Linux/Unix sysadmins.<br>
&nbsp;&nbsp; <a href="http://inotify.aiken.cz/"><b>incron</b></a> - is an inode-based filesystem notification technology.<br>
&nbsp;&nbsp; <a href="https://github.com/axkibe/lsyncd"><b>lsyncd</b></a> - synchronizes local directories with remote targets (Live Syncing Daemon).<br>
&nbsp;&nbsp; <a href="https://github.com/rgburke/grv"><b>GRV</b></a> - is a terminal based interface for viewing Git repositories.<br>
&nbsp;&nbsp; <a href="https://jonas.github.io/tig/"><b>Tig</b></a> - text-mode interface for Git.<br>
&nbsp;&nbsp; <a href="https://github.com/tldr-pages/tldr"><b>tldr</b></a> - simplified and community-driven man pages.<br>
&nbsp;&nbsp; <a href="https://github.com/mholt/archiver"><b>archiver</b></a> - easily create and extract .zip, .tar, .tar.gz, .tar.bz2, .tar.xz, .tar.lz4, .tar.sz, and .rar.<br>
&nbsp;&nbsp; <a href="https://github.com/tj/commander.js"><b>commander.js</b></a> - minimal CLI creator in JavaScript.<br>
&nbsp;&nbsp; <a href="https://github.com/tomnomnom/gron"><b>gron</b></a> - make JSON greppable!<br>
&nbsp;&nbsp; <a href="https://github.com/itchyny/bed"><b>bed</b></a> - binary editor written in Go.<br>
</p>

#### GUI Tools &nbsp;[<sup>[TOC]</sup>](#anger-table-of-contents)



##### :black_small_square: Network

<p>
&nbsp;&nbsp; <a href="https://www.wireshark.org/"><b>Wireshark</b></a> - is the world’s foremost and widely-used network protocol analyzer.<br>
&nbsp;&nbsp; <a href="https://www.ettercap-project.org/"><b>Ettercap</b></a> - is a comprehensive network monitor tool.<br>
&nbsp;&nbsp; <a href="https://etherape.sourceforge.io/"><b>EtherApe</b></a> - is a graphical network monitoring solution.<br>
&nbsp;&nbsp; <a href="https://packetsender.com/"><b>Packet Sender</b></a> - is a networking utility for packet generation and built-in UDP/TCP/SSL client and servers.<br>
&nbsp;&nbsp; <a href="https://ostinato.org/"><b>Ostinato</b></a> - is a packet crafter and traffic generator.<br>
&nbsp;&nbsp; <a href="https://jmeter.apache.org/"><b>JMeter™</b></a> - open source software to load test functional behavior and measure performance.<br>
&nbsp;&nbsp; <a href="https://github.com/locustio/locust"><b>locust</b></a> - scalable user load testing tool written in Python.<br>
</p>

##### :black_small_square: Browsers

<p>
&nbsp;&nbsp; <a href="https://www.torproject.org/"><b>TOR Browser</b></a> - protect your privacy and defend yourself against network surveillance and traffic analysis.<br>
</p>

##### :black_small_square: Password Managers

<p>
&nbsp;&nbsp; <a href="https://keepassxc.org/"><b>KeePassXC</b></a> - store your passwords safely and auto-type them into your everyday websites and apps.<br>
&nbsp;&nbsp; <a href="https://bitwarden.com/"><b>Bitwarden</b></a> - open source password manager with built-in sync.<br>
&nbsp;&nbsp; <a href="https://github.com/dani-garcia/vaultwarden/"><b>Vaultwarden</b></a> - unofficial Bitwarden compatible server written in Rust.<br>
</p>

##### :black_small_square: Messengers/IRC Clients

<p>
&nbsp;&nbsp; <a href="https://hexchat.github.io/index.html"><b>HexChat</b></a> - is an IRC client based on XChat.<br>
&nbsp;&nbsp; <a href="https://pidgin.im/"><b>Pidgin</b></a> - is an easy to use and free chat client used by millions.<br>
</p>

##### :black_small_square: Messengers (end-to-end encryption)

<p>
&nbsp;&nbsp; <a href="https://www.signal.org/"><b>Signal</b></a> - is an encrypted communications app.<br>
&nbsp;&nbsp; <a href="https://wire.com/en/"><b>Wire</b></a> - secure messaging, file sharing, voice calls and video conferences.<br>
&nbsp;&nbsp; <a href="https://github.com/prof7bit/TorChat"><b>TorChat</b></a> - decentralized anonymous instant messenger on top of Tor Hidden Services.<br>
&nbsp;&nbsp; <a href="https://matrix.org/"><b>Matrix</b></a> - an open network for secure, decentralized, real-time communication.<br>
</p>

##### :black_small_square: Text editors

<p>
&nbsp;&nbsp; <a href="https://www.sublimetext.com/3"><b>Sublime Text</b></a> - is a lightweight, cross-platform code editor known for its speed, ease of use.<br>
&nbsp;&nbsp; <a href="https://code.visualstudio.com/"><b>Visual Studio Code</b></a> - an open-source and free source code editor developed by Microsoft.<br>
&nbsp;&nbsp; <a href="https://atom.io/"><b>Atom</b></a> - a hackable text editor for the 21st Century.<br>
</p>

#### Web Tools &nbsp;[<sup>[TOC]</sup>](#anger-table-of-contents)

##### :black_small_square: Browsers

<p>
&nbsp;&nbsp; <a href="https://www.ssllabs.com/ssltest/viewMyClient.html"><b>SSL/TLS Capabilities of Your Browser</b></a> - test your browser's SSL implementation.<br>
&nbsp;&nbsp; <a href="https://caniuse.com/"><b>Can I use</b></a> - provides up-to-date browser support tables for support of front-end web technologies.<br>
&nbsp;&nbsp; <a href="https://panopticlick.eff.org/"><b>Panopticlick 3.0</b></a> - is your browser safe against tracking?<br>
&nbsp;&nbsp; <a href="https://privacy.net/analyzer/"><b>Privacy Analyzer</b></a> - see what data is exposed from your browser.<br>
&nbsp;&nbsp; <a href="https://browserleaks.com/"><b>Web Browser Security</b></a> - it's all about Web Browser fingerprinting.<br>
&nbsp;&nbsp; <a href="https://www.howsmyssl.com/"><b>How's My SSL?</b></a> - help a web server developer learn what real world TLS clients were capable of.<br>
&nbsp;&nbsp; <a href="https://suche.org/sslClientInfo"><b>sslClientInfo</b></a> - client test (incl TLSv1.3 information).<br>
</p>


</p>

##### :black_small_square: HTTP Headers & Web Linters

<p>
&nbsp;&nbsp; <a href="https://securityheaders.com/"><b>Security Headers</b></a> - analyse the HTTP response headers (with rating system to the results).<br>
&nbsp;&nbsp; <a href="https://observatory.mozilla.org/"><b>Observatory by Mozilla</b></a> - set of tools to analyze your website.<br>
&nbsp;&nbsp; <a href="https://webhint.io/"><b>webhint</b></a> - is a linting tool that will help you with your site's accessibility, speed, security, and more.<br>
</p>

##### :black_small_square: DNS



##### :black_small_square: Mail

<p>
&nbsp;&nbsp; <a href="https://luxsci.com/smtp-tls-checker"><b>smtp-tls-checker</b></a> - check an email domain for SMTP TLS support.<br>
&nbsp;&nbsp; <a href="https://mxtoolbox.com/SuperTool.aspx"><b>MX Toolbox</b></a> - all of your MX record, DNS, blacklist and SMTP diagnostics in one integrated tool.<br>
&nbsp;&nbsp; <a href="https://www.checktls.com/index.html"><b>Secure Email</b></a> - complete email test tools for email technicians.<br>
&nbsp;&nbsp; <a href="http://www.blacklistalert.org/"><b>blacklistalert</b></a> - checks to see if your domain is on a Real Time Spam Blacklist.<br>
&nbsp;&nbsp; <a href="http://multirbl.valli.org/"><b>MultiRBL</b></a> - complete IP check for sending Mailservers.<br>
&nbsp;&nbsp; <a href="https://dkimvalidator.com/"><b>DKIM SPF & Spam Assassin Validator</b></a> - checks mail authentication and scores messages with Spam Assassin.<br>
</p>

##### :black_small_square: Encoders/Decoders and Regex testing

<p>
&nbsp;&nbsp; <a href="https://www.url-encode-decode.com/"><b>URL Encode/Decode</b></a> - tool from above to either encode or decode a string of text.<br>
&nbsp;&nbsp; <a href="https://uncoder.io/"><b>Uncoder</b></a> - the online translator for search queries on log data.<br>
&nbsp;&nbsp; <a href="https://regex101.com/"><b>Regex101</b></a> - online regex tester and debugger: PHP, PCRE, Python, Golang and JavaScript.<br>
&nbsp;&nbsp; <a href="https://regexr.com/"><b>RegExr</b></a> - online tool to learn, build, & test Regular Expressions (RegEx / RegExp).<br>
&nbsp;&nbsp; <a href="https://www.regextester.com/"><b>RegEx Testing</b></a> - online regex testing tool.<br>
&nbsp;&nbsp; <a href="https://www.regexpal.com/"><b>RegEx Pal</b></a> - online regex testing tool + other tools.<br>
&nbsp;&nbsp; <a href="https://gchq.github.io/CyberChef/"><b>The Cyber Swiss Army Knife</b></a> - a web app for encryption, encoding, compression and data analysis.<br>
</p>


##### :black_small_square: Privacy

<p>
&nbsp;&nbsp; <a href="https://www.privacyguides.org/"><b>privacyguides.org</b></a> - provides knowledge and tools to protect your privacy against global mass surveillance.<br>
&nbsp;&nbsp; <a href="https://dnsprivacy.org/wiki/display/DP/DNS+Privacy+Test+Servers"><b>DNS Privacy Test Servers</b></a> - DNS privacy recursive servers list (with a 'no logging' policy).<br>
</p>

##### :black_small_square: Code parsers/playgrounds

<p>
&nbsp;&nbsp; <a href="https://www.shellcheck.net/"><b>ShellCheck</b></a> - finds bugs in your shell scripts.<br>
&nbsp;&nbsp; <a href="https://explainshell.com/"><b>explainshell</b></a> - get interactive help texts for shell commands.<br>
&nbsp;&nbsp; <a href="https://jsbin.com/?html,output"><b>jsbin</b></a> - live pastebin for HTML, CSS & JavaScript, and more.<br>
&nbsp;&nbsp; <a href="https://codesandbox.io/"><b>CodeSandbox</b></a> - online code editor for web application development.<br>
&nbsp;&nbsp; <a href="http://sandbox.onlinephpfunctions.com/"><b>PHP Sandbox</b></a> - test your PHP code with this code tester.<br>
&nbsp;&nbsp; <a href="https://www.repl.it/"><b>Repl.it</b></a> - an instant IDE to learn, build, collaborate, and host all in one place.<br>
&nbsp;&nbsp; <a href="http://www.vclfiddle.net/"><b>vclFiddle</b></a> - is an online tool for experimenting with the Varnish Cache VCL.<br>
&nbsp;&nbsp; <a href="https://github.com/hadolint/hadolint"><b>Haskell Dockerfile Linter</b></a> - a smarter Dockerfile linter that helps you build best practice Docker images.<br>
</p>

##### :black_small_square: Performance

<p>
&nbsp;&nbsp; <a href="https://gtmetrix.com/"><b>GTmetrix</b></a> - analyze your site’s speed and make it faster.<br>
&nbsp;&nbsp; <a href="https://performance.sucuri.net/"><b>Sucuri loadtimetester</b></a> - test here the
performance of any of your sites from across the globe.<br>
&nbsp;&nbsp; <a href="https://tools.pingdom.com/"><b>Pingdom Tools</b></a> - analyze your site’s speed around the world.<br>
&nbsp;&nbsp; <a href="https://pingme.io/"><b>PingMe.io</b></a> - run website latency tests across multiple geographic regions.<br>
&nbsp;&nbsp; <a href="https://developers.google.com/speed/pagespeed/insights/"><b>PageSpeed Insights</b></a> - analyze your site’s speed and make it faster.<br>
&nbsp;&nbsp; <a href="https://web.dev/"><b>web.dev</b></a> - helps developers like you learn and apply the web's modern capabilities to your own sites and apps.<br>
&nbsp;&nbsp; <a href="https://github.com/GoogleChrome/lighthouse"><b>Lighthouse</b></a> - automated auditing, performance metrics, and best practices for the web.<br>
</p>

##### :black_small_square: Mass scanners (search engines)

<p>
&nbsp;&nbsp; <a href="https://censys.io/"><b>Censys</b></a> - platform that helps information security practitioners discover, monitor, and analyze devices.<br>
&nbsp;&nbsp; <a href="https://www.shodan.io/"><b>Shodan</b></a> - the world's first search engine for Internet-connected devices.<br>
&nbsp;&nbsp; <a href="https://2000.shodan.io/#/"><b>Shodan 2000</b></a> - this tool looks for randomly generated data from Shodan.<br>
&nbsp;&nbsp; <a href="https://viz.greynoise.io/table"><b>GreyNoise</b></a> - mass scanner such as Shodan and Censys.<br>
&nbsp;&nbsp; <a href="https://www.zoomeye.org/"><b>ZoomEye</b></a> - search engine for cyberspace that lets the user find specific network components.<br>
&nbsp;&nbsp; <a href="https://netograph.io/"><b>netograph</b></a> - tools to monitor and understand deep structure of the web.<br>
&nbsp;&nbsp; <a href="https://fofa.so/"><b>FOFA</b></a> - is a cyberspace search engine.<br>
&nbsp;&nbsp; <a href="https://www.onyphe.io/"><b>onyphe</b></a> - is a search engine for open-source and cyber threat intelligence data collected.<br>
&nbsp;&nbsp; <a href="https://intelx.io/"><b>IntelligenceX</b></a> - is a search engine and data archive.<br>
&nbsp;&nbsp; <a href="https://app.binaryedge.io/"><b>binaryedge</b></a> - it scan the entire internet space and create real-time threat intelligence streams and reports.<br>
&nbsp;&nbsp; <a href="https://spyse.com/"><b>Spyse</b></a> - Internet assets registry: networks, threats, web objects, etc.<br>
&nbsp;&nbsp; <a href="https://wigle.net/"><b>wigle</b></a> - is a submission-based catalog of wireless networks. All the networks. Found by Everyone.<br>
&nbsp;&nbsp; <a href="https://publicwww.com/"><b>PublicWWW</b></a> - find any alphanumeric snippet, signature or keyword in the web pages HTML, JS and CSS code.<br>
&nbsp;&nbsp; <a href="https://inteltechniques.com/index.html"><b>IntelTechniques</b></a> - this repository contains hundreds of online search utilities.<br>
&nbsp;&nbsp; <a href="https://hunter.io/"><b>hunter</b></a> - lets you find email addresses in seconds and connect with the people that matter for your business.<br>
&nbsp;&nbsp; <a href="https://ghostproject.fr/"><b>GhostProject?</b></a> - search by full email address or username.<br>
&nbsp;&nbsp; <a href="https://www.databreaches.live/"><b>databreaches</b></a> - was my email affected by data breach?<br>
&nbsp;&nbsp; <a href="https://weleakinfo.com"><b>We Leak Info</b></a> - world's fastest and largest data breach search engine.<br>
&nbsp;&nbsp; <a href="https://pulsedive.com/"><b>Pulsedive</b></a> - scans of malicious URLs, IPs, and domains, including port scans and web requests.<br>
&nbsp;&nbsp; <a href="https://buckets.grayhatwarfare.com/"><b>Buckets by Grayhatwarfar</b></a> - database with public search for Open Amazon S3 Buckets and their contents.<br>
&nbsp;&nbsp; <a href="https://vigilante.pw/"><b>Vigilante.pw</b></a> - the breached database directory.<br>
&nbsp;&nbsp; <a href="https://builtwith.com/"><b>builtwith</b></a> - find out what websites are built with.<br>
&nbsp;&nbsp; <a href="https://nerdydata.com/"><b>NerdyData</b></a> - search the web's source code for technologies, across millions of sites.<br>
&nbsp;&nbsp; <a href="http://zorexeye.com/"><b>zorexeye</b></a> - search for sites, images, apps, softwares & more.<br>
&nbsp;&nbsp; <a href="https://www.mmnt.net/"><b>Mamont's open FTP Index</b></a> - if a target has an open FTP site with accessible content it will be listed here.<br>
&nbsp;&nbsp; <a href="https://osintframework.com/"><b>OSINT Framework</b></a> - focused on gathering information from free tools or resources.<br>
&nbsp;&nbsp; <a href="https://www.maltiverse.com/search"><b>maltiverse</b></a> - is a service oriented to cybersecurity analysts.<br>
&nbsp;&nbsp; <a href="https://leakedsource.ru/main/"><b>Leaked Source</b></a> - is a collaboration of data found online in the form of a lookup.<br>
&nbsp;&nbsp; <a href="https://search.weleakinfo.com/"><b>We Leak Info</b></a> - to help everyday individuals secure their online life, avoiding getting hacked.<br>
&nbsp;&nbsp; <a href="https://pipl.com/"><b>pipl</b></a> - is the place to find the person behind the email address, social username or phone number.<br>
&nbsp;&nbsp; <a href="https://abuse.ch/"><b>abuse.ch</b></a> - is operated by a random swiss guy fighting malware for non-profit.<br>
&nbsp;&nbsp; <a href="http://malc0de.com/database/"><b>malc0de</b></a> - malware search engine.<br>
&nbsp;&nbsp; <a href="https://cybercrime-tracker.net/index.php"><b>Cybercrime Tracker</b></a> - monitors and tracks various malware families that are used to perpetrate cyber crimes.<br>
&nbsp;&nbsp; <a href="https://github.com/eth0izzle/shhgit/"><b>shhgit</b></a> - find GitHub secrets in real time.<br>
&nbsp;&nbsp; <a href="https://searchcode.com/"><b>searchcode</b></a> - helping you find real world examples of functions, API's and libraries.<br>
&nbsp;&nbsp; <a href="http://www.insecam.org/"><b>Insecam</b></a> - the world biggest directory of online surveillance security cameras.<br>
&nbsp;&nbsp; <a href="http://index-of.es/"><b>index-of</b></a> - contains great stuff like: security, hacking, reverse engineering, cryptography, programming etc.<br>
&nbsp;&nbsp; <a href="https://opendata.rapid7.com/"><b>Rapid7 Labs Open Data</b></a> - is a great resources of datasets from Project Sonar.<br>
&nbsp;&nbsp; <a href="https://webtechsurvey.com/common-response-headers"><b>Common Response Headers</b></a> - the largest database of HTTP response headers.<br>
&nbsp;&nbsp; <a href="https://labs.inquest.net"><b>InQuest Labs</b></a> - InQuest Labs is an open, interactive, and API driven data portal for security researchers.<br>
</p>

##### :black_small_square: Generators

<p>
&nbsp;&nbsp; <a href="https://thispersondoesnotexist.com/"><b>thispersondoesnotexist</b></a> - generate fake faces in one click - endless possibilities.<br>
&nbsp;&nbsp; <a href="https://generated.photos"><b>AI Generated Photos</b></a> - 100.000 AI generated faces.<br>
&nbsp;&nbsp; <a href="https://www.fakenamegenerator.com/"><b>fakenamegenerator</b></a> - your randomly generated identity.<br>
&nbsp;&nbsp; <a href="https://tools.intigriti.io/redirector/"><b>Intigriti Redirector</b></a> - open redirect/SSRF payload generator.<br>
</p>

##### :black_small_square: Passwords

<p>
&nbsp;&nbsp; <a href="https://haveibeenpwned.com/"><b>have i been pwned?</b></a> - check if you have an account that has been compromised in a data breach.<br>
&nbsp;&nbsp; <a href="https://www.dehashed.com/"><b>dehashed</b></a> - is a hacked database search engine.<br>
&nbsp;&nbsp; <a href="https://leakedsource.ru/"><b>Leaked Source</b></a> - is a collaboration of data found online in the form of a lookup.<br>
</p>

##### :black_small_square: CVE/Exploits databases



##### :black_small_square: Mobile apps scanners

<p>
&nbsp;&nbsp; <a href="https://www.immuniweb.com/mobile/"><b>ImmuniWeb® Mobile App Scanner</b></a> - test security and privacy of mobile apps (iOS & Android).<br>
&nbsp;&nbsp; <a href="https://vulnerabilitytest.quixxi.com/"><b>Quixxi</b></a> - free Mobile App Vulnerability Scanner for Android & iOS.<br>
&nbsp;&nbsp; <a href="https://www.ostorlab.co/scan/mobile/"><b>Ostorlab</b></a> - analyzes mobile application to identify vulnerabilities and potential weaknesses.<br>
</p>

##### :black_small_square: Private Search Engines

<p>
&nbsp;&nbsp; <a href="https://www.startpage.com/"><b>Startpage</b></a> - the world's most private search engine.<br>
&nbsp;&nbsp; <a href="https://searx.me/"><b>searX</b></a> - a privacy-respecting, hackable metasearch engine.<br>
&nbsp;&nbsp; <a href="https://darksearch.io/"><b>darksearch</b></a> - the 1st real Dark Web search engine.<br>
&nbsp;&nbsp; <a href="https://www.qwant.com/"><b>Qwant</b></a> - the search engine that respects your privacy.<br>
&nbsp;&nbsp; <a href="https://duckduckgo.com/"><b>DuckDuckGo</b></a> - the search engine that doesn't track you.<br>
&nbsp;&nbsp; <a href="https://swisscows.com/"><b>Swisscows</b></a> - privacy safe web search<br>
&nbsp;&nbsp; <a href="https://search.disconnect.me/"><b>Disconnect</b></a> - the search engine that anonymizes your searches.<br>
&nbsp;&nbsp; <a href="https://metager.org/"><b>MetaGer</b></a> - the search engine that uses anonymous proxy and hidden Tor branches.<br>
</p>

##### :black_small_square: Secure Webmail Providers

<p>
&nbsp;&nbsp; <a href="https://countermail.com/"><b>CounterMail</b></a> - online email service, designed to provide maximum security and privacy.<br>
&nbsp;&nbsp; <a href="http://mail2tor.com/"><b>Mail2Tor</b></a> - is a Tor Hidden Service that allows anyone to send and receive emails anonymously.<br>
&nbsp;&nbsp; <a href="https://tutanota.com/"><b>Tutanota</b></a> - is the world's most secure email service and amazingly easy to use.<br>
&nbsp;&nbsp; <a href="https://protonmail.com/"><b>Protonmail</b></a> - is the world's largest secure email service, developed by CERN and MIT scientists.<br>
&nbsp;&nbsp; <a href="https://www.startmail.com/en/"><b>Startmail</b></a> - private & encrypted email made easy.<br>
</p>

##### :black_small_square: Crypto

<p>
&nbsp;&nbsp; <a href="https://keybase.io/"><b>Keybase</b></a> - it's open source and powered by public-key cryptography.<br>
</p>

##### :black_small_square: PGP Keyservers

<p>
&nbsp;&nbsp; <a href="https://keyserver.ubuntu.com/"><b>SKS OpenPGP Key server</b></a> - services for the SKS keyservers used by OpenPGP.<br>
</p>

#### Systems/Services &nbsp;[<sup>[TOC]</sup>](#anger-table-of-contents)

##### :black_small_square: Operating Systems

<p>
&nbsp;&nbsp; <a href="http://www.slackware.com/"><b>Slackware</b></a> - the most "Unix-like" Linux distribution.<br>
&nbsp;&nbsp; <a href="https://www.openbsd.org/"><b>OpenBSD</b></a> - multi-platform 4.4BSD-based UNIX-like operating system.<br>
&nbsp;&nbsp; <a href="https://hardenedbsd.org/"><b>HardenedBSD</b></a> - HardenedBSD aims to implement innovative exploit mitigation and security solutions.<br>
&nbsp;&nbsp; <a href="https://www.kali.org/"><b>Kali Linux</b></a> - Linux distribution used for Penetration Testing, Ethical Hacking and network security assessments.<br>
&nbsp;&nbsp; <a href="https://www.parrotsec.org/"><b>Parrot Security OS</b></a> - cyber security GNU/Linux environment.<br>
&nbsp;&nbsp; <a href="https://www.backbox.org/"><b>Backbox Linux</b></a> - penetration test and security assessment oriented Ubuntu-based Linux distribution.<br>
&nbsp;&nbsp; <a href="https://blackarch.org/"><b>BlackArch</b></a> - is an Arch Linux-based penetration testing distribution for penetration testers.<br>
&nbsp;&nbsp; <a href="https://www.pentoo.ch/"><b>Pentoo</b></a> - is a security-focused livecd based on Gentoo.<br>
&nbsp;&nbsp; <a href="https://securityonion.net/"><b>Security Onion</b></a> - Linux distro for intrusion detection, enterprise security monitoring, and log management.<br>
&nbsp;&nbsp; <a href="https://tails.boum.org/"><b>Tails</b></a> - is a live system that aims to preserve your privacy and anonymity.<br>
&nbsp;&nbsp; <a href="https://github.com/vedetta-com/vedetta"><b>vedetta</b></a> - OpenBSD router boilerplate.<br>
&nbsp;&nbsp; <a href="https://www.qubes-os.org"><b>Qubes OS</b></a> - is a security-oriented OS that uses Xen-based virtualization.<br>
</p>

##### :black_small_square: HTTP(s) Services

<p>
&nbsp;&nbsp; <a href="https://varnish-cache.org/"><b>Varnish Cache</b></a> - HTTP accelerator designed for content-heavy dynamic web sites.<br>
&nbsp;&nbsp; <a href="https://nginx.org/"><b>Nginx</b></a> - open source web and reverse proxy server that is similar to Apache, but very light weight.<br>
&nbsp;&nbsp; <a href="https://openresty.org/en/"><b>OpenResty</b></a> - is a dynamic web platform based on NGINX and LuaJIT.<br>
&nbsp;&nbsp; <a href="https://github.com/alibaba/tengine"><b>Tengine</b></a> - a distribution of Nginx with some advanced features.<br>
&nbsp;&nbsp; <a href="https://caddyserver.com/"><b>Caddy Server</b></a> - is an open source, HTTP/2-enabled web server with HTTPS by default.<br>
&nbsp;&nbsp; <a href="https://www.haproxy.org/"><b>HAProxy</b></a> - the reliable, high performance TCP/HTTP load balancer.<br>
</p>

##### :black_small_square: DNS Services

<p>
&nbsp;&nbsp; <a href="https://nlnetlabs.nl/projects/unbound/about/"><b>Unbound</b></a> - validating, recursive, and caching DNS resolver (with TLS).<br>
&nbsp;&nbsp; <a href="https://www.knot-resolver.cz/"><b>Knot Resolver</b></a> - caching full resolver implementation, including both a resolver library and a daemon.<br>
&nbsp;&nbsp; <a href="https://www.powerdns.com/"><b>PowerDNS</b></a> - is an open source authoritative DNS server, written in C++ and licensed under the GPL.<br>
</p>

##### :black_small_square: Other Services

<p>
&nbsp;&nbsp; <a href="https://github.com/z3APA3A/3proxy"><b>3proxy</b></a> - tiny free proxy server.<br>
</p>

##### :black_small_square: Security/hardening

<p>
&nbsp;&nbsp; <a href="https://twitter.com/EmeraldOnion"><b>Emerald Onion</b></a> - is a 501(c)(3) nonprofit organization and transit internet service provider (ISP).<br>
&nbsp;&nbsp; <a href="https://github.com/pi-hole/pi-hole"><b>pi-hole</b></a> - the Pi-hole® is a DNS sinkhole that protects your devices from unwanted content.<br>
&nbsp;&nbsp; <a href="https://github.com/stamparm/maltrail"><b>maltrail</b></a> - malicious traffic detection system.<br>
&nbsp;&nbsp; <a href="https://github.com/Netflix/security_monkey"><b>security_monkey</b></a> - monitors AWS, GCP, OpenStack, and GitHub orgs for assets and their changes over time.<br>
&nbsp;&nbsp; <a href="https://github.com/firecracker-microvm/firecracker"><b>firecracker</b></a> - secure and fast microVMs for serverless computing.<br>
&nbsp;&nbsp; <a href="https://github.com/StreisandEffect/streisand"><b>streisand</b></a> - sets up a new server running your choice of WireGuard, OpenSSH, OpenVPN, and more.<br>
</p>

#### Networks &nbsp;[<sup>[TOC]</sup>](#anger-table-of-contents)

##### :black_small_square: Tools

<p>
&nbsp;&nbsp; <a href="https://www.capanalysis.net/ca/"><b>CapAnalysis</b></a> - web visual tool to analyze large amounts of captured network traffic (PCAP analyzer).<br>
&nbsp;&nbsp; <a href="https://github.com/digitalocean/netbox"><b>netbox</b></a> - IP address management (IPAM) and data center infrastructure management (DCIM) tool.<br>
</p>

##### :black_small_square: Labs

<p>
&nbsp;&nbsp; <a href="https://labs.networkreliability.engineering/"><b>NRE Labs</b></a> - learn automation by doing it. Right now, right here, in your browser.<br>
</p>

##### :black_small_square: Other

<p>
&nbsp;&nbsp; <a href="https://ee.lbl.gov/"><b>LBNL's Network Research Group</b></a> - home page of the Network Research Group (NRG).<br>
</p>

#### Containers/Orchestration &nbsp;[<sup>[TOC]</sup>](#anger-table-of-contents)

##### :black_small_square: CLI Tools

<p>
&nbsp;&nbsp; <a href="https://github.com/google/gvisor"><b>gvisor</b></a> - container runtime sandbox.<br>
&nbsp;&nbsp; <a href="https://github.com/bcicen/ctop"><b>ctop</b></a> - top-like interface for container metrics.<br>
</p>

##### :black_small_square: Web Tools

<p>
&nbsp;&nbsp; <a href="https://github.com/moby/moby"><b>Moby</b></a> - a collaborative project for the container ecosystem to assemble container-based system.<br>
&nbsp;&nbsp; <a href="https://traefik.io/"><b>Traefik</b></a> - open source reverse proxy/load balancer provides easier integration with Docker and Let's encrypt.<br>
&nbsp;&nbsp; <a href="https://github.com/Kong/kong"><b>kong</b></a> - The Cloud-Native API Gateway.<br>
&nbsp;&nbsp; <a href="https://github.com/rancher/rancher"><b>rancher</b></a> - complete container management platform.<br>
&nbsp;&nbsp; <a href="https://github.com/portainer/portainer"><b>portainer</b></a> - making Docker management easy.<br>
&nbsp;&nbsp; <a href="https://github.com/jwilder/nginx-proxy"><b>nginx-proxy</b></a> - automated nginx proxy for Docker containers using docker-gen.<br>
&nbsp;&nbsp; <a href="https://github.com/bunkerity/bunkerized-nginx"><b>bunkerized-nginx</b></a> - nginx docker image "secure by default".<br>
</p>

##### :black_small_square: Security

<p>
&nbsp;&nbsp; <a href="https://github.com/docker/docker-bench-security"><b>docker-bench-security</b></a> - checks for dozens of common best-practices around deploying Docker.<br>
&nbsp;&nbsp; <a href="https://github.com/aquasecurity/trivy"><b>trivy</b></a> - vulnerability scanner for containers, suitable for CI.<br>
&nbsp;&nbsp; <a href="https://goharbor.io/"><b>Harbor</b></a> - cloud native registry project that stores, signs, and scans content.<br>
&nbsp;&nbsp; <a href="https://houdini.secsi.io/"><b>Houdini</b></a> - hundreds of offensive and useful docker images for network intrusion.<br>
</p>

##### :black_small_square: Manuals/Tutorials/Best Practices

<p>
&nbsp;&nbsp; <a href="https://github.com/wsargent/docker-cheat-sheet"><b>docker-cheat-sheet</b></a> - a quick reference cheat sheet on Docker.<br>
&nbsp;&nbsp; <a href="https://github.com/veggiemonk/awesome-docker"><b>awesome-docker</b></a> - a curated list of Docker resources and projects.<br>
&nbsp;&nbsp; <a href="https://github.com/yeasy/docker_practice"><b>docker_practice</b></a> - learn and understand Docker technologies, with real DevOps practice!<br>
&nbsp;&nbsp; <a href="https://github.com/docker/labs"><b>labs
</b></a> - is a collection of tutorials for learning how to use Docker with various tools.<br>
&nbsp;&nbsp; <a href="https://github.com/jessfraz/dockerfiles"><b>dockerfiles</b></a> - various Dockerfiles I use on the desktop and on servers.<br>
&nbsp;&nbsp; <a href="https://github.com/kelseyhightower/kubernetes-the-hard-way"><b>kubernetes-the-hard-way</b></a> - bootstrap Kubernetes the hard way on Google Cloud Platform. No scripts.<br>
&nbsp;&nbsp; <a href="https://github.com/jamesward/kubernetes-the-easy-way"><b>kubernetes-the-easy-way</b></a> - bootstrap Kubernetes the easy way on Google Cloud Platform. No scripts.<br>
&nbsp;&nbsp; <a href="https://github.com/dennyzhang/cheatsheet-kubernetes-A4"><b>cheatsheet-kubernetes-A4</b></a> - Kubernetes CheatSheets in A4.<br>
&nbsp;&nbsp; <a href="https://github.com/kabachook/k8s-security"><b>k8s-security</b></a> - kubernetes security notes and best practices.<br>
&nbsp;&nbsp; <a href="https://learnk8s.io/production-best-practices/"><b>kubernetes-production-best-practices</b></a> - checklists with best-practices for production-ready Kubernetes.<br>
&nbsp;&nbsp; <a href="https://github.com/freach/kubernetes-security-best-practice"><b>kubernetes-production-best-practices</b></a> - kubernetes security - best practice guide.<br>
&nbsp;&nbsp; <a href="https://github.com/hjacobs/kubernetes-failure-stories"><b>kubernetes-failure-stories</b></a> - is a compilation of public failure/horror stories related to Kubernetes.<br>
</p>

#### Manuals/Howtos/Tutorials &nbsp;[<sup>[TOC]</sup>](#anger-table-of-contents)

##### :black_small_square: Shell/Command line

<p>
&nbsp;&nbsp; <a href="https://github.com/dylanaraps/pure-bash-bible"><b>pure-bash-bible</b></a> - is a collection of pure bash alternatives to external processes.<br>
&nbsp;&nbsp; <a href="https://github.com/dylanaraps/pure-sh-bible"><b>pure-sh-bible</b></a> - is a collection of pure POSIX sh alternatives to external processes.<br>
&nbsp;&nbsp; <a href="https://github.com/Idnan/bash-guide"><b>bash-guide</b></a> - is a guide to learn bash.<br>
&nbsp;&nbsp; <a href="https://github.com/denysdovhan/bash-handbook"><b>bash-handbook</b></a> - for those who wanna learn Bash.<br>
&nbsp;&nbsp; <a href="https://wiki.bash-hackers.org/start"><b>The Bash Hackers Wiki</b></a> - hold documentation of any kind about GNU Bash.<br>
&nbsp;&nbsp; <a href="http://pubs.opengroup.org/onlinepubs/9699919799/utilities/contents.html"><b>Shell & Utilities</b></a> - describes the commands offered to application programs by POSIX-conformant systems.<br>
&nbsp;&nbsp; <a href="https://github.com/jlevy/the-art-of-command-line"><b>the-art-of-command-line</b></a> - master the command line, in one page.<br>
&nbsp;&nbsp; <a href="https://google.github.io/styleguide/shellguide.html"><b>Shell Style Guide</b></a> - a shell style guide for Google-originated open-source projects.<br>
</p>

##### :black_small_square: Text Editors

<p>
&nbsp;&nbsp; <a href="https://vim.rtorr.com/"><b>Vim Cheat Sheet</b></a> - great multi language vim guide.<br>
</p>

##### :black_small_square: Python

<p>
&nbsp;&nbsp; <a href="https://awesome-python.com/"><b>Awesome Python</b></a> - a curated list of awesome Python frameworks, libraries, software and resources.<br>
&nbsp;&nbsp; <a href="https://github.com/gto76/python-cheatsheet"><b>python-cheatsheet</b></a> - comprehensive Python cheatsheet.<br>
&nbsp;&nbsp; <a href="https://www.pythoncheatsheet.org/"><b>pythoncheatsheet.org</b></a> - basic reference for beginner and advanced developers.<br>
</p>

##### :black_small_square: Sed & Awk & Other

<p>
&nbsp;&nbsp; <a href="https://posts.specterops.io/fawk-yeah-advanced-sed-and-awk-usage-parsing-for-pentesters-3-e5727e11a8ad?gi=c8f9506b26b6"><b>F’Awk Yeah!</b></a> - advanced sed and awk usage (Parsing for Pentesters 3).<br>
</p>

##### :black_small_square: \*nix & Network

<p>
&nbsp;&nbsp; <a href="https://www.cyberciti.biz/"><b>nixCraft</b></a> - linux and unix tutorials for new and seasoned sysadmin.<br>
&nbsp;&nbsp; <a href="https://www.tecmint.com/"><b>TecMint</b></a> - the ideal Linux blog for Sysadmins & Geeks.<br>
&nbsp;&nbsp; <a href="http://www.omnisecu.com/index.php"><b>Omnisecu</b></a> - free Networking, System Administration and Security tutorials.<br>
&nbsp;&nbsp; <a href="https://github.com/cirosantilli/linux-cheat"><b>linux-cheat</b></a> - Linux tutorials and cheatsheets. Minimal examples. Mostly user-land CLI utilities.<br>
&nbsp;&nbsp; <a href="https://github.com/snori74/linuxupskillchallenge"><b>linuxupskillchallenge</b></a> - learn the skills required to sysadmin.<br>
&nbsp;&nbsp; <a href="http://cb.vu/unixtoolbox.xhtml"><b>Unix Toolbox</b></a> - Unix/Linux/BSD commands and tasks which are useful for IT work or for advanced users.<br>
&nbsp;&nbsp; <a href="https://linux-kernel-labs.github.io/refs/heads/master/index.html"><b>Linux Kernel Teaching</b></a> - is a collection of lectures and labs Linux kernel topics.<br>
&nbsp;&nbsp; <a href="https://peteris.rocks/blog/htop/"><b>htop explained</b></a> - explanation of everything you can see in htop/top on Linux.<br>
&nbsp;&nbsp; <a href="https://linuxguideandhints.com/"><b>Linux Guide and Hints</b></a> - tutorials on system administration in Fedora and CentOS.<br>
&nbsp;&nbsp; <a href="https://github.com/NanXiao/strace-little-book"><b>strace-little-book</b></a> - a little book which introduces strace.<br>
&nbsp;&nbsp; <a href="https://github.com/goldshtn/linux-tracing-workshop"><b>linux-tracing-workshop</b></a> - examples and hands-on labs for Linux tracing tools workshops.<br>
&nbsp;&nbsp; <a href="https://github.com/bagder/http2-explained"><b>http2-explained</b></a> - a detailed document explaining and documenting HTTP/2.<br>
&nbsp;&nbsp; <a href="https://github.com/bagder/http3-explained"><b>http3-explained</b></a> - a document describing the HTTP/3 and QUIC protocols.<br>
&nbsp;&nbsp; <a href="https://www.manning.com/books/http2-in-action"><b>HTTP/2 in Action</b></a> - an excellent introduction to the new HTTP/2 standard.<br>
&nbsp;&nbsp; <a href="https://www.saminiir.com/lets-code-tcp-ip-stack-1-ethernet-arp/"><b>Let's code a TCP/IP stack</b></a> - great stuff to learn network and system programming at a deeper level.<br>
&nbsp;&nbsp; <a href="https://github.com/trimstray/nginx-admins-handbook"><b>Nginx Admin's Handbook</b></a> - how to improve NGINX performance, security and other important things.<br>
&nbsp;&nbsp; <a href="https://github.com/digitalocean/nginxconfig.io"><b>nginxconfig.io</b></a> - NGINX config generator on steroids.<br>
&nbsp;&nbsp; <a href="https://infosec.mozilla.org/guidelines/openssh"><b>openssh guideline</b></a> - is to help operational teams with the configuration of OpenSSH server and client.<br>
&nbsp;&nbsp; <a href="https://gravitational.com/blog/ssh-handshake-explained/"><b>SSH Handshake Explained</b></a> - is a relatively brief description of the SSH handshake.<br>
&nbsp;&nbsp; <a href="https://kb.isc.org/docs/using-this-knowledgebase"><b>ISC's Knowledgebase</b></a> - you'll find some general information about BIND 9, ISC DHCP, and Kea DHCP.<br>
&nbsp;&nbsp; <a href="https://packetlife.net/"><b>PacketLife.net</b></a> - a place to record notes while studying for Cisco's CCNP certification.<br>
</p>

##### :black_small_square: Microsoft

<p>
&nbsp;&nbsp; <a href="https://github.com/infosecn1nja/AD-Attack-Defense"><b>AD-Attack-Defense</b></a> - attack and defend active directory using modern post exploitation activity.<br>
</p>

##### :black_small_square: Large-scale systems

<p>
&nbsp;&nbsp; <a href="https://github.com/donnemartin/system-design-primer"><b>The System Design Primer</b></a> - learn how to design large-scale systems.<br>
&nbsp;&nbsp; <a href="https://github.com/binhnguyennus/awesome-scalability"><b>Awesome Scalability</b></a> - best practices in building High Scalability, High Availability, High Stability, and more.<br>
&nbsp;&nbsp; <a href="https://engineering.videoblocks.com/web-architecture-101-a3224e126947?gi=a896808d22a"><b>Web Architecture 101</b></a> - the basic architecture concepts.<br>
</p>

##### :black_small_square: System hardening

<p>
&nbsp;&nbsp; <a href="https://www.cisecurity.org/cis-benchmarks/"><b>CIS Benchmarks</b></a> - secure configuration settings for over 100 technologies, available as a free PDF.<br>
&nbsp;&nbsp; <a href="https://highon.coffee/blog/security-harden-centos-7/"><b>Security Harden CentOS 7</b></a> - this walks you through the steps required to security harden CentOS.<br>
&nbsp;&nbsp; <a href="https://www.lisenet.com/2017/centos-7-server-hardening-guide/"><b>CentOS 7 Server Hardening Guide</b></a> - great guide for hardening CentOS; familiar with OpenSCAP.<br>
&nbsp;&nbsp; <a href="https://github.com/decalage2/awesome-security-hardening"><b>awesome-security-hardening</b></a> - is a collection of security hardening guides, tools and other resources.<br>
&nbsp;&nbsp; <a href="https://github.com/trimstray/the-practical-linux-hardening-guide"><b>The Practical Linux Hardening Guide</b></a> - provides a high-level overview of hardening GNU/Linux systems.<br>
&nbsp;&nbsp; <a href="https://madaidans-insecurities.github.io/guides/linux-hardening.html"><b>Linux Hardening Guide</b></a> - how to harden Linux as much as possible for security and privacy.<br>
</p>

##### :black_small_square: Security & Privacy

<p>
&nbsp;&nbsp; <a href="https://www.hackingarticles.in/"><b>Hacking Articles</b></a> - LRaj Chandel's Security & Hacking Blog.<br>
&nbsp;&nbsp; <a href="https://github.com/toniblyx/my-arsenal-of-aws-security-tools"><b>AWS security tools</b></a> - make your AWS cloud environment more secure.<br>
&nbsp;&nbsp; <a href="https://inventory.rawsec.ml/index.html"><b>Rawsec's CyberSecurity Inventory</b></a> - an inventory of tools and resources about CyberSecurity.<br>
&nbsp;&nbsp; <a href="https://tls.ulfheim.net/"><b>The Illustrated TLS Connection</b></a> - every byte of a TLS connection explained and reproduced.<br>
&nbsp;&nbsp; <a href="https://github.com/ssllabs/research/wiki/SSL-and-TLS-Deployment-Best-Practices"><b>SSL Research</b></a> - SSL and TLS Deployment Best Practices by SSL Labs.<br>
&nbsp;&nbsp; <a href="http://selinuxgame.org/index.html"><b>SELinux Game</b></a> - learn SELinux by doing. Solve Puzzles, show skillz.<br>
&nbsp;&nbsp; <a href="https://smallstep.com/blog/everything-pki.html"><b>Certificates and PKI</b></a> - everything you should know about certificates and PKI but are too afraid to ask.<br>
&nbsp;&nbsp; <a href="https://appsecco.com/books/subdomain-enumeration/"><b>The Art of Subdomain Enumeration</b></a> - a reference for subdomain enumeration techniques.<br>
&nbsp;&nbsp; <a href="https://lifehacker.com/the-comprehensive-guide-to-quitting-google-1830001964"><b>Quitting Google</b></a> - the comprehensive guide to quitting Google.<br>
</p>

##### :black_small_square: Web Apps

<p>
&nbsp;&nbsp; <a href="https://www.owasp.org/index.php/Main_Page"><b>OWASP</b></a> - worldwide not-for-profit charitable organization focused on improving the security of software.<br>
&nbsp;&nbsp; <a href="https://www.owasp.org/index.php/Category:OWASP_Application_Security_Verification_Standard_Project"><b>OWASP ASVS 3.0.1</b></a> - OWASP Application Security Verification Standard Project.<br>
&nbsp;&nbsp; <a href="https://github.com/Santandersecurityresearch/asvs"><b>OWASP ASVS 3.0.1 Web App</b></a> - simple web app that helps developers understand the ASVS requirements.<br>
&nbsp;&nbsp; <a href="https://github.com/OWASP/ASVS/tree/master/4.0"><b>OWASP ASVS 4.0</b></a> - is a list of application security requirements or tests.<br>
&nbsp;&nbsp; <a href="https://www.owasp.org/index.php/OWASP_Testing_Project"><b>OWASP Testing Guide v4</b></a> - includes a "best practice" penetration testing framework.<br>
&nbsp;&nbsp; <a href="https://github.com/OWASP/DevGuide"><b>OWASP Dev Guide</b></a> - this is the development version of the OWASP Developer Guide.<br>
&nbsp;&nbsp; <a href="https://github.com/OWASP/wstg"><b>OWASP WSTG</b></a> - is a comprehensive open source guide to testing the security of web apps.<br>
&nbsp;&nbsp; <a href="https://www.owasp.org/index.php/OWASP_API_Security_Project"><b>OWASP API Security Project</b></a> - focuses specifically on the top ten vulnerabilities in API security.<br>
&nbsp;&nbsp; <a href="https://infosec.mozilla.org/guidelines/web_security.html"><b>Mozilla Web Security</b></a> - help operational teams with creating secure web applications.<br>
&nbsp;&nbsp; <a href="https://github.com/Netflix/security-bulletins"><b>security-bulletins</b></a> - security bulletins that relate to Netflix Open Source.<br>
&nbsp;&nbsp; <a href="https://github.com/shieldfy/API-Security-Checklist"><b>API-Security-Checklist</b></a> - security countermeasures when designing, testing, and releasing your API.<br>
&nbsp;&nbsp; <a href="https://enable-cors.org/index.html"><b>Enable CORS</b></a> - enable cross-origin resource sharing.<br>
&nbsp;&nbsp; <a href="https://appsecwiki.com/#/"><b>Application Security Wiki</b></a> - is an initiative to provide all application security related resources at one place.<br>
&nbsp;&nbsp; <a href="https://github.com/GrrrDog/weird_proxies/wiki"><b>Weird Proxies</b></a> - reverse proxy related attacks; it is a result of analysis of various proxies.<br>
&nbsp;&nbsp; <a href="https://dfir.it/blog/2015/08/12/webshell-every-time-the-same-purpose/"><b>Webshells</b></a> - great series about malicious payloads.<br>
&nbsp;&nbsp; <a href="https://portswigger.net/blog/practical-web-cache-poisoning"><b>Practical Web Cache Poisoning</b></a> - show you how to compromise websites by using esoteric web features.<br>
&nbsp;&nbsp; <a href="https://github.com/bl4de/research/tree/master/hidden_directories_leaks"><b>Hidden directories and files</b></a> - as a source of sensitive information about web application.<br>
&nbsp;&nbsp; <a href="https://bo0om.ru/en/"><b>Explosive blog</b></a> - great blog about cybersec and pentests.<br>
&nbsp;&nbsp; <a href="https://www.netsparker.com/security-cookies-whitepaper/"><b>Security Cookies</b></a> - this paper will take a close look at cookie security.<br>
&nbsp;&nbsp; <a href="https://github.com/GitGuardian/APISecurityBestPractices"><b>APISecurityBestPractices</b></a> - help you keep secrets (API keys, db credentials, certificates) out of source code.<br>
</p>

##### :black_small_square: All-in-one

<p>
&nbsp;&nbsp; <a href="https://lzone.de/cheat-sheet/"><b>LZone Cheat Sheets</b></a> - all cheat sheets.<br>
&nbsp;&nbsp; <a href="https://github.com/rstacruz/cheatsheets"><b>Dan’s Cheat Sheets’s</b></a> - massive cheat sheets documentation.<br>
&nbsp;&nbsp; <a href="https://devhints.io/"><b>Rico's cheatsheets</b></a> - this is a modest collection of cheatsheets.<br>
&nbsp;&nbsp; <a href="https://devdocs.io/"><b>DevDocs API</b></a> - combines multiple API documentations in a fast, organized, and searchable interface.<br>
&nbsp;&nbsp; <a href="https://cheat.sh/"><b>cheat.sh</b></a> - the only cheat sheet you need.<br>
&nbsp;&nbsp; <a href="https://gnulinux.guru/"><b>gnulinux.guru</b></a> - collection of cheat sheets about bash, vim and networking.<br>
&nbsp;&nbsp; <a href="https://andreasbm.github.io/web-skills/"><b>Web Skills</b></a> - visual overview of useful skills to learn as a web developer.<br>
</p>

##### :black_small_square: Ebooks

<p>
&nbsp;&nbsp; <a href="https://github.com/EbookFoundation/free-programming-books"><b>free-programming-books</b></a> - list of free learning resources in many languages.<br>
</p>

##### :black_small_square: Other

<p>
&nbsp;&nbsp; <a href="https://bitvijays.github.io/LFC-VulnerableMachines.html"><b>CTF Series : Vulnerable Machines</b></a> - the steps below could be followed to find vulnerabilities and exploits.<br>
&nbsp;&nbsp; <a href="https://github.com/manoelt/50M_CTF_Writeup"><b>50M_CTF_Writeup</b></a> - $50 million CTF from Hackerone - writeup.<br>
&nbsp;&nbsp; <a href="https://github.com/j00ru/ctf-tasks"><b>ctf-tasks</b></a> - an archive of low-level CTF challenges developed over the years.<br>
&nbsp;&nbsp; <a href="https://hshrzd.wordpress.com/how-to-start/"><b>How to start RE/malware analysis?</b></a> - collection of some hints and useful links for the beginners.<br>
&nbsp;&nbsp; <a href="http://www.kegel.com/c10k.html"><b>The C10K problem</b></a> - it's time for web servers to handle ten thousand clients simultaneously, don't you think?<br>
&nbsp;&nbsp; <a href="https://blog.benjojo.co.uk/post/why-is-ethernet-mtu-1500"><b>How 1500 bytes became the MTU of the internet</b></a> - great story about the Maximum Transmission Unit.<br>
&nbsp;&nbsp; <a href="http://poormansprofiler.org/"><b>poor man's profiler</b></a> - like dtrace's don't really provide methods to see what programs are blocking on.<br>
&nbsp;&nbsp; <a href="https://nickcraver.com/blog/2017/05/22/https-on-stack-overflow/"><b>HTTPS on Stack Overflow</b></a> - this is the story of a long journey regarding the implementation of SSL.<br>
&nbsp;&nbsp; <a href="https://drawings.jvns.ca/"><b>Julia's Drawings</b></a> - some drawings about programming and unix world, zines about systems & debugging tools.<br>
&nbsp;&nbsp; <a href="https://github.com/corkami/collisions"><b>Hash collisions</b></a> - this great repository is focused on hash collisions exploitation.<br>
&nbsp;&nbsp; <a href="https://github.com/in3rsha/sha256-animation"><b>sha256-animation</b></a> - animation of the SHA-256 hash function in your terminal.<br>
&nbsp;&nbsp; <a href="https://sha256algorithm.com/"><b>sha256algorithm</b></a> - sha256 algorithm explained online step by step visually.<br>
&nbsp;&nbsp; <a href="https://labs.ripe.net/Members/cteusche/bgp-meets-cat"><b>BGP Meets Cat</b></a> - after 3072 hours of manipulating BGP, Job Snijders has succeeded in drawing a Nyancat.<br>
&nbsp;&nbsp; <a href="https://github.com/benjojo/bgp-battleships"><b>bgp-battleships</b></a> - playing battleships over BGP.<br>
&nbsp;&nbsp; <a href="https://github.com/alex/what-happens-when"><b>What happens when...</b></a> - you type google.com into your browser and press enter?<br>
&nbsp;&nbsp; <a href="https://github.com/vasanthk/how-web-works"><b>how-web-works</b></a> - based on the 'What happens when...' repository.<br>
&nbsp;&nbsp; <a href="https://robertheaton.com/2018/11/28/https-in-the-real-world/"><b>HTTPS in the real world</b></a> - great tutorial explain how HTTPS works in the real world.<br>
&nbsp;&nbsp; <a href="https://about.gitlab.com/2018/11/14/how-we-spent-two-weeks-hunting-an-nfs-bug/"><b>Gitlab and NFS bug</b></a> - how we spent two weeks hunting an NFS bug in the Linux kernel.<br>
&nbsp;&nbsp; <a href="https://about.gitlab.com/2017/02/10/postmortem-of-database-outage-of-january-31/"><b>Gitlab melts down</b></a> - postmortem on the database outage of January 31 2017 with the lessons we learned.<br>
&nbsp;&nbsp; <a href="http://www.catb.org/esr/faqs/hacker-howto.html"><b>How To Become A Hacker</b></a> - if you want to be a hacker, keep reading.<br>
&nbsp;&nbsp; <a href="http://ithare.com/infographics-operation-costs-in-cpu-clock-cycles/"><b>Operation Costs in CPU</b></a> - should help to estimate costs of certain operations in CPU clocks.<br>
&nbsp;&nbsp; <a href="https://cstack.github.io/db_tutorial/"><b>Let's Build a Simple Database</b></a> - writing a sqlite clone from scratch in C.<br>
&nbsp;&nbsp; <a href="https://djhworld.github.io/post/2019/05/21/i-dont-know-how-cpus-work-so-i-simulated-one-in-code/"><b>simple-computer</b></a> - great resource to understand how computers work under the hood.<br>
&nbsp;&nbsp; <a href="https://www.troyhunt.com/working-with-154-million-records-on/"><b>The story of "Have I been pwned?"</b></a> - working with 154 million records on Azure Table Storage.<br>
&nbsp;&nbsp; <a href="https://www.top500.org/"><b>TOP500 Supercomputers</b></a> - shows the 500 most powerful commercially available computer systems.<br>
&nbsp;&nbsp; <a href="https://www.shellntel.com/blog/2017/2/8/how-to-build-a-8-gpu-password-cracker"><b>How to build a 8 GPU password cracker</b></a> - hours of frustration like desktop components do.<br>
&nbsp;&nbsp; <a href="https://home.cern/science/computing"><b>CERN Data Centre</b></a> - 3D visualizations of the CERN computing environments (and more).<br>
&nbsp;&nbsp; <a href="http://howfuckedismydatabase.com/"><b>How fucked is my database</b></a> - evaluate how fucked your database is with this handy website.<br>
&nbsp;&nbsp; <a href="https://krisbuytaert.be/blog/linux-troubleshooting-101-2016-edition/index.html"><b>Linux Troubleshooting 101 , 2016 Edition</b></a> - everything is a DNS Problem...<br>
&nbsp;&nbsp; <a href="https://open.buffer.com/5-whys-process/"><b>Five Whys</b></a> - you know what the problem is, but you cannot solve it?<br>
&nbsp;&nbsp; <a href="https://gvnshtn.com/maersk-me-notpetya/"><b>Maersk, me & notPetya</b></a> - how did ransomware successfully hijack hundreds of domain controllers?<br>
&nbsp;&nbsp; <a href="https://howhttps.works/"><b>howhttps.works</b></a> - how HTTPS works ...in a comic!<br>
&nbsp;&nbsp; <a href="https://howdns.works/"><b>howdns.works</b></a> - a fun and colorful explanation of how DNS works.<br>
&nbsp;&nbsp; <a href="https://postgresqlco.nf/en/doc/param/"><b>POSTGRESQLCO.NF</b></a> - your postgresql.conf documentation and recommendations.<br>
</p>

#### Inspiring Lists &nbsp;[<sup>[TOC]</sup>](#anger-table-of-contents)

##### :black_small_square: SysOps/DevOps

<p>
&nbsp;&nbsp; <a href="https://github.com/kahun/awesome-sysadmin"><b>Awesome Sysadmin</b></a> - amazingly awesome open source sysadmin resources.<br>
&nbsp;&nbsp; <a href="https://github.com/alebcay/awesome-shell"><b>Awesome Shell</b></a> - awesome command-line frameworks, toolkits, guides and gizmos.<br>
&nbsp;&nbsp; <a href="https://github.com/learnbyexample/Command-line-text-processing"><b>Command-line-text-processing</b></a> - finding text to search and replace, sorting to beautifying, and more.<br>
&nbsp;&nbsp; <a href="https://github.com/caesar0301/awesome-pcaptools"><b>Awesome Pcaptools</b></a> - collection of tools developed by other researchers to process network traces.<br>
&nbsp;&nbsp; <a href="https://github.com/zoidbergwill/awesome-ebpf"><b>awesome-ebpf</b></a> - a curated list of awesome projects related to eBPF.<br>
&nbsp;&nbsp; <a href="https://github.com/leandromoreira/linux-network-performance-parameters"><b>Linux Network Performance</b></a> - where some of the network sysctl variables fit into the Linux/Kernel network flow.<br>
&nbsp;&nbsp; <a href="https://github.com/dhamaniasad/awesome-postgres"><b>Awesome Postgres</b></a> - list of awesome PostgreSQL software, libraries, tools and resources.<br>
&nbsp;&nbsp; <a href="https://github.com/enochtangg/quick-SQL-cheatsheet"><b>quick-SQL-cheatsheet</b></a> - a quick reminder of all SQL queries and examples on how to use them.<br>
&nbsp;&nbsp; <a href="https://github.com/Kickball/awesome-selfhosted"><b>Awesome-Selfhosted</b></a> - list of Free Software network services and web applications which can be hosted locally.<br>
&nbsp;&nbsp; <a href="https://wiki.archlinux.org/index.php/List_of_applications"><b>List of applications</b></a> - huge list of apps sorted by category, as a reference for those looking for packages.<br>
&nbsp;&nbsp; <a href="https://github.com/InterviewMap/CS-Interview-Knowledge-Map"><b>CS-Interview-Knowledge-Map</b></a> - build the best interview map.<br>
&nbsp;&nbsp; <a href="https://github.com/Tikam02/DevOps-Guide"><b>DevOps-Guide</b></a> - DevOps Guide from basic to advanced with Interview Questions and Notes.<br>
&nbsp;&nbsp; <a href="https://issue.freebsdfoundation.org/publication/?m=33057&l=1&view=issuelistBrowser"><b>FreeBSD Journal</b></a> - it is a great list of periodical magazines about FreeBSD and other important things.<br>
&nbsp;&nbsp; <a href="https://github.com/bregman-arie/devops-interview-questions"><b>devops-interview-questions</b></a> - contains interview questions on various DevOps and SRE related topics.<br></p>

##### :black_small_square: Developers

<p>
&nbsp;&nbsp; <a href="https://github.com/kamranahmedse/developer-roadmap"><b>Web Developer Roadmap</b></a> - roadmaps, articles and resources to help you choose your path, learn and improve.<br>
&nbsp;&nbsp; <a href="https://github.com/thedaviddias/Front-End-Checklist"><b>Front-End-Checklist</b></a> - the perfect Front-End Checklist for modern websites and meticulous developers.<br>
&nbsp;&nbsp; <a href="https://github.com/thedaviddias/Front-End-Performance-Checklist"><b>Front-End-Performance-Checklist</b></a> - Front-End Performance Checklist that runs faster than the others.<br>
&nbsp;&nbsp; <a href="https://rszalski.github.io/magicmethods/"><b>Python's Magic Methods</b></a> - what are magic methods? They're everything in object-oriented Python.<br>
&nbsp;&nbsp; <a href="https://github.com/satwikkansal/wtfpython"><b>wtfpython</b></a> - a collection of surprising Python snippets and lesser-known features.<br>
&nbsp;&nbsp; <a href="https://github.com/twhite96/js-dev-reads"><b>js-dev-reads</b></a> - a list of books and articles for the discerning web developer to read.<br>
&nbsp;&nbsp; <a href="https://github.com/RomuloOliveira/commit-messages-guide"><b>Commit messages guide</b></a> - a guide to understand the importance of commit messages.<br>
</p>

##### :black_small_square: Security/Pentesting

<p>
&nbsp;&nbsp; <a href="https://github.com/qazbnm456/awesome-web-security"><b>Awesome Web Security</b></a> - a curated list of Web Security materials and resources.<br>
&nbsp;&nbsp; <a href="https://github.com/joe-shenouda/awesome-cyber-skills"><b>awesome-cyber-skills</b></a> - a curated list of hacking environments where you can train your cyber skills.<br>
&nbsp;&nbsp; <a href="https://github.com/devsecops/awesome-devsecops"><b>awesome-devsecops</b></a> - an authoritative list of awesome devsecops tools.<br>
&nbsp;&nbsp; <a href="https://github.com/jivoi/awesome-osint"><b>awesome-osint</b></a> - is a curated list of amazingly awesome OSINT.<br>
&nbsp;&nbsp; <a href="https://github.com/HolyBugx/HolyTips"><b>HolyTips</b></a> - tips and tutorials on Bug Bounty Hunting and Web App Security.<br>
&nbsp;&nbsp; <a href="https://github.com/hslatman/awesome-threat-intelligence"><b>awesome-threat-intelligence</b></a> - a curated list of Awesome Threat Intelligence resources.<br>
&nbsp;&nbsp; <a href="https://github.com/infosecn1nja/Red-Teaming-Toolkit"><b>Red-Teaming-Toolkit</b></a> - a collection of open source and commercial tools that aid in red team operations.<br>
&nbsp;&nbsp; <a href="https://github.com/snoopysecurity/awesome-burp-extensions"><b>awesome-burp-extensions</b></a> - a curated list of amazingly awesome Burp Extensions.<br>
&nbsp;&nbsp; <a href="https://github.com/Hack-with-Github/Free-Security-eBooks"><b>Free Security eBooks</b></a> - list of a Free Security and Hacking eBooks.<br>
&nbsp;&nbsp; <a href="https://github.com/yeahhub/Hacking-Security-Ebooks"><b>Hacking-Security-Ebooks</b></a> - top 100 Hacking & Security E-Books.<br>
&nbsp;&nbsp; <a href="https://github.com/nikitavoloboev/privacy-respecting"><b>privacy-respecting</b></a> - curated list of privacy respecting services and software.<br>
&nbsp;&nbsp; <a href="https://github.com/wtsxDev/reverse-engineering"><b>reverse-engineering</b></a> - list of awesome reverse engineering resources.<br>
&nbsp;&nbsp; <a href="https://github.com/michalmalik/linux-re-101"><b>linux-re-101</b></a> - a collection of resources for linux reverse engineering.<br>
&nbsp;&nbsp; <a href="https://github.com/onethawt/reverseengineering-reading-list"><b>reverseengineering-reading-list</b></a> - a list of Reverse Engineering articles, books, and papers.<br>
&nbsp;&nbsp; <a href="https://github.com/0xInfection/Awesome-WAF"><b>Awesome-WAF</b></a> - a curated list of awesome web-app firewall (WAF) stuff.<br>
&nbsp;&nbsp; <a href="https://github.com/jakejarvis/awesome-shodan-queries"><b>awesome-shodan-queries</b></a> - interesting, funny, and depressing search queries to plug into shodan.io.<br>
&nbsp;&nbsp; <a href="https://github.com/danielmiessler/RobotsDisallowed"><b>RobotsDisallowed</b></a> - a curated list of the most common and most interesting robots.txt disallowed directories.<br>
&nbsp;&nbsp; <a href="https://github.com/Kayzaks/HackingNeuralNetworks"><b>HackingNeuralNetworks</b></a> - is a small course on exploiting and defending neural networks.<br>
&nbsp;&nbsp; <a href="https://gist.github.com/joepie91/7e5cad8c0726fd6a5e90360a754fc568"><b>wildcard-certificates</b></a> - why you probably shouldn't use a wildcard certificate.<br>
&nbsp;&nbsp; <a href="https://gist.github.com/joepie91/5a9909939e6ce7d09e29"><b>Don't use VPN services</b></a> -  which is what every third-party "VPN provider" does.<br>
&nbsp;&nbsp; <a href="https://github.com/InQuest/awesome-yara"><b>awesome-yara</b></a> - a curated list of awesome YARA rules, tools, and people.<br>
&nbsp;&nbsp; <a href="https://github.com/drduh/macOS-Security-and-Privacy-Guide"><b>macOS-Security-and-Privacy-Guide</b></a> - guide to securing and improving privacy on macOS.<br>
&nbsp;&nbsp; <a href="https://github.com/usnistgov/macos_security"><b>macos_security</b></a> - macOS Security Compliance Project.<br>
&nbsp;&nbsp; <a href="https://github.com/PaulSec/awesome-sec-talks"><b>awesome-sec-talks</b></a> - is a collected list of awesome security talks.<br>
&nbsp;&nbsp; <a href="https://github.com/k4m4/movies-for-hackers"><b>Movies for Hackers</b></a> - list of movies every hacker & cyberpunk must watch.<br>
&nbsp;&nbsp; <a href="https://github.com/danieldizzy/Cryptography_1"><b>Cryptography_1</b></a> - materials used whilst taking Prof. Dan Boneh Stanford Crypto course.<br>
&nbsp;&nbsp; <a href="https://github.com/ashutosh1206/Crypton"><b>Crypton</b></a> - library to learn and practice Offensive and Defensive Cryptography.<br>
</p>

##### :black_small_square: Other

<p>
&nbsp;&nbsp; <a href="https://www.cheatography.com/"><b>Cheatography</b></a> - over 3,000 free cheat sheets, revision aids and quick references.<br>
&nbsp;&nbsp; <a href="https://github.com/mre/awesome-static-analysis"><b>awesome-static-analysis</b></a> - static analysis tools for all programming languages.<br>
&nbsp;&nbsp; <a href="https://github.com/ossu/computer-science"><b>computer-science</b></a> - path to a free self-taught education in Computer Science.<br>
&nbsp;&nbsp; <a href="https://github.com/danluu/post-mortems"><b>post-mortems</b></a> - is a collection of postmortems (config errors, hardware failures, and more).<br>
&nbsp;&nbsp; <a href="https://github.com/danistefanovic/build-your-own-x"><b>build-your-own-x</b></a> - build your own (insert technology here).<br>
&nbsp;&nbsp; <a href="https://github.com/rby90/Project-Based-Tutorials-in-C"><b>Project-Based-Tutorials-in-C</b></a> - is a curated list of project-based tutorials in C.<br>
&nbsp;&nbsp; <a href="https://github.com/kylelobo/The-Documentation-Compendium"><b>The-Documentation-Compendium</b></a> - various README templates & tips on writing high-quality documentation.<br>
&nbsp;&nbsp; <a href="https://github.com/mahmoud/awesome-python-applications"><b>awesome-python-applications</b></a> - free software that works great, and also happens to be open-source Python.<br>
&nbsp;&nbsp; <a href="https://github.com/awesomedata/awesome-public-datasets"><b>awesome-public-datasets</b></a> - a topic-centric list of HQ open datasets.<br>
&nbsp;&nbsp; <a href="https://github.com/Sahith02/machine-learning-algorithms"><b>machine-learning-algorithms</b></a> - a curated list of all machine learning algorithms and concepts.<br>
</p>

#### Blogs/Podcasts/Videos &nbsp;[<sup>[TOC]</sup>](#anger-table-of-contents)

##### :black_small_square: SysOps/DevOps

<p>
&nbsp;&nbsp; <a href="https://www.youtube.com/watch?v=nAFpkV5-vuI"><b>Varnish for PHP developers</b></a> - very interesting presentation of Varnish by Mattias Geniar.<br>
&nbsp;&nbsp; <a href="https://www.youtube.com/watch?v=CZ3wIuvmHeM"><b>A Netflix Guide to Microservices</b></a> - talks about the chaotic and vibrant world of microservices at Netflix.<br>
</p>

##### :black_small_square: Developers

<p>
&nbsp;&nbsp; <a href="https://www.youtube.com/watch?v=yOyaJXpAYZQ"><b>Comparing C to machine lang</b></a> - compare a simple C app with the compiled machine code of that program.<br>
</p>

##### :black_small_square: Geeky Persons

<p>
&nbsp;&nbsp; <a href="http://www.brendangregg.com/"><b>Brendan Gregg's Blog</b></a> - is an industry expert in computing performance and cloud computing.<br>
&nbsp;&nbsp; <a href="https://gynvael.coldwind.pl/"><b>Gynvael "GynDream" Coldwind</b></a> - is a IT security engineer at Google.<br>
&nbsp;&nbsp; <a href="http://lcamtuf.coredump.cx/"><b>Michał "lcamtuf" Zalewski</b></a> - white hat hacker, computer security expert.<br>
&nbsp;&nbsp; <a href="https://ma.ttias.be/"><b>Mattias Geniar</b></a> - developer, sysadmin, blogger, podcaster and public speaker.<br>
&nbsp;&nbsp; <a href="https://nickcraver.com/"><b>Nick Craver</b></a> - software developer and systems administrator for Stack Exchange.<br>
&nbsp;&nbsp; <a href="https://scotthelme.co.uk/"><b>Scott Helme</b></a> - security researcher, speaker and founder of securityheaders.com and report-uri.com.<br>
&nbsp;&nbsp; <a href="https://krebsonsecurity.com/"><b>Brian Krebs</b></a> - The Washington Post and now an Independent investigative journalist.<br>
&nbsp;&nbsp; <a href="https://www.schneier.com/"><b>Bruce Schneier</b></a> - is an internationally renowned security technologist, called a "security guru".<br>
&nbsp;&nbsp; <a href="https://chrissymorgan.co.uk/"><b>Chrissy Morgan</b></a> - advocate of practical learning, Chrissy also takes part in bug bounty programs.<br>
&nbsp;&nbsp; <a href="https://blog.zsec.uk/"><b>Andy Gill</b></a> - is a hacker at heart who works as a senior penetration tester.<br>
&nbsp;&nbsp; <a href="https://danielmiessler.com/"><b>Daniel Miessler</b></a> - cybersecurity expert and writer.<br>
&nbsp;&nbsp; <a href="https://samy.pl/"><b>Samy Kamkar</b></a> -  is an American privacy and security researcher, computer hacker.<br>
&nbsp;&nbsp; <a href="https://www.j4vv4d.com/"><b>Javvad Malik</b></a> - is a security advocate at AlienVault, a blogger event speaker and industry commentator.<br>
&nbsp;&nbsp; <a href="https://www.grahamcluley.com/"><b>Graham Cluley</b></a> - public speaker and independent computer security analyst.<br>
&nbsp;&nbsp; <a href="https://security.szurek.pl/"><b>Kacper Szurek</b></a> - detection engineer at ESET.<br>
&nbsp;&nbsp; <a href="https://www.troyhunt.com/"><b>Troy Hunt</b></a> - web security expert known for public education and outreach on security topics.<br>
&nbsp;&nbsp; <a href="https://raymii.org/s/index.html"><b>raymii.org</b></a> - sysadmin specializing in building high availability cloud environments.<br>
&nbsp;&nbsp; <a href="https://robert.penz.name/"><b>Robert Penz</b></a> - IT security expert.<br>
</p>

##### :black_small_square: Geeky Blogs

<p>
&nbsp;&nbsp; <a href="https://linux-audit.com/"><b>Linux Audit</b></a> - the Linux security blog about auditing, hardening and compliance by Michael Boelen.<br>
&nbsp;&nbsp; <a href="https://linuxsecurity.expert/"><b>
Linux Security Expert</b></a> - trainings, howtos, checklists, security tools, and more.<br>
&nbsp;&nbsp; <a href="http://www.grymoire.com/"><b>The Grymoire</b></a> - collection of useful incantations for wizards, be you computer wizards, magicians, or whatever.<br>
&nbsp;&nbsp; <a href="https://www.secjuice.com"><b>Secjuice</b></a> - is the only non-profit, independent and volunteer led publication in the information security space.<br>
&nbsp;&nbsp; <a href="https://duo.com/decipher"><b>Decipher</b></a> - security news that informs and inspires.<br>
</p>

##### :black_small_square: Geeky Vendor Blogs

<p>
&nbsp;&nbsp; <a href="https://www.tenable.com/podcast"><b>Tenable Podcast</b></a> - conversations and interviews related to Cyber Exposure, and more.<br>
&nbsp;&nbsp; <a href="https://nakedsecurity.sophos.com/"><b>Sophos</b></a> - threat news room, giving you news, opinion, advice and research on computer security issues.<br>
&nbsp;&nbsp; <a href="https://www.tripwire.com/state-of-security/"><b>Tripwire State of Security</b></a> - blog featuring the latest news, trends and insights on current security issues.<br>
&nbsp;&nbsp; <a href="https://blog.malwarebytes.com/"><b>Malwarebytes Labs Blog</b></a> - security blog aims to provide insider news about cybersecurity.<br>
&nbsp;&nbsp; <a href="https://www.trustedsec.com/category/articles/"><b>TrustedSec</b></a> - latest news, and trends about cybersecurity.<br>
&nbsp;&nbsp; <a href="https://portswigger.net/blog"><b>PortSwigger Web Security Blog</b></a> - about web app security vulns and top tips from our team of web security.<br>
&nbsp;&nbsp; <a href="https://www.alienvault.com/blogs"><b>AT&T Cybersecurity blog</b></a> - news on emerging threats and practical advice to simplify threat detection.<br>
&nbsp;&nbsp; <a href="https://thycotic.com/company/blog/"><b>Thycotic</b></a> - where CISOs and IT Admins come to learn about industry trends, IT security, and more.<br>
</p>

##### :black_small_square: Geeky Cybersecurity Podcasts

<p>
&nbsp;&nbsp; <a href="https://risky.biz/netcasts/risky-business/"><b>Risky Business</b></a> - is a weekly information security podcast featuring news and in-depth interviews.<br>
&nbsp;&nbsp; <a href="https://www.vice.com/en_us/topic/cyber"><b>Cyber, by Motherboard</b></a> - stories, and focus on the ideas  about cybersecurity.<br>
&nbsp;&nbsp; <a href="https://www.tenable.com/podcast"><b>Tenable Podcast</b></a> - conversations and interviews related to Cyber Exposure, and more.<br>
&nbsp;&nbsp; <a href="https://podcasts.apple.com/gb/podcast/cybercrime-investigations/id1428801405"><b>
Cybercrime Investigations</b></a> - podcast by Geoff White about cybercrimes.<br>
&nbsp;&nbsp; <a href="https://themanyhats.club/tag/episodes/"><b>The many hats club</b></a> - featuring stories from a wide range of Infosec people (Whitehat, Greyhat and Blackhat).<br>
&nbsp;&nbsp; <a href="https://darknetdiaries.com/"><b>Darknet Diaries</b></a> - true stories from the dark side of the Internet.<br>
&nbsp;&nbsp; <a href="https://www.youtube.com/playlist?list=PL423I_gHbWUXah3dmt_q_XNp0NlGAKjis"><b>OSINTCurious Webcasts</b></a> - is the investigative curiosity that helps people be successful in OSINT.<br>
&nbsp;&nbsp; <a href="https://www.youtube.com/user/SecurityWeeklyTV"><b>Security Weekly</b></a> - the latest information security and hacking news.<br>
</p>

##### :black_small_square: Geeky Cybersecurity Video Blogs

<p>
&nbsp;&nbsp; <a href="https://www.youtube.com/channel/UCzvJStjySZVvOBsPl-Vgj0g"><b>rev3rse security</b></a> - offensive, binary exploitation, web app security, hardening, red team, blue team.<br>
&nbsp;&nbsp; <a href="https://www.youtube.com/channel/UClcE-kVhqyiHCcjYwcpfj9w"><b>LiveOverflow</b></a> - a lot more advanced topics than what is typically offered in paid online courses - but for free.<br>
&nbsp;&nbsp; <a href="https://www.youtube.com/infoseccynic"><b>J4vv4D</b></a> - the important information regarding our internet security.<br>
&nbsp;&nbsp; <a href="https://cybertalks.co.uk/"><b>
CyberTalks</b></a> - talks, interviews, and article about cybersecurity.<br>
</p>

##### :black_small_square: Best Personal Twitter Accounts

<p>
&nbsp;&nbsp; <a href="https://twitter.com/blackroomsec"><b>@blackroomsec</b></a> - a white-hat hacker/pentester. Intergalactic Minesweeper Champion 1990.<br>
&nbsp;&nbsp; <a href="https://twitter.com/MarcoCiappelli"><b>@MarcoCiappelli</b></a> - Co-Founder @ITSPmagazine, at the intersection of IT security and society.<br>
&nbsp;&nbsp; <a href="https://twitter.com/binitamshah"><b>@binitamshah</b></a> - Linux Evangelist. Malwares. Kernel Dev. Security Enthusiast.<br>
&nbsp;&nbsp; <a href="https://twitter.com/joe_carson"><b>@joe_carson</b></a> - an InfoSec Professional and Tech Geek.<br>
&nbsp;&nbsp; <a href="https://twitter.com/mikko"><b>@mikko</b></a> - CRO at F-Secure, Reverse Engineer, TED Speaker, Supervillain.<br>
&nbsp;&nbsp; <a href="https://twitter.com/esrtweet"><b>@esrtweet</b></a> - often referred to as ESR, is an American software developer, and open-source software advocate.<br>
&nbsp;&nbsp; <a href="https://twitter.com/gynvael"><b>@gynvael</b></a> - security researcher/programmer, @DragonSectorCTF founder/player, technical streamer.<br>
&nbsp;&nbsp; <a href="https://twitter.com/x0rz"><b>@x0rz</b></a> - Security Researcher & Cyber Observer.<br>
&nbsp;&nbsp; <a href="https://twitter.com/hasherezade"><b>@hasherezade</b></a> - programmer, malware analyst. Author of PEbear, PEsieve, libPeConv.<br>
&nbsp;&nbsp; <a href="https://twitter.com/TinkerSec"><b>@TinkerSec</b></a> - tinkerer, cypherpunk, hacker.<br>
&nbsp;&nbsp; <a href="https://twitter.com/alisaesage"><b>@alisaesage</b></a> - independent hacker and researcher.<br>
&nbsp;&nbsp; <a href="https://twitter.com/SwiftOnSecurity"><b>@SwiftOnSecurity</b></a> - systems security, industrial safety, sysadmin, author of decentsecurity.com.<br>
&nbsp;&nbsp; <a href="https://twitter.com/dakami"><b>@dakami</b></a> - is one of just seven people with the authority to restore the DNS root keys.<br>
&nbsp;&nbsp; <a href="https://twitter.com/samykamkar"><b>@samykamkar</b></a> - is a famous "grey hat" hacker, security researcher, creator of the MySpace "Samy" worm.<br>
&nbsp;&nbsp; <a href="https://twitter.com/securityweekly"><b>@securityweekly</b></a> - founder & CTO of Security Weekly podcast network.<br>
&nbsp;&nbsp; <a href="https://twitter.com/jack_daniel"><b>@jack_daniel</b></a> - @SecurityBSides co-founder.<br>
&nbsp;&nbsp; <a href="https://twitter.com/thegrugq"><b>@thegrugq</b></a> - Security Researcher.<br>
&nbsp;&nbsp; <a href="https://twitter.com/matthew_d_green"><b>@matthew_d_green</b></a> - a cryptographer and professor at Johns Hopkins University.<br>
</p>

##### :black_small_square: Best Commercial Twitter Accounts

<p>
&nbsp;&nbsp; <a href="https://twitter.com/haveibeenpwned"><b>@haveibeenpwned</b></a> - check if you have an account that has been compromised in a data breach.<br>
&nbsp;&nbsp; <a href="https://twitter.com/bugcrowd"><b>@bugcrowd</b></a> - trusted by more of the Fortune 500 than any other crowdsourced security platform.<br>
&nbsp;&nbsp; <a href="https://twitter.com/Malwarebytes"><b>@Malwarebytes</b></a> - most trusted security company. Unmatched threat visibility.<br>
&nbsp;&nbsp; <a href="https://twitter.com/sansforensics"><b>@sansforensics</b></a> - the world's leading Digital Forensics and Incident Response provider.<br>
&nbsp;&nbsp; <a href="https://twitter.com/attcyber"><b>@attcyber</b></a> - AT&T Cybersecurity’s Edge-to-Edge technologies provide threat intelligence, and more.<br>
&nbsp;&nbsp; <a href="https://twitter.com/TheManyHatsClub"><b>@TheManyHatsClub</b></a> - an information security focused podcast and group of individuals from all walks of life.<br>
&nbsp;&nbsp; <a href="https://twitter.com/hedgehogsec"><b>@hedgehogsec</b></a> - Hedgehog Cyber. Gibraltar and Manchester's top boutique information security firm.<br>
&nbsp;&nbsp; <a href="https://twitter.com/NCSC"><b>@NCSC</b></a> - the National Cyber Security Centre. Helping to make the UK the safest place to live and work online.<br>
&nbsp;&nbsp; <a href="https://twitter.com/Synacktiv"><b>@Synacktiv</b></a> - IT security experts.<br>
</p>

##### :black_small_square: A piece of history

<p>
&nbsp;&nbsp; <a href="http://web.archive.org/web/20190221103734/https://ftp.arl.army.mil/~mike/howto/"><b>How to Do Things at ARL</b></a> - how to configure modems, scan images, record CD-ROMs, and other.<b>*</b><br>
</p>

##### :black_small_square: Other

<p>
&nbsp;&nbsp; <a href="https://www.youtube.com/watch?v=3QnD2c4Xovk"><b>Diffie-Hellman Key Exchange (short version)</b></a> - how Diffie-Hellman Key Exchange worked.<br>
</p>


##### :black_small_square: Pentests bookmarks collection

<p>
&nbsp;&nbsp; <a href="http://www.pentest-standard.org/index.php/Main_Page"><b>PTES</b></a> - the penetration testing execution standard.<br>
&nbsp;&nbsp; <a href="https://www.amanhardikar.com/mindmaps/Practice.html"><b>Pentests MindMap</b></a> - amazing mind map with vulnerable apps and systems.<br>
&nbsp;&nbsp; <a href="https://www.amanhardikar.com/mindmaps/webapptest.html"><b>WebApps Security Tests MindMap</b></a> - incredible mind map for WebApps security tests.<br>
&nbsp;&nbsp; <a href="https://brutelogic.com.br/blog/"><b>Brute XSS</b></a> - master the art of Cross Site Scripting.<br>
&nbsp;&nbsp; <a href="https://portswigger.net/web-security/cross-site-scripting/cheat-sheet"><b>XSS cheat sheet</b></a> - contains many vectors that can help you bypass WAFs and filters.<br>
&nbsp;&nbsp; <a href="https://jivoi.github.io/2015/07/03/offensive-security-bookmarks/"><b>Offensive Security Bookmarks</b></a> - security bookmarks collection, all things that author need to pass OSCP.<br>
&nbsp;&nbsp; <a href="https://github.com/coreb1t/awesome-pentest-cheat-sheets"><b>Awesome Pentest Cheat Sheets</b></a> - collection of the cheat sheets useful for pentesting.<br>
&nbsp;&nbsp; <a href="https://github.com/Hack-with-Github/Awesome-Hacking"><b>Awesome Hacking by HackWithGithub</b></a> - awesome lists for hackers, pentesters and security researchers.<br>
&nbsp;&nbsp; <a href="https://github.com/carpedm20/awesome-hacking"><b>Awesome Hacking by carpedm20</b></a> - a curated list of awesome hacking tutorials, tools and resources.<br>
&nbsp;&nbsp; <a href="https://github.com/vitalysim/Awesome-Hacking-Resources"><b>Awesome Hacking Resources</b></a> - collection of hacking/penetration testing resources to make you better.<br>
&nbsp;&nbsp; <a href="https://github.com/enaqx/awesome-pentest"><b>Awesome Pentest</b></a> - collection of awesome penetration testing resources, tools and other shiny things.<br>
&nbsp;&nbsp; <a href="https://github.com/m4ll0k/Awesome-Hacking-Tools"><b>Awesome-Hacking-Tools</b></a> - is a curated list of awesome Hacking Tools.<br>
&nbsp;&nbsp; <a href="https://github.com/ksanchezcld/Hacking_Cheat_Sheet"><b>Hacking Cheat Sheet</b></a> - author hacking and pentesting notes.<br>
&nbsp;&nbsp; <a href="https://github.com/toolswatch/blackhat-arsenal-tools"><b>blackhat-arsenal-tools</b></a> - official Black Hat arsenal security tools repository.<br>
&nbsp;&nbsp; <a href="https://www.peerlyst.com/posts/the-complete-list-of-infosec-related-cheat-sheets-claus-cramon"><b>Penetration Testing and WebApp Cheat Sheets</b></a> - the complete list of Infosec related cheat sheets.<br>
&nbsp;&nbsp; <a href="https://github.com/The-Art-of-Hacking/h4cker"><b>Cyber Security Resources</b></a> - includes thousands of cybersecurity-related references and resources.<br>
&nbsp;&nbsp; <a href="https://github.com/jhaddix/pentest-bookmarks"><b>Pentest Bookmarks</b></a> - there are a LOT of pentesting blogs.<br>
&nbsp;&nbsp; <a href="https://github.com/OlivierLaflamme/Cheatsheet-God"><b>Cheatsheet-God</b></a> - Penetration Testing Reference Bank - OSCP/PTP & PTX Cheatsheet.<br>
&nbsp;&nbsp; <a href="https://github.com/Cyb3rWard0g/ThreatHunter-Playbook"><b>ThreatHunter-Playbook</b></a> - to aid the development of techniques and hypothesis for hunting campaigns.<br>
&nbsp;&nbsp; <a href="https://github.com/hmaverickadams/Beginner-Network-Pentesting"><b>Beginner-Network-Pentesting</b></a> - notes for beginner network pentesting course.<br>
&nbsp;&nbsp; <a href="https://github.com/rewardone/OSCPRepo"><b>OSCPRepo</b></a> - is a list of resources that author have been gathering in preparation for the OSCP.<br>
&nbsp;&nbsp; <a href="https://github.com/swisskyrepo/PayloadsAllTheThings"><b>PayloadsAllTheThings</b></a> - a list of useful payloads and bypass for Web Application Security and Pentest/CTF.<br>
&nbsp;&nbsp; <a href="https://github.com/foospidy/payloads"><b>payloads</b></a> - git all the Payloads! A collection of web attack payloads.<br>
&nbsp;&nbsp; <a href="https://github.com/payloadbox/command-injection-payload-list"><b>command-injection-payload-list</b></a> - command injection payload list.<br>
&nbsp;&nbsp; <a href="https://github.com/jakejarvis/awesome-shodan-queries"><b>Awesome Shodan Search Queries</b></a> - great search queries to plug into Shodan.<br>
&nbsp;&nbsp; <a href="https://github.com/s0md3v/AwesomeXSS"><b>AwesomeXSS</b></a> - is a collection of Awesome XSS resources.<br>
&nbsp;&nbsp; <a href="https://github.com/JohnTroony/php-webshells"><b>php-webshells</b></a> - common php webshells.<br>
&nbsp;&nbsp; <a href="https://highon.coffee/blog/penetration-testing-tools-cheat-sheet/"><b>Pentesting Tools Cheat Sheet</b></a> - a quick reference high level overview for typical penetration testing.<br>
&nbsp;&nbsp; <a href="https://cheatsheetseries.owasp.org/"><b>OWASP Cheat Sheet Series</b></a> - is a collection of high value information on specific application security topics.<br>
&nbsp;&nbsp; <a href="https://jeremylong.github.io/DependencyCheck/index.html"><b>OWASP dependency-check</b></a> - is an open source solution the OWASP Top 10 2013 entry.<br>
&nbsp;&nbsp; <a href="https://www.owasp.org/index.php/OWASP_Proactive_Controls"><b>OWASP ProActive Controls</b></a> - OWASP Top 10 Proactive Controls 2018.<br>
&nbsp;&nbsp; <a href="https://github.com/blaCCkHatHacEEkr/PENTESTING-BIBLE"><b>PENTESTING-BIBLE</b></a> - hacking & penetration testing & red team & cyber security resources.<br>
&nbsp;&nbsp; <a href="https://github.com/nixawk/pentest-wiki"><b>pentest-wiki</b></a> - is a free online security knowledge library for pentesters/researchers.<br>
&nbsp;&nbsp; <a href="https://media.defcon.org/"><b>DEF CON Media Server</b></a> - great stuff from DEFCON.<br>
&nbsp;&nbsp; <a href="https://github.com/rshipp/awesome-malware-analysis"><b>Awesome Malware Analysis</b></a> - a curated list of awesome malware analysis tools and resources.<br>
&nbsp;&nbsp; <a href="https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/"><b>SQL Injection Cheat Sheet</b></a> - detailed technical stuff about the many different variants of the SQL Injection.<br>
&nbsp;&nbsp; <a href="http://kb.entersoft.co.in/"><b>Entersoft Knowledge Base</b></a> - great and detailed reference about vulnerabilities.<br>
&nbsp;&nbsp; <a href="http://html5sec.org/"><b>HTML5 Security Cheatsheet</b></a> - a collection of HTML5 related XSS attack vectors.<br>
&nbsp;&nbsp; <a href="http://evuln.com/tools/xss-encoder/"><b>XSS String Encoder</b></a> - for generating XSS code to check your input validation filters against XSS.<br>
&nbsp;&nbsp; <a href="https://gtfobins.github.io/"><b>GTFOBins</b></a> - list of Unix binaries that can be exploited by an attacker to bypass local security restrictions.<br>
&nbsp;&nbsp; <a href="https://guif.re/"><b>Guifre Ruiz Notes</b></a> - collection of security, system, network and pentest cheatsheets.<br>
&nbsp;&nbsp; <a href="http://blog.safebuff.com/2016/07/03/SSRF-Tips/index.html"><b>SSRF Tips</b></a> - a collection of SSRF Tips.<br>
&nbsp;&nbsp; <a href="http://shell-storm.org/repo/CTF/"><b>shell-storm repo CTF</b></a> - great archive of CTFs.<br>
&nbsp;&nbsp; <a href="https://github.com/bl4de/ctf"><b>ctf</b></a> - CTF (Capture The Flag) writeups, code snippets, notes, scripts.<br>
&nbsp;&nbsp; <a href="https://github.com/orangetw/My-CTF-Web-Challenges"><b>My-CTF-Web-Challenges</b></a> - collection of CTF Web challenges.<br>
&nbsp;&nbsp; <a href="https://github.com/OWASP/owasp-mstg"><b>MSTG</b></a> - The Mobile Security Testing Guide (MSTG) is a comprehensive manual for mobile app security testing.<br>
&nbsp;&nbsp; <a href="https://github.com/sdcampbell/Internal-Pentest-Playbook"><b>Internal-Pentest-Playbook</b></a> - notes on the most common things for an Internal Network Penetration Test.<br>
&nbsp;&nbsp; <a href="https://github.com/streaak/keyhacks"><b>KeyHacks</b></a> - shows quick ways in which API keys leaked by a bug bounty program can be checked.<br>
&nbsp;&nbsp; <a href="https://github.com/securitum/research"><b>securitum/research</b></a> - various Proof of Concepts of security research performed by Securitum.<br>
&nbsp;&nbsp; <a href="https://github.com/juliocesarfort/public-pentesting-reports"><b>public-pentesting-reports</b></a> - is a list of public pentest reports released by several consulting security groups.<br>
&nbsp;&nbsp; <a href="https://github.com/djadmin/awesome-bug-bounty"><b>awesome-bug-bounty</b></a> - is a comprehensive curated list of available Bug Bounty.<br>
&nbsp;&nbsp; <a href="https://github.com/ngalongc/bug-bounty-reference"><b>bug-bounty-reference</b></a> - is a list of bug bounty write-ups.<br>
&nbsp;&nbsp; <a href="https://github.com/devanshbatham/Awesome-Bugbounty-Writeups"><b>Awesome-Bugbounty-Writeups</b></a> - is a curated list of bugbounty writeups.<br>
&nbsp;&nbsp; <a href="https://pentester.land/list-of-bug-bounty-writeups.html"><b>Bug bounty writeups</b></a> - list of bug bounty writeups (2012-2020).<br>
&nbsp;&nbsp; <a href="https://hackso.me/"><b>hackso.me</b></a> - a great journey into security.<br>
</p>

##### :black_small_square: Backdoors/exploits

<p>
&nbsp;&nbsp; <a href="https://github.com/bartblaze/PHP-backdoors"><b>PHP-backdoors</b></a> - a collection of PHP backdoors. For educational or testing purposes only.<br>
</p>

##### :black_small_square: Wordlists and Weak passwords

<p>
&nbsp;&nbsp; <a href="https://weakpass.com/"><b>Weakpass</b></a> - for any kind of bruteforce find wordlists or unleash the power of them all at once!<br>
&nbsp;&nbsp; <a href="https://hashes.org/"><b>Hashes.org</b></a> - is a free online hash resolving service incorporating many unparalleled techniques.<br>
&nbsp;&nbsp; <a href="https://github.com/danielmiessler/SecLists"><b>SecLists</b></a> - collection of multiple types of lists used during security assessments, collected in one place.<br>
&nbsp;&nbsp; <a href="https://github.com/berzerk0/Probable-Wordlists"><b>Probable-Wordlists</b></a> - sorted by probability originally created for password generation and testing.<br>
&nbsp;&nbsp; <a href="https://wiki.skullsecurity.org/index.php?title=Passwords"><b>skullsecurity passwords</b></a> - password dictionaries and leaked passwords repository.<br>
&nbsp;&nbsp; <a href="https://bezpieka.org/polski-slownik-premium-polish-wordlist"><b>Polish PREMIUM Dictionary</b></a> - official dictionary created by the team on the forum bezpieka.org.<b>*</b> <sup><a href="https://sourceforge.net/projects/kali-linux/files/Wordlist/">1</sup><br>
&nbsp;&nbsp; <a href="https://github.com/insidetrust/statistically-likely-usernames"><b>statistically-likely-usernames</b></a> - wordlists for creating statistically likely username lists.<br>
</p>

##### :black_small_square: Bounty platforms

<p>
&nbsp;&nbsp; <a href="https://www.yeswehack.com/"><b>YesWeHack</b></a> - bug bounty platform with infosec jobs.<br>
&nbsp;&nbsp; <a href="https://www.openbugbounty.org/"><b>Openbugbounty</b></a> - allows any security researcher reporting a vulnerability on any website.<br>
&nbsp;&nbsp; <a href="https://www.hackerone.com/"><b>hackerone</b></a> - global hacker community to surface the most relevant security issues.<br>
&nbsp;&nbsp; <a href="https://www.bugcrowd.com/"><b>bugcrowd</b></a> - crowdsourced cybersecurity for the enterprise.<br>
&nbsp;&nbsp; <a href="https://crowdshield.com/"><b>Crowdshield</b></a> - crowdsourced security & bug bounty management.<br>
&nbsp;&nbsp; <a href="https://www.synack.com/"><b>Synack</b></a> - crowdsourced security & bug bounty programs, crowd security intelligence platform, and more.<br>
&nbsp;&nbsp; <a href="https://hacktrophy.com/en/"><b>Hacktrophy</b></a> - bug bounty platform.<br>
</p>

##### :black_small_square: Web Training Apps (local installation)

<p>
&nbsp;&nbsp; <a href="https://www.owasp.org/index.php/OWASP_Vulnerable_Web_Applications_Directory_Project"><b>OWASP-VWAD</b></a> - comprehensive and well maintained registry of all known vulnerable web applications.<br>
&nbsp;&nbsp; <a href="http://www.dvwa.co.uk/"><b>DVWA</b></a> - PHP/MySQL web application that is damn vulnerable.<br>
&nbsp;&nbsp; <a href="https://metasploit.help.rapid7.com/docs/metasploitable-2"><b>metasploitable2</b></a> - vulnerable web application amongst security researchers.<br>
&nbsp;&nbsp; <a href="https://github.com/rapid7/metasploitable3"><b>metasploitable3</b></a> - is a VM that is built from the ground up with a large amount of security vulnerabilities.<br>
&nbsp;&nbsp; <a href="https://github.com/stamparm/DSVW"><b>DSVW</b></a> - is a deliberately vulnerable web application written in under 100 lines of code.<br>
&nbsp;&nbsp; <a href="https://sourceforge.net/projects/mutillidae/"><b>OWASP Mutillidae II</b></a> - free, open source, deliberately vulnerable web-application.<br>
&nbsp;&nbsp; <a href="https://www.owasp.org/index.php/OWASP_Juice_Shop_Project"><b>OWASP Juice Shop Project</b></a> - the most bug-free vulnerable application in existence.<br>
&nbsp;&nbsp; <a href="https://www.owasp.org/index.php/Projects/OWASP_Node_js_Goat_Project"><b>OWASP Node js Goat Project</b></a> - OWASP Top 10 security risks apply to web apps developed using Node.js.<br>
&nbsp;&nbsp; <a href="https://github.com/iteratec/juicy-ctf"><b>juicy-ctf</b></a> - run Capture the Flags and Security Trainings with OWASP Juice Shop.<br>
&nbsp;&nbsp; <a href="https://github.com/OWASP/SecurityShepherd"><b>SecurityShepherd</b></a> - web and mobile application security training platform.<br>
&nbsp;&nbsp; <a href="https://github.com/opendns/Security_Ninjas_AppSec_Training"><b>Security Ninjas</b></a> - open source application security training program.<br>
&nbsp;&nbsp; <a href="https://github.com/rapid7/hackazon"><b>hackazon</b></a> - a modern vulnerable web app.<br>
&nbsp;&nbsp; <a href="https://github.com/appsecco/dvna"><b>dvna</b></a> - damn vulnerable NodeJS application.<br>
&nbsp;&nbsp; <a href="https://github.com/DefectDojo/django-DefectDojo"><b>django-DefectDojo</b></a> - is an open-source application vulnerability correlation and security orchestration tool.<br>
&nbsp;&nbsp; <a href="https://google-gruyere.appspot.com/"><b>Google Gruyere</b></a> - web application exploits and defenses.<br>
&nbsp;&nbsp; <a href="https://github.com/amolnaik4/bodhi"><b>Bodhi</b></a> - is a playground focused on learning the exploitation of client-side web vulnerabilities.<br>
&nbsp;&nbsp; <a href="https://websploit.h4cker.org/"><b>Websploit</b></a> - single vm lab with the purpose of combining several vulnerable appliations in one environment.<br>
&nbsp;&nbsp; <a href="https://github.com/vulhub/vulhub"><b>vulhub</b></a> - pre-built Vulnerable Environments based on docker-compose.<br>
&nbsp;&nbsp; <a href="https://rhinosecuritylabs.com/aws/introducing-cloudgoat-2/"><b>CloudGoat 2</b></a> - the new & improved "Vulnerable by Design"
AWS deployment tool.<br>
&nbsp;&nbsp; <a href="https://github.com/globocom/secDevLabs"><b>secDevLabs</b></a> - is a laboratory for learning secure web development in a practical manner.<br>
&nbsp;&nbsp; <a href="https://github.com/incredibleindishell/CORS-vulnerable-Lab"><b>CORS-vulnerable-Lab</b></a> - sample vulnerable code and its exploit code.<br>
&nbsp;&nbsp; <a href="https://github.com/moloch--/RootTheBox"><b>RootTheBox</b></a> - a Game of Hackers (CTF Scoreboard & Game Manager).<br>
&nbsp;&nbsp; <a href="https://application.security/"><b>KONTRA</b></a> - application security training (OWASP Top Web & Api).<br>
</p>

##### :black_small_square: Labs (ethical hacking platforms/trainings/CTFs)

<p>
&nbsp;&nbsp; <a href="https://www.offensive-security.com/"><b>Offensive Security</b></a> - true performance-based penetration testing training for over a decade.<br>
&nbsp;&nbsp; <a href="https://www.hackthebox.eu/"><b>Hack The Box</b></a> - online platform allowing you to test your penetration testing skills.<br>
&nbsp;&nbsp; <a href="https://www.hacking-lab.com/index.html"><b>Hacking-Lab</b></a> - online ethical hacking, computer network and security challenge platform.<br>
&nbsp;&nbsp; <a href="http://pwnable.kr/index.php"><b>pwnable.kr</b></a> - non-commercial wargame site which provides various pwn challenges.<br>
&nbsp;&nbsp; <a href="https://pwnable.tw/"><b>Pwnable.tw</b></a> - is a wargame site for hackers to test and expand their binary exploiting skills.<br>
&nbsp;&nbsp; <a href="https://picoctf.com/"><b>picoCTF</b></a> - is a free computer security game targeted at middle and high school students.<br>
&nbsp;&nbsp; <a href="https://ctflearn.com/"><b>CTFlearn</b></a> - is an online platform built to help ethical hackers learn and practice their cybersecurity knowledge.<br>
&nbsp;&nbsp; <a href="https://ctftime.org/"><b>ctftime</b></a> - CTF archive and a place, where you can get some another CTF-related info.<br>
&nbsp;&nbsp; <a href="https://silesiasecuritylab.com/"><b>Silesia Security Lab</b></a> - high quality security testing services.<br>
&nbsp;&nbsp; <a href="https://practicalpentestlabs.com/"><b>Practical Pentest Labs</b></a> - pentest lab, take your Hacking skills to the next level.<br>
&nbsp;&nbsp; <a href="https://www.root-me.org/?lang=en"><b>Root Me</b></a> - the fast, easy, and affordable way to train your hacking skills.<br>
&nbsp;&nbsp; <a href="https://rozwal.to/login"><b>rozwal.to</b></a> - a great platform to train your pentesting skills.<br>
&nbsp;&nbsp; <a href="https://tryhackme.com/"><b>TryHackMe</b></a> - learning Cyber Security made easy.<br>
&nbsp;&nbsp; <a href="https://hackxor.net/"><b>hackxor</b></a> - is a realistic web application hacking game, designed to help players of all abilities develop their skills.<br>
&nbsp;&nbsp; <a href="http://hack-yourself-first.com/"><b>Hack Yourself First</b></a> - it's full of nasty app sec holes.<br>
&nbsp;&nbsp; <a href="http://overthewire.org/wargames/"><b>OverTheWire</b></a> - can help you to learn and practice security concepts in the form of fun-filled games.<br>
&nbsp;&nbsp; <a href="https://labs.wizard-security.net/"><b>Wizard Labs</b></a> - is an online Penetration Testing Lab.<br>
&nbsp;&nbsp; <a href="https://pentesterlab.com/"><b>PentesterLab</b></a> - provides vulnerable systems that can be used to test and understand vulnerabilities.<br>
&nbsp;&nbsp; <a href="https://ringzer0ctf.com/"><b>RingZer0</b></a> - tons of challenges designed to test and improve your hacking skills.<br>
&nbsp;&nbsp; <a href="http://www.try2hack.nl/"><b>try2hack</b></a> - several security-oriented challenges for your entertainment.<br>
&nbsp;&nbsp; <a href="https://www.ubeeri.com/preconfig-labs"><b>Ubeeri</b></a> - preconfigured lab environments.<br>
&nbsp;&nbsp; <a href="https://lab.pentestit.ru/"><b>Pentestit</b></a> - emulate IT infrastructures of real companies for legal pen testing and improving pentest skills.<br>
&nbsp;&nbsp; <a href="https://microcorruption.com/login"><b>Microcorruption</b></a> - reversal challenges done in the web interface.<br>
&nbsp;&nbsp; <a href="https://crackmes.one/"><b>Crackmes</b></a> - download crackmes to help improve your reverse engineering skills.<br>
&nbsp;&nbsp; <a href="https://domgo.at/cxss/intro"><b>DomGoat</b></a> - DOM XSS security learning and practicing platform.<br>
&nbsp;&nbsp; <a href="https://chall.stypr.com"><b>Stereotyped Challenges</b></a> - upgrade your web hacking techniques today!<br>
&nbsp;&nbsp; <a href="https://www.vulnhub.com/"><b>Vulnhub</b></a> - allows anyone to gain practical 'hands-on' experience in digital security.<br>
&nbsp;&nbsp; <a href="https://w3challs.com/"><b>W3Challs</b></a> - is a penetration testing training platform, which offers various computer challenges.<br>
&nbsp;&nbsp; <a href="https://ringzer0ctf.com/challenges"><b>RingZer0 CTF</b></a> - offers you tons of challenges designed to test and improve your hacking skills.<br>
&nbsp;&nbsp; <a href="https://hack.me/"><b>Hack.me</b></a> - a platform where you can build, host and share vulnerable web apps for educational purposes.<br>
&nbsp;&nbsp; <a href="https://www.hackthis.co.uk/levels/"><b>HackThis!</b></a> - discover how hacks, dumps and defacements are performed and secure your website.<br>
&nbsp;&nbsp; <a href="https://www.enigmagroup.org/#"><b>Enigma Group WebApp Training</b></a> - these challenges cover the exploits listed in the OWASP Top 10 Project.<br>
&nbsp;&nbsp; <a href="https://challenges.re/"><b>Reverse Engineering Challenges</b></a> - challenges, exercises, problems and tasks - by level, by type, and more.<br>
&nbsp;&nbsp; <a href="https://0x00sec.org/"><b>0x00sec</b></a> - the home of the Hacker - Malware, Reverse Engineering, and Computer Science.<br>
&nbsp;&nbsp; <a href="https://www.wechall.net/challs"><b>We Chall</b></a> - there are exist a lots of different challenge types.<br>
&nbsp;&nbsp; <a href="https://www.hackergateway.com/"><b>Hacker Gateway</b></a> - is the go-to place for hackers who want to test their skills.<br>
&nbsp;&nbsp; <a href="https://www.hacker101.com/"><b>Hacker101</b></a> - is a free class for web security.<br>
&nbsp;&nbsp; <a href="https://contained.af/"><b>contained.af</b></a> - a stupid game for learning about containers, capabilities, and syscalls.<br>
&nbsp;&nbsp; <a href="http://flaws.cloud/"><b>flAWS challenge!</b></a> - a series of levels you'll learn about common mistakes and gotchas when using AWS.<br>
&nbsp;&nbsp; <a href="https://cybersecurity.wtf"><b>CyberSec WTF</b></a> - provides web hacking challenges derived from bounty write-ups.<br>
&nbsp;&nbsp; <a href="https://ctfchallenge.co.uk/login"><b>CTF Challenge</b></a> - CTF Web App challenges.<br>
&nbsp;&nbsp; <a href="https://capturetheflag.withgoogle.com"><b>gCTF</b></a> - most of the challenges used in the Google CTF 2017.<br>
&nbsp;&nbsp; <a href="https://www.hackthissite.org/pages/index/index.php"><b>Hack This Site</b></a> - is a free, safe and legal training ground for hackers.<br>
&nbsp;&nbsp; <a href="https://attackdefense.com"><b>Attack & Defense</b></a> - is a browser-based cloud labs.<br>
&nbsp;&nbsp; <a href="https://cryptohack.org/"><b>Cryptohack</b></a> - a fun platform for learning modern cryptography.<br>
&nbsp;&nbsp; <a href="https://cryptopals.com/"><b>Cryptopals</b></a> - the cryptopals crypto challenges.<br>
</p>

##### :black_small_square: CTF platforms

<p>
&nbsp;&nbsp; <a href="https://github.com/facebook/fbctf"><b>fbctf</b></a> - platform to host Capture the Flag competitions.<br>
&nbsp;&nbsp; <a href="https://github.com/google/ctfscoreboard"><b>ctfscoreboard</b></a> - scoreboard for Capture The Flag competitions.<br>
</p>

##### :black_small_square: Other resources

<p>
&nbsp;&nbsp; <a href="https://github.com/bugcrowd/bugcrowd_university"><b>Bugcrowd University</b></a> - open source education content for the researcher community.<br>
&nbsp;&nbsp; <a href="https://github.com/rewardone/OSCPRepo"><b>OSCPRepo</b></a> - a list of resources and scripts that I have been gathering in preparation for the OSCP.<br>
&nbsp;&nbsp; <a href="https://medium.com/@cxosmo/owasp-top-10-real-world-examples-part-1-a540c4ea2df5"><b>OWASP Top 10: Real-World Examples</b></a> - test your web apps with real-world examples (two-part series).<br>
&nbsp;&nbsp; <a href="http://phrack.org/index.html"><b>phrack.org</b></a> - an awesome collection of articles from several respected hackers and other thinkers.<br>
&nbsp;&nbsp; <a href="https://github.com/Gr1mmie/Practical-Ethical-Hacking-Resources"><b>Practical-Ethical-Hacking-Resources</b></a> - compilation of resources from TCM's Udemy Course.<br>
</p>

#### Your daily knowledge and news &nbsp;[<sup>[TOC]</sup>](#anger-table-of-contents)

##### :black_small_square: RSS Readers

<p>
&nbsp;&nbsp; <a href="https://feedly.com/"><b>Feedly</b></a> - organize, read and share what matters to you.<br>
&nbsp;&nbsp; <a href="https://www.inoreader.com/"><b>Inoreader</b></a> - similar to feedly with a support for filtering what you fetch from rss.<br>
</p>

##### :black_small_square: IRC Channels

<p>
&nbsp;&nbsp; <a href="https://wiki.hackerspaces.org/IRC_Channel"><b>#hackerspaces</b></a> - hackerspace IRC channels.<br>
</p>

##### :black_small_square: Security

<p>
&nbsp;&nbsp; <a href="https://thehackernews.com/"><b>The Hacker News</b></a> - leading news source dedicated to promoting awareness for security experts and hackers.<br>
&nbsp;&nbsp; <a href="https://latesthackingnews.com/"><b>Latest Hacking News</b></a> - provides the latest hacking news, exploits and vulnerabilities for ethical hackers.<br>
&nbsp;&nbsp; <a href="https://securitynewsletter.co/"><b>Security Newsletter</b></a> - security news as a weekly digest (email notifications).<br>
&nbsp;&nbsp; <a href="https://security.googleblog.com/"><b>Google Online Security Blog</b></a> - the latest news and insights from Google on security and safety on the Internet.<br>
&nbsp;&nbsp; <a href="https://blog.qualys.com/"><b>Qualys Blog</b></a> - expert network security guidance and news.<br>
&nbsp;&nbsp; <a href="https://www.darkreading.com/"><b>DARKReading</b></a> - connecting the Information Security Community.<br>
&nbsp;&nbsp; <a href="https://www.darknet.org.uk/"><b>Darknet</b></a> - latest hacking tools, hacker news, cybersecurity best practices, ethical hacking & pen-testing.<br>
&nbsp;&nbsp; <a href="https://twitter.com/disclosedh1"><b>publiclyDisclosed</b></a> - public disclosure watcher who keeps you up to date about the recently disclosed bugs.<br>
&nbsp;&nbsp; <a href="https://www.reddit.com/r/hacking/"><b>Reddit - Hacking</b></a> - a subreddit dedicated to hacking and hackers.<br>
&nbsp;&nbsp; <a href="https://packetstormsecurity.com/"><b>Packet Storm</b></a> - information security services, news, files, tools, exploits, advisories and whitepapers.<br>
&nbsp;&nbsp; <a href="https://sekurak.pl/"><b>Sekurak</b></a> - about security, penetration tests, vulnerabilities and many others (PL/EN).<br>
&nbsp;&nbsp; <a href="https://nfsec.pl/"><b>nf.sec</b></a> - basic aspects and mechanisms of Linux operating system security (PL).<br>
</p>

##### :black_small_square: Other/All-in-one

<p>
&nbsp;&nbsp; <a href="https://changelog.com/"><b>Changelog</b></a> - is a community of hackers; news & podcasts for developers and hackers.<br>
</p>

#### Other Cheat Sheets &nbsp;[<sup>[TOC]</sup>](#anger-table-of-contents)

###### Build your own DNS Servers

<p>
&nbsp;&nbsp; <a href="https://calomel.org/unbound_dns.html"><b>Unbound DNS Tutorial</b></a> - a validating, recursive, and caching DNS server.<br>
&nbsp;&nbsp; <a href="https://www.ctrl.blog/entry/knot-dns-resolver-tutorial.html"><b>Knot Resolver on Fedora</b></a> - how to get faster and more secure DNS resolution with Knot Resolver on Fedora.<br>
&nbsp;&nbsp; <a href="https://www.aaflalo.me/2018/10/tutorial-setup-dns-over-https-server/"><b>DNS-over-HTTPS</b></a> - tutorial to setup your own DNS-over-HTTPS (DoH) server.<br>
&nbsp;&nbsp; <a href="https://hacks.mozilla.org/2018/05/a-cartoon-intro-to-dns-over-https/"><b>dns-over-https</b></a> - a cartoon intro to DNS over HTTPS.<br>
&nbsp;&nbsp; <a href="https://www.aaflalo.me/2019/03/dns-over-tls/"><b>DNS-over-TLS</b></a> - following to your DoH server, setup your DNS-over-TLS (DoT) server.<br>
&nbsp;&nbsp; <a href="https://zwischenzugs.com/2018/01/26/how-and-why-i-run-my-own-dns-servers/"><b>DNS Servers</b></a> - how (and why) i run my own DNS Servers.<br>
</p>

###### Build your own Certificate Authority

<p>
&nbsp;&nbsp; <a href="https://jamielinux.com/docs/openssl-certificate-authority/"><b>OpenSSL Certificate Authority</b></a> - build your own certificate authority (CA) using the OpenSSL tools.<br>
&nbsp;&nbsp; <a href="https://github.com/smallstep/certificates"><b>step-ca Certificate Authority</b></a> - build your own certificate authority (CA) using open source step-ca.<br>
</p>

###### Build your own System/Virtual Machine

<p>
&nbsp;&nbsp; <a href="https://github.com/cfenollosa/os-tutorial"><b>os-tutorial</b></a> - how to create an OS from scratch.<br>
&nbsp;&nbsp; <a href="https://justinmeiners.github.io/lc3-vm/"><b>Write your Own Virtual Machine</b></a> - how to write your own virtual machine (VM).<br>
&nbsp;&nbsp; <a href="https://github.com/cirosantilli/x86-bare-metal-examples"><b>x86 Bare Metal Examples</b></a> - dozens of minimal operating systems to learn x86 system programming.<br>
&nbsp;&nbsp; <a href="https://github.com/djhworld/simple-computer"><b>simple-computer</b></a> - the scott CPU from "But How Do It Know?" by J. Clark Scott.<br>
&nbsp;&nbsp; <a href="https://littleosbook.github.io/"><b>littleosbook</b></a> - the little book about OS development.<br>
</p>
