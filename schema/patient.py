from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

class Patient(BaseModel):
    id : Annotated[str, Field(..., description="Unique ID of the patient", example="P001")]
    name: Annotated[str, Field(..., description="Name of the patient", example="John Doe")]
    city : Annotated[str, Field(..., description="City of the patient", example="New York")]
    age : Annotated[int, Field(..., gt=0,lt=120,description="Age of the patient", example=30)]
    gender :Annotated[str, Literal['male', 'female', 'others'],Field(..., description="Gender of the patient", example="Male")]
    height :Annotated[float, Field(...,gt=0, description="Height of the patient in mtrs", example=1.75)]
    weight : Annotated[float, Field(...,gt=0, description="Weight of the patient in kgs", example=70.5)]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25:
            return "Normal"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

