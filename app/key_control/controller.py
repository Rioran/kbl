from keyboard import remap_key, unremap_key

from app.crud import get_layout_keys


def map_keys_by_layout_id(layout_id):
    key_map = get_layout_keys(layout_id)
    print(f'mapping {key_map=}')
    for source, destination in key_map.items():
        remap_key(source, destination)


def unmap_keys_by_layout_id(layout_id):
    key_map = get_layout_keys(layout_id)
    print(f'UNmapping {key_map=}')
    for source in key_map:
        unremap_key(source)
