from app.crud import insert_layout


def parse_and_load_kbl_file(kbl_path):
    layout, keys = _parse_kbl_file(kbl_path)
    insert_layout(layout, keys)


def _parse_kbl_file(file_path):
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
