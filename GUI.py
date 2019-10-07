HEIGHT = 500
WIDTH = 500



import tkinter as tk

root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = '#809fff')
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)


button = tk.Button(frame, text = "bandymo mygtukas", bg = 'grey', fg = 'red')
button.pack()

label = tk.Label(frame, text = "Teksto vieta", bg = 'yellow')
label.pack()

entry = tk.Entry(frame, text = "Teksto ivestis", bg = '#ff3333')
entry.pack()
root.mainloop()