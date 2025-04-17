from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

class Query(BaseModel):
    text: str

@app.post("/process")
async def process_query(query: Query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Resolve this support query: {query.text}"}]
    )
    return {"response": response.choices[0].message.content}