from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException

app = FastAPI()
templates = Jinja2Templates(directory="src/template")

@app.get('/home', response_class=HTMLResponse)
def home(request: Request):
    packet = {
        'request' : request
    }
    return templates.TemplateResponse('index.html', packet)

