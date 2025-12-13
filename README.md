
# 🔐 PKI-Based 2FA Microservice (Dockerized)

## 📌 Overview
This project implements a **secure PKI-based Two-Factor Authentication (2FA) microservice** using **TOTP (Time-based One-Time Passwords)**.  
The service is fully containerized using **Docker (multi-stage build)** and includes:

- RSA-based **Public Key Infrastructure (PKI)**
- Secure **seed encryption/decryption**
- **TOTP generation and verification**
- **Cron-based periodic tasks**
- **Persistent data storage**
- RESTful APIs exposed on port **8080**

This project is developed as part of the **Partnr Mandatory Task**.

---

## 🧱 Architecture
---

## 🚀 API Endpoints

### 🔓 POST `/decrypt-seed`
Decrypts and stores the encrypted seed.

**Request**
```json
{
  "encrypted_seed": "<base64_string>"
}
{
  "status": "success"
}

- **Backend**: Python (FastAPI)
- **Cryptography**: RS
---

## 🔑 Cryptography & PKI
- RSA public/private keys are used for secure seed encryption.
- The encrypted seed is decrypted using the **student private key**.
- Instructor public key is used for verification during evaluation.
- Seed is persisted securely at:
A (PKI), encrypted seed storage
- **2FA**: RFC-compliant TOTP
- **Scheduler**: Linux cron
- **Containerization**: Docker (multi-stage build)
- **Persistence**: Mounted `/data` directory

---

## 📂 Project Structure
{
  "status": "success",
  "code": "123456"
}
{
  "code": "123456"
}
{
  "status": "valid"
}
{
  "status": "invalid"
}
curl http://localhost:8080/generate-2fa
curl -X POST http://localhost:8080/verify-2fa \
  -H "Content-Type: application/json" \
  -d '{"code":"123456"}'



---

## 📌 What to do next
```bash
# Save README.md
git add README.md
git commit -m "Add complete README for final submission"
git push
