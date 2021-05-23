import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox
import re

# ClassName.__doc__




colapp = "antique white"
col1 = "RoyalBlue2"
col2 = "medium orchid"
col3 = "DarkOliveGreen1"
col4 = "DarkOrange2"

fontverysmall = ("Arial", 9)
fontsmall = ("Arial", 14)
fontmiddle = ("Arial", 20)
fontbig = ("Arial", 32)



    def isValidValueEntry(self, tkentry):
        try:
            float(tkentry.get())
        except ValueError:
            #messagebox.showerror("Ошибка", "Введено не число")
            #tkentry.delete(0, 'end')
            return False
        return True

    def setDisBtn(self):
        self.frame_res.btn.setDisable()

    def setEnBtn(self):
        self.frame_res.btn.setEnabled()

    def getResult(self,event):
        if self.checkAllEntry():
            a = float(self.line1.points.x.get())
            b = float(self.line1.points.y.get())
            c = float(self.line1.points.c.get())
            line1 = IPt.Line(a,b,c)
            a = float(self.line2.points.x.get())
            b = float(self.line2.points.y.get())
            c = float(self.line2.points.c.get())
            line2 = IPt.Line(a,b,c)

            intersect = IPt.Intersect(line1, line2)

            try:
                res = intersect.find_cross()
            except Exception as e:
                res = e
            self.frame_res.lbl['text'] = res


    def check(self, event):
        self.checkAllEntry()

    def checkAllEntry(self):
        isValid = True
        if(self.isValidValueEntry(self.line1.points.x)==False):
            isValid = False
        if(self.isValidValueEntry(self.line1.points.y)==False):
            isValid = False
        if(self.isValidValueEntry(self.line1.points.c)==False):
            isValid = False

        if(self.isValidValueEntry(self.line2.points.x)==False):
            isValid = False
        if(self.isValidValueEntry(self.line2.points.y)==False):
            isValid = False
        if(self.isValidValueEntry(self.line2.points.c)==False):
            isValid = False

        if (isValid):
            self.setEnBtn()
            self.frame_res.lbl['text'] = "Результат"
        else:
            self.setDisBtn()
            self.frame_res.lbl['text'] = "Введено не число"
        return isValid



class FrameResult(tk.Frame):
    def __init__(self):
        super().__init__()
        self['bg'] = colapp

        self.btn = ButtonResult(master=self)
        self.btn.pack(expand = True, fill=tk.X, padx = smallpad, pady = smallpad)

        self.lbl = LabelResult(master=self, text="Результат")
        self.lbl['bg'] = col3
        self.lbl.pack(padx = smallpad, pady = smallpad)

class ButtonResult(tk.Button):
    def __init__(self, master, bg=col3):
        super().__init__(master)
        #self['width'] = middlewidth
        self['font'] = fontverysmall
        self['bg'] = col3
        self['text'] = "Найти точку пересечения"

    def setDisable(self):
        self['state'] = "disabled"

    def setEnabled(self):
        self['state'] = "normal"


class LabelResult(tk.Label):
    def __init__(self):
        super().__init__()

#class MyFrame(tk.Frame):
#    def __init__self():
#        super().__init__()
#        self['bg'] = colapp


class FramePoints(tk.Frame):
    def __init__(self):
        super().__init__()
        self['bg'] = colapp
        self.x = EntryCoord(master=self)
        self.lblx = LabelCoord(master=self, text="x")
        self.lblplus = LabelCoord(master=self, text="+")
        self.lbly = LabelCoord(master=self, text="y")
        self.y = EntryCoord(master=self)

        self.lblc = LabelCoord(master=self, text=" = ")
        self.c = EntryCoord(master=self)

        #компоновка элементов
        #(ввод x)x +
        self.x.pack(side=tk.LEFT, padx = smallpad, pady = smallpad)
        self.lblx.pack(side=tk.LEFT, padx = 0, pady = 0)
        self.lblplus.pack(side=tk.LEFT, padx = 0, pady = 0)

        #(ввод y)y
        self.y.pack(side=tk.LEFT, padx = 0, pady = smallpad)
        self.lbly.pack(side=tk.LEFT, padx = 0, pady = 0)

        # = (ввод с)
        self.lblc.pack(side=tk.LEFT, padx = 0, pady = 0)
        self.c.pack(side=tk.LEFT, padx = smallpad, pady = smallpad)

class LabelStraight(tk.Label):
    def __init__(self, master, text):
        super().__init__(master=master, text=text, bg = col4, font = fontverysmall)
        #self.config.font = ("Courier", 44)

class LabelResult(tk.Label):
    def __init__(self, master, text):
        super().__init__(master=master, text=text, bg = col4, font = fontsmall)
        #self.config.font = ("Courier", 44)

class FrameLabelStraight(tk.Frame):
    def __init__(self, nomer):
        super().__init__()
        self['width'] = middlewidth
        self['bg'] = "red"
        self.lbl_line = LabelStraight(master=self, text="Уравенение прямой {}".format(nomer))
        self.lbl_line.pack(fill = tk.X)

class FrameLine(tk.LabelFrame):
    def __init__(self, nomer):
        super().__init__()
        self['bg'] = colapp
        self.lbl = FrameLabelStraight(nomer)
        self.lbl.pack(fill = tk.X, padx = smallpad)

        self.points = FramePoints()
        self.points.pack()

class LabelCoord(tk.Label):
    def __init__(self, master, text):
        super().__init__(master=master, text=text, width=1, bg = colapp, font = fontsmall)
        #self.config.font = ("Courier", 44)

class EntryCoord(tk.Entry):
    def __init__(self, master):
        super().__init__(master=master, width=smallwidth, bg = "white", font = fontsmall, show="")
        self.insert(0,"1")

#class MainMenu(tk.Menu):
#    def __init__(self, app):
#        super().__init__(app)
#        app.config(menu=self)
#        filemenu = tk.Menu(self, tearoff=0)
#        filemenu.add_command(label="Открыть...")
#        filemenu.add_command(label="Новый")
#        filemenu.add_command(label="Сохранить...")
#        filemenu.add_command(label="Выход")

#        helpmenu = tk.Menu(self, tearoff=0)
#        helpmenu.add_command(label="Помощь")
#        helpmenu.add_command(label="О программе")

#        self.add_cascade(label="Файл",
#                                menu=filemenu)
#        self.add_cascade(label="Справка",
#                                menu=helpmenu)


if __name__ == "__main__":
    app = App()
    #mainmunu = MainMenu(app)
    app.mainloop()


#class App(tk.Tk):
#    def __init__(self):
#        super().__init__()
#        self.btnChoseColor = tk.Button(self, text="Поменять цвет!", command=self.click_chose_color)
#        self.btnNewWindow = tk.Button(self, text="Не нажимать!", command=self.new_window)
#        self.btnChoseColor.grid(column=0, row=0)
#        self.btnNewWindow.grid(column=0, row=1)

#    def click_chose_color(self):
#        (rgb, hx) = colorchooser.askcolor()
#        self.btnChoseColor.config(bg=hx)
#    def new_window(self):
#        app = App()
#        app.title("Еще окно")
#        app.lbl = tk.Label(app, text="создать еще окно???")
#        app.lbl.grid(column=0, row=0)
#        app.btnChoseColor.grid(column=0, row=1)
#        app.btnNewWindow.grid(column=0, row=2)
#        app.mainloop()


#def keyReleased(self,event):
#    if event.keysym == 'Right':
#        self.move('Right')
#    elif event.keysym == 'Left':
#      direction=  self.move('Left')
#    elif event.keysym == 'Up':
#        self.move('Up')
#    elif event.keysym =='Down':
#        self.move('Down')


#    entry = tk.Entry(self)
#    entry.bind("<FocusIn>", self.print_type)
#    entry.bind("<Key>", self.print_key)
#    entry.pack(padx=20, pady=20)

#def print_type(self, event):
#    print(event.type)

#def print_key(self, event):
#    args = event.keysym, event.keycode, event.char
#    print("Знак: {}, Код: {}, Символ: {}".format(*args))
