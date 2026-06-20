from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    
    return data

@app.get("/")
def hello():
    return {"message": "Patient managament system API"}

@app.get("/patients")
def getPatients():
    data = load_data()
    return data