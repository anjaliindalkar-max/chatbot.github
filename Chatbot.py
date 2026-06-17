import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# -----------------------------
# Chatbot Response Function
# -----------------------------
def get_response(user):
    user = user.lower()

    if any(word in user for word in ["hi", "hello", "hey"]):
        return "Hello! Welcome to CKT College. How can I help you today?"

    elif any(word in user for word in ["course", "courses"]):
        return """Available Courses

• Artificial Intelligence
• Data Science
• Web Development
• Cyber Security
• Machine Learning
• Cloud Computing
"""

    elif any(word in user for word in ["admission", "apply", "registration"]):
        return """Admission Process

1. Fill Application Form
2. Upload Required Documents
3. Pay Registration Fee
4. Document Verification
5. Admission Confirmation

Admissions are currently open.
"""

    elif any(word in user for word in ["fee", "fees", "cost"]):
        return """Course Fees

• AI & Data Science : Rs. 85,000/year
• Web Development : Rs. 70,000/year
• Cyber Security : Rs. 90,000/year

Scholarships are available for eligible students.
"""

    elif any(word in user for word in ["contact", "phone", "email"]):
        return """Contact Information

Phone : +91 XXXXX XXXXX
Email : info@cktcollege.edu.in
Website : www.cktcollege.edu.in
"""

    elif any(word in user for word in ["timing", "timings", "hours"]):
        return """College Timings

Monday - Friday : 9:00 AM - 5:00 PM
Saturday : 9:00 AM - 1:00 PM
Sunday : Closed
"""

    elif "scholarship" in user:
        return """Scholarships

• Merit-Based Scholarship
• Sports Scholarship
• Need-Based Financial Aid

Contact the admission office for eligibility details.
"""

    elif any(word in user for word in ["principal", "head"]):
        return """Principal Information

For information regarding the Principal,
please visit the college website or office.
"""

    elif "help" in user:
        return """Available Commands

• Courses
• Admission
• Fees
• Contact
• Timings
• Scholarship
• Help
"""

    else:
        return "Sorry, I couldn't understand that. Please try again."

# -----------------------------
# Send Message Function
# -----------------------------
def send_message():
    user = entry.get().strip()

    if user == "":
        return

    current_time = datetime.now().strftime("%H:%M")

    chat_area.insert(
        tk.END,
        f"\nYou ({current_time}): {user}\n",
        "user"
    )

    response = get_response(user)

    chat_area.insert(
        tk.END,
        f"CKT Assistant ({current_time}): {response}\n\n",
        "bot"
    )

    chat_area.see(tk.END)
    entry.delete(0, tk.END)

# -----------------------------
# Quick Buttons
# -----------------------------
def quick_message(text):
    entry.delete(0, tk.END)
    entry.insert(0, text)
    send_message()

# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("CKT College Student Help Desk")
root.geometry("900x700")
root.configure(bg="#f5f7fa")

# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="CKT COLLEGE STUDENT HELP DESK",
    font=("Segoe UI", 22, "bold"),
    bg="#f5f7fa",
    fg="#1f4e79"
)
title.pack(pady=15)

# -----------------------------
# Chat Area
# -----------------------------
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=85,
    height=25,
    font=("Segoe UI", 11)
)
chat_area.pack(padx=15, pady=10)

# Chat Styles
chat_area.tag_config(
    "user",
    foreground="blue",
    font=("Segoe UI", 11, "bold")
)

chat_area.tag_config(
    "bot",
    foreground="green",
    font=("Segoe UI", 11)
)

# Welcome Message
chat_area.insert(
    tk.END,
    """Welcome to CKT College Student Help Desk

I can assist you with:

• Courses
• Admissions
• Fees
• Contact Information
• Timings
• Scholarships

Type your question below or use the buttons provided.
"""
)

# -----------------------------
# Input Box
# -----------------------------
entry = tk.Entry(
    root,
    width=65,
    font=("Segoe UI", 12)
)
entry.pack(pady=8)

# Enter Key Support
entry.bind("<Return>", lambda event: send_message())

# -----------------------------
# Send Button
# -----------------------------
send_btn = tk.Button(
    root,
    text="Send",
    width=15,
    font=("Segoe UI", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    command=send_message
)
send_btn.pack(pady=10)

# -----------------------------
# Quick Access Buttons
# -----------------------------
frame = tk.Frame(root, bg="#f5f7fa")
frame.pack(pady=15)

buttons = [
    ("Courses", "courses"),
    ("Admission", "admission"),
    ("Fees", "fees"),
    ("Contact", "contact"),
    ("Timings", "timings"),
    ("Scholarship", "scholarship")
]

for i, (text, command) in enumerate(buttons):
    tk.Button(
        frame,
        text=text,
        width=12,
        font=("Segoe UI", 10),
        command=lambda c=command: quick_message(c)
    ).grid(row=0, column=i, padx=5)

root.mainloop()