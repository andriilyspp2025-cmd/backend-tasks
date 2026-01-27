from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app=FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def health_check():
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
}
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)