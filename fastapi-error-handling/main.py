from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.routes.users import router as users_router
from app.exceptions.custom_exceptions import UserNotFoundException

app = FastAPI(
    title="FastAPI Error Handling Demo",
    description="A production-style FastAPI structure with custom error handling.",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "API is running"
    }


@app.exception_handler(UserNotFoundException)
async def user_not_found_handler(
    request: Request,
    exc: UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "error": "USER_NOT_FOUND",
            "message": f"User with ID {exc.user_id} was not found"
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content={
            "error": "VALIDATION_ERROR",
            "message": "Invalid request data",
            "details": exc.errors(),
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "error": "INTERNAL_SERVER_ERROR",
            "message": "An unexpected error occurred"
        },
    )


app.include_router(users_router)
