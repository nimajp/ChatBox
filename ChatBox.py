import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Client setup
SERVER_IP = "192.168.113.62"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

# Function to send messages continuously
def send_message(event=None):
    message = message_entry.get().strip()
    if message:
        try:
            client.send(message.encode("utf-8"))
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, f"You: {message}\n", "user_message")
            chat_box.config(state=tk.DISABLED)
            chat_box.yview(tk.END)  # Auto scroll
            message_entry.delete(0, tk.END)  # Clear input after sending
        except:
            chat_box.insert(tk.END, "Error sending message!\n", "error_message")

# Function to receive messages in a loop
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message:
                chat_box.config(state=tk.NORMAL)
                chat_box.insert(tk.END, f"Friend: {message}\n", "friend_message")
                chat_box.config(state=tk.DISABLED)
                chat_box.yview(tk.END)  # Auto scroll
        except:
            break  # Stop the loop if the connection is closed

# GUI setup
root = tk.Tk()
root.title("Chat Box")

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
chat_box.pack(padx=10, pady=10)

message_frame = tk.Frame(root)
message_frame.pack(pady=5)

message_entry = tk.Entry(message_frame, width=40)
message_entry.pack(side=tk.LEFT, padx=5)
message_entry.bind("<Return>", send_message)  # Press "Enter" to send

send_button = tk.Button(message_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=5)

# Adding styles
chat_box.tag_configure("user_message", foreground="blue")
chat_box.tag_configure("friend_message", foreground="green")
chat_box.tag_configure("error_message", foreground="red")

# Start receiving messages in a separate thread
threading.Thread(target=receive_messages, daemon=True).start()

root.mainloop()
