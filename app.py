from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def utility_processor():
    return dict(enumerate=enumerate)


# Load transactions from a JSON file
def load_transactions():
    try:
        with open('transactions.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # If the file doesn't exist or is empty, return an empty list

# Write transactions to a JSON file
def save_transactions(transactions):
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file, indent=4)

# Initialize the transactions list
transactions = load_transactions()

@app.route('/')
def index():
    # Calculate net balance
    net_balance = sum([t["amount"] for t in transactions])
    return render_template('index.html', transactions=transactions, net_balance=net_balance)



# Route to add a new transaction
@app.route('/add', methods=['POST'])
def add_transaction():
    # Extract form data
    description = request.form['description']
    amount = float(request.form['amount'])
    type_of_transaction = request.form['type']  # 'income' or 'expense'
    
    # Ensure expenses are negative and income is positive
    if type_of_transaction == 'expense':
        amount = -amount  # Negate the amount for expenses
    
    # Add the transaction to the in-memory list
    transactions.append({
        "description": description,
        "amount": amount,
        "type": type_of_transaction
    })
    
    # Save updated transactions to the JSON file
    save_transactions(transactions)
    
    return redirect('/')



# Route to delete a transaction
@app.route('/delete/<int:index>', methods=['POST'])
def delete_transaction(index):
    try:
        # Remove the transaction from the in-memory list
        transactions.pop(index)
        
        # Save the updated list of transactions to the JSON file
        save_transactions(transactions)
    except IndexError:
        pass  # Handle invalid index gracefully
    
    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True)
