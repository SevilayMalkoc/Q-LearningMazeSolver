import tkinter
from tkinter import messagebox
from time import sleep


class tkWindow():

    def __init__(self):
        self.window = None

        # first window
        self.label1 = None
        self.label2 = None
        self.label4 = None
        self.label5 = None
        self.label6 = None
        self.label7 = None
        self.entry4 = None
        self.entry5 = None
        self.entry6 = None
        self.entry7 = None
        self.var_theme = None
        self.heading = None
        self.entry1 = None
        self.entry2 = None
        self.theme = None
        self.button = None

        # second window
        self.regenerate = None
        self.train_AI = None

        # third window
        self.entry_other = None
        self.entry_gamma = None
        self.entry_neg_reward = None
        self.entry_pos_reward = None
        self.entry_epsilon = None
        self.other_label = None
        self.gamma_label = None
        self.neg_reward = None
        self.pos_reward = None
        self.epsilon_label = None
        self.start_training_button = None
        self.var_other = None
        self.var_gamma = None
        self.var_epsilon = None
        self.var_neg = None
        self.var_pos = None

        # fourth window
        self.var1 = None
        self.var2 = None
        self.speed_up = None
        self.slowdown = None
        self.end = None

        # variables
        self.maze_height = None
        self.maze_width = None
        self.maze_baslangic_x = None
        self.maze_baslangic_y = None
        self.maaze_cikis_x = None
        self.maze_cikis_y = None
        self.color = None
        self.button_text = None

        # flags
        self.create = False
        self.back = False
        self.close_flag = False
        self.redefine_flag = False
        self.regen_flag = False
        self.training_flag = False
        self.inc_flag = False
        self.dec_flag = False
        self.reward_flag = False
        self.q_values_flag = False
        self.pause_flag = False
        self.redo = False
        self.end_training_flag = False

    def origin(self):
        self.window = tkinter.Tk()
        self.window.title("Create Maze")
        self.window.resizable(width=True, height=True)
        self.window.geometry("300x400+500+200")
        self.window.protocol("WM_DELETE_WINDOW", self.callback)

        # first window contents
        self.label1 = tkinter.Label(self.window, text="Width:")
        self.label2 = tkinter.Label(self.window, text="Height:")
        self.label4 = tkinter.Label(self.window, text="Start x: ")
        self.label5 = tkinter.Label(self.window, text="Start y: ")
        self.label6 = tkinter.Label(self.window, text="End x: ")
        self.label7 = tkinter.Label(self.window, text="End y: ")

        self.heading = tkinter.Label(self.window, text="Maze")
        self.heading.config(font=("Times New Roman", 20))

        self.var_theme = tkinter.StringVar(self.window)
        self.var_theme.set("Retro")  # default value

        self.entry1 = tkinter.Entry()
        self.entry2 = tkinter.Entry()
        self.entry4 = tkinter.Entry()
        self.entry5 = tkinter.Entry()
        self.entry6 = tkinter.Entry()
        self.entry7 = tkinter.Entry()

        self.entry1.insert(0, "25")
        self.entry2.insert(0, "25")
        self.entry4.insert(0, "1")
        self.entry5.insert(0, "1")
        self.entry6.insert(0, "7")
        self.entry7.insert(0, "1")

        self.button = tkinter.Button(self.window, text="Create Maze", command=self.create_maze)
        self.button.config(font=("Times New Roman", 11))

        # second window contents
        self.regenerate = tkinter.Button(self.window, text="Create Random Maze", command=self.regen)
        self.train_AI = tkinter.Button(self.window, text="Train", command=self.train)
        self.train_AI.config(font=("Times New Roman", 12))

        # third window contents
        self.entry_other = tkinter.Entry(self.window)
        self.entry_gamma = tkinter.Entry(self.window)
        self.entry_neg_reward = tkinter.Entry(self.window)
        self.entry_pos_reward = tkinter.Entry(self.window)

        self.entry_gamma.insert(0, "0.9")
        self.entry_neg_reward.insert(0, "-5")
        self.entry_pos_reward.insert(0, "+5")
        self.entry_other.insert(0, "+3")

        self.gamma_label = tkinter.Label(self.window, text="Gamma")
        self.neg_reward = tkinter.Label(self.window, text="Reward for walls")
        self.pos_reward = tkinter.Label(self.window, text="Reward for goal")
        self.other_label = tkinter.Label(self.window, text="Reward for others")

        self.start_training_button = tkinter.Button(self.window, text="Start Training", command=self.start_training)
        self.start_training_button.config(font=("Times New Roman", 15))

        # fourth window contents
        self.var1 = tkinter.IntVar()

        self.var2 = tkinter.IntVar()
        self.speed_up = tkinter.Button(self.window, text="Speed up", command=self.speed_inc)
        self.slowdown = tkinter.Button(self.window, text="Slow down", command=self.speed_dec)

        self.button_text = tkinter.StringVar()

        self.end = tkinter.Button(self.window, text="Finish Training", command=self.end_command)
        self.end.config(font=("Times New Roman", 12))

        # starting first window
        self.first_window()
        self.window.mainloop()

    def first_window(self):
        self.heading.pack()
        self.label1.place(x=40, y=60)
        self.entry1.place(x=110, y=60)
        self.label2.place(x=40, y=90)
        self.entry2.place(x=110, y=90)
        self.label4.place(x=40, y=120)
        self.entry4.place(x=110, y=120)
        self.label5.place(x=40, y=150)
        self.entry5.place(x=110, y=150)
        self.label6.place(x=40, y=180)
        self.entry6.place(x=110, y=180)
        self.label7.place(x=40, y=210)
        self.entry7.place(x=110, y=210)
        self.button.pack(side=tkinter.BOTTOM, pady=50)

    def second_window(self):

        self.regenerate.pack(pady=5)
        self.train_AI.pack(pady=10)

    def third_window(self):
        self.gamma_label.pack()
        self.entry_gamma.pack()
        self.neg_reward.pack()
        self.entry_neg_reward.pack()
        self.pos_reward.pack()
        self.entry_pos_reward.pack()
        self.other_label.pack()
        self.entry_other.pack()
        self.start_training_button.pack(pady=25)

    def fourth_window(self):

        self.speed_up.pack(pady=5)
        self.slowdown.pack(pady=5)
        self.end.pack()

    # all the event handling functions
    def create_maze(self):
        try:
            self.maze_width = int(self.entry1.get())
            self.maze_height = int(self.entry2.get())
            self.maze_baslangic_x = int(self.entry4.get())*16
            self.maze_baslangic_y = int(self.entry5.get())*16
            self.maze_cikis_x = int(self.entry6.get())*16
            self.maze_cikis_y = int(self.entry7.get())*16

            self.color = self.var_theme.get()

        except Exception:
            print(Exception)
            messagebox.showinfo("Error", "Invalid Input. Please Try again.")
            return
        self.create = True

        self.label1.place_forget()
        self.label2.place_forget()
        self.label4.place_forget()
        self.label5.place_forget()
        self.label6.place_forget()
        self.label7.place_forget()
        self.heading.pack_forget()
        self.entry1.place_forget()
        self.entry2.place_forget()
        self.entry4.place_forget()
        self.entry5.place_forget()
        self.entry6.place_forget()
        self.entry7.place_forget()
        self.button.pack_forget()

        self.second_window()

        sleep(1.5)
        self.window.after(1, lambda: self.window.focus_force())

    def callback(self):
        self.close_flag = True

    def regen(self):
        self.regen_flag = True

    def train(self):
        self.train_AI.pack_forget()
        self.regenerate.pack_forget()

        self.third_window()

    def redefine_goal(self):
        self.redefine_flag = True

    def reward_command(self):
        self.var2.set(0)
        self.q_values_flag = False
        self.reward_flag = not self.reward_flag

    def end_command(self):
        self.window.withdraw()
        self.end_training_flag = True
        self.close_flag = True

    def speed_inc(self):
        self.inc_flag = True

    def speed_dec(self):
        self.dec_flag = True

    def start_training(self):
        try:
            self.var_gamma = self.entry_gamma.get()
            self.var_neg = self.entry_neg_reward.get()
            self.var_pos = self.entry_pos_reward.get()
            self.var_other = self.entry_other.get()

        except Exception:
            messagebox.showinfo(title="Error", message="Invalid Arguments")
            return
        self.gamma_label.pack_forget()
        self.entry_gamma.pack_forget()
        self.neg_reward.pack_forget()
        self.entry_neg_reward.pack_forget()
        self.pos_reward.pack_forget()
        self.entry_pos_reward.pack_forget()
        self.other_label.pack_forget()
        self.entry_other.pack_forget()
        self.start_training_button.pack_forget()

        self.training_flag = True
        self.fourth_window()

