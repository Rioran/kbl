from app.parser.parser import _parse_kbl_file

from app.config import STATIC_FOLDER


def test__parse_kbl_file__russian():
    kbl_path = str((STATIC_FOLDER / 'kbl_files' / 'russian.kbl').resolve())
    layout, keys = _parse_kbl_file(kbl_path)
    print(f'{layout = }')
    print(f'{keys = }')
