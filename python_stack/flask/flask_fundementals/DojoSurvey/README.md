Champion Survey (Flask)

A simple web application built with Python and Flask that collects user data via
a form and displays the results on a separate page.

🚀 Features

  - Form Submission: Collects user information including name, location, and
    language.
  - POST Request Handling: Processes data securely using Flask's request.form.
  - Ninja Bonus: Includes Radio Buttons for experience level.
  - Sensei Bonus: Includes Checkboxes for learning interests, handled via
    getlist().
  - Bootstrap Integration: Styled with a clean CSS framework for a professional
    look.

📂 Project Structure

/champion_survey
    ├── server.py          # Flask routing and logic
    └── /templates
        ├── index.html     # Survey form page
        └── result.html    # Submission results page

🛠️ Setup & Usage

1.  Install Flask:
    pip install Flask
2.  Run the Server:
    python server.py
3.  Open Browser: Visit http://localhost:5000 to take the survey.

