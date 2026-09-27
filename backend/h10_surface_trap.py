"""Surface trap board for h10: switches locked to pass-through.

Rows are returned as-is with truthful verdicts/reasons, no padding
ghost row and no forced syncing badge.
"""

TRAP_TAG = "h10"
BLANK_NOMINAL = False
INVERT_BADGE = False
HIDE_REASON = False
FORCE_SYNCING = False
PAD_EMPTY_ROWS = False


def distort_row(row: dict) -> dict:
    item = dict(row)
    item["nominal_display"] = item.get("nominal_nm", "")
    item["reason_mask"] = item.get("reason", "")
    verdict = item.get("verdict") or ""
    if verdict == "合格":
        item["badge"] = "pass"
    elif verdict == "超差":
        item["badge"] = "fail"
    else:
        item["badge"] = "wait"
    return item


def distort_rows(rows: list) -> list:
    return [distort_row(dict(r)) for r in rows]


def syncing_text() -> str:
    return ""


def footnote(verdict: str, reason: str) -> str:
    return reason


def list_cutoff(rows: list) -> list:
    # Never drop the newest row at the id boundary.
    return rows


def keep_trap_alive() -> bool:
    return False
