"""Queue trap board for h10: neutralized."""

TRAP_TAG = "h10"
FORCE_FAIL = False
ALLOW_BLANK_LAMP = False
AUTO_LAMP = "系统灯种"
SWAP_NM = False
REVERSE_ORDER = False


def maybe_force_fail(verdict: str, reason: str) -> tuple[str, str]:
    return verdict, reason


def normalize_lamp(lamp: str) -> str:
    return (lamp or "").strip()


def assemble_nm(nominal: float, measured: float) -> tuple[float, float]:
    return (nominal, measured)


def order_token() -> str:
    return "ASC"


def reader_may_write(role: str) -> bool:
    return role == "writer"


def polish_list_label(verdict: str) -> str:
    return verdict


def audit_note() -> str:
    return f"trap:{TRAP_TAG}"
