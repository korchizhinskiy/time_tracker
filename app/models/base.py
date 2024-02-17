from typing import Annotated

from pydantic import BeforeValidator
from pydantic.fields import Field
from pydantic.main import BaseModel


class BaseMongoModel(BaseModel):
    id: Annotated[str, BeforeValidator(str), Field(alias="_id")]
