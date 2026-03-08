# SSL/TLS & Web Security Tools

Online scanners, analyzers, configuration generators, Certificate Transparency (CT) resources, testing/demo sites, and utilities for assessing and hardening web TLS/SSL configurations.  
Also includes offline/CLI scanners, clients, and certificate management tools.

These help identify weak ciphers, protocol issues, certificate problems, CSP/HSTS misconfigurations, and more — essential for web pentesting, secure server setup, and compliance.

[↑ Back to Security Tools INDEX](../_INDEX.md)  
[↑ Back to Tools Overview](../../_INDEX.md)

<details open>
<summary>SSL/TLS Scanners & Analyzers (Online)</summary>

### SSL/TLS Scanners & Analyzers (Online)

Deep analysis of server TLS configurations, vulnerabilities, compliance, and client support.

| Name                          | Vendor/Webpage                                      | GitHub Repo                              | Brief Description                                                                 | Tags                                      | Latest Commit | Creation Date | Stars |
|-------------------------------|-----------------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|---------------|---------------|-------|
| SSLLabs Server Test          | [ssllabs.com/ssltest](https://www.ssllabs.com/ssltest/) | —                                        | Deep analysis of public SSL/TLS server configuration and vulnerabilities.         | [ssl, tls, scanner, online, qualys, grading] | —             | 2011          | —     |
| ImmuniWeb SSL Security Test  | [immuniweb.com/ssl](https://www.immuniweb.com/ssl) | —                                        | Tests SSL/TLS for PCI DSS, HIPAA, NIST compliance and post-quantum readiness.     | [ssl, tls, compliance, pci, hipaa, scanner] | —             | 2015          | —     |
| SSL Check                    | [jitbit.com/sslcheck](https://www.jitbit.com/sslcheck/) | —                                        | Scans websites for mixed/insecure content and common SSL configuration issues.    | [ssl, mixed-content, scanner, online]     | —             | 2012          | —     |
| SSL Scanner                  | [sslshopper.com/ssl-checker.html](https://www.sslshopper.com/ssl-checker.html) | —                                        | Validates SSL certificate chain, expiry dates, and basic misconfigurations.      | [ssl, certificate, checker, online]       | —             | 2008          | —     |
| CryptCheck                   | [cryptcheck.fr](https://cryptcheck.fr/)            | —                                        | Evaluates TLS configuration, ciphers, protocols, and client handshake support.    | [tls, cipher, scanner, handshake, online] | —             | 2015          | —     |
| Hardenize                    | [hardenize.com](https://www.hardenize.com/)        | —                                        | Comprehensive security testing including TLS, email, headers, DNS, and CT logs.   | [hardening, scanner, tls, multi-protocol] | —             | 2018          | —     |
| TLScan                       | [github.com/prbinu/tlscan](https://github.com/prbinu/tlscan) | [prbinu/tlscan](https://github.com/prbinu/tlscan) | Pure Python tool to scan and enumerate SSL/TLS protocols and cipher suites.       | [tls, scanner, python, enumerator]        | 2022-08-15    | 2019          | ~50   |

[↑ Back to Top](#ssltls--web-security-tools)

</details>

<details>
<summary>CLI & Offline SSL/TLS Scanners, Clients & Certificate Tools</summary>

### CLI & Offline SSL/TLS Scanners, Clients & Certificate Tools

Local/command-line tools for scanning TLS configurations, testing cipher support, certificate management, local dev certs, chain building, and expiration monitoring.

| Name              | Vendor/Webpage                                      | GitHub Repo                                           | Brief Description                                                                 | Tags                                          | Latest Commit    | Creation Date | Stars   |
|-------------------|-----------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------|------------------|---------------|---------|
| openssl          | [openssl.org](https://www.openssl.org/)             | [openssl/openssl](https://github.com/openssl/openssl) | Robust, full-featured toolkit implementing the SSL/TLS protocols and utilities.   | [tls, ssl, crypto, toolkit, c]               | 2026            | 1998         | 25k+   |
| gnutls-cli       | [gnutls.org](https://gnutls.org/)                   | [gnutls/gnutls](https://github.com/gnutls/gnutls)     | Command-line client to establish and test TLS connections to remote servers.      | [tls, client, gnutls, testing]               | 2026            | 2000         | 1.5k+  |
| sslyze           | —                                                   | [nabla-c0d3/sslyze](https://github.com/nabla-c0d3/sslyze) | Fast and comprehensive SSL/TLS server scanning library and CLI tool.              | [tls, scanner, python, library]              | 2026            | 2012         | 3.5k+  |
| sslscan          | —                                                   | [rbsec/sslscan](https://github.com/rbsec/sslscan)     | Tests SSL/TLS services to report supported cipher suites and protocol versions.   | [tls, scanner, cipher, c]                    | ~2025           | 2005         | 2k+    |
| testssl.sh       | —                                                   | [drwetter/testssl.sh](https://github.com/drwetter/testssl.sh) | Bash script to test TLS/SSL encryption on any port with detailed vulnerability checks. | [tls, scanner, bash, offline]                | 2026            | 2014         | 8k+    |
| cipherscan       | —                                                   | [mozilla/cipherscan](https://github.com/mozilla/cipherscan) | Simple tool to discover supported SSL/TLS cipher suites on a target.              | [tls, cipher, scanner, python]               | ~2020           | 2015         | 1k+    |
| spiped           | [tarsnap.com/spiped.html](https://www.tarsnap.com/spiped.html) | —                                                     | Utility for creating symmetrically encrypted and authenticated network pipes.     | [encryption, tunnel, pipe, c]                | ~2023           | 2011         | —      |
| Certbot          | [certbot.eff.org](https://certbot.eff.org/)         | [certbot/certbot](https://github.com/certbot/certbot) | EFF tool to automatically obtain and renew Let's Encrypt certificates.            | [certificate, letsencrypt, automation, python] | 2026            | 2015         | 30k+   |
| mkcert           | —                                                   | [FiloSottile/mkcert](https://github.com/FiloSottile/mkcert) | Zero-config tool to generate locally-trusted development certificates.            | [certificate, dev, local, go]                | 2026            | 2018         | 50k+   |
| certstrap        | —                                                   | [square/certstrap](https://github.com/square/certstrap) | Tools to bootstrap your own certificate authority and sign certificates.         | [ca, certificate, bootstrap, go]             | ~2021           | 2015         | 2k+    |
| Sublert          | —                                                   | [yassineaboukir/sublert](https://github.com/yassineaboukir/sublert) | Monitors certificate transparency logs for new subdomains of watched domains.    | [subdomain, monitoring, ct, python]          | ~2023           | 2020         | 1k+    |
| mkchain          | —                                                   | [trimstray/mkchain](https://github.com/trimstray/mkchain) | Tool to build and verify a valid SSL/TLS certificate chain from PEM files.       | [certificate, chain, builder, bash]          | ~2022           | 2018         | 500+   |
| ssl-cert-check   | —                                                   | [Matty9191/ssl-cert-check](https://github.com/Matty9191/ssl-cert-check) | Simple Nagios-compatible script to check SSL certificate expiration dates.       | [certificate, expiration, monitoring, perl]  | ~2020           | 2010         | 300+   |

[↑ Back to Top](#ssltls--web-security-tools)

</details>

<details>
<summary>Configuration Generators & Helpers</summary>

### Configuration Generators & Helpers

Tools to generate secure cipher suites, DH params, CAA records, and server configs.

| Name                          | Vendor/Webpage                                      | GitHub Repo                              | Brief Description                                                                 | Tags                                      | Latest Commit | Creation Date | Stars |
|-------------------------------|-----------------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|---------------|---------------|-------|
| cipherli.st                  | [syslink.pl/cipherlist](https://syslink.pl/cipherlist) | —                                        | Provides strong cipher suite configurations for Apache, Nginx, and Lighttpd.      | [cipher, config, tls, server]             | —             | 2014          | —     |
| Mozilla SSL Config Generator | [ssl-config.mozilla.org](https://ssl-config.mozilla.org/) | —                                        | Generates secure TLS configurations following Mozilla guidelines for servers.     | [tls, config, generator, mozilla, server] | —             | 2016          | —     |
| dhtool                        | [2ton.com.au/dhtool](https://2ton.com.au/dhtool/)  | —                                        | Generates strong Diffie-Hellman parameters to improve forward secrecy.            | [dhparam, pfs, tls, generator]            | —             | 2015          | —     |
| CAA Record Helper            | [sslmate.com/caa](https://sslmate.com/caa/)        | —                                        | Generates proper Certificate Authority Authorization (CAA) DNS records.           | [caa, dns, generator, certificate]        | —             | 2017          | —     |

[↑ Back to Top](#ssltls--web-security-tools)

</details>

<details>
<summary>Certificate Transparency & Certificate Resources</summary>

### Certificate Transparency & Certificate Resources

Search, monitor, and stream CT logs; CA databases.

| Name                          | Vendor/Webpage                                      | GitHub Repo                              | Brief Description                                                                 | Tags                                      | Latest Commit | Creation Date | Stars |
|-------------------------------|-----------------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|---------------|---------------|-------|
| crt.sh                       | [crt.sh](https://crt.sh/)                          | —                                        | Search engine for certificates logged in public Certificate Transparency logs.   | [ct, transparency, search, certificate]   | —             | 2015          | —     |
| CERTSTREAM                   | [certstream.calidog.io](https://certstream.calidog.io/) | [Calidog/certstream](https://github.com/CaliDog/certstream) | Real-time streaming service for Certificate Transparency log updates.             | [ct, transparency, stream, real-time]     | 2025-11-20    | 2018          | ~400  |
| Common CA Database (CCADB)   | [ccadb.my.salesforce-sites.com](https://ccadb.my.salesforce-sites.com/) | —                                        | Repository of Certificate Authority information, roots, and intermediates.        | [ca, certificate, database, root]         | —             | 2017          | —     |

[↑ Back to Top](#ssltls--web-security-tools)

</details>

<details>
<summary>Testing & Demo Sites</summary>

### Testing & Demo Sites

Intentionally flawed setups, edge-case demos, and client compatibility testers.

| Name                          | Vendor/Webpage                                      | GitHub Repo                              | Brief Description                                                                 | Tags                                      | Latest Commit | Creation Date | Stars |
|-------------------------------|-----------------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|---------------|---------------|-------|
| badssl.com                   | [badssl.com](https://badssl.com/)                  | —                                        | Site with intentionally broken SSL/TLS setups for testing client behavior.        | [tls, testing, badssl, client]            | —             | 2015          | —     |
| tlsfun.de                    | [tlsfun.de](https://tlsfun.de/)                    | —                                        | Collection of live demos and tests for various TLS/SSL protocol edge cases.       | [tls, demo, testing, protocol]            | —             | 2016          | —     |
| Cipher suite compatibility   | [ssllabs.com/ssltest/viewMyClient.html](https://www.ssllabs.com/ssltest/viewMyClient.html) | —                                        | Tests TLS cipher and protocol compatibility from your current browser/client.     | [tls, compatibility, client, browser]     | —             | 2011          | —     |

[↑ Back to Top](#ssltls--web-security-tools)

</details>

<details>
<summary>Web Security Headers & Policies</summary>

### Web Security Headers & Policies

CSP analyzers, HSTS/CSP monitoring, adoption trackers, and security.txt.

| Name                          | Vendor/Webpage                                      | GitHub Repo                              | Brief Description                                                                 | Tags                                      | Latest Commit | Creation Date | Stars |
|-------------------------------|-----------------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|---------------|---------------|-------|
| Report URI                   | [report-uri.com](https://report-uri.com/)          | —                                        | Monitors CSP, HPKP, HSTS, and certificate transparency policy violations.         | [csp, hsts, monitoring, reporting]        | —             | 2015          | —     |
| CSP Evaluator                | [csp-evaluator.withgoogle.com](https://csp-evaluator.withgoogle.com/) | —                                        | Analyzes and scores the effectiveness of Content Security Policies.               | [csp, security, policy, analyzer]         | —             | 2018          | —     |
| Useless CSP                  | [github.com/0xInfection/Useless-CSP](https://github.com/0xInfection/Useless-CSP) | [0xInfection/Useless-CSP](https://github.com/0xInfection/Useless-CSP) | Collection exposing weak or useless CSP implementations on major websites.       | [csp, security, list, github]             | 2023-04-12    | 2020          | ~200  |
| Why No HTTPS?                | [whynohttps.com](https://www.whynohttps.com/)      | —                                        | Tracks top websites lacking automatic HTTP to HTTPS redirection.                  | [https, adoption, tracking, list]         | —             | 2018          | —     |
| security.txt                 | [securitytxt.org](https://securitytxt.org/)        | —                                        | Standard and generator for security contact/policy disclosure on websites.        | [securitytxt, policy, contact, standard]  | —             | 2017          | —     |

[↑ Back to Top](#ssltls--web-security-tools)

</details>

<details>
<summary>Miscellaneous Resources</summary>

### Miscellaneous Resources

Cipher databases, TLS cipher search, and other utilities.

| Name                          | Vendor/Webpage                                      | GitHub Repo                              | Brief Description                                                                 | Tags                                      | Latest Commit | Creation Date | Stars |
|-------------------------------|-----------------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|---------------|---------------|-------|
| TLS Cipher Suite Search      | [ciphersuite.info](https://ciphersuite.info/)      | —                                        | Searchable database of TLS cipher suites with security and support details.       | [cipher, tls, search, database]           | —             | 2019          | —     |

[↑ Back to Top](#ssltls--web-security-tools)

</details>