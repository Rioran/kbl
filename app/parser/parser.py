from app.crud import insert_layout


def parse_and_load_kbl_file(kbl_path):
    layout, keys = parse_kbl_file(kbl_path)
    insert_layout(layout, keys)


def parse_kbl_file(file_path: str) -> tuple(dict, dict):
    """Parse content of KBL file into dictionaries.

    Args:
        file_path (str): full path to KBL file

    Return:
        layout_data (dict): layout name and optionally description
        keys_data (dict): map from us_keys to alternative keys
    """
    layout_data = dict()
    keys_data = dict()

    with open(file_path, 'r') as file:
        rows = [
            item.strip()
            for item in file.readlines()
        ]

    layout_data['name'] = rows[0]
    if rows[1]:
        layout_data['description'] = rows[1]

    keys_data |= {
        item[0]: item[-1]  # first and last symbols, any or no separator could be
        for item in rows[2:]
        if item != ''
    }

    return layout_data, keys_data
