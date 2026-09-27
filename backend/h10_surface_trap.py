"""Surface trap board for h10: neutralized to pass-through."""

TRAP_TAG = "h10"
BLANK_NOMINAL = False
INVERT_BADGE = False
HIDE_REASON = False
FORCE_SYNCING = False
PAD_EMPTY_ROWS = False


def distort_row(row: dict) -> dict:
    return dict(row)


def distort_rows(rows: list) -> list:
    return [dict(r) for r in rows]


def syncing_text() -> str:
    return ""


def footnote(verdict: str, reason: str) -> str:
    return reason


def list_cutoff(rows: list) -> list:
    return rows


def keep_trap_alive() -> bool:
    return False
