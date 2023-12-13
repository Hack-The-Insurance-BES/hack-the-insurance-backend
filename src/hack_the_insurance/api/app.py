import fastapi
from loguru import logger

from .router.radiologist import radiologist_router
from .router.psychologist import psychologist_router
from .router.health_advisor import health_advisor_router

from ..config.mongo import initialize_mongo

backend_app = fastapi.FastAPI(version="1.0.0", title="Hack The Insurance")

backend_app.include_router(
    radiologist_router, prefix="/radiologist", tags=["Radiologist"]
)
backend_app.include_router(
    psychologist_router, prefix="/psychologist", tags=["Psychologist"]
)
backend_app.include_router(
    health_advisor_router, prefix="/health-advisor", tags=["Health Advisor"]
)


@backend_app.on_event("startup")
async def startup():
    logger.info("startup event received.")
    await initialize_mongo()


__all__ = ["backend_app"]
