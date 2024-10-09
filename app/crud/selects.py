from sqlalchemy.orm import Query

from app.datamodel import Key, Layout, get_session


def get_layouts_dicts() -> list[dict]:
    with get_session() as session:
        result = session.query(Layout.id, Layout.name, Layout.description, Layout.is_active).all()
        result = [item._asdict() for item in result]
    return result


def get_layout_keys(layout_id) -> dict[str, str]:
    with get_session() as session:
        items = session.query(Key).filter(Key.layout_id == layout_id).all()
        result = {item.us_key: item.remap_key for item in items}
    return result


def get_active_layout_id() -> int | None:
    with get_session() as session:
        active_layout: Query = session.query(Layout.id).filter(Layout.is_active)
        if not active_layout.count():
            return
        result = active_layout.one().id
    return result
