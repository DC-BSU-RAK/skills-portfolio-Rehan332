import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os

# ---------------------------
# Create root first (required for PhotoImage)
# ---------------------------
root = tk.Tk()
root.title("Maths Quiz Game")
root.geometry("800x520")
root.resizable(False, False)

# ---------------------------
# Globals used by functions
# ---------------------------
level = None                 # "Easy", "Moderate", "Advanced"
score = 0                    # total score out of 100
question_number = 0          # 1..10
attempt = 1                  # 1 or 2
num1 = 0
num2 = 0
operation = "+"
current_answer = 0
answer_entry = None
bg_label = None
timer_label = None
time_left = 120              # seconds for whole quiz
timer_running = False

# Keep references to PhotoImage to prevent garbage collection
_loaded_images = {}

# ---------------------------
# Utility: load background safely (images must be in same folder)
# ---------------------------
def load_bg(filename, size=(800, 520)):
    """Load an image file and return a PhotoImage, or None if it fails."""
    if not os.path.exists(filename):
        print(f"⚠️ Image not found: {filename}")
        return None
    try:
        im = Image.open(filename)
        im = im.resize(size)
        photo = ImageTk.PhotoImage(im)
        _loaded_images[filename] = photo
        print(f"✅ Loaded background: {filename}")
        return photo
    except Exception as e:
        print(f"❌ Error loading {filename}: {e}")
        return None

# Load images (names expected in same folder)
bg_home   = load_bg("home_bg.jpg")
bg_easy   = load_bg("easy_bg.jpg")
bg_medium = load_bg("medium_bg.jpg")
bg_hard   = load_bg("hard_bg.jpg")
bg_result = load_bg("result_bg.jpg")

# ---------------------------
# Professional custom popups (no system dialog)
# ---------------------------
def success_popup(message):
    popup = tk.Toplevel(root)
    popup.title("Correct")
    popup.geometry("360x150")
    popup.resizable(False, False)
    popup.configure(bg="#f7f9fb")
    # center
    popup.update_idletasks()
    x = (popup.winfo_screenwidth() // 2) - (360 // 2)
    y = (popup.winfo_screenheight() // 2) - (150 // 2)
    popup.geometry(f"+{x}+{y}")

    frm = tk.Frame(popup, bg="#f7f9fb", padx=18, pady=12)
    frm.pack(expand=True, fill="both")

    lbl_icon = tk.Label(frm, text="✅", font=("Segoe UI Emoji", 30), bg="#f7f9fb")
    lbl_icon.grid(row=0, column=0, rowspan=2, padx=(0,12))

    lbl_title = tk.Label(frm, text="Great!", font=("Segoe UI", 14, "bold"), bg="#f7f9fb")
    lbl_title.grid(row=0, column=1, sticky="w")

    lbl_msg = tk.Label(frm, text=message, font=("Segoe UI", 12), bg="#f7f9fb", wraplength=210, justify="left")
    lbl_msg.grid(row=1, column=1, sticky="w")

    btn = tk.Button(frm, text="OK", command=popup.destroy, bg="#2271b1", fg="white", relief="flat", padx=10, pady=6)
    btn.grid(row=2, column=0, columnspan=2, pady=(12,0))
    popup.grab_set()

def info_popup(message, title="Info"):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("360x150")
    popup.resizable(False, False)
    popup.configure(bg="#fff9f0")
    popup.update_idletasks()
    x = (popup.winfo_screenwidth() // 2) - (360 // 2)
    y = (popup.winfo_screenheight() // 2) - (150 // 2)
    popup.geometry(f"+{x}+{y}")
    frm = tk.Frame(popup, bg="#fff9f0", padx=18, pady=12)
    frm.pack(expand=True, fill="both")
    lbl_icon = tk.Label(frm, text="⚠️", font=("Segoe UI Emoji", 28), bg="#fff9f0")
    lbl_icon.grid(row=0, column=0, rowspan=2, padx=(0,12))
    lbl_title = tk.Label(frm, text=title, font=("Segoe UI", 14, "bold"), bg="#fff9f0")
    lbl_title.grid(row=0, column=1, sticky="w")
    lbl_msg = tk.Label(frm, text=message, font=("Segoe UI", 12), bg="#fff9f0", wraplength=210, justify="left")
    lbl_msg.grid(row=1, column=1, sticky="w")
    btn = tk.Button(frm, text="OK", command=popup.destroy, bg="#e07a00", fg="white", relief="flat", padx=10, pady=6)
    btn.grid(row=2, column=0, columnspan=2, pady=(12,0))
    popup.grab_set()

# ---------------------------
# GUI helpers
# ---------------------------
def clear_screen():
    global bg_label, timer_label
    for w in root.winfo_children():
        w.destroy()
    # recreate background label and timer_label placeholders for consistent layout
    bg_label = tk.Label(root, bg="white")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    timer_label = None

def place_background(photo, fallback_color):
    """Put a background image (PhotoImage) or a fallback color."""
    global bg_label
    # remove old bg_label if present
    if bg_label is not None:
        try:
            bg_label.destroy()
        except:
            pass
    if photo:
        bg_label = tk.Label(root, image=photo)
        bg_label.image = photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    else:
        bg_label = tk.Label(root, bg=fallback_color)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def grade_from_score(s):
    """Return letter grade based on 0-100 score."""
    if s >= 90: return "A+"
    if s >= 80: return "A"
    if s >= 70: return "B"
    if s >= 60: return "C"
    return "D"

# ---------------------------
# Required functions (as requested)
# ---------------------------

def displayMenu():
    """Displays the difficulty level menu at the beginning of the quiz."""
    global timer_label
    clear_screen()
    place_background(bg_home, "#cfe9ff")

    # Title
    title = tk.Label(root, text="DIFFICULTY LEVEL", font=("Segoe UI", 24, "bold"), bg="#ffffff")
    title.place(relx=0.5, rely=0.12, anchor="center")

    # Buttons with images if available
    # Easy
    easy_btn = ttk.Button(root, text="Easy (1-digit)", command=lambda: start_quiz("Easy"))
    easy_btn.place(relx=0.35, rely=0.35, anchor="center", width=220, height=40)

    # Moderate
    mod_btn = ttk.Button(root, text="Moderate (2-digit)", command=lambda: start_quiz("Moderate"))
    mod_btn.place(relx=0.65, rely=0.35, anchor="center", width=220, height=40)

    # Advanced
    adv_btn = ttk.Button(root, text="Advanced (4-digit)", command=lambda: start_quiz("Advanced"))
    adv_btn.place(relx=0.5, rely=0.5, anchor="center", width=240, height=40)

    # Info / Start instructions
    instruct = tk.Label(root, text="Choose a level to begin. Each play is 10 questions.\n10 pts first try, 5 pts second try.",
                       font=("Segoe UI", 11), bg="#ffffff")
    instruct.place(relx=0.5, rely=0.67, anchor="center")

    # Exit
    quit_btn = ttk.Button(root, text="Exit", command=root.quit)
    quit_btn.place(relx=0.5, rely=0.82, anchor="center", width=100)

def randomInt(difficulty):
    """Return a random integer appropriate for the difficulty."""
    if difficulty == "Easy":
        return random.randint(1, 9)
    elif difficulty == "Moderate":
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)

def decideOperation():
    """Randomly decide whether the problem is addition or subtraction."""
    return random.choice(['+', '-'])

def displayProblem():
    """Displays the current question and input controls."""
    global answer_entry, timer_label, attempt, num1, num2, operation, current_answer, time_left

    clear_screen()

    # set background based on level
    bg = bg_easy if level == "Easy" else bg_medium if level == "Moderate" else bg_hard
    fallback = "#e8f8ef" if level == "Easy" else "#fff6df" if level == "Moderate" else "#feecec"
    place_background(bg, fallback)

    # Timer label
    timer_label = tk.Label(root, text=f"Time Left: {time_left}s", font=("Segoe UI", 12, "bold"), bg="#ffffff")
    timer_label.place(relx=0.92, rely=0.05, anchor="center")

    # Question header
    header = tk.Label(root, text=f"Question {question_number} of 10", font=("Segoe UI", 16, "bold"), bg="#ffffff")
    header.place(relx=0.5, rely=0.12, anchor="center")

    # Generate question values
    num1 = randomInt(level)
    num2 = randomInt(level)
    operation = decideOperation()
    # Ensure subtraction can be negative (assignment allows negative answers) — keep as is
    current_answer = num1 + num2 if operation == '+' else num1 - num2

    question_label = tk.Label(root, text=f"{num1} {operation} {num2} =", font=("Segoe UI", 28, "bold"), bg="#ffffff")
    question_label.place(relx=0.5, rely=0.35, anchor="center")

    # Input entry
    answer_entry = tk.Entry(root, font=("Segoe UI", 20), justify="center", width=10)
    answer_entry.place(relx=0.5, rely=0.5, anchor="center")
    answer_entry.focus_set()

    # Feedback area (not system messagebox)
    feedback = tk.Label(root, text="", font=("Segoe UI", 13, "bold"), bg="#ffffff")
    feedback.place(relx=0.5, rely=0.62, anchor="center")

    # Submit button
    submit_btn = ttk.Button(root, text="Submit Answer", command=lambda: isCorrect(feedback))
    submit_btn.place(relx=0.5, rely=0.72, anchor="center", width=160, height=36)

    # Show current score small
    score_lbl = tk.Label(root, text=f"Score: {score}/100", font=("Segoe UI", 11, "bold"), bg="#ffffff")
    score_lbl.place(relx=0.08, rely=0.05, anchor="w")

def isCorrect(feedback_label_widget):
    """Check the user's answer; award points and advance or allow retry."""
    global score, attempt, question_number, answer_entry

    if answer_entry is None:
        return

    user_text = answer_entry.get().strip()
    # allow negative answers and validate integer
    try:
        user_val = int(user_text)
    except ValueError:
        feedback_label_widget.config(text="⚠️ Please enter a valid integer", fg="red")
        return

    correct = num1 + num2 if operation == '+' else num1 - num2

    if user_val == correct:
        # correct
        if attempt == 1:
            score += 10
            # professional popup
            success_popup("Correct on first try! (+10 points)")
        else:
            score += 5
            success_popup("Correct on second try! (+5 points)")

        # Prepare next question
        question_number += 1
        attempt = 1
        # small delay to let user see popup; then show next or results
        root.after(600, lambda: displayResults() if question_number > 10 else displayProblem())
    else:
        if attempt == 1:
            attempt = 2
            info_popup("Incorrect — you have one more attempt.", title="Try Again")
            # clear input and keep on same question
            answer_entry.delete(0, tk.END)
        else:
            # wrong twice -> show correct and proceed
            info_popup(f"Wrong again. Correct answer: {correct}", title="Answer")
            question_number += 1
            attempt = 1
            root.after(600, lambda: displayResults() if question_number > 10 else displayProblem())

def displayResults():
    """Show the user's final score out of 100 and rank; prompt for replay."""
    global timer_running
    timer_running = False

    clear_screen()
    place_background(bg_result, "#ffffff")

    # Score and rank
    lbl = tk.Label(root, text="Quiz Completed!", font=("Segoe UI", 28, "bold"), bg="#ffffff")
    lbl.place(relx=0.5, rely=0.18, anchor="center")

    score_lbl = tk.Label(root, text=f"Your Score: {score}/100", font=("Segoe UI", 20), bg="#ffffff")
    score_lbl.place(relx=0.5, rely=0.32, anchor="center")

    rank = grade_from_score(score)
    rank_lbl = tk.Label(root, text=f"Rank: {rank}", font=("Segoe UI", 18, "bold"), bg="#ffffff")
    rank_lbl.place(relx=0.5, rely=0.42, anchor="center")

    # Buttons: Play again, Exit
    play_btn = ttk.Button(root, text="Play Again", command=lambda: displayMenu())
    play_btn.place(relx=0.44, rely=0.62, anchor="center", width=140, height=36)

    quit_btn = ttk.Button(root, text="Exit", command=root.quit)
    quit_btn.place(relx=0.56, rely=0.62, anchor="center", width=140, height=36)

# ---------------------------
# Timer logic (per quiz)
# ---------------------------
def start_timer():
    global time_left, timer_running
    timer_running = True

    def tick():
        global time_left, timer_running
        if not timer_running:
            return
        # Update timer label if exists
        for w in root.winfo_children():
            # locate timer label by text starting "Time Left"
            if isinstance(w, tk.Label) and w.cget("text").startswith("Time Left"):
                w.config(text=f"Time Left: {time_left}s")
                break
        if time_left <= 0:
            # end the quiz immediately
            info_popup("Time's up! The quiz will finish now.", title="Time Up")
            displayResults()
            return
        time_left -= 1
        root.after(1000, tick)

    root.after(1000, tick)

# ---------------------------
# Quiz initialization helper
# ---------------------------
def start_quiz(chosen_level):
    """Initialize quiz state and begin."""
    global level, score, question_number, attempt, time_left
    level = chosen_level
    score = 0
    question_number = 1
    attempt = 1
    time_left = 120
    # show first question and start timer
    displayProblem()
    start_timer()

# ---------------------------
# Start application
# ---------------------------
displayMenu()
root.mainloop()
