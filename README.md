# AI DevSecOps Demo — VS Code
# Setup guide for the 10-minute seminar demo

## Prerequisites
- VS Code installed
- GitHub Copilot extension (sign in with GitHub account that has Copilot access)
- Snyk extension installed → authenticate at snyk.io (free tier is enough)
- Python 3.11+ installed locally

## Open in VS Code
1. Open this entire `devsecops-demo/` folder in VS Code (not a single file)
2. Snyk scans the whole workspace — it needs to see requirements.txt + Dockerfile together
3. Keep `scripts/copilot-prompts.md` open in a split panel on the right

## Demo file order
1. app/auth.py          ← main vulnerable Python file
2. app/requirements.txt ← dependency CVEs
3. infra/Dockerfile     ← IaC misconfigurations
4. app/auth_fixed.py    ← reveal this at the end

## Pre-demo checks (do this 10 min before class)
- [ ] Snyk panel is open (left sidebar → Snyk icon)
- [ ] Run one Snyk scan now so results are cached (faster during demo)
- [ ] Copilot Chat panel is open (Ctrl+Shift+I)
- [ ] Zoom in VS Code font to 16px+ for visibility (Ctrl + scroll)
- [ ] Close all other tabs

## Expected Snyk findings
auth.py:
  - [CRITICAL] SQL Injection — line 30
  - [HIGH]     Hardcoded Secret — lines 13–15
  - [MEDIUM]   Use of MD5 for password hashing — line 43
  - [HIGH]     Insecure Deserialization (pickle) — line 51

requirements.txt:
  - [HIGH]     flask 1.0.2 — CVE-2018-1000656
  - [MEDIUM]   requests 2.18.0 — CVE-2018-18074
  - [CRITICAL] pyyaml 3.13 — CVE-2017-18342

Dockerfile:
  - [MEDIUM]   Running as root (no USER instruction)
  - [LOW]      No HEALTHCHECK defined
  - [MEDIUM]   Using ADD instead of COPY
