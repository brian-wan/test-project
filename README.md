# test-project

A small Tkinter GUI for adding, subtracting, or dividing two numbers, with
arithmetic logic kept separate from the GUI so it can be tested headlessly.

## Run

```bash
pip install -r requirements.txt
PYTHONPATH=src python -m addapp.gui
```

## Test

```bash
pip install -r requirements.txt
pytest
```

See `AGENTS.md` for stack, layout, and CI details.
