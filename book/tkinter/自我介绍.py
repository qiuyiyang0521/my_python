import tkinter as tk


class App:
    def __init__(self, root) -> None:
        self.theLabel = tk.Label(root, text="我叫邱一阳!")
        self.theLabel.pack()


root = tk.Tk()
root.title("自我介绍")
app = App(root)
tk.mainloop()
