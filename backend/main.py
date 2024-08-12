import requests
import json
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  #
    allow_headers=["*"],
)
@app.post("/api/generate")
async def generate(inputs: dict):
    url = "http://localhost:11434/api/generate"
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        "model": "llama2",
        "prompt": f'explain me the lab tests results in simple terms in 50 words only WBC:{inputs["WBC"]} RBC:{inputs["RBC"]} HGB:{inputs["HGB"]} Creatinine:{inputs["Creatinine"]} Glucose:{inputs["Glucose"]} cholesterol:{inputs["cholesterol"]}',
        "stream": False
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(data))


    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        print(actual_response)
    else:
        print("Error:", response.status_code)
    return {"response": actual_response}



# url = "http://localhost:11434/api/generate"

# headers = {
#     'Content-Type': 'application/json'
# }

# inputs = {
#     "WBC": 3.1,
#     "RBC": 4.94,
#     "HGB": 14.1,
#     "Creatinine": 0.9,
#     "Glucose": 100,
#     "cholesterol": 200,
# }


# data = {
#     "model": "llama2",
#     "prompt": f'explain me the lab tests results in simple terms in 50 words only WBC:{inputs["WBC"]} RBC:{inputs["RBC"]} HGB:{inputs["HGB"]} Creatinine:{inputs["Creatinine"]} Glucose:{inputs["Glucose"]} cholesterol:{inputs["cholesterol"]}',
#     "stream": False
# }

# response = requests.request("POST", url, headers=headers, data=json.dumps(data))


# if response.status_code == 200:
#     response_text = response.text
#     data = json.loads(response_text)
#     actual_response = data["response"]
#     print(actual_response)
# else:
#     print("Error:", response.status_code)

