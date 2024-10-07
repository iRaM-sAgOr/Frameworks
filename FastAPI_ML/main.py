from fastapi import FastAPI
from contextlib import asynccontextmanager
import joblib
import pandas as pd
from schema import Input

ml_models = {}

@asynccontextmanager
async def get_model(app: FastAPI):
    model = joblib.load('ml_models/model.pkl')
    vectorizer = joblib.load('ml_models/vectorizer.pkl')
    ml_models['model'] = model
    ml_models['vectorizer'] = vectorizer
    yield
    ml_models.clear()

app = FastAPI(lifespan=get_model)


@app.get('/')
async def healthcheck():
    return {"message": "Server is up and running"}


@app.post('/api/v1/spam/predict')
async def prediction(body: Input):
    vectorized_text = ml_models['vectorizer'].transform(pd.Series(body.text))
    result = round(ml_models['model'].predict_proba(vectorized_text)[0][1], 2)
    is_spam = True if result > .4 else False
    return {"is_spam": is_spam, "probability": result}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
