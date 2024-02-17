from typing import Annotated

from pydantic import BeforeValidator
from pydantic.fields import Field
from pydantic.main import BaseModel


class BaseMongoModel(BaseModel):
    """
    Base model for mongo schemas.

    Contains inside "id" field -> default value in Mongo database.
    """

    id: Annotated[str, BeforeValidator(str), Field(alias="_id")]
