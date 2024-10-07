from app.datamodel import Key, Layout, get_session


def insert_layout_entry(data: dict) -> int:
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
