import tkinter as tk
from tkinter import ttk, messagebox
import socket
import threading

class PortScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Port Scanner")
        self.root.geometry("500x400")

        # Target input
        ttk.Label(root, text="Target IP or Hostname:").pack(pady=5)
        self.target_entry = ttk.Entry(root, width=40)
        self.target_entry.pack()

        # Port range input
        range_frame = ttk.Frame(root)
        range_frame.pack(pady=10)

        ttk.Label(range_frame, text="Start Port:").grid(row=0, column=0)
        self.start_port = ttk.Entry(range_frame, width=10)
        self.start_port.insert(0, "1")
        self.start_port.grid(row=0, column=1, padx=5)

        ttk.Label(range_frame, text="End Port:").grid(row=0, column=2)
        self.end_port = ttk.Entry(range_frame, width=10)
        self.end_port.insert(0, "1024")
        self.end_port.grid(row=0, column=3)

        # Scan button
        self.scan_button = ttk.Button(root, text="Start Scan", command=self.start_scan)
        self.scan_button.pack(pady=10)

        # Result area
        self.tree = ttk.Treeview(root, columns=("Port", "Status"), show='headings')
        self.tree.heading("Port", text="Port")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def scan_port(self, target, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target, port))
                if result == 0:
                    self.tree.insert("", "end", values=(port, "Open"))
        except:
            pass

    def start_scan(self):
        self.tree.delete(*self.tree.get_children())  # Clear results
        target = self.target_entry.get().strip()
        try:
            target_ip = socket.gethostbyname(target)
        except socket.gaierror:
            messagebox.showerror("Invalid Host", "Could not resolve host.")
            return

        try:
            start = int(self.start_port.get())
            end = int(self.end_port.get())
        except ValueError:
            messagebox.showerror("Invalid Port", "Port range must be numeric.")
            return

        # Threaded scanning
        for port in range(start, end + 1):
            thread = threading.Thread(target=self.scan_port, args=(target_ip, port))
            thread.start()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PortScannerApp(root)
    root.mainloop()
