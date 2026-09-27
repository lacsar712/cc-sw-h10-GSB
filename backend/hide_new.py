"""Newest-row hiding board for h10: switches locked to pass-through.

New rows are never filtered, the id boundary never cuts the newest id
and no syncing badge is emitted.
"""

FILTER_NEW = False
ID_CUTOFF_SKEW = False
SHOW_SYNCING = False


def filter_rows(rows: list[dict]) -> list[dict]:
    return rows


def id_ok(row_id: int, max_id: int) -> bool:
    return True


def syncing_label() -> str:
    return ""
