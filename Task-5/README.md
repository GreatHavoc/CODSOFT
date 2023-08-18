# Contact Book Software

Welcome to the Contact Book software project! This application allows you to store, update, and delete contacts. Contacts are stored and retrieved from a database. Additionally, the software extracts country codes and names from an Excel file and uses the ttkbootstrap library to provide a customized and visually appealing user interface.

## Features

- Store, update, and delete contacts.
- Contacts are stored and retrieved from a database.
- Extract country codes and names from an Excel file.
- Customized user interface using the ttkbootstrap library.

## Requirements

- Windows operating system (for using the provided executable).
- If you want to run the script directly, you will need Python (3.6 or higher), the `ttkbootstrap` library (install using `pip install ttkbootstrap`), and the `openpyxl` library (install using `pip install openpyxl`).

## How to Use

### Option 1: Using the Executable (Windows)

1. Download the "Contact-Book.exe" file from the "direct run" folder.
2. Double-click the executable file to run the Contact Book software.
3. The software GUI will open up, allowing you to perform various contact operations.

### Option 2: Running the Script (Python)

1. Navigate to the project directory:


	cd Task-5


2. Run the contact book software script:


	python contact_book.py (before running install the requirements)


3. The software GUI will open up, allowing you to perform various contact operations.

## Extracting Country Codes from Excel

1. Prepare an Excel file named "country.xlsx" with columns "Country" and "Code".
2. Place the Excel file in the project directory.
3. The software will automatically extract country codes and names from the Excel file during runtime.


## Future Enhancements

- Import and export contacts using different file formats.
- Support for additional contact details.

## Contributing

Contributions are welcome! If you want to contribute to this project, please fork the repository and create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).