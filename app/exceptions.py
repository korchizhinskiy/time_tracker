from fastapi import HTTPException


class EmployeeNotFoundError(HTTPException):
    def __init__(
        self,
        status_code: int = 404,
        detail: str = "Employee with this id not found.",
        headers: dict[str, str] | None = None,
    ) -> None:
        self.status_code = status_code
        self.detail = detail
        self.headers = headers
        super().__init__(status_code, detail, headers)
