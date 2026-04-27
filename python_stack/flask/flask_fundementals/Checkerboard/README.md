# Checkerboard - Flask Assignment

A Flask application that renders a dynamic checkerboard grid based on URL parameters.

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
| `/` | `localhost:5000/` | 8x8 checkerboard |
| `/<x>` | `localhost:5000/4` | 8x4 checkerboard |
| `/<x>/<y>` | `localhost:5000/6/10` | 6x10 checkerboard |

## How it Works

- Nested Jinja2 loops build the grid row by row
- Cell color is determined by `(row + column) % 2`
  - Even → Red
  - Odd → Black
- Any unknown route → "Sorry! No response. Try again."

## Levels

- **Level 1** `/` → default 8x8 board
- **Level 2** `/<x>` → 8 rows, x columns
- **Level 3** `/<x>/<y>` → x rows, y columns dynamically