import tkinter as tk
import tkinter.messagebox


class MyGUIOne:
    # destorys the frames of the first page so the frames for the second page can be created
    def destoryWindow(self):
        self.upperFrame.destroy()
        self.middleFrame.destroy()
        # open next window by initializing MyGUITwo and pass in the score
        MyGUITwo.__init__(self, self.score)

    # calculates the total score based on the answer choices the user selects
    def calculateChoice(self):
        self.score += self.radioValQ1.get()
        self.score += self.radioValQ2.get()
        self.score += self.radioValQ3.get()

    # Shows the total score
    def showScore(self):
        self.calculateChoice()

        message = " "

        if self.score < 30:
            message = "Python"
        elif self.score < 36:
            message = "Ruby"
        elif self.score < 42:
            message = "Java"
        elif self.score <= 48:
            message = "C++"

        tk.messagebox.showinfo("Your programming language is", message)

        # replace submit button with quit button
        self.quitButton = tk.Button(self.middleFrame, text="Quit", command=self.root.destroy)
        self.quitButton.place(anchor='s', rely=1, relx=.5, relwidth=.4)

    # initalizes the first page
    def __init__(self):
        # Each answer choice is associated with a score. Variable score keeps track of the total score
        self.score = 0

        # variables to set the dimensions of the canvas
        self.HEIGHT = 700
        self.WIDTH = 800

        # root window
        self.root = tk.Tk()

        # create canvas
        self.canvas = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
        self.canvas.pack()

        # add background image
        self.bgImage = tk.PhotoImage(file='background2.png')
        self.bgLabel = tk.Label(self.root, image=self.bgImage)
        self.bgLabel.place(relwidth=1, relheight=1)

        # set up upper frame
        self.upperFrame = tk.Frame(self.root, bg='white', bd=10, highlightbackground="#fbe1f2",
                                   highlightcolor="#fbe1f2", highlightthickness=5)
        self.upperFrame.place(relx=.1, rely=.05, relwidth=.8, relheight=.075)
        self.headerLabel = tk.Label(self.upperFrame, text='Which Programming Language Are You?', font=60)
        self.headerLabel.place(relx=.2, rely=.25)

        # set up middle frame
        self.middleFrame = tk.Frame(self.root, bg='white', bd=10, highlightbackground="#fbe1f2",
                                    highlightcolor="#fbe1f2", highlightthickness=5)
        self.middleFrame.place(relx=.1, rely=.15, relwidth=.8, relheight=.8)

        # create an intvar to associate each radio button choice with a value for each question
        self.radioValQ1 = tk.IntVar()
        self.radioValQ2 = tk.IntVar()
        self.radioValQ3 = tk.IntVar()

        # create first question then place on screen
        self.firstAnswer = tk.Label(self.middleFrame, text="What is your favorite color?", bg='#e1fbfa')
        self.firstAnswer.place(anchor="w", relx=0, rely=.05, relwidth=.30)

        # create answer choices
        self.firstrb1 = tk.Radiobutton(self.middleFrame, text="Red", variable=self.radioValQ1, value=1)
        self.firstrb1.place(anchor="w", relx=.0, rely=.10, relwidth=.1)
        self.firstrb2 = tk.Radiobutton(self.middleFrame, text="Blue", variable=self.radioValQ1, value=2)
        self.firstrb2.place(anchor="w", relx=.0, rely=.15, relwidth=.1)
        self.firstrb3 = tk.Radiobutton(self.middleFrame, text="Purple", variable=self.radioValQ1, value=3)
        self.firstrb3.place(anchor="w", relx=.0, rely=.20, relwidth=.1)
        self.firstrb4 = tk.Radiobutton(self.middleFrame, text="Green", variable=self.radioValQ1, value=4)
        self.firstrb4.place(anchor="w", relx=.0, rely=.25, relwidth=.1)

        # create second question then place on screen
        self.firstAnswer = tk.Label(self.middleFrame, text="What operating system do you prefer?", bg='#e1fbfa')
        self.firstAnswer.place(anchor="w", relx=0, rely=.35)

        # create answer choices
        self.secondrb1 = tk.Radiobutton(self.middleFrame, text="Mac OS", variable=self.radioValQ2, value=5)
        self.secondrb1.place(anchor="w", relx=.0, rely=.40)
        self.secondrb2 = tk.Radiobutton(self.middleFrame, text="Windows", variable=self.radioValQ2, value=6)
        self.secondrb2.place(anchor="w", relx=.0, rely=.45)
        self.secondrb3 = tk.Radiobutton(self.middleFrame, text="Linux", variable=self.radioValQ2, value=7)
        self.secondrb3.place(anchor="w", relx=.0, rely=.50)
        self.secondrb4 = tk.Radiobutton(self.middleFrame, text="Android", variable=self.radioValQ2, value=8)
        self.secondrb4.place(anchor="w", relx=.0, rely=.55)

        # create second question then place on screen
        self.thirdAnswer = tk.Label(self.middleFrame, text="What brand of computer do you use?", bg='#e1fbfa')
        self.thirdAnswer.place(anchor="w", relx=0, rely=.65)

        # create answer choices
        self.thirdrb1 = tk.Radiobutton(self.middleFrame, text="Asus", variable=self.radioValQ3, value=9)
        self.thirdrb1.place(anchor="w", relx=.0, rely=.70)
        self.thirdrb2 = tk.Radiobutton(self.middleFrame, text="Dell", variable=self.radioValQ3, value=10)
        self.thirdrb2.place(anchor="w", relx=.0, rely=.75)
        self.thirdrb3 = tk.Radiobutton(self.middleFrame, text="HP", variable=self.radioValQ3, value=11)
        self.thirdrb3.place(anchor="w", relx=.0, rely=.801)
        self.thirdrb4 = tk.Radiobutton(self.middleFrame, text="Mac", variable=self.radioValQ3, value=12)
        self.thirdrb4.place(anchor="w", relx=.0, rely=.85)

        # create snext page button
        self.button = tk.Button(self.middleFrame, text="Next Page", bg='red', fg='gray', font=60,
                                command=lambda: [self.calculateChoice(), self.destoryWindow()])

        self.button.place(anchor='s', rely=1, relx=.5)

        self.root.mainloop()

        # questions to be asked:
        # what is your favorite color?
        # What operating system do you prefer?
        # favorite non alphanumeric character
        # How do you spend your free time
        # What brand of computer do you use
        # Method of approachinga project
        # Favorite beverage


class MyGUITwo:
    # destorys the frames of the first page so the frames for the second page can be created
    def destoryWindow(self):
        self.upperFrame.destroy()
        self.middleFrame.destroy()
        # open next window by initializing MyGUITwo and pass in the score
        MyGUIThree.__init__(self, self.score)


    def __init__(self, prevScore):
        # Each answer choice is associated with a score. Variable score keeps track of the total score
        self.score = prevScore

        # set up upper frame
        self.upperFrame = tk.Frame(self.root, bg='white', bd=10, highlightbackground="#fbe1f2",
                                   highlightcolor="#fbe1f2", highlightthickness=5)
        self.upperFrame.place(relx=.1, rely=.05, relwidth=.8, relheight=.075)
        self.headerLabel = tk.Label(self.upperFrame, text='Which Programming Language Are You?', font=60)
        self.headerLabel.place(relx=.2, rely=.25)

        # set up middle frame
        self.middleFrame = tk.Frame(self.root, bg='white', bd=10, highlightbackground="#fbe1f2",
                                    highlightcolor="#fbe1f2", highlightthickness=5)
        self.middleFrame.place(relx=.1, rely=.15, relwidth=.8, relheight=.8)

        # create an intvar to associate each radio button choice with a value for each question
        self.radioValQ1 = tk.IntVar()
        self.radioValQ2 = tk.IntVar()
        self.radioValQ3 = tk.IntVar()

        # create first question then place on screen
        self.firstAnswer = tk.Label(self.middleFrame, text="How do you spend your free time?", bg='#e1fbfa')
        self.firstAnswer.place(anchor="w", relx=0, rely=.05)

        # create answer choices
        self.firstrb1 = tk.Radiobutton(self.middleFrame, text="Watching TV", variable=self.radioValQ1, value=1)
        self.firstrb1.place(anchor="w", relx=.0, rely=.10)
        self.firstrb2 = tk.Radiobutton(self.middleFrame, text="Playing video games", variable=self.radioValQ1, value=2)
        self.firstrb2.place(anchor="w", relx=.0, rely=.15)
        self.firstrb3 = tk.Radiobutton(self.middleFrame, text="Studying/Homework", variable=self.radioValQ1, value=3)
        self.firstrb3.place(anchor="w", relx=.0, rely=.20)
        self.firstrb4 = tk.Radiobutton(self.middleFrame, text="Spending time with friends", variable=self.radioValQ1, value=4)
        self.firstrb4.place(anchor="w", relx=.0, rely=.25)

        # create second question then place on screen
        self.firstAnswer = tk.Label(self.middleFrame, text="What is your favorite alphanumeric character?", bg='#e1fbfa')
        self.firstAnswer.place(anchor="w", relx=0, rely=.35)

        # create answer choices
        self.secondrb1 = tk.Radiobutton(self.middleFrame, text="<", variable=self.radioValQ2, value=5)
        self.secondrb1.place(anchor="w", relx=.0, rely=.40)
        self.secondrb2 = tk.Radiobutton(self.middleFrame, text=">", variable=self.radioValQ2, value=6)
        self.secondrb2.place(anchor="w", relx=.0, rely=.45)
        self.secondrb3 = tk.Radiobutton(self.middleFrame, text="#", variable=self.radioValQ2, value=7)
        self.secondrb3.place(anchor="w", relx=.0, rely=.50)
        self.secondrb4 = tk.Radiobutton(self.middleFrame, text="&", variable=self.radioValQ2, value=8)
        self.secondrb4.place(anchor="w", relx=.0, rely=.55)

        # create second question then place on screen
        self.thirdAnswer = tk.Label(self.middleFrame, text="What is your favorite drink?", bg='#e1fbfa')
        self.thirdAnswer.place(anchor="w", relx=0, rely=.65)

        # create answer choices
        self.thirdrb1 = tk.Radiobutton(self.middleFrame, text="Water", variable=self.radioValQ3, value=9)
        self.thirdrb1.place(anchor="w", relx=.0, rely=.70)
        self.thirdrb2 = tk.Radiobutton(self.middleFrame, text="Soda", variable=self.radioValQ3, value=10)
        self.thirdrb2.place(anchor="w", relx=.0, rely=.75)
        self.thirdrb3 = tk.Radiobutton(self.middleFrame, text="Beer", variable=self.radioValQ3, value=11)
        self.thirdrb3.place(anchor="w", relx=.0, rely=.80)
        self.thirdrb4 = tk.Radiobutton(self.middleFrame, text="Wine", variable=self.radioValQ3, value=12)
        self.thirdrb4.place(anchor="w", relx=.0, rely=.85)

        # create next page button
        self.button = tk.Button(self.middleFrame, text="Next Page", bg='red', fg='gray', font=60,
                                command=lambda: [self.calculateChoice(), self.destoryWindow()])

        self.button.place(anchor='s', rely=1, relx=.5)



        self.root.mainloop


class MyGUIThree:
    def __init__(self, prevScore):
        # Each answer choice is associated with a score. Variable score keeps track of the total score
        self.score = prevScore

        # set up upper frame
        self.upperFrame = tk.Frame(self.root, bg='white', bd=10, highlightbackground="#fbe1f2",
                                   highlightcolor="#fbe1f2", highlightthickness=5)
        self.upperFrame.place(relx=.1, rely=.05, relwidth=.8, relheight=.075)
        self.headerLabel = tk.Label(self.upperFrame, text='Which Programming Language Are You?', font=60)
        self.headerLabel.place(relx=.2, rely=.25)

        # set up middle frame
        self.middleFrame = tk.Frame(self.root, bg='white', bd=10, highlightbackground="#fbe1f2",
                                    highlightcolor="#fbe1f2", highlightthickness=5)
        self.middleFrame.place(relx=.1, rely=.15, relwidth=.8, relheight=.8)

        # create an intvar to associate each radio button choice with a value for each question
        self.radioValQ1 = tk.IntVar()
        self.radioValQ2 = tk.IntVar()
        self.radioValQ3 = tk.IntVar()

        # create first question then place on screen
        self.firstAnswer = tk.Label(self.middleFrame, text="What is your classification?", bg='#e1fbfa')
        self.firstAnswer.place(anchor="w", relx=0, rely=.05)

        # create answer choices
        self.firstrb1 = tk.Radiobutton(self.middleFrame, text="Freshman", variable=self.radioValQ1, value=1)
        self.firstrb1.place(anchor="w", relx=.0, rely=.10)
        self.firstrb2 = tk.Radiobutton(self.middleFrame, text="Sophomore", variable=self.radioValQ1, value=2)
        self.firstrb2.place(anchor="w", relx=.0, rely=.15)
        self.firstrb3 = tk.Radiobutton(self.middleFrame, text="Junior", variable=self.radioValQ1, value=3)
        self.firstrb3.place(anchor="w", relx=.0, rely=.20)
        self.firstrb4 = tk.Radiobutton(self.middleFrame, text="Senior", variable=self.radioValQ1, value=4)
        self.firstrb4.place(anchor="w", relx=.0, rely=.25)

        # create second question then place on screen
        self.firstAnswer = tk.Label(self.middleFrame, text="What is your preferred streaming service?", bg='#e1fbfa')
        self.firstAnswer.place(anchor="w", relx=0, rely=.35)

        # create answer choices
        self.secondrb1 = tk.Radiobutton(self.middleFrame, text="Hulu", variable=self.radioValQ2, value=5)
        self.secondrb1.place(anchor="w", relx=.0, rely=.40)
        self.secondrb2 = tk.Radiobutton(self.middleFrame, text="Netflix", variable=self.radioValQ2, value=6)
        self.secondrb2.place(anchor="w", relx=.0, rely=.45)
        self.secondrb3 = tk.Radiobutton(self.middleFrame, text="Disney Plus", variable=self.radioValQ2, value=7)
        self.secondrb3.place(anchor="w", relx=.0, rely=.50)
        self.secondrb4 = tk.Radiobutton(self.middleFrame, text="Pirating", variable=self.radioValQ2, value=8)
        self.secondrb4.place(anchor="w", relx=.0, rely=.55)

        # create second question then place on screen
        self.thirdAnswer = tk.Label(self.middleFrame, text="How do you take on projects?", bg='#e1fbfa')
        self.thirdAnswer.place(anchor="w", relx=0, rely=.65)

        # create answer choices
        self.thirdrb1 = tk.Radiobutton(self.middleFrame, text="Plan", variable=self.radioValQ3, value=9)
        self.thirdrb1.place(anchor="w", relx=.0, rely=.70)
        self.thirdrb2 = tk.Radiobutton(self.middleFrame, text="Wait till last minute", variable=self.radioValQ3, value=10)
        self.thirdrb2.place(anchor="w", relx=.0, rely=.75)
        self.thirdrb3 = tk.Radiobutton(self.middleFrame, text="Make it up as I go", variable=self.radioValQ3, value=11)
        self.thirdrb3.place(anchor="w", relx=.0, rely=.80)
        self.thirdrb4 = tk.Radiobutton(self.middleFrame, text="Wait till the last minute", variable=self.radioValQ3, value=12)
        self.thirdrb4.place(anchor="w", relx=.0, rely=.85)

        self.button = tk.Button(self.middleFrame, text="Submit Quiz", bg='red', fg='gray', font=60,
                                command=lambda: [self.showScore()])
        self.button.place(anchor='s', rely=1, relx=.5)






MyGUIOne()
