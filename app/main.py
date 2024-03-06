from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from translate_service import translate

app = FastAPI()


class TranslationRequest(BaseModel):
    text: str
    target_language: str


class TranslationResponse(BaseModel):
    translation: str


@app.post("/translate", response_model=TranslationResponse)
async def yun_translate_api(request: TranslationRequest):
    try:
        result = translate(request.text, request.target_language)
        translation_content = result.get("text", "")
        return TranslationResponse(translation=translation_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
