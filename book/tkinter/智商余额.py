import tkinter as tk

root = tk.Tk()

textLabel = tk.Label(root, text="您所下载的内容有高智商内容，请您的智商余额到达250再下载！")
textLabel.pack(side=tk.LEFT)

photo = tk.PhotoImage(file="image.gif")
imgLabel = tk.Label(root, image=photo)
imgLabel.pack(side=tk.RIGHT)
