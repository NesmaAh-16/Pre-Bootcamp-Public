# Flask Hello World

A minimal Flask web application that displays "Hello World!" in the browser.

## Requirements

- Python 3.x
- Flask

## Installation

```bash
pip install flask
```

## Run

```bash
python app.py
```

Then open your browser at: `http://localhost:5000`

## How it works

| Part | Description |
|---|---|
| `Flask(__name__)` | Creates the app |
| `@app.route('/')` | Listens on the homepage |
| `hello_world()` | Returns text to the browser |
| `debug=True` | Auto-restarts on code changes |