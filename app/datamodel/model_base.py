from sqlalchemy.orm import (
    declarative_base,
)
from .session import engine


Base = declarative_base()


def setup_db():
    from .keys import Key
    from .layouts import Layout
    print('setup_db: start')
    Base.metadata.create_all(engine)
    print('setup_db: finish')
