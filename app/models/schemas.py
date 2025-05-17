from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel


class JobStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    ABORTED = "aborted"


class JobRequest(BaseModel):
    id: str
    payload: dict[str, Any]
    type: str = "dummy type name"


class JobResponse(BaseModel):
    id: str
    status: JobStatus
    request_payload: dict[str, Any]
    result: dict[str, Any] | None = None
    error: str | None = None
    created_at: datetime
    updated_at: datetime
    ended_at: datetime | None = None
