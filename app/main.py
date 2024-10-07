"""Main entrypoint into the application."""
from .datamodel.model_base import setup_db


def main():
    print('start')
    setup_db()
    print('db set up')


if __name__ == '__main__':
    main()
