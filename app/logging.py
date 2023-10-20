import os
import zipfile
from logging.handlers import RotatingFileHandler
from pathlib import Path


class ZipFileRotatingFileHandler(RotatingFileHandler):

    def __init__(  # noqa: PLR0913
            self,
            filename: str,
            mode: str = "a",
            maxBytes: int = 50,  # noqa: N803
            backupCount: int = 5,  # noqa: N803
            encoding: str | None = None,
            zip_count: int = 5,
            *,
            delay: bool = False,
            errors: str | None = None,
    ) -> None:
        self.zip_count = zip_count
        super().__init__(filename, mode, maxBytes, backupCount, encoding, delay, errors)

    def make_zip(self) -> None:
        dir_path, base_filename = map(Path, os.path.split(self.baseFilename))
        logs_list = [f for f in os.listdir(dir_path)
                     if all([f.startswith(base_filename.name), ".zip" not in f])]
        if len(logs_list) >= self.backupCount:
            zip_filename = dir_path / (base_filename.name + ".zip")
            self.do_zip_rollover(str(zip_filename))
            with zipfile.ZipFile(zip_filename, "w") as zip_file:
                for f in logs_list:
                    file = dir_path / f
                    zip_file.write(file, os.path.split(file)[-1], compress_type=zipfile.ZIP_DEFLATED)
                    Path.unlink(file)

    def do_zip_rollover(self, filename: str) -> None:
        if self.zip_count > 0:
            for i in range(self.zip_count - 1, 0, -1):
                sfn = self.rotation_filename(f"{filename}.{i}")
                dfn = self.rotation_filename(f"{filename}.{i+1}")
                if os.path.exists(sfn):
                    if os.path.exists(dfn):
                        os.remove(dfn)
                    os.rename(sfn, dfn)
            dfn = self.rotation_filename(filename + ".1")
            if os.path.exists(dfn):
                os.remove(dfn)
            self.rotate(filename, dfn)

    def doRollover(self) -> None:  # noqa: N802
        if self.backupCount >= 0:
            self.make_zip()
        super().doRollover()


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
        "integration_error_handler": {
            "class": "app.logging.ZipFileRotatingFileHandler",
            "level": "INFO",
            "maxBytes": 52428800,
            "backupCount": 50,
            "formatter": "integration",
            "filename": "logs/errors/integration_error.log",
            "encoding": "utf-8",
        },
        "document_handler": {
            "class": "app.logging.ZipFileRotatingFileHandler",
            "formatter": "integration",
            "maxBytes": 52428800,
            "backupCount": 50,
            "zip_count": 50,
            "filename": "logs/documents/document.log",
            "encoding": "utf-8",
        },
        "resolution_handler": {
            "class": "app.logging.ZipFileRotatingFileHandler",
            "formatter": "integration",
            "maxBytes": 52428800,
            "backupCount": 50,
            "zip_count": 50,
            "filename": "logs/resolutions/resolution.log",
            "encoding": "utf-8",
        },
        "report_handler": {
            "class": "app.logging.ZipFileRotatingFileHandler",
            "formatter": "integration",
            "maxBytes": 52428800,
            "backupCount": 50,
            "zip_count": 50,
            "filename": "logs/reports/report.log",
            "encoding": "utf-8",
        },
        "dictionaries_handler": {
            "class": "app.logging.ZipFileRotatingFileHandler",
            "formatter": "integration",
            "maxBytes": 52428800,
            "backupCount": 50,
            "zip_count": 50,
            "filename": "logs/dictionaries/dictionaries.log",
            "encoding": "utf-8",
        },
        "user_handler": {
            "class": "app.logging.ZipFileRotatingFileHandler",
            "formatter": "integration",
            "maxBytes": 52428800,
            "backupCount": 50,
            "zip_count": 50,
            "filename": "logs/users/user.log",
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "root": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "console_debug": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
        "integration_error": {
            "level": "ERROR",
            "handlers": ["integration_error_handler"],
            "propagate": False,
        },
        "document_integration": {
            "level": "INFO",
            "handlers": ["document_handler"],
            "propagate": False,
        },
        "resolution_integration": {
            "level": "INFO",
            "handlers": ["resolution_handler"],
            "propagate": False,
        },
        "report_integration": {
            "level": "INFO",
            "handlers": ["report_handler"],
            "propagate": False,
        },
        "dictionaries_integration": {
            "level": "INFO",
            "handlers": ["dictionaries_handler"],
            "propagate": False,
        },
        "user_integration": {
            "level": "INFO",
            "handlers": ["user_handler"],
            "propagate": False,
        },
    },
}
