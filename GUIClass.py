import mysql.connector
import tkinter as tk

class MyGUI:
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
        self.rb1 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 1)
        self.rb1.place(anchor="w", relx=.0, rely=.10, relwidth=.1)
        self.rb2 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 2)
        self.rb2.place(anchor="w", relx=.0, rely=.15, relwidth=.1)
        self.rb3 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 3)
        self.rb3.place(anchor="w", relx=.0, rely=.20, relwidth=.1)
        self.rb4 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 4)
        self.rb4.place(anchor="w", relx=.0, rely=.25, relwidth=.1)

        #create second question then place on screen
        self.firstAnswer = tk.Label(self.middleFrame, text="Do you Prefer this or that?", bg='#e1fbfa')
        self.firstAnswer.place(anchor="w", relx=0, rely=.35, relwidth=.30)

        #create answer choices
        self.rb1 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 1)
        self.rb1.place(anchor="w", relx=.0, rely=.40, relwidth=.1)
        self.rb2 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 2)
        self.rb2.place(anchor="w", relx=.0, rely=.45, relwidth=.1)
        self.rb3 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 3)
        self.rb3.place(anchor="w", relx=.0, rely=.50, relwidth=.1)
        self.rb4 = tk.Radiobutton(self.middleFrame, text = "this", variable = self.radioVal, value = 4)
        self.rb4.place(anchor="w", relx=.0, rely=.55, relwidth=.1)
        

        self.root.mainloop()


MyGUI()
