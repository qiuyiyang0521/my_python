import tkinter as tk


class App:
    def __init__(self, root):

        frame = tk.Frame(root)
        frame.pack()

        self.hi_there = tk.Button(
            frame, text="打招呼", fg="blue", bg="red", command=self.say_hi, padx=10, pady=10)
        self.hi_there.pack(padx=10, pady=10)

    def say_hi(self):
        print("大家好，我邱一阳")


root = tk.Tk()
app = App(root)

root.mainloop()
