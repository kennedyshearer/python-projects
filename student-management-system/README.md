# Student Management System

A desktop application built with PyQt6 for managing student records with a modern graphical user interface.

## Features

- **Add Students**: Register new students with name, course, and mobile number
- **View Students**: Display all student records in a table format
- **Search Students**: Find specific students by name
- **Edit Students**: Update existing student information
- **Delete Students**: Remove student records with confirmation
- **Modern UI**: Clean interface with toolbar, status bar, and intuitive navigation

## Screenshots

The application features a clean, modern interface with:
- Main table displaying student records (ID, Name, Course, Mobile)
- Toolbar with quick access buttons
- Status bar with contextual actions
- Dialog-based forms for data entry and editing

## Prerequisites

- Python 3.6 or higher
- PyQt6

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd app12_student__management_system
```

2. Install the required dependencies:
```bash
pip install PyQt6
```

3. Run the application:
```bash
python main.py
```

## Database

The application uses SQLite database (`database.db`) to store student records. The database contains a `students` table with the following structure:

- `id` (Primary Key, Auto-increment)
- `name` (Text)
- `course` (Text) - Options: Biology, Math, Astronomy, Physics
- `mobile` (Text)

## Usage

### Adding a Student
1. Click the "Add Student" button in the toolbar or go to File → Add Student
2. Fill in the student's name, select a course, and enter mobile number
3. Click "Register" to save the record

### Searching for a Student
1. Click the "Search" button in the toolbar or go to Edit → Search
2. Enter the student's name
3. The matching record will be highlighted in the table

### Editing a Student
1. Click on any row in the table to select a student
2. Click "Edit Record" in the status bar
3. Modify the information as needed
4. Click "Update" to save changes

### Deleting a Student
1. Click on any row in the table to select a student
2. Click "Delete Record" in the status bar
3. Confirm the deletion in the dialog

## Project Structure

```
app12_student__management_system/
├── main.py              # Main application file
├── database.db          # SQLite database file
├── icons/               # Application icons
│   ├── add.png         # Add student icon
│   └── search.png      # Search icon
└── README.md           # This file
```

## Classes Overview

- **MainWindow**: Main application window with table and menu
- **DatabaseConnection**: Handles database connectivity
- **InsertDialog**: Dialog for adding new students
- **SearchDialog**: Dialog for searching students
- **EditDialog**: Dialog for editing student records
- **DeleteDialog**: Dialog for confirming student deletion
- **AboutDialog**: About information dialog
