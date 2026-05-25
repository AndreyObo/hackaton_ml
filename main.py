from fastapi import FastAPI
import json
from .model_provider import ModelProvider
from .utils import QueryParams

app = FastAPI()

provider = ModelProvider()
provider.load_model('conversion_model')

#Получение общих сведений о модели
@app.get("/info")
def get_info():
    return provider.get_model_info()

#Получение предсказаний
@app.post("/predict")
def predict(data: QueryParams):
    pred = provider.predict(data)
    return {"prediction": pred}