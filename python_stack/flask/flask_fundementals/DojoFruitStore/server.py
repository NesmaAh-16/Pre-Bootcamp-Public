from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    # 1. Capture data from form (remember: they arrive as strings)
    strawberry_qty = int(request.form['strawberry'])
    raspberry_qty = int(request.form['raspberry'])
    apple_qty = int(request.form['apple'])
    
    first_name = request.form['first_name']
    student_id = request.form['student_id']
    
    # 2. Perform calculations
    total_count = strawberry_qty + raspberry_qty + apple_qty
    
    # 3. Print the required terminal message
    print(f"Charging {first_name} for {total_count} fruits.")
    
    # 4. Get current date/time for the receipt
    now = datetime.now().strftime("%B %d %Y %I:%M:%S %p")

    # 5. Pass all info to the template
    return render_template("checkout.html", 
        s_qty=strawberry_qty, 
        r_qty=raspberry_qty, 
        a_qty=apple_qty,
        total=total_count,
        name=first_name,
        id=student_id,
        timestamp=now
    )

@app.route('/fruits')         
def fruits():
    # Bonus: Display images of fruits
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)