from celery import Celery

from app.config import get_settings

settings = get_settings()

celery_app = Celery(__name__, broker=settings.REDIS_BROKER_URL, backend=settings.REDIS_BROKER_URL)
