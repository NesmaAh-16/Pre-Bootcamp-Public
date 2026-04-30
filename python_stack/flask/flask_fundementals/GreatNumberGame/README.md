Great Number Game (Flask)

An interactive web-based guessing game built with Python and Flask. The
application uses session management to track a randomly generated number and
provides real-time feedback to the user based on their guesses.

🎯 Features

Core Logic

  - Random Number Generation: Upon the first visit or reset, the server picks a
    secret number between 1 and 100.
  - Session Persistence: The target number and attempt count are stored in the
    session, ensuring they stay the same until the game ends.
  - Visual Feedback: Large colored boxes indicate if a guess was "Too High"
    (Red), "Too Low" (Red), or "Correct" (Green).

🥋 Ninja Bonuses

  - Attempts Tracker: Keeps track of how many times the user has guessed during
    the current round.
  - Positioning & Colors: Professional styling using a dedicated CSS stylesheet
    to match the project wireframes.

🎓 Sensei Bonuses

  - Attempt Limit (Game Over): Users only have 5 attempts. If they fail to guess
    correctly within 5 tries, a "You Lose!" message appears with the correct
    number.
  - Leaderboard:
      - Successful players can submit their name upon winning.
      - A dedicated /leaderboard route displays a list of winners.
      - Scores are sorted automatically so that players with the fewest attempts
        appear at the top.

🛠️ Technologies Used

  - Python 3.x
  - Flask (Framework)
  - Jinja2 (Templating)
  - CSS3 (Custom Styling)

📂 Folder Structure

/great_number_game
    ├── server.py          # Flask logic, routing, and session handling
    ├── /static
    │   └── /css
    │       └── style.css  # Game layout and status box styling
    └── /templates
        ├── index.html     # Main game interface
        └── leaderboard.html # High-scores display page

🚀 Getting Started

1. Installation

Ensure you have Flask installed in your Python environment:

pip install Flask

2. Run the Application

Navigate to the project root and start the server:

python server.py

3. Play the Game

Open your browser and visit: http://localhost:5000

💡 Technical Note

The leaderboard is currently stored in a global variable in server.py. This
means the scores will persist as long as the server is running but will reset if
the server is restarted. This was chosen to demonstrate advanced list
manipulation and sorting in Python.


