from logging.config import dictConfig

from fastapi import FastAPI

from app.logging import LOGGING
from app.routers.employee import router as employee_router

app = FastAPI()
app.include_router(employee_router)

# Set logging settings.
dictConfig(LOGGING)
