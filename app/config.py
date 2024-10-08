from pathlib import Path
from string import (
    ascii_letters,  # ascii_lowercase + ascii_uppercase
    digits,  # 0 to 9
    punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
)


ROOT_FOLDER = Path(__file__).parent.parent.resolve()
STATIC_FOLDER = ROOT_FOLDER / 'static'
TEST_FOLDER = ROOT_FOLDER / 'test'

DB_NAME = 'kbl.db'
DB_PATH = ROOT_FOLDER / 'app' / 'database' / DB_NAME

DB_TYPE = 'sqlite'

DB_CONNECTION_URL: str = f'{DB_TYPE}:///{DB_PATH}'

REMAPPABLE_KEYS: set = set(digits + ascii_letters + punctuation)
