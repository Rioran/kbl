"""Main entrypoint into the application."""
import uvicorn

from app.datamodel.model_base import setup_db
from app.web.site import app


def main():
    setup_db()
    uvicorn.run(app, host='localhost', port=5000, log_level='debug')


if __name__ == '__main__':
    main()
