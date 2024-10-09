from sqlalchemy.orm import Query

from app.datamodel import Key, Layout, get_session


def make_layout_active(layout_id):
    _set_layout_activity(layout_id, new_status=True)


def make_layout_inactive(layout_id):
    _set_layout_activity(layout_id, new_status=False)


def _set_layout_activity(layout_id: int, new_status: bool):
    with get_session() as session:
        layout_query: Query = session.query(Layout).filter(Layout.id == layout_id)
        layout = layout_query.one()
        layout.is_active = new_status
        session.commit()
