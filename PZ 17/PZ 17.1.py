import tkinter as tk
from tkinter import ttk


def create_registration_form():
    root = tk.Tk()
    root.title("Elegant Registration Form")
    root.geometry("500x600")
    root.configure(bg="#f5f5f5")

    # Header
    header_frame = tk.Frame(root, bg="#4b8fe2", height=80)
    header_frame.pack(fill="x")

    header_label = tk.Label(header_frame, text="CREATE ACCOUNT", font=("Arial", 18, "bold"),
                            fg="white", bg="#4b8fe2")
    header_label.pack(pady=20)

    # Form Frame
    form_frame = tk.Frame(root, bg="#f5f5f5", padx=30, pady=20)
    form_frame.pack(fill="both", expand=True)

    # Form Fields
    fields = [
        ("Full Name", 0),
        ("Email", 1),
        ("Password", 2),
        ("Confirm Password", 3),
        ("Phone Number", 4)
    ]

    entries = []
    for field, row in fields:
        label = tk.Label(form_frame, text=field, font=("Arial", 10),
                         bg="#f5f5f5", anchor="w")
        label.grid(row=row, column=0, sticky="w", pady=(10, 0))

        entry = tk.Entry(form_frame, font=("Arial", 12),
                         highlightthickness=1, highlightbackground="#cccccc")
        entry.grid(row=row + 1, column=0, sticky="ew", pady=(0, 10), ipady=5)
        entries.append(entry)

    # Checkbox
    check_var = tk.IntVar()
    checkbox = tk.Checkbutton(form_frame, text="I agree to the Terms and Conditions",
                              variable=check_var, bg="#f5f5f5")
    checkbox.grid(row=6, column=0, sticky="w", pady=10)

    # Register Button
    register_btn = tk.Button(form_frame, text="REGISTER", bg="#4b8fe2",
                             fg="white", font=("Arial", 12, "bold"),
                             relief="flat", padx=20, pady=10)
    register_btn.grid(row=7, column=0, pady=20)

    # Footer
    footer_label = tk.Label(root, text="Already have an account? Sign in",
                            font=("Arial", 10), bg="#f5f5f5", fg="#4b8fe2")
    footer_label.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    create_registration_form()