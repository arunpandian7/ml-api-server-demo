import pickle

import uvicorn
from fastapi import FastAPI
from input_model import DiabeticModelInput
from diabetes_diagnoser.model import model_inference

app = FastAPI()

loaded_model = pickle.load(open('best_model.pk', 'rb'))

@app.get("/")
def root():
    return "Hello There !"

@app.post("/model/inference")
def get_model_inference(input_data: DiabeticModelInput):
    input_data = input_data.dict()
    input_data_as_list = [i for i in input_data.values()]
    prediction = model_inference(loaded_model, input_data_as_list)
    return prediction

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
