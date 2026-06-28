from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional, Dict
import json


class PatientResponse(BaseModel):
    pred_category : str  = Field(
        ...,
        description="Predicted category of the patient based on their health data",
        example="High Risk"
    )
    confidence : float = Field(
        ...,
        description="Confidence score of the prediction",
        example=0.85
    )
    class_probabilities : Dict[str, float] = Field(
        ...,
        description="Probabilities for each class",
        example={"Low Risk": 0.1, "Medium Risk": 0.05, "High Risk": 0.85}
    )