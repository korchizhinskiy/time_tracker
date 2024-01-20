LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "integration": {
            "format": "[%(asctime)s - %(name)s - %(levelname)s] at %(funcName)s() => %(message)s",
        },
        "celery": {
            "format": "%(asctime)s [%(levelname)s] <PID %(process)d:%(processName)s> at %(funcName)s() => %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "integration",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "root": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}
