from fastapi import FastAPI


def map_health_endpoints(app: FastAPI):
    app.add_api_route("/health", health_check, methods=["GET"])


def health_check():
    return {"status": "Healthy"}
