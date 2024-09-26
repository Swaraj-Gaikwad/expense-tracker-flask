# Expense Tracker Flask App

This is a simple **Expense Tracker** application built using **Flask**. The app allows users to add income and expense entries, view them, and delete them if needed. It also calculates and displays the net balance based on the total income and expenses.

## Features

- **Add Income/Expense**: Users can enter the amount, description, date, and type (income/expense).
- **Delete Income/Expense**: Users can delete a transaction from the list.
- **Show Net Balance**: Displays the net balance, which is calculated as:
Net Balance = Total Income - Total Expenses


## Technologies Used

- **Flask**: A lightweight web framework for Python to create the web app.
- **HTML/CSS**: For building the front-end of the application.
- **JSON**: For storing transaction data.

## Installation and Setup

To run this project locally, follow these steps:

- 1. **Clone the repository**:
 git clone https://github.com/Swaraj-Gaikwad/expense-tracker-flask.git

- 2. **Navigate to the project directory**:
cd expense-tracker-flask

- 3. **Create a virtual environment and activate it**:
    - python -m venv env
    - env\Scripts\activate

- 4. **Install the required dependencies**:
pip install flask

- 5. **Open the app in a browser**

**How to Use**:
- Home Page: The home page displays all existing transactions along with the net balance.
- Add Transaction: Use the form on the home page to add a new transaction. Enter the amount, description, date, and type (income or expense).
- Delete Transaction: Click the delete button next to any transaction to remove it.
- Net Balance: The net balance is automatically updated based on the income and expenses

**Project Structure**:
- expense_tracker_flask/
- │
- ├── env/                  # Virtual environment folder (excluded from Git)
- ├── app.py                # Main Flask application
- ├── templates/            # HTML templates
- │   └── index.html        # Home page for the app
- ├── static/               # Static assets (CSS)
- │   └── style.css         # Custom CSS
- ├── transactions.json     # JSON file for storing transactions
- ├── README.md             # Project documentation
- └── .gitignore            # Files and directories to ignore in Git

**License**
This project is licensed under the MIT License. Feel free to use and modify the code as needed.



