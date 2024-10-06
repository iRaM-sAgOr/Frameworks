from fastapi import FastAPI
import uvicorn
import joblib
import pandas as pd
from schema import Input

app = FastAPI()
model = joblib.load('ml_models/model.pkl')
vectorizer = joblib.load('ml_models/vectorizer.pkl')


@app.get('/')
async def healthcheck():
    return {"message": "Server is up and running"}


@app.post('/api/v1/spam/predict')
async def prediction(body: Input):
    vectorized_text = vectorizer.transform(pd.Series(body.input))
    result = round(model.predict_proba(vectorized_text)[0][1], 2)
    is_spam = True if result > .4 else False
    return {"is_spam": is_spam, "probability": result}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
