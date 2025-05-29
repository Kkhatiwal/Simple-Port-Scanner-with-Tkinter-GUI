import socket
import tkinter as tk
from tkinter import scrolledtext

def scan_ports():
    target = ip_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())
    
    output_box.delete('1.0', tk.END)  # Clear previous results
    output_box.insert(tk.END, f"Scanning {target} from port {start_port} to {end_port}...\n\n")
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            output_box.insert(tk.END, f"Port {port}: OPEN\n")
        sock.close()

# Create GUI
root = tk.Tk()
root.title("Simple Port Scanner")
root.geometry("400x400")

# IP Address input
tk.Label(root, text="Target IP Address:").pack()
ip_entry = tk.Entry(root)
ip_entry.pack()

# Start Port input
tk.Label(root, text="Start Port:").pack()
start_port_entry = tk.Entry(root)
start_port_entry.pack()

# End Port input
tk.Label(root, text="End Port:").pack()
end_port_entry = tk.Entry(root)
end_port_entry.pack()

# Scan button
scan_button = tk.Button(root, text="Start Scan", command=scan_ports)
scan_button.pack(pady=10)

# Output box
output_box = scrolledtext.ScrolledText(root, width=50, height=15)
output_box.pack(pady=10)

root.mainloop()
