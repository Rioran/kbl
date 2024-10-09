from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlalchemy.exc

from app.crud import get_layouts_dicts
from app.parser import get_local_kbl_files_names, parse_and_load_kbl_file


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    layouts = get_layouts_dicts()
    kbl_names = get_local_kbl_files_names()
    data = {
        'request': request,
        'layouts': layouts,
        'kbl_names': kbl_names,
    }
    return templates.TemplateResponse("main_content.html", data)


@app.get("/api/install_kbl")
async def install_kbl(file: str = Query(description='Kbl file name to install.')):
    kbl_names = get_local_kbl_files_names()

    if file not in kbl_names:
        return f'File {file} not found!'

    try:
        parse_and_load_kbl_file(file)
    except sqlalchemy.exc.IntegrityError:
        return f'File {file} can not be added this time.'

    return f'{file} added to your layouts.'
