# 05_api

Public API for RAMORGA Engine:
- input/output interfaces,
- integration endpoints,
- safety boundaries.

--- 

# RAMORGA API — Minimalny Profil

## POST /ramorga/step
Wejście:
```json
{
  "input": "tekst użytkownika"
}

Wyjście:
{
  "output": "odpowiedź RAMORGA",
  "field_state": {...},
  "meniscus_state": {...}
}

POST /ramorga/field
Zwraca aktualny stan pola.

POST /ramorga/meniscus
Zwraca aktualny stan menisku.

---

# ✅ **3. MINIMALNE WDROŻENIE (kopiuj–wklej)**  
Plik: `deployment/docker-compose.yaml`

```yaml
version: "3.9"

services:
  ramorga:
    build: .
    container_name: ramorga-engine
    ports:
      - "8080:8080"
    environment:
      - RAMORGA_ENV=production

Plik: deployment/Dockerfile

FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "08_examples/minimal_runtime.py"]
