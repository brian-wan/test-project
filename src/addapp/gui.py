import tkinter as tk

from addapp.calculator import add, parse_number, subtract


class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Add Two Numbers")

        tk.Label(root, text="Number A:").grid(row=0, column=0, padx=8, pady=8, sticky="e")
        self.entry_a = tk.Entry(root)
        self.entry_a.grid(row=0, column=1, padx=8, pady=8)

        tk.Label(root, text="Number B:").grid(row=1, column=0, padx=8, pady=8, sticky="e")
        self.entry_b = tk.Entry(root)
        self.entry_b.grid(row=1, column=1, padx=8, pady=8)

        add_button = tk.Button(root, text="Add", command=self.on_add)
        add_button.grid(row=2, column=0, padx=8, pady=8)

        subtract_button = tk.Button(root, text="Subtract", command=self.on_subtract)
        subtract_button.grid(row=2, column=1, padx=8, pady=8)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=8)

        root.bind("<Return>", lambda _event: self.on_add())

    def on_add(self) -> None:
        try:
            a = parse_number(self.entry_a.get())
            b = parse_number(self.entry_b.get())
        except ValueError as exc:
            self.result_label.config(text=str(exc))
            return

        self.result_label.config(text=f"Result: {add(a, b)}")

    def on_subtract(self) -> None:
        try:
            a = parse_number(self.entry_a.get())
            b = parse_number(self.entry_b.get())
        except ValueError as exc:
            self.result_label.config(text=str(exc))
            return

        self.result_label.config(text=f"Result: {subtract(a, b)}")


def main() -> None:
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
