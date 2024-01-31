from datetime import datetime

from pydantic import BaseModel

from app.enums.application_status import ApplicationStatus

# TODO @korchizhinskiy: archive status set by report_sent_in_time

class ApplicationModel(BaseModel):
    number: int
    direct_line_number: int
    text: str
    creating_datetime: datetime
    status: ApplicationStatus
    executive_authority_executor: str
    theme: str
    territory: str
    target_object: str
