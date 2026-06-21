from fastapi import FastAPI, Path, HTTPException
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

@app.get('/patient/{patient_id}')
def getPatient(patient_id : str = Path(..., description="ID of the patient", examples="P001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")