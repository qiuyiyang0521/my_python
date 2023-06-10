import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time) # 每秒更新一次时间

root = tk.Tk()
root.title("时间查看器")

time_label = tk.Label(root, font=("Helvetica", 80))
time_label.pack()

update_time()

root.mainloop()
