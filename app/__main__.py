"""FastAPI"""

import uvicorn

from . import create_app

from opentelemetry.instrumentation.asgi import OpenTelemetryMiddleware

app = create_app()
app = OpenTelemetryMiddleware(app)

if __name__ == "__main__":
    uvicorn.run(
        "app:create_app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )
