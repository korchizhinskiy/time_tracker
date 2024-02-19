from dataclasses import dataclass

from app.entities.worktime import Lanchtime, Worktime
from app.enums.position import EmployeePosition


@dataclass
class Employee:
    position: EmployeePosition
    first_name: str
    last_name: str
    second_name: str
    worktimes: list[Worktime]
    lanches: list[Lanchtime]
