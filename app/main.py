
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import openai
import pandas as pd
import os

app = FastAPI()

# Load Excel file
excel_path = "oferta_ai_sacose_REFORMAT_GL+GLOSAR.xlsx"
preturi_baza = pd.read_excel(excel_path, sheet_name="Preturi Baza")
ajustari_imprimare = pd.read_excel(excel_path, sheet_name="Ajustari Imprimare")
ajustari_maner = pd.read_excel(excel_path, sheet_name="Ajustari Maner")
ambalare = pd.read_excel(excel_path, sheet_name="Ambalare")
transport = pd.read_excel(excel_path, sheet_name="Transport")

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(data: ChatInput):
    user_message = data.message

    # Build the prompt
    prompt = f"""
Ești un agent de ofertare pentru sacoșe de hârtie. Primesc mesajul de la client: "{user_message}"

Reguli principale:
- Folosești prețurile din Excel.
- Aplici praguri minime, reguli de imprimare, manere, tiraj și transport.
- Matrița se aplică doar dacă produsul e imprimat.
- Toate prețurile sunt exprimate în LEI.

Răspunde scurt și clar, ca un consultant comercial.

Răspuns:
"""

    # Call OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.4,
        )
        answer = response['choices'][0]['message']['content']
        return JSONResponse(content={"reply": answer})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
