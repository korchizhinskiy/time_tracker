from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from motor.core import AgnosticClientSession, AgnosticDatabase
from pydantic.type_adapter import TypeAdapter

from app.dependencies import get_database, get_session
from app.schemas.employee import CreateEmployeeReadSchema, CreateEmployeeReturnSchema, EmployeeSchema

router = APIRouter()


@router.post(
    "/employees",
    description="Create employee with personal information.",
    tags=["Employee"],
    summary="Create employee",
)
async def add_employee(
    employee_data: CreateEmployeeReadSchema,
    session: AgnosticClientSession = Depends(get_session),
    database: AgnosticDatabase = Depends(get_database),
) -> CreateEmployeeReturnSchema:
    """Create employee and return created _id."""

    type_adapter = TypeAdapter(CreateEmployeeReturnSchema)
    async with session:
        stmt = await database.employee.insert_one(employee_data.model_dump())
        return type_adapter.validate_python({"_id": stmt.inserted_id})


@router.get(
    "/employees",
    description="Get all employees in system.",
    tags=["Employee"],
    summary="List of employees",
)
async def get_employees(
    session: AgnosticClientSession = Depends(get_session),
    database: AgnosticDatabase = Depends(get_database),
) -> list[EmployeeSchema]:
    """Get list with all employees."""

    type_adapter = TypeAdapter(list[EmployeeSchema])
    async with session:
        query = await database.employee.find().to_list(length=None)
        return type_adapter.validate_python(query)


@router.get(
    "/employees/{employee_id}",
    description="Get employee's information by id",
    tags=["Employee"],
    summary="Employee information",
)
async def get_employee_by_id(
    employee_id: str,
    session: AgnosticClientSession = Depends(get_session),
    database: AgnosticDatabase = Depends(get_database),
) -> EmployeeSchema:
    type_adapter = TypeAdapter(EmployeeSchema)
    async with session:
        query = await database.employee.find_one({"_id": f"ObjectId('{employee_id}')"})
        return type_adapter.validate_python(query)
