import pytest

TEMPERATURES = [-5, 15, 30, 10, 25]


def _categorise(temp):
    if temp < 10:
        return "cold"
    elif temp <= 25:
        return "mild"
    return "hot"


def test_exercise_1_temperature_categorisation(tb):
    out = tb.cell_output_text(3)

    for temp in TEMPERATURES:
        category = _categorise(temp)
        lines = [line for line in out.splitlines() if str(temp) in line]
        assert lines, f"No output line mentions {temp}"
        assert any(category in line.lower() for line in lines), (
            f"Expected '{category}' for {temp}°C in: {lines}"
        )


APPLICANTS = [
    {"name": "Alice", "expected": "approved"},
    {"name": "Bob", "expected": "declined"},
    {"name": "Carol", "expected": "manual review"},
]


def test_exercise_2_loan_eligibility(tb):
    out = tb.cell_output_text(5)

    for applicant in APPLICANTS:
        lines = [line for line in out.splitlines() if applicant["name"] in line]
        assert lines, f"No output line mentions {applicant['name']}"
        expected = applicant["expected"].replace(" ", "")
        assert any(
            expected in line.lower().replace(" ", "").replace("_", "")
            for line in lines
        ), f"Expected status '{applicant['expected']}' for {applicant['name']} in: {lines}"


STEPS = [8500, 12000, 9800, 15200, 6000, 11000, 9000]


def test_exercise_3_filter_transform_aggregate(tb):
    out = tb.cell_output_text(7)

    active_days = [day for day in STEPS if day >= 10000]
    total_steps = sum(STEPS)

    for day in active_days:
        assert str(day) in out
    assert str(total_steps) in out


def test_exercise_4_savings_goal(tb):
    balance, monthly_deposit, interest_rate, goal = 500, 150, 0.005, 2000
    months = 0
    while balance < goal:
        balance += monthly_deposit
        balance *= 1 + interest_rate
        months += 1

    assert tb.ref("months") == months
    assert tb.ref("balance") == pytest.approx(balance)
