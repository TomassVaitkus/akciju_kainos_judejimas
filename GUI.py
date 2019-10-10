# # naudojamai informacijos saltiniai:
# https://www.tutorialspoint.com/python/python_gui_programming.htm
# https://www.w3schools.com/colors/colors_picker.asp



HEIGHT = 500
WIDTH = 500



import tkinter as tk

root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = '#ccccff')
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)


button = tk.Button(frame, text = "bandymo mygtukas", bg = 'grey', fg = '#e6e6ff')
button.pack()

label = tk.Label(frame, text = "Teksto vieta", bg = '#a3a375')
label.pack()

entry = tk.Entry(frame, text = "Teksto ivestis", bg = '#f5f5f0')
entry.pack()
root.mainloop()