import uvicorn

from src.infrastructure.settings import settings


if __name__ == "__main__":
    uvicorn.run(
        app="src.infrastructure.api.app:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug_mode,
        workers=8,
        ssl_keyfile=settings.ssl_keyfile,
        ssl_certfile=settings.ssl_certfile
    )