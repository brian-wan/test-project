import pytest

tk = pytest.importorskip("tkinter", reason="tkinter is not installed in this environment")

from addapp.gui import App


@pytest.fixture
def app():
    try:
        root = tk.Tk()
    except tk.TclError as exc:
        pytest.skip(f"no display available for Tkinter: {exc}")
    application = App(root)
    yield application
    root.destroy()


def test_gui_add_valid_inputs(app):
    app.entry_a.insert(0, "2")
    app.entry_b.insert(0, "3")
    app.on_add()
    assert app.result_label.cget("text") == "Result: 5.0"


def test_gui_add_negative_and_decimal(app):
    app.entry_a.insert(0, "-1.5")
    app.entry_b.insert(0, "4")
    app.on_add()
    assert app.result_label.cget("text") == "Result: 2.5"


def test_gui_add_invalid_input_shows_error(app):
    app.entry_a.insert(0, "not-a-number")
    app.entry_b.insert(0, "1")
    app.on_add()
    assert "not a valid number" in app.result_label.cget("text")
