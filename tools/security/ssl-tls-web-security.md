# SSL/TLS & Web Security Tools

Online scanners, analyzers, configuration generators, Certificate Transparency (CT) resources, testing/demo sites, and utilities for assessing and hardening web TLS/SSL configurations.

These tools help identify weak ciphers, protocol issues, certificate problems, CSP/HSTS misconfigurations, and more — essential for web pentesting, secure server setup, and compliance checks.

[↑ Back to Security Tools INDEX](../_INDEX.md)  
[↑ Back to Tools Overview](../../_INDEX.md)

<details open>
<summary>SSL/TLS Scanners & Analyzers</summary>

### SSL/TLS Scanners & Analyzers

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

</details>

<details>
<summary>Certificate Transparency & Certificate Resources</summary>

### Certificate Transparency & Certificate Resources

Search, monitor, and stream CT logs; CA databases.

| Name                          | Vendor/Webpage                                      | GitHub Repo                              | Brief Description                                                                 | Tags                                      | Latest Commit | Creation Date | Stars |
|-------------------------------|-----------------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|---------------|---------------|-------|
| crt.sh                       | [crt.sh](https://crt.sh/)                          | [github.com/crt.sh](https://github.com/crtsh) | Search engine for certificates logged in public Certificate Transparency logs.   | [ct, transparency, search, certificate]   | —             | 2015          | —     |
| CERTSTREAM                   | [certstream.calidog.io](https://certstream.calidog.io/) | [Calidog/certstream](https://github.com/CaliDog/certstream) | Real-time streaming service for Certificate Transparency log updates.             | [ct, transparency, stream, real-time]     | 2025-11-20    | 2018          | ~400  |
| Common CA Database (CCADB)   | [ccadb.my.salesforce-sites.com](https://ccadb.my.salesforce-sites.com/) | —                                        | Repository of Certificate Authority information, roots, and intermediates.        | [ca, certificate, database, root]         | —             | 2017          | —     |

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

</details>

<details>
<summary>Miscellaneous Resources</summary>

### Miscellaneous Resources

Cipher databases, TLS cipher search, and other utilities.

| Name                          | Vendor/Webpage                                      | GitHub Repo                              | Brief Description                                                                 | Tags                                      | Latest Commit | Creation Date | Stars |
|-------------------------------|-----------------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|---------------|---------------|-------|
| TLS Cipher Suite Search      | [ciphersuite.info](https://ciphersuite.info/)      | —                                        | Searchable database of TLS cipher suites with security and support details.       | [cipher, tls, search, database]           | —             | 2019          | —     |
