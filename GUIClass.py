import tkinter as tk

class MyGUIOne:
    def destoryWindow(self):
        self.upperFrame.destroy()
        self.middleFrame.destroy()
        #open next window
        #PageTwo.__init__(self, mycursor, mydb)

    def showChoice (self):
        if (self.radioVal.get() == 1):
            charge = .07 * float (self.entry.get())
            tk.messagebox.showinfo("Selection", "The charge is $ " + str(format (charge, '.2f')))

        if (self.radioVal.get() == 2):
            charge = .12 * float (self.entry.get())
            tk.messagebox.showinfo("Selection", "The charge is $ " + str(format (charge, '.2f')))

        if (self.radioVal.get() == 3):
            charge = .05 * float (self.entry.get())
            tk.messagebox.showinfo("Charge", "The charge is $ " + str(format (charge, '.2f')))

    def __init__(self):
        self.HEIGHT = 700
        self.WIDTH = 800

        # root window
        self.root = tk.Tk()

        #create canvas
        self.canvas = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
        self.canvas.pack()

        #add background image
        self.bgImage = tk.PhotoImage(file = 'background2.png')
        self.bgLabel = tk.Label(self.root, image = self.bgImage)
        self.bgLabel.place(relwidth = 1, relheight = 1)

        #set up upper frame
        self.upperFrame = tk.Frame(self.root, bg = 'white', bd = 10, highlightbackground="#fbe1f2", highlightcolor="#fbe1f2", highlightthickness=5)
        self.upperFrame.place(relx = .1, rely = .05, relwidth = .8, relheight = .075)
        self.headerLabel = tk.Label(self.upperFrame, text = 'Which Programming Language Are You?', font = 60)
        self.headerLabel.place(relx = .2, rely = .25)

        #set up middle frame
        self.middleFrame = tk.Frame(self.root, bg = 'white', bd = 10, highlightbackground="#fbe1f2", highlightcolor="#fbe1f2", highlightthickness=5)
        self.middleFrame.place(relx = .1, rely = .15, relwidth = .8, relheight = .8)

        #create an intvar to associate each radio button choice with a value
        self.radioVal = tk.IntVar()

        #create first question then place on screen
        self.firstAnswer = tk.Label(self.middleFrame, text="Do you Prefer this or that?", bg='#e1fbfa')
        self.firstAnswer.place(anchor="w", relx=0, rely=.05, relwidth=.30)

        #create answer choices
        self.firstrb1 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 1)
        self.firstrb1.place(anchor="w", relx=.0, rely=.10, relwidth=.1)
        self.firstrb2 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 2)
        self.firstrb2.place(anchor="w", relx=.0, rely=.15, relwidth=.1)
        self.firstrb3 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 3)
        self.firstrb3.place(anchor="w", relx=.0, rely=.20, relwidth=.1)
        self.firstrb4 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 4)
        self.firstrb4.place(anchor="w", relx=.0, rely=.25, relwidth=.1)

        #create second question then place on screen
        self.firstAnswer = tk.Label(self.middleFrame, text="Do you Prefer this or that?", bg='#e1fbfa')
        self.firstAnswer.place(anchor="w", relx=0, rely=.35, relwidth=.30)

        #create answer choices
        self.secondrb1 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 1)
        self.secondrb1.place(anchor="w", relx=.0, rely=.40, relwidth=.1)
        self.secondrb2 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 2)
        self.secondrb2.place(anchor="w", relx=.0, rely=.45, relwidth=.1)
        self.secondrb3 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 3)
        self.secondrb3.place(anchor="w", relx=.0, rely=.50, relwidth=.1)
        self.secondrb4 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 4)
        self.secondrb4.place(anchor="w", relx=.0, rely=.55, relwidth=.1)

        #create second question then place on screen
        self.thirdAnswer = tk.Label(self.middleFrame, text="Do you Prefer this or that?", bg='#e1fbfa')
        self.thirdAnswer.place(anchor="w", relx=0, rely=.65, relwidth=.30)

        #create answer choices
        self.thirdrb1 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 1)
        self.thirdrb1.place(anchor="w", relx=.0, rely=.70, relwidth=.1)
        self.thirdrb2 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 2)
        self.thirdrb2.place(anchor="w", relx=.0, rely=.75, relwidth=.1)
        self.thirdrb3 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 3)
        self.thirdrb3.place(anchor="w", relx=.0, rely=.80, relwidth=.1)
        self.thirdrb4 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 4)
        self.thirdrb4.place(anchor="w", relx=.0, rely=.85, relwidth=.1)

        #create submit button
        self.button = tk.Button(self.middleFrame, text="Next Page", bg='red', fg='gray', font=60,
                                command=lambda: [self.destoryWindow()])

        self.button.place (anchor = 's', rely = 1, relx = .5)

        

        self.root.mainloop()


MyGUIOne()
#