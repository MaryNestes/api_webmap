from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import router
from .database.database import database, engine


app = FastAPI()
app.include_router(router)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()
