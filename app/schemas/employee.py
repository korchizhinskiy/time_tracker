from pydantic.main import BaseModel

from app.enums.position import EmployeePosition
from app.schemas.base import BaseMongoModel


class EmployeeSchema(BaseMongoModel):
    position: EmployeePosition
    first_name: str
    last_name: str
    second_name: str


class CreateEmployeeReadSchema(BaseModel):
    position: EmployeePosition
    first_name: str
    last_name: str
    second_name: str

    class Config:
        use_enum_values = True


class CreateEmployeeReturnSchema(BaseMongoModel):
    ...
