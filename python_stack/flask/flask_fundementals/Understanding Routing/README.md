# Flask Routes App

A simple Flask application demonstrating URL routing and dynamic parameters.

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
Then open: `http://localhost:5000`

## Routes

| Route | Example | Output |
|---|---|---|
| `/` | `localhost:5000/` | `Hi World!` |
| `/<name>` | `localhost:5000/Ahmad` | `Ahmad` |
| `/say/<name>` | `localhost:5000/say/Ahmad` | `Hi Ahmad!` |
| `/repeat/<times>/<name>` | `localhost:5000/repeat/3/hello` | `hello hello hello` |

## Error Handling
- `404` → Sorry! No response. Try again.