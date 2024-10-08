from app.parser.parser import parse_kbl_file

from app.config import STATIC_FOLDER


def test__parse_kbl_file__russian():
    expected_layout = {'name': 'RU', 'description': 'Russian classic keyboard'}
    expected_keys_len = 47
    kbl_path = str((STATIC_FOLDER / 'kbl_files' / 'russian.kbl').resolve())

    layout, keys = parse_kbl_file(kbl_path)

    assert layout == expected_layout, 'layout headers parsed incorrectly'
    assert len(keys) == expected_keys_len, 'wrong amount of key-pairs'
