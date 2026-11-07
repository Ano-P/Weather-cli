
import pytest
from unittest.mock import Mock

import weather as app


def sample_response():
    return {
        "current": {
            "temperature_2m": 24.5
        },
        "daily": {
            "time": [
                "2026-11-07",
                "2026-11-08",
                "2026-11-09",
                "2026-11-10"
            ],
            "temperature_2m_max": [27, 29, 25, 26],
            "temperature_2m_min": [16, 18, 14, 15]
        }
    }


def test_weather_returns_correct_data(monkeypatch):
    response = Mock()
    response.json.return_value = sample_response()
    response.raise_for_status.return_value = None

    monkeypatch.setattr(
        app.requests,
        "get",
        Mock(return_value=response)
    )

    result = app.weather(-34.42, 150.89, "celsius")

    assert result["current_temp"] == 24.5
    assert result["dates"] == sample_response()["daily"]["time"]
    assert result["max_temp"] == [27, 29, 25, 26]
    assert result["min_temp"] == [16, 18, 14, 15]


def test_weather_rejects_invalid_response(monkeypatch):
    response = Mock()
    response.json.return_value = []
    response.raise_for_status.return_value = None

    monkeypatch.setattr(
        app.requests,
        "get",
        Mock(return_value=response)
    )

    with pytest.raises(ValueError):
        app.weather(-34.42, 150.89, "celsius")


def test_weather_rejects_incomplete_forecast(monkeypatch):
    data = sample_response()
    data["daily"]["time"] = data["daily"]["time"][:3]

    response = Mock()
    response.json.return_value = data
    response.raise_for_status.return_value = None

    monkeypatch.setattr(
        app.requests,
        "get",
        Mock(return_value=response)
    )

    with pytest.raises(ValueError, match="Incomplete forecast data"):
        app.weather(-34.42, 150.89, "celsius")
