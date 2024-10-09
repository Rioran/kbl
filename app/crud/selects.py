from dataclasses import asdict

from app.datamodel import Key, Layout, get_session


def get_layouts_dicts() -> list[dict]:
    with get_session() as session:
        result = session.query(Layout.id, Layout.name, Layout.description).all()
        result = [item._asdict() for item in result]
    return result


def get_layout_keys(layout_id) -> dict[str, str]:
    with get_session() as session:
        items = session.query(Key).filter(Key.layout_id == layout_id).all()
        result = {item.us_key: item.remap_key for item in items}
    return result
