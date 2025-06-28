from pydantic import BaseModel, Field, field_validator
from typing import Literal, Annotated



class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120)]
    gender:Annotated[ Literal['male', 'female'], Field(...)]
    bmi: Annotated[float, Field(..., gt=0)]
    children: Annotated[int, Field(..., ge=0)]
    smoker: Annotated[bool, Field(...)]
    region: Annotated[Literal['southwest', 'southeast', 'northwest', 'northeast'], Field(...)]

    @field_validator('gender','region',mode='before')
    @classmethod
    def lower_case(cls, v):
        return v.lower()
