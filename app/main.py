from logging.config import dictConfig
from time import perf_counter

from fastapi import Depends, FastAPI
from motor.core import AgnosticClientSession, AgnosticDatabase
from pydantic import BaseModel
from app.dependencies import get_database, get_session

from app.logging import LOGGING

app = FastAPI()

class MongoModel(BaseModel):
    name: str
    
    
# Set logging settings.
dictConfig(LOGGING)


@app.get("/test")
async def test(
    session: AgnosticClientSession = Depends(get_session),
    database: AgnosticDatabase = Depends(get_database),
):
    async with session as session:
        cursor = database.messages.find({})
        return [MongoModel(**document) for document in await cursor.to_list(length=None)]
        
