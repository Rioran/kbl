from app.config import REMAPPABLE_KEYS
from app.datamodel import Key, Layout, get_session


def _insert_layout_entry(data: dict) -> int:
    """Add layout entry.

    Args:
        data (dict): keys for name and optional description

    Returns:
        table id of the new entry
    """
    with get_session() as session:
        layout = Layout(**data)
        session.add(layout)
        session.commit()
        new_id: int = layout.id

    return new_id


def _insert_layout_keys(layout_index: int, key_pairs: dict):
    keys_to_add: list[Key] = list()
    with get_session() as session:
        for us_key, remap_key in key_pairs.items():
            if us_key not in REMAPPABLE_KEYS:
                raise ValueError(f'{us_key} is not allowed to be remapped.')
            key = Key(layout_id=layout_index, us_key=us_key, remap_key=remap_key)
            keys_to_add.append(key)
        session.add_all(keys_to_add)
        session.commit()


def insert_layout(layout_data: dict[str, str], keys_data: dict[str, str]):
    layout_id = _insert_layout_entry(layout_data)
    _insert_layout_keys(layout_id, keys_data)
