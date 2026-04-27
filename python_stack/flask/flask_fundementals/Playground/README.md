# Playground - Flask Assignment

A Flask application that renders dynamic colored boxes based on URL parameters.

## Project Structure
project/
├── main.py
├── templates/
│   └── index.html
└── static/
└── style.css
## Installation
```bash
pip install flask
```

## Run
```bash
python main.py
```

## Routes

| Route | Example | Output |
|---|---|---|
| `/play` | `localhost:5000/play` | 3 blue boxes |
| `/play/<x>` | `localhost:5000/play/7` | 7 blue boxes |
| `/play/<x>/<color>` | `localhost:5000/play/5/green` | 5 green boxes |

## Rules & Protection

- `x` must be an integer — otherwise 404
- `x` maximum is 100 boxes
- Allowed colors: `red` `blue` `green` `yellow` `purple` `orange`
- Any unknown route → "Sorry! No response. Try again."

## Levels

- **Level 1** `/play` → always 3 blue boxes
- **Level 2** `/play/(x)` → x blue boxes dynamically
- **Level 3** `/play/(x)/(color)` → x boxes in any allowed color