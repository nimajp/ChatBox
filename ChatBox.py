import tkinter as tk

# Function to get text and display it
def show_text():
    entered_text = text_box.get("1.0", tk.END).strip()
    if entered_text:
        chat_label.config(text=entered_text)
        text_box.delete("1.0", tk.END)  # Clear the text box after sending

# Create main window
root = tk.Tk()
root.title("Simple ChatBox UI")
root.geometry("300x250")

# Label to display the chat message
chat_label = tk.Label(root, text="", fg="black", wraplength=250, justify="left")
chat_label.pack(pady=10, padx=10, anchor="w")

# Frame to hold text box and button
input_frame = tk.Frame(root)
input_frame.pack(side="bottom", fill="x", pady=10)

# Text Box for input
text_box = tk.Text(input_frame, height=2, width=25)
text_box.pack(side="left", padx=5, expand=True, fill="both")

# Send Button
button = tk.Button(input_frame, text="Send", command=show_text)
button.pack(side="right", padx=5)

# Run the application
root.mainloop()
