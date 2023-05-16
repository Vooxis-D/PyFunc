# coding:utf-8
import tkinter

app = tkinter.Tk()

app.title("PyFuncs")

dims_X = 540
dims_Y = 350

app.resizable(height=False, width=False)

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
pos_X = (screen_width // 2) - (dims_X // 2)
pos_Y = (screen_height // 2) - (dims_Y // 2)

dims = f"{str(dims_X)}x{str(dims_Y)}+{str(pos_X)}+{str(pos_Y - 35)}"
app.geometry(dims)

app.mainloop()
