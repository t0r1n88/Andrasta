try:
    import Tkinter as tk
except:
    import tkinter as tk
    from tkinter import StringVar


class Test():
    def __init__(self):
        self.root = tk.Tk()
        entry_id = StringVar()
        self.Entry = tk.Entry(self.root,textvariable=entry_id)
        self.label = tk.Label(self.root,
                              text="Label")


        self.buttonForget = tk.Button(self.root,
                                      text='Click to hide Label',
                                      command=lambda: self.Entry.grid_remove())
        self.buttonRecover = tk.Button(self.root,
                                       text='Click to show Label',
                                       command=lambda: self.Entry.grid())

        self.buttonForget.grid(column=0, row=0, padx=10, pady=10)
        self.buttonRecover.grid(column=0, row=1, padx=10, pady=10)
        self.label.grid(column=0, row=2, padx=10, pady=20)
        self.Entry.grid(column=0, row=3, padx=10, pady=20)
        self.root.mainloop()

    def quit(self):
        self.root.destroy()


app = Test()