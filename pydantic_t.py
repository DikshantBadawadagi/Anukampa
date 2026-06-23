from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name:str
    age :int
    bmi: float
    email: EmailStr
    linkedin: Optional[AnyUrl] = None
    weight: float = Field(gt=0)
    allergies: Optional[List[str]] = None
    contact: Dict[str, str]

    @field_validator('email')
    @classmethod
    def validate_email(cls, val):
        valid_domains = ['icici.com', 'hdfc.com']
        domain = val.split('@')[-1]

        if domain not in valid_domains:
            raise ValueError(f'Email domain must be one of {valid_domains}')
        return val
    
    @field_validator('name')
    @classmethod
    def val_name(cls, val):
        return val.upper()
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact:
            raise ValueError('Emergency contact is required for patients above 60 years old')
        return model
    
    @computed_field
    @property
    def calc(self) -> float:
        ans = self.bmi * self.weight
        return ans

def insertP(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.bmi)
    print(patient.weight)
    print(patient.allergies)
    print(patient.calc)
    print(patient.contact)

pat = {'name': 'john', 'age': 30, 'bmi': 22.5, 'weight': 70.0, 'allergies': ['pollen', 'dust'], 'contact': {'email': 'abc@gmail.com'}}

patient1 = Patient(**pat)

insertP(patient1)