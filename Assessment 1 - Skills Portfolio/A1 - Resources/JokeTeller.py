from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Initialize root window
root = Tk()
root.title("Joke Telling Assistant")
root.geometry("700x500")
root.resizable(False, False)

# Function to raise frames
def switch_frame(frame):
    frame.tkraise()

# Function to load jokes from the file
def load_jokes():
    try:
        with open("randomJokes.txt", "r") as file:
            jokes = file.readlines()
        return [joke.strip().split('?', 1) for joke in jokes if '?' in joke]
    except FileNotFoundError:
        messagebox.showerror("Error", "randomJokes.txt file not found!")
        return []

# Function to display the setup of a random joke
def show_joke():
    global current_joke
    if jokes:
        current_joke = random.choice(jokes)
        setup_label.config(text=current_joke[0] + '?')
        punchline_label.config(text="Click 'Show Punchline' to reveal the answer!")
        punchline_button.config(state=NORMAL)
        show_punchline_indicator.config(text="")

# Function to display the punchline of the current joke
def show_punchline():
    if current_joke:
        punchline_label.config(text=current_joke[1])
        show_punchline_indicator.config(text="😄", font=("Arial", 20))

# Function to reset and go back to home
def go_home():
    global current_joke
    current_joke = None
    setup_label.config(text="Click 'Alexa tell me a Joke' to start!")
    punchline_label.config(text="")
    show_punchline_indicator.config(text="")
    switch_frame(home_frame)

# Load jokes
jokes = load_jokes()
current_joke = None

# Create frames for home and task screens
home_frame = Frame(root, bg="#2C3E50")
home_frame.place(relwidth=1, relheight=1)

# Load the background image for home_frame
try:
    bg_image_home = Image.open("image 4 (3).jpg")
    bg_image_home = bg_image_home.resize((700, 500))
    bg_photo_home = ImageTk.PhotoImage(bg_image_home)
    bg_label_home = Label(home_frame, image=bg_photo_home)
    bg_label_home.place(relwidth=1, relheight=1)
except:
    pass

task_frame = Frame(root, bg="#ECF0F1")
task_frame.place(relwidth=1, relheight=1)

# Load the background image for task_frame
try:
    bg_image_task = Image.open("image 4 (2).jpg")
    bg_image_task = bg_image_task.resize((700, 500))
    bg_photo_task = ImageTk.PhotoImage(bg_image_task)
    bg_label_task = Label(task_frame, image=bg_photo_task)
    bg_label_task.place(relwidth=1, relheight=1)
except:
    pass

# ========== HOME FRAME WIDGETS ==========

# Title label with shadow effect
title_shadow = Label(
    home_frame,
    text="🎭 Joke Telling Assistant 🎭",
    font=("Arial Black", 24, "bold"),
    fg="#34495E",
    bg="#ECF0F1"
)
title_shadow.place(x=122, y=152)

title_label = Label(
    home_frame,
    text="🎭 Joke Telling Assistant 🎭",
    font=("Arial Black", 24, "bold"),
    fg="#E74C3C",
    bg="#ECF0F1"
)
title_label.place(x=120, y=150)

# Subtitle
subtitle_label = Label(
    home_frame,
    text="Get ready to laugh out loud!",
    font=("Arial", 14, "italic"),
    fg="#7F8C8D",
    bg="#ECF0F1"
)
subtitle_label.place(x=230, y=210)

# Start button with better styling
Start_button = Button(
    home_frame,
    text="START",
    font=("Arial Black", 16, "bold"),
    fg="white",
    bg="#27AE60",
    activebackground="#229954",
    activeforeground="white",
    borderwidth=0,
    padx=40,
    pady=15,
    cursor="hand2",
    command=lambda: switch_frame(task_frame)
)
Start_button.place(x=275, y=280)

# Credits
credits_label = Label(
    home_frame,
    text="Press START to begin your comedy journey!",
    font=("Arial", 10),
    fg="#95A5A6",
    bg="#ECF0F1"
)
credits_label.place(x=220, y=450)

# ========== TASK FRAME WIDGETS ==========

# Header
header_label = Label(
    task_frame,
    text="🎤 Joke Time! 🎤",
    font=("Arial Black", 20, "bold"),
    fg="#2C3E50",
    bg="#F8F9FA"
)
header_label.place(x=220, y=20)

# Box for the setup label (joke setup)
setup_box = Frame(task_frame, bg="#FFFFFF", bd=3, relief="ridge")
setup_box.place(x=50, y=80, width=600, height=120)

setup_label = Label(
    setup_box,
    text="Click 'Alexa tell me a Joke' to start!",
    font=("Arial", 14, "bold"),
    fg="#34495E",
    bg="#FFFFFF",
    wraplength=580,
    justify="center"
)
setup_label.pack(expand=True)

# Indicator for punchline
show_punchline_indicator = Label(
    task_frame,
    text="",
    font=("Arial", 20),
    bg="#ECF0F1"
)
show_punchline_indicator.place(x=330, y=210)

# Box for the punchline label (joke punchline)
punchline_box = Frame(task_frame, bg="#FFF9E6", bd=3, relief="ridge")
punchline_box.place(x=50, y=250, width=600, height=100)

punchline_label = Label(
    punchline_box,
    text="",
    font=("Arial", 13, "italic"),
    fg="#E67E22",
    bg="#FFF9E6",
    wraplength=580,
    justify="center"
)
punchline_label.pack(expand=True)

# Button container frame for better organization
button_frame = Frame(task_frame, bg="#ECF0F1")
button_frame.place(x=150, y=370)

# Alexa tell me a joke button
alexa_button = Button(
    button_frame,
    text="🎲 Alexa tell me a Joke",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#3498DB",
    activebackground="#2E86C1",
    activeforeground="white",
    borderwidth=0,
    padx=15,
    pady=10,
    cursor="hand2",
    command=show_joke
)
alexa_button.grid(row=0, column=0, padx=5)

# Show Punchline button
punchline_button = Button(
    button_frame,
    text="😂 Show Punchline",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#E67E22",
    activebackground="#D35400",
    activeforeground="white",
    borderwidth=0,
    padx=15,
    pady=10,
    cursor="hand2",
    command=show_punchline,
    state=NORMAL
)
punchline_button.grid(row=0, column=1, padx=5)

# Next Joke button
next_button = Button(
    button_frame,
    text="⏭️ Next Joke",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#27AE60",
    activebackground="#229954",
    activeforeground="white",
    borderwidth=0,
    padx=15,
    pady=10,
    cursor="hand2",
    command=show_joke
)
next_button.grid(row=0, column=2, padx=5)

# Bottom button frame
bottom_button_frame = Frame(task_frame, bg="#ECF0F1")
bottom_button_frame.place(x=250, y=440)

# Home button
home_button = Button(
    bottom_button_frame,
    text="🏠 Home",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#95A5A6",
    activebackground="#7F8C8D",
    activeforeground="white",
    borderwidth=0,
    padx=20,
    pady=8,
    cursor="hand2",
    command=go_home
)
home_button.grid(row=0, column=0, padx=5)

# Quit button
quit_button = Button(
    bottom_button_frame,
    text="❌ Quit",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#E74C3C",
    activebackground="#C0392B",
    activeforeground="white",
    borderwidth=0,
    padx=20,
    pady=8,
    cursor="hand2",
    command=root.quit
)
quit_button.grid(row=0, column=1, padx=5)

# Start with the home screen
switch_frame(home_frame)

# Run the application
root.mainloop()