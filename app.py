from flask import Flask, render_template, request, redirect, url_for, flash
import datetime


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed to flash sms

#  Global variable to storage balance (real scenario must be a DB)
balance = 1000

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/purchase-form', methods=['GET', 'POST'])
def purchase_form():
    if request.method == 'POST':
        # Record data from purchase
        product_name = request.form['product_name']
        unit_price = request.form['unit_price']
        number_of_pieces = request.form['number_of_pieces']

        # Validate:
        #   - Field NO empty
        #   - Corcet input str, int...
        if not product_name or not unit_price or not number_of_pieces:
            flash('Fill form correctly, please.', 'error')
            return redirect(url_for('purchase_form'))

        try:
            unit_price = float(unit_price)
            number_of_pieces = int(number_of_pieces)
        except ValueError:
            flash('Please add correct numeric value to price and amount', 'error')
            return redirect(url_for('purchase_form'))

        # Here we can process the purchase (save in DB, update stock...)
        flash('Purchase registred!!', 'success')

        # No return to main page, stay un purchase
        return redirect(url_for('purchase_form'))

    # Si es un GET, simplemente mostramos el formulario
    return render_template('purchase-form.html')


@app.route('/sale-form', methods=["GET", "POST"])
def sale_form():
    if request.method == "POST":
        # Record data from purchase
        product_name = request.form['product_name']
        unit_price = request.form['unit_price']
        number_of_pieces = request.form['number_of_pieces']

        # Validate
        if not product_name or not unit_price or not number_of_pieces:
            flash('Please fill out all fields.', 'error')
        else:
            flash(f'Sale of {product_name} was successful!', 'success')
            # Aquí puedes agregar la lógica para guardar la venta
        # stay in sale_form
        return redirect(url_for('sale_form'))
    return render_template('sale-form.html')

@app.route('/balance-change-form', methods=["GET", "POST"])
def balance_change_form():
    global balance  # Access to global variable

    if request.method == "POST":
        # Record data
        operation_type = request.form['operation_type']
        change_value = float(request.form['change_value'])

        # validate
        if operation_type not in ['add', 'subtract']:
            flash('Invalid operation selected!', 'error')
            return redirect(url_for('balance_change_form'))

        # Carry out the corresponding operation.
        if operation_type == 'add':
            balance += change_value
            flash(f'Balance increased by {change_value}€. New balance: {balance}€', 'success')
        elif operation_type == 'subtract':
            balance -= change_value
            flash(f'Balance decreased by {change_value}€. New balance: {balance}€', 'success')

        # stay in balance_change_form
        return redirect(url_for('balance_change_form'))

    return render_template('balance-change-form.html', balance=balance)


# Example f historical data, they should come from a DB
history_data = [
    {"id": 1, "operation": "Purchase", "product": "Product A", "amount": 50, "date": "2025-01-01"},
    {"id": 2, "operation": "Sale", "product": "Product B", "amount": 30, "date": "2025-01-02"},
    {"id": 3, "operation": "Purchase", "product": "Product C", "amount": 20, "date": "2025-01-05"},
    {"id": 4, "operation": "Sale", "product": "Product A", "amount": 10, "date": "2025-01-06"},
    {"id": 5, "operation": "Purchase", "product": "Product B", "amount": 40, "date": "2025-01-07"}
]

@app.route('/history/', methods=['GET'])
def history():
    # get parameters 'from' y 'to' from URL
    from_date = request.args.get('from')
    to_date = request.args.get('to')

    # Convert date to datatime object to check if exists
    if from_date:
        from_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')
    if to_date:
        to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')

    # Filter historical by date
    filtered_history = []

    for entry in history_data:
        entry_date = datetime.datetime.strptime(entry['date'], '%Y-%m-%d')

        # If not coincident shows FULL
        if from_date and to_date:
            if from_date <= entry_date <= to_date:
                filtered_history.append(entry)
        elif from_date:
            if entry_date >= from_date:
                filtered_history.append(entry)
        elif to_date:
            if entry_date <= to_date:
                filtered_history.append(entry)
        else:
            filtered_history.append(entry)

    # Show filter data in the web!
    return render_template('history.html', history=filtered_history)
if __name__ == '__main__':
    app.run(debug=True)