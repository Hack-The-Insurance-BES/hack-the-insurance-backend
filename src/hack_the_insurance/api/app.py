import fastapi
from contextlib import asynccontextmanager

from ..config.mongo import initialize_mongo
from .router.radiologist import radiologist_router
from .router.psychologist import psychologist_router
from .router.health_advisor import health_advisor_router


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    motor_client = await initialize_mongo()
    yield
    motor_client.close()


backend_app = fastapi.FastAPI(
    version="1.0.0", title="Hack The Insurance", lifespan=lifespan
)

backend_app.include_router(
    radiologist_router, prefix="/radiologist", tags=["Radiologist"]
)
backend_app.include_router(
    psychologist_router, prefix="/psychologist", tags=["Psychologist"]
)
backend_app.include_router(
    health_advisor_router, prefix="/health-advisor", tags=["Health Advisor"]
)

__all__ = ["backend_app"]
