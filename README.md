# Weather CLI

A command-line weather application built with Python. It retrieves weather information for a location using the Open-Meteo API and displays the current temperature alongside an upcoming daily forecast.

This project focuses on working with external APIs, processing JSON responses, handling errors and organising Python code into reusable functions.

## Features

- **Location lookup:** Search for a location using its name.
- **Current weather:** Retrieve the current temperature for the selected location.
- **Daily forecast:** Display upcoming daily maximum and minimum temperatures.
- **Temperature units:** Support temperature unit selection.
- **Error handling:** Handle connection failures, request timeouts, HTTP errors and invalid API responses.
- **Response validation:** Check API data before processing it.
- **Automated tests:** Use pytest to test important parts of the weather data processing.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | Sending HTTP requests to external APIs |
| Open-Meteo API | Retrieving geographical and weather information |
| Pytest | Running automated tests |
| Git and GitHub | Version control and project hosting |

## APIs and Data Sources

This project uses Open-Meteo to retrieve weather information and geographical coordinates.

- [Open-Meteo](https://open-meteo.com/): Weather API and documentation.
- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api): Used to find geographical coordinates for a location.
- [Open-Meteo Forecast API](https://open-meteo.com/en/docs): Used to retrieve current weather and daily forecast information.

## Requirements

Before running the project, you need:

- Python 3 installed.
- pip, Python's package installer.
- An active internet connection.

The project also uses pytest for automated testing.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ano-P/Weather-cli.git
```

### 2. Navigate into the project directory

```bash
cd Weather-cli
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows Command Prompt:

```bash
.venv\Scripts\activate
```

For macOS or Linux:

```bash
source .venv/bin/activate
```

### 5. Install the dependencies

```bash
python -m pip install requests pytest
```

## Usage

Once the dependencies are installed, run the application using:

```bash
python weather.py
```

Follow the prompts displayed in the terminal. Enter your chosen location and select your preferred temperature unit.

The application retrieves the relevant weather information and displays the current temperature and upcoming forecast.

### Example Output

The following example shows a sample weather report:

```text
================================
    WOLLONGONG, AUSTRALIA WEATHER
================================

CURRENT CONDITIONS
Temperature: 15.9°C

UPCOMING FORECAST

2026-11-09: High 17.3°C | Low 10.5°C
2026-11-10: High 20.2°C | Low 10.1°C
2026-11-11: High 24.1°C | Low 12.8°C

--------------------------------
Weather data provided by Open-Meteo
https://open-meteo.com/
```

## Error Handling

The application includes error handling to deal with problems during API requests and data processing.

Some of the situations handled include:

- **Request timeouts:** When the API takes too long to respond.
- **Connection errors:** When a stable connection to the API cannot be established.
- **HTTP errors:** When the server responds with an unsuccessful HTTP status code.
- **Invalid responses:** When the returned JSON data does not have the expected structure.
- **Incomplete forecast data:** When required forecast information is missing or contains fewer entries than expected.
- **Unknown locations:** When the location lookup does not return a matching result.

These checks help prevent the application from processing invalid or incomplete weather information.

## Project Structure

```text
Weather-cli/
│
├── weather.py
│
├── tests/
│   └── test_weather.py
│
└── README.md
```

### Main Components

**weather.py**

Contains the main application logic.

- `main()`: Coordinates the application workflow.
- `lookup()`: Finds geographical coordinates for the requested location.
- `weather()`: Retrieves and validates weather information.
- `formatting()`: Organises the weather information into a readable report.

**tests/test_weather.py**

Contains automated tests for the weather data processing.

The tests cover:

- Correct processing of valid weather data.
- Rejection of invalid API responses.
- Rejection of incomplete forecast data.

## Running Tests

This project uses pytest for automated testing.

To run the tests, execute:

```bash
pytest -v
```

The tests use simulated API responses, so they do not need to make real requests to Open-Meteo.

They check whether the application processes valid data correctly and rejects invalid or incomplete responses.

## Current Limitations

- Requires an internet connection to retrieve weather information.
- Depends on the availability of the Open-Meteo API.
- Provides a command-line interface rather than a graphical interface.
- Does not currently provide detailed hourly forecasts.

## Project Status

This is a personal Python project developed to practise API integration, JSON processing, error handling, automated testing and version control.