import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

# Known malware hashes (example MD5 for Ramnit.a and Ramnit.b)
known_malware_hashes = {
    "Ramnit.a": "5f4b3eaff6b42120e004adf01d33dff2",
    "Ramnit.b": "3f3e15e2262fa1f7c107d0c92b3ad06e",
}

def calculate_md5(file_path):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def scan_file(file_path):
    """Scan a file for known malware hashes."""
    file_hash = calculate_md5(file_path)
    if file_hash is None:
        return "Error scanning file."

    # Check if the file hash matches any known malware
    for name, hash_value in known_malware_hashes.items():
        if file_hash == hash_value:
            return f"Warning: {name} detected!"
    
    return "No malware detected."

def browse_file():
    """Open file dialog to select a file to scan."""
    file_path = filedialog.askopenfilename(title="Select a file to scan")
    if file_path:
        result = scan_file(file_path)
        result_label.config(text=result)

# Create the main window
window = tk.Tk()
window.title("ELTechnical Antivirus")
window.geometry("400x200")

# Create UI elements
browse_button = tk.Button(window, text="Browse File", command=browse_file)
browse_button.pack(pady=20)

result_label = tk.Label(window, text="No file scanned yet.", wraplength=350)
result_label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
