# Hotel Booking System

A Python-based hotel booking application that allows users to book hotels and spa packages with secure credit card validation and authentication.

## Features

- **Hotel Management**: View and book available hotels
- **Spa Package Booking**: Book spa packages at selected hotels
- **Secure Payment Processing**: Credit card validation and authentication
- **Reservation Tickets**: Generate booking confirmations
- **Data Persistence**: CSV-based data storage for hotels, cards, and security

## Project Structure

```
app11_hotel_booking/
├── main.py                 # Main application file
├── hotels.csv             # Hotel data (id, name, city, capacity, available)
├── cards.csv              # Credit card data for validation
├── card_security.csv      # Credit card security passwords
├── planning.txt           # Project planning notes
└── README.md              # This file
```

## Installation

1. Clone or download this project
2. Ensure you have Python 3.x installed
3. Install required dependencies:
   ```bash
   pip install pandas
   ```

## Requirements

- Python 3.x
- pandas library

## Usage

1. Run the main application:
   ```bash
   python main.py
   ```

2. The application will:
   - Display available hotels
   - Prompt for hotel ID selection
   - Validate credit card information
   - Authenticate payment
   - Generate reservation tickets
   - Optionally book spa packages

## Data Files

### hotels.csv
Contains hotel information with columns:
- `id`: Unique hotel identifier
- `name`: Hotel name
- `city`: Hotel location
- `capacity`: Number of guests the hotel can accommodate
- `available`: Booking availability (yes/no)

### cards.csv
Contains valid credit card information for testing:
- `number`: Card number
- `expiration`: Expiration date
- `holder`: Cardholder name
- `cvc`: Security code

### card_security.csv
Contains credit card passwords for authentication:
- `number`: Card number
- `password`: Associated password

## Classes

### Hotel
- Base class for hotel management
- Methods: `book()`, `available()`, `get_hotel_count()`

### SpaHotel
- Inherits from Hotel class
- Adds spa package booking functionality

### ReservationTicket
- Generates booking confirmation tickets
- Includes customer name and hotel information

### SpaTicket
- Generates spa package booking confirmations

### CreditCard
- Handles credit card validation
- Validates card details against stored data

### SecureCreditCard
- Inherits from CreditCard
- Adds password authentication functionality

## Example Usage

```
Enter the id of the hotel: 134
Enter your name: John Doe
Thank you for your reservation!
Here is your booking information:
Name: John Doe
Hotel name: Tourist Sunny Apartment

Do you want to book a SPA package? yes
Thank you for your SPA reservation!
Here is your SPA booking information:
Name: John Doe
Hotel name: Tourist Sunny Apartment
```

## Security Features

- Credit card validation against stored data
- Password-based authentication for secure transactions
- Data persistence with CSV files
