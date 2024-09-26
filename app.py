from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from datetime import datetime

app = Flask(__name__)

def load_transactions():
    try:
        with open('transaction.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    
def save_transactions(transactions):
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file)


@app.route('/')
def index():
    transactions = load_transactions()
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expenses = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    net_balance = total_income - total_expenses
    return render_template('index.html', transactions = transactions, net_balance = net_balance)


@app.route('/add', methods = ['POST'])
def add_transactions():
    transactions = load_transactions()
    amount = float(request.form['amount'])
    description = request.form['description']
    date = request.form['date'] or str(datetime.today().date())
    trans_type = request.form['type']
    transaction = {"amount": amount, "description": description, "date": date, "type": trans_type}
    transactions.append(transaction)
    save_transactions(transactions)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_transaction(index):
    transactions = load_transactions()
    if 0 <= index < len(transactions):
        transactions.pop(index)
        save_transactions(transactions)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)
