# Weather Data API

A Flask-based REST API that provides access to historical temperature data from the European Climate Assessment & Dataset (ECA&D). The API serves daily mean temperature data for various weather stations across Europe.

## Features

- **Web Interface**: Simple HTML interface displaying available weather stations
- **REST API**: Multiple endpoints for accessing temperature data
- **Historical Data**: Access to extensive historical temperature records
- **Flexible Queries**: Get data by station, date, or year

## API Endpoints

### Home Page
- **GET** `/` - Displays the web interface with a list of available weather stations

### Temperature Data
- **GET** `/api/v1/<station>/<date>` - Get temperature for a specific station and date
- **GET** `/api/v1/<station>` - Get all temperature data for a specific station  
- **GET** `/api/v1/yearly/<station>/<year>` - Get temperature data for a specific station and year

## API Examples

```bash
# Get temperature for station 10 on October 25, 1988
GET http://127.0.0.1:5000/api/v1/10/1988-10-25

# Get all temperature data for station 10
GET http://127.0.0.1:5000/api/v1/10

# Get temperature data for station 10 in year 1988
GET http://127.0.0.1:5000/api/v1/yearly/10/1988
```

## Response Format

### Single Data Query

```bash
{
  "station": "10",
  "date": "1988-10-25",
  "temperature": 12.5
}
```

### Multiple Records

```bash
[
  {
    "STAID": 10,
    "SOUID": 123,
    "DATE": "1988-10-25T00:00:00.000Z",
    "TG": 125,
    "Q_TG": 0
  }
]
```
