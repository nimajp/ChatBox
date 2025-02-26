import socket
import tkinter as tk
from tkinter import scrolledtext

# Create socket for client and connect to the server
# Replace 'Your_Public_IP' with the actual public IP of the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('Server IPv4', 12345))  # Server IP address and port

# Function to send message to the server
def send_message():
    message = entry.get()  # Get message from text entry
    if message:
        chat_box.config(state=tk.NORMAL)  # Enable chat box to add text
        chat_box.insert(tk.END, "You: " + message + '\n')  # Add message to chat box
        entry.delete(0, tk.END)  # Clear text entry after sending message
        chat_box.config(state=tk.DISABLED)  # Disable chat box to prevent manual typing

        # Send message to the server
        client.send(message.encode())

        # Receive the server's response
        response = client.recv(1024).decode()
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "Server: " + response + '\n')  # Show server response
        chat_box.config(state=tk.DISABLED)

        chat_box.yview(tk.END)  # Auto-scroll to the latest message

# Create main window for GUI
root = tk.Tk()
root.title("Chat with Server")

# Create chat box (ScrolledText for scrollable area)
chat_box = scrolledtext.ScrolledText(root, width=50, height=15, wrap=tk.WORD, state=tk.DISABLED)
chat_box.pack(pady=10)

# Create text entry for typing messages
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Create button to send the message
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Start the GUI loop
root.mainloop()

# Close client connection after exiting
client.close()
