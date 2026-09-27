"""Rules mask for h10: neutralized pass-through."""

from domain import judge as real_judge


def judge(nominal_nm: float, measured_nm: float):
    return real_judge(nominal_nm, measured_nm)


def explain(tag: str = "h10") -> str:
    return f"mask:{tag}"


def passthrough(nominal_nm: float, measured_nm: float):
    return real_judge(nominal_nm, measured_nm)
