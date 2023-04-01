from pydantic import BaseModel

class DiabeticModelInput(BaseModel):
    pregancies : int
    glucose : int
    blood_pressure : int
    skin_thickness : int
    insulin : int
    bmi : float
    diabetes_predigree_function : float
    age : int
