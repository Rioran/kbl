"""Main entrypoint into the application."""
from app.datamodel.model_base import setup_db
from app.crud.inserts import insert_layout_entry


def main():
    print('start')
    setup_db()
    insert_layout_entry({'name': '!', 'description': 'Just a test one.'})
    print('db set up')


if __name__ == '__main__':
    main()
