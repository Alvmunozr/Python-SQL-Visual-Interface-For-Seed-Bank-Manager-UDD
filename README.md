# Python-SQL-Visual-Interface-For-Seed-Bank-Manager-UDD



# Seed Bank Management

This project is a Python application with a **Tkinter**-based graphical user interface, designed to manage the database of a seed bank in Chile. It is intended for a reserve that preserves and manages various plant species, providing tools to store, search, and analyze seed information.

---

## Main Features

### 1. **Data Management**

- **Add:** Allows you to add seeds with details such as common name, quantity, type, and storage location.
- **Search:** Quickly search for seeds by any field.
- **Edit:** Modify existing records.
- **Delete:** Remove individual records or all records from the database.

### 2. **Export/Import Data**

- **Export to Excel:** Generate an Excel file with all records stored in the database.
- **Import from Excel:** Load data from an Excel file.

### 3. **Quick Statistics**

- Calculate the total number of stored records.
- Calculate the average quantity available.

### 4. **Quick Edit**

- Quickly increase or decrease the seed quantity directly from the interface.

### 5. **Intuitive Interface**

- User-friendly design with customizable styles.
- Dropdown menus for additional functionalities.

---

## System Requirements

- **Python 3.8 or higher.**
- Required libraries (found in `requirements.txt`):
  - `tkinter`
  - `sqlite3`
  - `pandas`
  - `openpyxl`

---

## Initial Setup

### 1. **Clone the Repository**

```bash
git clone https://github.com/youruser/seed-bank-management.git
cd seed-bank-management
```

### 2. **Install Dependencies**

If using a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Then, install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. **Set Up the Database**

The application will automatically create the `base_datos.db` file if it does not exist. If you need initial data, you can import an Excel file with the corresponding structure.

---

## Running the Project

To start the application:

```bash
python main.py
```

---

## Using the Application

1. **Add Data:** Fill in the form fields and press the "ADD DATA" button.
2. **Search Records:** Enter a term in the "Search" field and press the "SEARCH" button.
3. **Edit or Delete:** Select a record in the table to edit or delete it.
4. **Export/Import Data:** Use the "OTHER" dropdown menu to export to Excel or load data from a file.

---

## Database Structure

The SQLite database uses a table called `datos` with the following structure:

| Field      | Type    | Description                        |
| ---------- | ------- | ---------------------------------- |
| `ID`       | INTEGER | Unique identifier (autoincrement). |
| `NOMBRE`   | TEXT    | Common name of the seed.           |
| `CANTIDAD` | INTEGER | Available quantity.                |
| `GUARDADA` | TEXT    | Storage location.                  |
| `TIPO`     | TEXT    | Type of seed.                      |

---

## License

This project is licensed under the [MIT License](LICENSE). This means you are free to use, modify, and distribute the software as long as you include proper credit. Check the `LICENSE` file for more details.

---

## Contributions

If you would like to contribute to this project:

1. Fork the repository.
2. Create a branch for your feature or fix:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Submit a pull request detailing your changes.

---

## Contact

For inquiries or feedback, you can contact me at:

- **GitHub:** [alvmunozr](https://github.com/alvmunozr)

