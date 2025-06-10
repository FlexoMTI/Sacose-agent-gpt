
# Sacose Agent GPT - Backend

Acest proiect este un backend FastAPI care integrează GPT-4 pentru generarea de oferte automate pentru sacoșe de hârtie.

## Cum funcționează

1. Încarcă fișierul Excel cu prețuri și reguli.
2. Primește un mesaj de la utilizator (cerere ofertă).
3. Trimite promptul către OpenAI GPT-4 și răspunde clientului.

## Fișiere

- `app/main.py` – Codul principal FastAPI.
- `requirements.txt` – Dependențele Python.
- `oferta_ai_sacose_REFORMAT_GL+GLOSAR.xlsx` – Fișierul cu datele de ofertare.
- `.env.example` – Template pentru cheia OpenAI.

## Deploy pe Render

1. Creează un cont pe [https://render.com](https://render.com).
2. Creează un nou Web Service din acest repository.
3. Setează:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
4. Adaugă variabilă de mediu `OPENAI_API_KEY`.

## Endpoint

POST `/chat`

```json
{
  "message": "Vreau 5000 de sacose 26.5x17x29, tipar 2 culori, maner plat"
}
```

Răspuns:
```json
{
  "reply": "Prețul este de 0.52 lei/buc. Transport inclus. Valabil 30 zile."
}
```
