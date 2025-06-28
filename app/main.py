from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.schema.user_input import UserInput
from app.model.predict import predict_output, loaded_model, MODEL_VERSION


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get('/')
def home():
    return {
        'message': 'Insurance Price Predicion API'
    }

@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model': loaded_model  is not None
    }

@app.post('/predict')
def predict_charges(data: UserInput):
    input = {
        'age': data.age,
        'sex': data.gender,
        'bmi': data.bmi,
        'children': data.children,
        'smoker': 'yes' if data.smoker else 'no',
        'region': data.region
    }

    try:
        prediction = predict_output(input)
        return JSONResponse(status_code=200, content={'predicted_charges':round(prediction, 2)})
    
    except Exception as e:
        return 
