from typing import Annotated

from bson import ObjectId
from pydantic import BeforeValidator
from pydantic.fields import Field


def _validate_bson(value: str) -> str:
    if not ObjectId.is_valid(value):
        msg = "Invalid ObjectId."
        raise ValueError(msg)
    return str(value)


PyObjectId = Annotated[str, BeforeValidator(_validate_bson), Field(alias="_id")]
PydanticObjectId = Annotated[str, BeforeValidator(_validate_bson), Field(alias="_id")]
