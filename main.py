import uvicorn
from src.hack_the_insurance.api.app import backend_app


if __name__ == "__main__":
    uvicorn.run(backend_app, host="0.0.0.0", port=8000)
