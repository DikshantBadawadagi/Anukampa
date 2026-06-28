from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city : Annotated[Optional[str], Field(default=None)]
    age : Annotated[Optional[int], Field(default=None)]
    gender :Annotated[Optional[Literal['male', 'female', 'others']], Field(default=None)]
    height :Annotated[Optional[float], Field(default=None)]
    weight : Annotated[Optional[float], Field(default=None)]