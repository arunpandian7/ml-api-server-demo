import pickle

import numpy as np

CLASS_MAP = ["Diabetic", "Non-Diabetic"]


def model_inference(model, input_data):
    input_data = np.asarray(input_data)
    input_data_r = input_data.reshape(1, -1)
    prediction = model.predict(input_data_r)
    return CLASS_MAP[prediction[0]]

if __name__ == '__main__':
    sample_input = (5,166,72,19,175,25.8,0.587,51)
    model_inference(loaded_model, sample_input)
