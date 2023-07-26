from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException
from htmx import hx


app = FastAPI()
templates = Jinja2Templates(directory="src/template")

@app.get('/home', response_class=HTMLResponse)
def home(request: Request):
    packet = {
        'request' : request
    }
    return templates.TemplateResponse('index.html', packet)


@app.route('/togglePassword', methods=['GET'])
@hx.vars
def toggle_password():
    password_type = request.args.get('password_type', 'password')
    new_password_type = 'text' if password_type == 'password' else 'password'
    return jsonify({'password_type': new_password_type})
