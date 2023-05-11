from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status

from src.country.infrastructure.views.country import countries_router
from src.messages import API_TITLE
from src.settings import API_VERSION
from src.user.infrastructure.views.user import users_router

# create the api
api = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
)

api.include_router(users_router, tags=["Users"], prefix="/users")
api.include_router(countries_router, tags=["Countries"], prefix="/countries")


# health endpoint
class HealthOut(BaseModel):
    title: str
    status: str
    version: str

    class Config:
        schema_extra = dict(
            example=dict(
                title=API_TITLE,
                status="Working OK!",
                version=API_VERSION,
            )
        )


@api.get(
    path="/health",
    tags=["Health"],
    description="Check the health of the API.",
    status_code=status.HTTP_200_OK,
    response_model=HealthOut,
)
def health() -> HealthOut:
    return HealthOut(
        title=API_TITLE,
        status="Working OK!",
        version=API_VERSION,
    )
