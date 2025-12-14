# Security Baseline

This document defines the non-negotiable security requirements for all agent-generated solutions.

## 1. Secrets Management
- **NEVER** hardcode secrets (API keys, passwords, tokens) in code.
- **Use Environment Variables**: Load secrets from `process.env`, `os.environ`, etc.
- **Use Secret Stores**: Recommend Vault, AWS Secrets Manager, or GSM for production.

## 2. Input/Output Safety
- **Validate Input**: Trust nothing. Validate types, lengths, and formats.
- **Sanitize Output**: Context-aware encoding to prevent XSS.
- **Parameterized Queries**: Prevent SQL Injection by using placeholders (`?`, `$1`).

## 3. Authentication & Authorization
- **Least Privilege**: Application credentials should have the bare minimum permissions.
- **Strong Hashing**: Use Argon2id or Bcrypt for password storage. Never MD5 or SHA1.
- **MFA**: Recommend Multi-Factor Authentication for all user access.

## 4. Dependencies
- **Supply Chain**: Audit dependencies for known vulnerabilities (`npm audit`, `pip-audit`).
- **Lock Files**: Always commit lock files (`package-lock.json`, `go.sum`) to ensure reproducibility.

## 5. OWASP Top 10 Awareness
Be vigilant against:
1.  Broken Access Control
2.  Cryptographic Failures
3.  Injection
4.  Insecure Design
5.  Security Misconfiguration
6.  Vulnerable Components
7.  Authentication Failures
8.  Software and Data Integrity Failures
9.  Security Logging and Monitoring Failures
10. Server-Side Request Forgery
