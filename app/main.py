
import app.views as views

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(views.router, prefix="/api")