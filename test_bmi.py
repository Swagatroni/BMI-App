import pytest
from bmi_app import calculate_bmi, classify

def test_calculate_bmi(monkeypatch):
    # Mock input
    monkeypatch.setattr('builtins.input', lambda _: '160')
    assert calculate_bmi() == pytest.approx(24.34, 0.01)

def test_classify_underweight(monkeypatch, capsys):
    # Mock input
    monkeypatch.setattr('builtins.input', lambda _: '18.0')

    # Capture stdout
    classify()
    captured = capsys.readouterr()

    assert captured.out.strip() == "You are Underweight"

def test_classify_normal_weight(monkeypatch, capsys):
    # Mock input
    monkeypatch.setattr('builtins.input', lambda _: '22.0')

    # Capture stdout
    classify()
    captured = capsys.readouterr()

    assert captured.out.strip() == "You have a Normal Weight"

def test_classify_overweight(monkeypatch, capsys):
    # Mock input
    monkeypatch.setattr('builtins.input', lambda _: '27.0')

    # Capture stdout
    classify()
    captured = capsys.readouterr()

    assert captured.out.strip() == "You Overweight"

def test_classify_normal_weight(monkeypatch, capsys):
    # Mock input
    monkeypatch.setattr('builtins.input', lambda _: '35.0')

    # Capture stdout
    classify()
    captured = capsys.readouterr()

    assert captured.out.strip() == "You are Obese"

