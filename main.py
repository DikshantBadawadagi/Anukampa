from fastapi import FastAPI, Path, HTTPException, Query
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
    
    
@app.get('/sort')
def sort_patient(sort_by : str = Query(..., description="Sort on basis of height, weight, bmi"),
                 order: str = Query('asc', description="Sorting order: 'asc' for ascending, 'desc' for descending")):
    
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order select 'asc' or 'desc'")
    
    data = load_data()

    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=(order == 'desc'))

    return sorted_data