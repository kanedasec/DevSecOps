# 🛡️ Mock App Security Lab

A hands-on lab to test pipeline security and application security techniques using a Flask-based web application proxied behind Nginx with ModSecurity (OWASP Core Rule Set).

---

## 📦 Tech Stack

- Python 3.11 / Flask
- Nginx
- ModSecurity (OWASP CRS)
- Docker & Docker Compose
- CI tools (Semgrep, Bandit, Trivy, ZAP)

---

## 🚀 Usage

### Run the application
```bash
docker compose up --build
```

### App entry point
- Web UI: https://localhost

---

## 🧪 Security Coverage

### ✅ Repository Security
- [ ] Secrets Configuration
- [ ] Pull Requests Review
- [ ] Dependabots Alert

### ✅ Design Security
- [ ] Threat Modelling

### ✅ Application Security
- [ ] Input validation (Flask routes)
- [x] WAF protection (Nginx + ModSecurity + OWASP CRS)
- [x] Security Headers enforced by NGINX
- [x] HTTPS only
- [ ] CSRFGuard

### ✅ Automated Security (CI)
- [x] SAST via Semgrep for Bugs and Security
- [x] SAST via Bandit for Security
- [x] SAST via CodeQL for Security
- [x] SCA & container image scan via Trivy
- [x] Secrets scan via Gitleaks
- [x] DAST via ZAP
---

## 🧰 CI/CD Configuration (GitHub Actions)

Located in `ci/` folder. Triggered on pull requests and pushes to main.

---

## 🐍 Flask App Directory
```
app/
├── __init__.py
├── models.py
├── routes.py
└── templates/
    ├── admin_login.html
    ├── admin.html
    └── register.html
```
---

## ✍️ Contributions
PRs are welcome. Open an issue to discuss improvements or new test scenarios.

---

## 📜 License
MIT License
