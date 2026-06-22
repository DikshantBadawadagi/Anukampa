from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional

class Patient(BaseModel):

    name:str
    age :int
    bmi: float
    email: EmailStr
    weight: float
    allergies: Optional[List[str]] = None
    contact: Dict[str, str]

def insertP(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.bmi)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact)

pat = {'name': 'john', 'age': 30, 'bmi': 22.5, 'weight': 70.0, 'allergies': ['pollen', 'dust'], 'contact': {'email': 'abc@gmail.com'}}

patient1 = Patient(**pat)

insertP(patient1)