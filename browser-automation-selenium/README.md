# Browser Automation with Selenium

A Python-based web automation tool that uses Selenium WebDriver to automate browser interactions. This project includes both a command-line interface and a graphical user interface (GUI) for easy interaction.

## Features

- **Web Login Automation**: Automatically logs into web applications
- **Form Filling**: Automates form submission with user-provided data
- **File Download**: Handles file downloads from web pages
- **GUI Interface**: User-friendly graphical interface built with Tkinter
- **Chrome Browser Support**: Uses Chrome WebDriver for automation

## Prerequisites

- Python 3.6 or higher
- Google Chrome browser installed
- ChromeDriver (included in the project)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd app14-browser-automation-selenium
```

2. Install required Python packages:
```bash
pip install selenium
```

3. Ensure ChromeDriver is available:
   - The project includes ChromeDriver in the `chromedriver-win64/` directory
   - Make sure the ChromeDriver version is compatible with your Chrome browser version

## Usage

### Command Line Interface

Run the main automation script directly:

```bash
python main.py
```

This will execute the default automation sequence:
- Login to demoqa.com with predefined credentials
- Fill out a form with sample data
- Download a file
- Close the browser

### Graphical User Interface

Launch the GUI application:

```bash
python gui.py
```

The GUI provides:
- Login form fields for username and password
- Form fields for personal information (name, email, addresses)
- Submit button to run the automation
- Close browser button to terminate the session

## Project Structure

```
app14-browser-automation-selenium/
├── main.py                 # Main automation logic
├── gui.py                  # Graphical user interface
├── chromedriver-win64/     # ChromeDriver executable
│   ├── chromedriver.exe
│   ├── LICENSE.chromedriver
│   └── THIRD_PARTY_NOTICES.chromedriver
└── README.md              # This file
```

## Code Overview

### WebAutomation Class (`main.py`)

The main automation class provides the following methods:

- `__init__()`: Initializes Chrome WebDriver with custom options
- `login(username, password)`: Automates login to demoqa.com
- `fill_form(fullname, email, current_address, permanent_address)`: Fills and submits forms
- `download()`: Downloads files from the web page
- `close()`: Closes the browser session

### GUI Application (`gui.py`)

The Tkinter-based GUI provides:
- Input fields for all required data
- Submit functionality to run automation
- Browser control options

## Configuration

### Chrome Options

The automation uses several Chrome options for optimal performance:
- Disabled search engine choice screen
- Custom download directory (current working directory)
- Headless mode support (can be enabled)

### Target Website

Currently configured to work with [demoqa.com](https://demoqa.com), a testing website for automation practice.

## Customization

To adapt this automation for other websites:

1. Modify the URL in the `login()` method
2. Update element selectors (IDs, XPaths) to match the target website
3. Adjust form field mappings in the `fill_form()` method
4. Update the GUI labels and fields as needed

## Troubleshooting

### Common Issues

1. **ChromeDriver Version Mismatch**: Ensure ChromeDriver version matches your Chrome browser version
2. **Element Not Found**: Check if the target website structure has changed
3. **Timeout Errors**: Increase wait times in WebDriverWait calls if needed

### Debug Mode

To run with visible browser (non-headless):
- Remove or comment out headless options in the Chrome options
