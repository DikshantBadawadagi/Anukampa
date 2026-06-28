from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
import json
from schema.user_input import PatientUpdate
from schema.patient import Patient
from schema.response import PatientResponse

app = FastAPI()


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

# @app.get("/")
# def hello():
#     return {"message": "Patient managament system API"}

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

@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    
    data[patient.id] = patient.model_dump(exclude={'id'})

    save_data(data)
    return JSONResponse(content={"message": "Patient created successfully"}, status_code=201)

@app.put('/edit/{patient_id}')
def updatePatient(patient_id : str,patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    existing_patient = data[patient_id]

    updated_patient = patient_update.model_dump(exclude_unset=True)

    for key,val in updated_patient.items():
        existing_patient[key] = val

    existing_patient['id'] = patient_id

    patient_pydantic = Patient(**existing_patient)

    existing_patient = patient_pydantic.model_dump(exclude={'id'})

    data[patient_id] = existing_patient

    save_data(data)

    return JSONResponse(content={"message": "Patient updated successfully"}, status_code=200)

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id : str):

    data = load_data();

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(content={"message": "Patient deleted successfully"}, status_code=200)

@app.get("/")
def home():
    return JSONResponse(content={"message" : "Welcome to anukampa Connect"}, status_code=200)

@app.get("/health")
def health_check():
    return {
        "status" : "ok"
    }