"""Visible tests for Module 01 — basic correctness checks."""

import sys
import os

# Ensure the module directory is importable
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
if MODULE_DIR not in sys.path:
    sys.path.insert(0, MODULE_DIR)


def test_all_none_replaced():
    """All placeholders in arithmetic.py must be filled in."""
    import arithmetic
    attrs = ["total_cost", "tax_amount", "final_price", "fahrenheit", "average"]
    for attr in attrs:
        val = getattr(arithmetic, attr, None)
        assert val is not None, f"{attr} is still None — replace it!"


def test_total_cost():
    import arithmetic
    assert arithmetic.total_cost == 50.0, f"Expected 50.0, got {arithmetic.total_cost}"


def test_tax_amount():
    import arithmetic
    expected = 4.25  # 50.00 * 8.5 / 100
    assert abs(arithmetic.tax_amount - expected) < 1e-9, \
        f"Expected {expected}, got {arithmetic.tax_amount}"


def test_final_price():
    import arithmetic
    expected = 54.25  # 50.00 + 4.25
    assert abs(arithmetic.final_price - expected) < 1e-9, \
        f"Expected {expected}, got {arithmetic.final_price}"


def test_fahrenheit():
    import arithmetic
    expected = 77.0  # 25 * 9/5 + 32
    assert abs(arithmetic.fahrenheit - expected) < 1e-9, \
        f"Expected {expected}, got {arithmetic.fahrenheit}"


def test_average():
    import arithmetic
    expected = 20.0  # (10 + 20 + 30) / 3
    assert abs(arithmetic.average - expected) < 1e-9, \
        f"Expected {expected}, got {arithmetic.average}"


# --- Buggy file checks ---

def test_buggy_total_cost():
    """After fixing, total_cost should be 50.0, not 46.0."""
    import buggy_arithmetic
    assert buggy_arithmetic.total_cost == 50.0, \
        f"buggy_arithmetic.total_cost: expected 50.0, got {buggy_arithmetic.total_cost}"


def test_buggy_tax_amount():
    """After fixing, tax_amount should be 4.25, not 425.0."""
    import buggy_arithmetic
    expected = 4.25
    assert abs(buggy_arithmetic.tax_amount - expected) < 1e-9, \
        f"buggy_arithmetic.tax_amount: expected {expected}, got {buggy_arithmetic.tax_amount}"


def test_buggy_final_price():
    """After fixing, final_price should be 54.25."""
    import buggy_arithmetic
    expected = 54.25
    assert abs(buggy_arithmetic.final_price - expected) < 1e-9, \
        f"buggy_arithmetic.final_price: expected {expected}, got {buggy_arithmetic.final_price}"


def test_buggy_fahrenheit():
    """After fixing, fahrenheit should be 77.0."""
    import buggy_arithmetic
    expected = 77.0
    assert abs(buggy_arithmetic.fahrenheit - expected) < 1e-9, \
        f"buggy_arithmetic.fahrenheit: expected {expected}, got {buggy_arithmetic.fahrenheit}"


def test_buggy_average():
    """After fixing, average should be 20.0, not 40.0."""
    import buggy_arithmetic
    expected = 20.0
    assert abs(buggy_arithmetic.average - expected) < 1e-9, \
        f"buggy_arithmetic.average: expected {expected}, got {buggy_arithmetic.average}"


# --- Transfer section ---

def test_transfer_variables_exist():
    """Transfer variables must be defined."""
    import arithmetic
    for attr in ["distance_leg1", "distance_leg2", "total_distance",
                 "total_time", "average_speed"]:
        val = getattr(arithmetic, attr, None)
        assert val is not None, f"{attr} is not defined — add it to arithmetic.py!"


def test_distance_leg1():
    import arithmetic
    expected = 18.0 * 2.5  # 45.0
    assert abs(arithmetic.distance_leg1 - expected) < 1e-9, \
        f"distance_leg1: expected {expected}, got {arithmetic.distance_leg1}"


def test_distance_leg2():
    import arithmetic
    expected = 12.0 * 1.5  # 18.0
    assert abs(arithmetic.distance_leg2 - expected) < 1e-9, \
        f"distance_leg2: expected {expected}, got {arithmetic.distance_leg2}"


def test_total_distance():
    import arithmetic
    expected = 45.0 + 18.0  # 63.0
    assert abs(arithmetic.total_distance - expected) < 1e-9, \
        f"total_distance: expected {expected}, got {arithmetic.total_distance}"


def test_total_time():
    import arithmetic
    expected = 2.5 + 1.5  # 4.0
    assert abs(arithmetic.total_time - expected) < 1e-9, \
        f"total_time: expected {expected}, got {arithmetic.total_time}"


def test_average_speed():
    import arithmetic
    expected = 63.0 / 4.0  # 15.75
    assert abs(arithmetic.average_speed - expected) < 1e-9, \
        f"average_speed: expected {expected}, got {arithmetic.average_speed}"
