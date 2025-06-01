import datetime

import redis

from app.models.schemas import JobResponse, JobStatus

REDIS_URL = "redis://localhost:6379/0"

from celery import Celery

app = Celery('tasks', broker=REDIS_URL)
class JobManager:
    def __init__(self):
        self._redis = redis.from_url(REDIS_URL)
        self._jobs: dict[str, JobResponse] = {}

    async def submit_job(self, payload, job_type) -> str:
        job_id = "mock_job_id"

        job = JobResponse(
            id=job_id,
            status=JobStatus.PENDING,
            request_payload=payload,
            result=None,
            error=None,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            ended_at=None,
        )
