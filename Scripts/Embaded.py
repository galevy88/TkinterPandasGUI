from cgitb import handler, text
from logging import root
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure  import Figure


want_list = []

def buttonYES(root, idx, handler):
    print("call_yes")
    root.destroy()
    handler.manage_wanted_list(idx, True)
    
    
def buttonNO(root, idx, handler):
    print("call_no")
    root.destroy()
    handler.manage_wanted_list(idx, False)
    


def showData(cell, idx, handler):
    root = Tk()
    root.wm_title("embaded")

    label = Label(text=cell.get_cell_id(), font=("Ariel" , 20 , "bold"))
    label.pack()

    label = Label(text=cell.get_temprature(), font=("Ariel" , 20 , "bold"))
    label.pack()

    fig = Figure(figsize=(7,5), dpi=100)
    fig.add_subplot(111).plot(cell.get_df())

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()
    canvas.get_tk_widget().pack()

    #calls action() when pressed
    button_yes = Button(text="Yes", command=lambda:buttonYES(root, idx, handler))
    button_yes.pack()
    #calls action() when pressed
    button_no = Button(text="No", command=lambda:buttonNO(root, idx, handler))
    button_no.pack()


    # #calls action() when pressed
    # button_no = Button(text="No", command=action)
    # button_no.pack()

    root.mainloop()


