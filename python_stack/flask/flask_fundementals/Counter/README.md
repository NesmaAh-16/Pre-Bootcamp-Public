Counter Assignment

A simple, interactive web application built with Python and Flask that
demonstrates session management, server-side routing, and data persistence.

📌 Project Overview

The goal of this assignment is to understand how to use session to track user
activity. The application counts how many times a user has visited the root
route and allows the user to manipulate that counter through various actions.

✨ Features

Core Requirements

  - Visit Counter: Automatically increments every time the root page (/) is
    loaded.
  - Destroy Session: A button that clears all session data and redirects the
    user back to the start.

Ninja Bonuses

  - +2 Button: Increments the counter by 2 in a single click.
  - Reset Button: Resets the counter value without destroying the entire
    session.

Sensei Bonuses

  - Custom Increment: A form where the user can input a specific number (e.g., 5
    or 10) to increment the counter by that amount.
  - Visit Tracking: A separate logic that tracks the actual number of times the
    page has been refreshed, distinct from the counter value modified by
    buttons.

🛠️ Technologies Used

  - Python 3.x
  - Flask (Web Framework)
  - Jinja2 (Templating Engine)
  - Bootstrap 5 (For a clean, responsive UI)

📂 Folder Structure

/counter_assignment
    ├── server.py          # Flask server and routing logic
    └── /templates
        └── index.html     # Main UI template

🚀 Getting Started

1. Clone or Create the Directory

Ensure you have the files organized as shown in the folder structure above.

2. Install Dependencies

Make sure you have Flask installed in your environment:

pip install Flask

3. Run the Server

Navigate to the project directory in your terminal and run:

python server.py

4. View the App

Open your web browser and go to: http://localhost:5000

💡 How It Works

1.  Secret Key: The application uses app.secret_key to encrypt the session
    cookie, making the counter secure.
2.  Session Persistence: Data is stored in the user's browser as a cookie. Even
    if the server restarts, the count remains until the session is cleared.
3.  The Redirect Pattern: To prevent form resubmission errors (POPups on
    refresh), the app uses the Post-Redirect-Get pattern for all buttons and
    forms.


