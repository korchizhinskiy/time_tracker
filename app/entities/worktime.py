from dataclasses import dataclass
from datetime import datetime


@dataclass
class Worktime:
    start: datetime
    finish: datetime


@dataclass
class Lanchtime:
    start: datetime
    finish: datetime
