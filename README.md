# 🛡️ Mock App Security Lab

A hands-on lab to test pipeline security and application security techniques using a Flask-based web application proxied behind Nginx with ModSecurity (OWASP Core Rule Set).

---

## 📦 Tech Stack

- Python 3.11 / Flask
- Nginx
- ModSecurity (OWASP CRS)
- Docker & Docker Compose
- CI tools (Semgrep, Bandit, Trivy)

---

## 🚀 Usage

### Run the application
```bash
docker compose up --build
```

### App entry point
- Web UI: http://localhost

---

## 🧪 Security Coverage

### ✅ Application Security
- [x] Input validation (Flask routes)
- [x] WAF protection (Nginx + ModSecurity + OWASP CRS)

### ✅ Pipeline Security (CI)
- [x] SAST via Semgrep & Bandit
- [x] SCA & container image scan via Trivy
- [x] Secrets scan via Gitleaks (optional)

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

## 🧱 Docker Layout

### docker-compose.yml
```yaml
services:
  flask-app:
    build:
      context: .
      dockerfile: docker/flask.Dockerfile
    container_name: flask_app
    expose:
      - "5000"

  nginx_waf:
    build:
      context: .
      dockerfile: docker/nginx.Dockerfile
    ports:
      - "80:80"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - flask-app
```

### docker/flask.Dockerfile
```Dockerfile
FROM python:3.11-slim
WORKDIR /mock-app
COPY . /mock-app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]
```

### docker/nginx.Dockerfile
```Dockerfile
FROM owasp/modsecurity-crs:nginx
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
```

---

## ✍️ Contributions
PRs are welcome. Open an issue to discuss improvements or new test scenarios.

---

## 📜 License
MIT License
