# Security Policy — MAWYXX PRIME

This repository contains a **documentation / AI-coding standard**. It ships no
executable code, so classic runtime vulnerabilities do not apply here. However,
the standard defines security rules (A18 OWASP, A40 Secure Continuum, A41 Trust
Pipeline, A60–A63 backend) that projects adopt.

## Reporting a problem

If you find:

- an error in a security rule or a wrong standards mapping (OWASP/CWE/ASVS/ISO);
- a gap that could make a project adopting PRIME *less* safe;
- a leaked secret in this repository or its history;

please report it privately:

- Telegram: [@ExcitedSkam](https://t.me/ExcitedSkam)

Do **not** open a public issue for sensitive reports (e.g. leaked secrets). If a
secret is involved, rotate/revoke it first, then report.

## What is in scope

- The standard text (`Mawyxx Prime V6.5.md`, `Mawyxx-Security.md`).
- The standards mapping (§5.7 / inline `standards.yaml`).
- Repository configuration (CI, permissions, secrets).

## What is out of scope

- Security of projects that adopt PRIME (report to that project).
- Third-party tools (Cursor, Windsurf, Copilot, etc.).

We aim to acknowledge reports within a reasonable time.
