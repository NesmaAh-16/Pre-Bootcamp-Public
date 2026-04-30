Dojo Fruit Store (Flask)

A web application built with Python and Flask that simulates an online fruit
store. This project focuses on handling POST requests, processing form data, and
using static files.

🚀 Features

  - Order Processing: Users can select quantities for different fruits and
    submit their personal information.
  - Dynamic Calculations: The server converts string inputs to integers and
    calculates the total item count.
  - Real-time Logging: Prints a "Charging..." message to the terminal for every
    successful checkout.
  - Timestamps: Automatically generates and displays the current date and time
    on the receipt.
  - Static Assets: Includes custom CSS and handles fruit image displays via the
    /fruits route.

📂 Project Structure

/dojo_fruit_store
    ├── server.py          # Main Flask logic and route handling
    ├── /static            # Folder for static assets
    │   ├── /css
    │   │   └── style.css  # Custom styling
    │   └── /img           # Fruit images
    └── /templates
        ├── index.html     # Main store page with form
        ├── checkout.html  # Order confirmation receipt
        └── fruits.html    # Page displaying fruit gallery

🛠️ Setup & Usage

1.  Install Flask:

    pip install Flask

2.  Run the Server:

    python server.py

3.  Purchase Fruit:

      - Visit http://localhost:5000 in your browser.
      - Enter quantities, your name, and ID.
      - Click "Buy me stuff!" to see your receipt.

4.  Terminal Output: Check your terminal window after checkout to see the
    charging confirmation message.

💡 Key Learnings

  - POST Data: Understanding how to extract data from request.form using the
    name attribute from HTML inputs.
  - Data Types: Converting string inputs from a web form into integers for
    mathematical calculations.
  - Template Variables: Passing multiple variables from Python to HTML using the
    render_template function.
  - Static Routing: Correctly using url_for to link CSS and image files.
