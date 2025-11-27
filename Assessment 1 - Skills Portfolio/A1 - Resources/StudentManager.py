from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os

# ===================== FIX WORKING DIRECTORY =====================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

def get_path(filename):
    return os.path.join(BASE_DIR, filename)


# Initialize root window
root = Tk()
root.title("Student Manager System")
root.geometry("700x500")
root.resizable(False, False)

# Global variable for current student data
current_students = []

# ==================== UTILITY FUNCTIONS ====================

def switch_frame(frame):
    """Switch between different frames"""
    frame.tkraise()

def read_student_data():
    """Read and process student data from file"""
    try:
        with open(get_path("studentMarks.txt"), "r") as file:
            lines = file.readlines()
        
        lines = [line.strip() for line in lines if line.strip()]
        
        if not lines:
            messagebox.showinfo("Info", "No student records found.")
            return 0, []
        
        # Skip the first line (number of students)
        if lines[0].isdigit():
            lines = lines[1:]
        
        students = []
        for line in lines:
            data = line.strip().split(",")
            if len(data) != 6:
                continue
            
            student_id = data[0]
            name = data[1]
            coursework_marks = list(map(int, data[2:5]))
            exam_mark = int(data[5])
            
            total_coursework = sum(coursework_marks)
            total_marks = total_coursework + exam_mark
            percentage = (total_marks / 160) * 100
            
            grade = (
                "A" if percentage >= 70 else
                "B" if percentage >= 60 else
                "C" if percentage >= 50 else
                "D" if percentage >= 40 else
                "F"
            )
            
            students.append({
                "id": student_id,
                "name": name,
                "coursework": coursework_marks,
                "total_coursework": total_coursework,
                "exam": exam_mark,
                "percentage": percentage,
                "grade": grade
            })
        
        return len(students), students
    
    except FileNotFoundError:
        messagebox.showerror("Error", "studentMarks.txt file not found!")
        return 0, []
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return 0, []

def save_student_data(students):
    """Save student data back to file"""
    try:
        with open("studentMarks.txt", "w") as file:
            # Write the number of students first
            file.write(f"{len(students)}\n")
            for student in students:
                cw_marks = ','.join(map(str, student['coursework']))
                line = f"{student['id']},{student['name']},{cw_marks},{student['exam']}\n"
                file.write(line)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Could not save to file: {e}")
        return False

# ==================== FRAMES SETUP ====================

# Home Frame
home_frame = Frame(root, bg="#2C3E50")
home_frame.place(relwidth=1, relheight=1)

try:
    bg_home = Image.open(get_path("student_home_bg.jpg"))
    bg_home = bg_home.resize((700, 500))
    bg_photo_home = ImageTk.PhotoImage(bg_home)
    Label(home_frame, image=bg_photo_home).place(relwidth=1, relheight=1)
except:
    pass

# Main Menu Frame
main_menu_frame = Frame(root, bg="#ECF0F1")
main_menu_frame.place(relwidth=1, relheight=1)

try:
    bg_main = Image.open(get_path("main_menu_bg.jpg"))
    bg_main = bg_main.resize((700, 500))
    bg_photo_main = ImageTk.PhotoImage(bg_main)
    Label(main_menu_frame, image=bg_photo_main).place(relwidth=1, relheight=1)
except:
    pass

# View All Records Frame
view_all_frame = Frame(root, bg="#ECF0F1")
view_all_frame.place(relwidth=1, relheight=1)

try:
    bg_view = Image.open(get_path("view_records_bg.jpg"))
    bg_view = bg_view.resize((700, 500))
    bg_photo_view = ImageTk.PhotoImage(bg_view)
    Label(view_all_frame, image=bg_photo_view).place(relwidth=1, relheight=1)
except:
    pass

# View Individual Frame
view_individual_frame = Frame(root, bg="#ECF0F1")
view_individual_frame.place(relwidth=1, relheight=1)

try:
    bg_individual = Image.open(get_path("individual_bg.jpg"))
    bg_individual = bg_individual.resize((700, 500))
    bg_photo_individual = ImageTk.PhotoImage(bg_individual)
    Label(view_individual_frame, image=bg_photo_individual).place(relwidth=1, relheight=1)
except:
    pass

# Highest/Lowest Frame
stats_frame = Frame(root, bg="#ECF0F1")
stats_frame.place(relwidth=1, relheight=1)

try:
    bg_stats = Image.open(get_path("stats_bg.jpg"))
    bg_stats = bg_stats.resize((700, 500))
    bg_photo_stats = ImageTk.PhotoImage(bg_stats)
    Label(stats_frame, image=bg_photo_stats).place(relwidth=1, relheight=1)
except:
    pass

# Extension Menu Frame
extension_frame = Frame(root, bg="#ECF0F1")
extension_frame.place(relwidth=1, relheight=1)

try:
    bg_ext = Image.open(get_path("extension_bg.jpg"))
    bg_ext = bg_ext.resize((700, 500))
    bg_photo_ext = ImageTk.PhotoImage(bg_ext)
    Label(extension_frame, image=bg_photo_ext).place(relwidth=1, relheight=1)
except:
    pass

# Sort Frame
sort_frame = Frame(root, bg="#ECF0F1")
sort_frame.place(relwidth=1, relheight=1)

try:
    bg_sort = Image.open(get_path("sort_bg.jpg"))
    bg_sort = bg_sort.resize((700, 500))
    bg_photo_sort = ImageTk.PhotoImage(bg_sort)
    Label(sort_frame, image=bg_photo_sort).place(relwidth=1, relheight=1)
except:
    pass

# Add Student Frame
add_frame = Frame(root, bg="#ECF0F1")
add_frame.place(relwidth=1, relheight=1)

try:
    bg_add = Image.open(get_path("add_bg.jpg"))
    bg_add = bg_add.resize((700, 500))
    bg_photo_add = ImageTk.PhotoImage(bg_add)
    Label(add_frame, image=bg_photo_add).place(relwidth=1, relheight=1)
except:
    pass

# Delete Frame
delete_frame = Frame(root, bg="#ECF0F1")
delete_frame.place(relwidth=1, relheight=1)

try:
    bg_delete = Image.open(get_path("delete_bg.jpg"))
    bg_delete = bg_delete.resize((700, 500))
    bg_photo_delete = ImageTk.PhotoImage(bg_delete)
    Label(delete_frame, image=bg_photo_delete).place(relwidth=1, relheight=1)
except:
    pass

# Update Frame
update_frame = Frame(root, bg="#ECF0F1")
update_frame.place(relwidth=1, relheight=1)

try:
    bg_update = Image.open(get_path("update_bg.jpg"))
    bg_update = bg_update.resize((700, 500))
    bg_photo_update = ImageTk.PhotoImage(bg_update)
    Label(update_frame, image=bg_photo_update).place(relwidth=1, relheight=1)
except:
    pass

# ==================== HOME FRAME WIDGETS ====================

Label(
    home_frame,
    text="🎓 Student Manager System 🎓",
    font=("Arial Black", 26, "bold"),
    fg="#3498DB",
    bg="#ECF0F1"
).place(x=130, y=150)

Label(
    home_frame,
    text="Manage Student Records Efficiently",
    font=("Arial", 14, "italic"),
    fg="#7F8C8D",
    bg="#ECF0F1"
).place(x=220, y=210)

Button(
    home_frame,
    text="START",
    font=("Arial Black", 16, "bold"),
    fg="white",
    bg="#27AE60",
    activebackground="#229954",
    activeforeground="white",
    padx=50,
    pady=15,
    cursor="hand2",
    borderwidth=0,
    command=lambda: switch_frame(main_menu_frame)
).place(x=260, y=280)

# ==================== MAIN MENU FRAME ====================

Label(
    main_menu_frame,
    text="Main Menu",
    font=("Arial Black", 22, "bold"),
    fg="#2C3E50",
    bg="#F8F9FA"
).place(x=270, y=30)

menu_buttons_y = 120
menu_button_spacing = 70

menu_items = [
    ("📋 View All Student Records", lambda: [view_all_students(), switch_frame(view_all_frame)]),
    ("👤 View Individual Student", lambda: switch_frame(view_individual_frame)),
    ("🏆 Show Highest Score", lambda: [show_highest(), switch_frame(stats_frame)]),
    ("📉 Show Lowest Score", lambda: [show_lowest(), switch_frame(stats_frame)]),
    ("⚙️ Extension Features", lambda: switch_frame(extension_frame))
]

for idx, (text, cmd) in enumerate(menu_items):
    Button(
        main_menu_frame,
        text=text,
        font=("Arial", 13, "bold"),
        fg="white",
        bg="#3498DB",
        activebackground="#2E86C1",
        activeforeground="white",
        width=30,
        pady=8,
        cursor="hand2",
        borderwidth=0,
        command=cmd
    ).place(x=180, y=menu_buttons_y + idx * menu_button_spacing)

Button(
    main_menu_frame,
    text="🏠 Home",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#95A5A6",
    activebackground="#7F8C8D",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=lambda: switch_frame(home_frame)
).place(x=300, y=450)

# ==================== VIEW ALL RECORDS FRAME ====================

Label(
    view_all_frame,
    text="All Student Records",
    font=("Arial Black", 20, "bold"),
    fg="#2C3E50",
    bg="#F8F9FA"
).place(x=220, y=20)

view_all_text = Text(
    view_all_frame,
    font=("Courier New", 9),
    width=80,
    height=20,
    wrap="word"
)
view_all_text.place(x=50, y=70)

scrollbar_all = Scrollbar(view_all_frame, command=view_all_text.yview)
scrollbar_all.place(x=665, y=70, height=340)
view_all_text.config(yscrollcommand=scrollbar_all.set)

def view_all_students():
    num_students, students = read_student_data()
    view_all_text.config(state="normal")
    view_all_text.delete(1.0, END)
    
    if not students:
        view_all_text.insert(END, "No student records found.\n")
    else:
        view_all_text.insert(END, "=" * 80 + "\n")
        view_all_text.insert(END, "STUDENT RECORDS\n")
        view_all_text.insert(END, "=" * 80 + "\n\n")
        
        for student in students:
            view_all_text.insert(END, f"Student Name: {student['name']}\n")
            view_all_text.insert(END, f"Student Number: {student['id']}\n")
            view_all_text.insert(END, f"Total Coursework Mark: {student['total_coursework']}/60\n")
            view_all_text.insert(END, f"Exam Mark: {student['exam']}/100\n")
            view_all_text.insert(END, f"Overall Percentage: {student['percentage']:.2f}%\n")
            view_all_text.insert(END, f"Grade: {student['grade']}\n")
            view_all_text.insert(END, "-" * 80 + "\n\n")
        
        total_percentage = sum(s['percentage'] for s in students)
        average_percentage = total_percentage / num_students
        
        view_all_text.insert(END, "=" * 80 + "\n")
        view_all_text.insert(END, "SUMMARY\n")
        view_all_text.insert(END, "=" * 80 + "\n")
        view_all_text.insert(END, f"Total Students: {num_students}\n")
        view_all_text.insert(END, f"Average Percentage: {average_percentage:.2f}%\n")
    
    view_all_text.config(state="disabled")

Button(
    view_all_frame,
    text="🔙 Back",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#E74C3C",
    activebackground="#C0392B",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=lambda: switch_frame(main_menu_frame)
).place(x=300, y=440)

# ==================== VIEW INDIVIDUAL FRAME ====================

Label(
    view_individual_frame,
    text="View Individual Student",
    font=("Arial Black", 20, "bold"),
    fg="#2C3E50",
    bg="#F8F9FA"
).place(x=200, y=20)

Label(
    view_individual_frame,
    text="Enter Student Name or ID:",
    font=("Arial", 13),
    fg="#2C3E50",
    bg="#ECF0F1"
).place(x=230, y=80)

individual_entry = Entry(view_individual_frame, font=("Arial", 12), width=30)
individual_entry.place(x=200, y=120)

individual_output = Text(
    view_individual_frame,
    font=("Courier New", 10),
    width=70,
    height=15,
    wrap="word"
)
individual_output.place(x=70, y=180)

def search_individual():
    search_term = individual_entry.get().strip()
    if not search_term:
        messagebox.showwarning("Warning", "Please enter a student name or ID")
        return
    
    _, students = read_student_data()
    individual_output.config(state="normal")
    individual_output.delete(1.0, END)
    
    found = False
    for student in students:
        if student['name'].lower() == search_term.lower() or student['id'] == search_term:
            individual_output.insert(END, "=" * 60 + "\n")
            individual_output.insert(END, f"Student Name: {student['name']}\n")
            individual_output.insert(END, f"Student Number: {student['id']}\n")
            individual_output.insert(END, f"Total Coursework Mark: {student['total_coursework']}/60\n")
            individual_output.insert(END, f"Exam Mark: {student['exam']}/100\n")
            individual_output.insert(END, f"Overall Percentage: {student['percentage']:.2f}%\n")
            individual_output.insert(END, f"Grade: {student['grade']}\n")
            individual_output.insert(END, "=" * 60 + "\n")
            found = True
            break
    
    if not found:
        individual_output.insert(END, "Student not found. Please check the name or ID.\n")
    
    individual_output.config(state="disabled")

Button(
    view_individual_frame,
    text="🔍 Search",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#3498DB",
    activebackground="#2E86C1",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=search_individual
).place(x=300, y=400)

Button(
    view_individual_frame,
    text="🔙 Back",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#E74C3C",
    activebackground="#C0392B",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=lambda: switch_frame(main_menu_frame)
).place(x=300, y=450)

# ==================== STATS FRAME (Highest/Lowest) ====================

Label(
    stats_frame,
    text="Student Statistics",
    font=("Arial Black", 20, "bold"),
    fg="#2C3E50",
    bg="#F8F9FA"
).place(x=230, y=20)

stats_output = Text(
    stats_frame,
    font=("Courier New", 10),
    width=70,
    height=18,
    wrap="word"
)
stats_output.place(x=70, y=80)

def show_highest():
    _, students = read_student_data()
    stats_output.config(state="normal")
    stats_output.delete(1.0, END)
    
    if not students:
        stats_output.insert(END, "No student records found.\n")
    else:
        highest_percentage = max(s['percentage'] for s in students)
        highest_students = [s for s in students if s['percentage'] == highest_percentage]
        
        stats_output.insert(END, "=" * 60 + "\n")
        stats_output.insert(END, "STUDENT(S) WITH HIGHEST OVERALL MARK\n")
        stats_output.insert(END, "=" * 60 + "\n\n")
        
        for student in highest_students:
            stats_output.insert(END, f"Student Name: {student['name']}\n")
            stats_output.insert(END, f"Student Number: {student['id']}\n")
            stats_output.insert(END, f"Total Coursework Mark: {student['total_coursework']}/60\n")
            stats_output.insert(END, f"Exam Mark: {student['exam']}/100\n")
            stats_output.insert(END, f"Overall Percentage: {student['percentage']:.2f}%\n")
            stats_output.insert(END, f"Grade: {student['grade']}\n")
            stats_output.insert(END, "-" * 60 + "\n\n")
    
    stats_output.config(state="disabled")

def show_lowest():
    _, students = read_student_data()
    stats_output.config(state="normal")
    stats_output.delete(1.0, END)
    
    if not students:
        stats_output.insert(END, "No student records found.\n")
    else:
        lowest_percentage = min(s['percentage'] for s in students)
        lowest_students = [s for s in students if s['percentage'] == lowest_percentage]
        
        stats_output.insert(END, "=" * 60 + "\n")
        stats_output.insert(END, "STUDENT(S) WITH LOWEST OVERALL MARK\n")
        stats_output.insert(END, "=" * 60 + "\n\n")
        
        for student in lowest_students:
            stats_output.insert(END, f"Student Name: {student['name']}\n")
            stats_output.insert(END, f"Student Number: {student['id']}\n")
            stats_output.insert(END, f"Total Coursework Mark: {student['total_coursework']}/60\n")
            stats_output.insert(END, f"Exam Mark: {student['exam']}/100\n")
            stats_output.insert(END, f"Overall Percentage: {student['percentage']:.2f}%\n")
            stats_output.insert(END, f"Grade: {student['grade']}\n")
            stats_output.insert(END, "-" * 60 + "\n\n")
    
    stats_output.config(state="disabled")

Button(
    stats_frame,
    text="🔙 Back",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#E74C3C",
    activebackground="#C0392B",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=lambda: switch_frame(main_menu_frame)
).place(x=300, y=440)

# ==================== EXTENSION MENU FRAME ====================

Label(
    extension_frame,
    text="Extension Features",
    font=("Arial Black", 22, "bold"),
    fg="#2C3E50",
    bg="#F8F9FA"
).place(x=220, y=30)

ext_buttons_y = 120
ext_button_spacing = 70

ext_items = [
    ("📊 Sort Student Records", lambda: switch_frame(sort_frame)),
    ("➕ Add Student Record", lambda: switch_frame(add_frame)),
    ("🗑️ Delete Student Record", lambda: switch_frame(delete_frame)),
    ("✏️ Update Student Record", lambda: switch_frame(update_frame))
]

for idx, (text, cmd) in enumerate(ext_items):
    Button(
        extension_frame,
        text=text,
        font=("Arial", 13, "bold"),
        fg="white",
        bg="#9B59B6",
        activebackground="#8E44AD",
        activeforeground="white",
        width=30,
        pady=8,
        cursor="hand2",
        borderwidth=0,
        command=cmd
    ).place(x=180, y=ext_buttons_y + idx * ext_button_spacing)

Button(
    extension_frame,
    text="🔙 Back",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#E74C3C",
    activebackground="#C0392B",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=lambda: switch_frame(main_menu_frame)
).place(x=300, y=450)

# ==================== SORT FRAME ====================

Label(
    sort_frame,
    text="Sort Student Records",
    font=("Arial Black", 20, "bold"),
    fg="#2C3E50",
    bg="#F8F9FA"
).place(x=220, y=20)

sort_var = StringVar(value="Ascending")

Radiobutton(
    sort_frame,
    text="📈 Ascending Order",
    variable=sort_var,
    value="Ascending",
    font=("Arial", 12),
    fg="#2C3E50",
    bg="#ECF0F1",
    cursor="hand2"
).place(x=260, y=70)

Radiobutton(
    sort_frame,
    text="📉 Descending Order",
    variable=sort_var,
    value="Descending",
    font=("Arial", 12),
    fg="#2C3E50",
    bg="#ECF0F1",
    cursor="hand2"
).place(x=260, y=100)

sort_output = Text(
    sort_frame,
    font=("Courier New", 9),
    width=75,
    height=17,
    wrap="word"
)
sort_output.place(x=60, y=140)

def sort_students():
    _, students = read_student_data()
    
    sorted_students = sorted(students, key=lambda x: x['percentage'], 
                            reverse=(sort_var.get() == "Descending"))
    
    sort_output.config(state="normal")
    sort_output.delete(1.0, END)
    
    sort_output.insert(END, f"Sorted in {sort_var.get()} Order\n")
    sort_output.insert(END, "=" * 70 + "\n\n")
    
    for student in sorted_students:
        sort_output.insert(END, f"Name: {student['name']} | ID: {student['id']} | ")
        sort_output.insert(END, f"Percentage: {student['percentage']:.2f}% | Grade: {student['grade']}\n")
        sort_output.insert(END, "-" * 70 + "\n")
    
    sort_output.config(state="disabled")

Button(
    sort_frame,
    text="📊 Sort",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#3498DB",
    activebackground="#2E86C1",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=sort_students
).place(x=300, y=400)

Button(
    sort_frame,
    text="🔙 Back",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#E74C3C",
    activebackground="#C0392B",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=lambda: switch_frame(extension_frame)
).place(x=300, y=450)

# ==================== ADD STUDENT FRAME ====================

Label(
    add_frame,
    text="Add New Student",
    font=("Arial Black", 20, "bold"),
    fg="#2C3E50",
    bg="#F8F9FA"
).place(x=240, y=20)

add_labels = ["Student ID:", "Student Name:", "Assignment 1 (out of 20):", 
              "Assignment 2 (out of 20):", "Assignment 3 (out of 20):", "Exam Mark (out of 100):"]
add_entries = []

y_pos = 80
for label_text in add_labels:
    Label(
        add_frame,
        text=label_text,
        font=("Arial", 11),
        fg="#2C3E50",
        bg="#ECF0F1"
    ).place(x=150, y=y_pos)
    
    entry = Entry(add_frame, font=("Arial", 11), width=25)
    entry.place(x=350, y=y_pos)
    add_entries.append(entry)
    y_pos += 50

def add_student():
    try:
        student_id = add_entries[0].get().strip()
        name = add_entries[1].get().strip()
        
        if not student_id or not name:
            messagebox.showerror("Error", "Student ID and Name are required!")
            return
        
        cw1 = int(add_entries[2].get().strip())
        cw2 = int(add_entries[3].get().strip())
        cw3 = int(add_entries[4].get().strip())
        exam = int(add_entries[5].get().strip())
        
        if not (0 <= cw1 <= 20 and 0 <= cw2 <= 20 and 0 <= cw3 <= 20):
            messagebox.showerror("Error", "Coursework marks must be between 0 and 20!")
            return
        
        if not (0 <= exam <= 100):
            messagebox.showerror("Error", "Exam mark must be between 0 and 100!")
            return
        
        _, students = read_student_data()
        
        # Check if ID already exists
        if any(s['id'] == student_id for s in students):
            messagebox.showerror("Error", "Student ID already exists!")
            return
        
        new_student = {
            "id": student_id,
            "name": name,
            "coursework": [cw1, cw2, cw3],
            "total_coursework": cw1 + cw2 + cw3,
            "exam": exam,
            "percentage": ((cw1 + cw2 + cw3 + exam) / 160) * 100,
            "grade": ""
        }
        
        students.append(new_student)
        
        if save_student_data(students):
            messagebox.showinfo("Success", f"Student {name} added successfully!")
            for entry in add_entries:
                entry.delete(0, END)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for marks!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

Button(
    add_frame,
    text="➕ Add Student",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#27AE60",
    activebackground="#229954",
    padx=20,
    pady=10,
    cursor="hand2",
    borderwidth=0,
    command=add_student
).place(x=280, y=390)

Button(
    add_frame,
    text="🔙 Back",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#E74C3C",
    activebackground="#C0392B",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=lambda: switch_frame(extension_frame)
).place(x=300, y=450)

# ==================== DELETE STUDENT FRAME ====================

Label(
    delete_frame,
    text="Delete Student Record",
    font=("Arial Black", 20, "bold"),
    fg="#2C3E50",
    bg="#F8F9FA"
).place(x=210, y=20)

Label(
    delete_frame,
    text="Enter Student Name or ID to Delete:",
    font=("Arial", 12),
    fg="#2C3E50",
    bg="#ECF0F1"
).place(x=200, y=80)

delete_entry = Entry(delete_frame, font=("Arial", 12), width=30)
delete_entry.place(x=210, y=120)

delete_output = Text(
    delete_frame,
    font=("Courier New", 10),
    width=70,
    height=12,
    wrap="word"
)
delete_output.place(x=70, y=180)

def search_delete():
    search_term = delete_entry.get().strip()
    if not search_term:
        messagebox.showwarning("Warning", "Please enter a student name or ID")
        return
    
    _, students = read_student_data()
    delete_output.config(state="normal")
    delete_output.delete(1.0, END)
    
    found_students = [s for s in students if s['name'].lower() == search_term.lower() or s['id'] == search_term]
    
    if found_students:
        delete_output.insert(END, "Found Student(s):\n")
        delete_output.insert(END, "=" * 60 + "\n\n")
        for student in found_students:
            delete_output.insert(END, f"Name: {student['name']}\n")
            delete_output.insert(END, f"ID: {student['id']}\n")
            delete_output.insert(END, f"Percentage: {student['percentage']:.2f}%\n")
            delete_output.insert(END, "-" * 60 + "\n")
    else:
        delete_output.insert(END, "No matching student found.\n")
    
    delete_output.config(state="disabled")

def delete_student():
    search_term = delete_entry.get().strip()
    if not search_term:
        messagebox.showwarning("Warning", "Please enter a student name or ID")
        return
    
    _, students = read_student_data()
    
    # Find and remove matching students
    remaining_students = [s for s in students if not (s['name'].lower() == search_term.lower() or s['id'] == search_term)]
    
    if len(remaining_students) < len(students):
        if save_student_data(remaining_students):
            messagebox.showinfo("Success", "Student deleted successfully!")
            delete_entry.delete(0, END)
            delete_output.config(state="normal")
            delete_output.delete(1.0, END)
            delete_output.config(state="disabled")
    else:
        messagebox.showwarning("Warning", "No matching student found.")

Button(
    delete_frame,
    text="🔍 Search",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#3498DB",
    activebackground="#2E86C1",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=search_delete
).place(x=240, y=360)

Button(
    delete_frame,
    text="🗑️ Delete",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#E74C3C",
    activebackground="#C0392B",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=delete_student
).place(x=360, y=360)

Button(
    delete_frame,
    text="🔙 Back",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#95A5A6",
    activebackground="#7F8C8D",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=lambda: switch_frame(extension_frame)
).place(x=300, y=420)

# ==================== UPDATE STUDENT FRAME ====================

Label(
    update_frame,
    text="Update Student Record",
    font=("Arial Black", 20, "bold"),
    fg="#2C3E50",
    bg="#F8F9FA"
).place(x=210, y=20)

Label(
    update_frame,
    text="Enter Student Name or ID:",
    font=("Arial", 12),
    fg="#2C3E50",
    bg="#ECF0F1"
).place(x=230, y=70)

update_search_entry = Entry(update_frame, font=("Arial", 12), width=30)
update_search_entry.place(x=210, y=105)

Label(
    update_frame,
    text="Field to Update:",
    font=("Arial", 12),
    fg="#2C3E50",
    bg="#ECF0F1"
).place(x=280, y=145)

update_field_var = StringVar(value="name")
update_options = ["Student ID", "Name", "Assignment 1", "Assignment 2", "Assignment 3", "Exam Mark"]
update_values = ["id", "name", "cw1", "cw2", "cw3", "exam"]

update_dropdown = ttk.Combobox(
    update_frame,
    values=update_options,
    state="readonly",
    font=("Arial", 11),
    width=28
)
update_dropdown.place(x=210, y=175)
update_dropdown.current(1)

Label(
    update_frame,
    text="New Value:",
    font=("Arial", 12),
    fg="#2C3E50",
    bg="#ECF0F1"
).place(x=305, y=210)

update_value_entry = Entry(update_frame, font=("Arial", 12), width=30)
update_value_entry.place(x=210, y=240)

update_output = Text(
    update_frame,
    font=("Courier New", 10),
    width=65,
    height=7,
    wrap="word"
)
update_output.place(x=90, y=280)

def update_student():
    search_term = update_search_entry.get().strip()
    if not search_term:
        messagebox.showwarning("Warning", "Please enter a student name or ID")
        return
    
    field_index = update_dropdown.current()
    field_name = update_values[field_index]
    new_value = update_value_entry.get().strip()
    
    if not new_value:
        messagebox.showwarning("Warning", "Please enter a new value")
        return
    
    _, students = read_student_data()
    updated = False
    
    for student in students:
        if student['name'].lower() == search_term.lower() or student['id'] == search_term:
            try:
                if field_name == "id":
                    student['id'] = new_value
                elif field_name == "name":
                    student['name'] = new_value
                elif field_name == "cw1":
                    student['coursework'][0] = int(new_value)
                elif field_name == "cw2":
                    student['coursework'][1] = int(new_value)
                elif field_name == "cw3":
                    student['coursework'][2] = int(new_value)
                elif field_name == "exam":
                    student['exam'] = int(new_value)
                
                # Recalculate
                student['total_coursework'] = sum(student['coursework'])
                total = student['total_coursework'] + student['exam']
                student['percentage'] = (total / 160) * 100
                student['grade'] = (
                    "A" if student['percentage'] >= 70 else
                    "B" if student['percentage'] >= 60 else
                    "C" if student['percentage'] >= 50 else
                    "D" if student['percentage'] >= 40 else
                    "F"
                )
                
                updated = True
                break
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid numeric value for marks!")
                return
    
    if updated:
        if save_student_data(students):
            messagebox.showinfo("Success", "Student record updated successfully!")
            update_search_entry.delete(0, END)
            update_value_entry.delete(0, END)
            
            update_output.config(state="normal")
            update_output.delete(1.0, END)
            update_output.insert(END, "Update successful!\n")
            update_output.config(state="disabled")
    else:
        messagebox.showwarning("Warning", "No matching student found.")

Button(
    update_frame,
    text="✏️ Update",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#E67E22",
    activebackground="#D35400",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=update_student
).place(x=300, y=400)

Button(
    update_frame,
    text="🔙 Back",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#95A5A6",
    activebackground="#7F8C8D",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0,
    command=lambda: switch_frame(extension_frame)
).place(x=300, y=450)

# Start with home frame
switch_frame(home_frame)
root.mainloop()