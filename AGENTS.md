# Project agent memory

This file is the project's committed home for project-intrinsic agent knowledge: build, test, release, architecture, and sharp-edge notes that should travel with the code.

- Add durable project-specific notes here as they are discovered through real work.

## Add/Subtract Two Numbers GUI

- Stack: Python 3 stdlib `tkinter` for the GUI, `pytest` for tests. No third-party GUI
  dependency.
- Both `add(a, b)` and `subtract(a, b)` live in `calculator.py` and share the same
  `entry_a`/`entry_b`/`result_label` widgets in the GUI via separate buttons
  (`on_add`/`on_subtract` handlers). The Enter key shortcut stays bound to Add only.
- Layout: `src/addapp/calculator.py` holds pure arithmetic/parsing logic with no Tk
  import. `src/addapp/gui.py` wires a Tkinter `App` class to that logic. Tests live in
  `tests/test_calculator.py` (pure logic) and `tests/test_gui.py` (real Tkinter widgets,
  no mocking).
- Operations beyond `add` (e.g. `divide`) follow the same convention: raise a plain
  `ValueError` with a user-facing message for any operation-specific error case (e.g.
  division by zero), so the GUI's existing `except ValueError` handling in each
  `on_<op>` method catches it and shows the message in `result_label` without a
  traceback ever reaching the user.
- Run the app: `PYTHONPATH=src python -m addapp.gui` (or `python src/addapp/gui.py`).
- Run tests: `pip install -r requirements.txt && pytest`.
- `tests/test_gui.py` needs a working Tk installation and a display. It uses
  `pytest.importorskip("tkinter")` plus a `tk.TclError` catch around `Tk()`, so it skips
  cleanly on machines without Tk/a display (e.g. a bare Python without `python3-tk`,
  or a headless dev sandbox) instead of failing collection or erroring out.
- CI (`.github/workflows/ci.yml`) runs on `ubuntu-latest`, installs `python3-tk` and
  `xvfb`, and runs the suite under `xvfb-run -a pytest -v` so the GUI tests actually
  execute against a real (virtual) display rather than just skipping.
