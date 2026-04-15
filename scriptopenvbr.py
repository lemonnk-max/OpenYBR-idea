import json
import struct
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def convert_json_to_ybr():
    root = tk.Tk()
    root.withdraw() 
    
    input_path = filedialog.askopenfilename(
        title="Select JSON file to convert",
        filetypes=[("JSON files", "*.json")]
    )
    
   
    if not input_path:
        return

    try:
    
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        json_payload = json.dumps(data).encode('utf-8')
        payload_size = len(json_payload)

        magic_bytes = bytes([0x80, 0x59, 0x20, 0x42, 0x20, 0x52])

        output_path = os.path.splitext(input_path)[0] + ".ybr"

        with open(output_path, 'wb') as f:

            f.write(magic_bytes)
            f.write(struct.pack('<I', payload_size))
            f.write(json_payload)
            
        messagebox.showinfo("Done!", f"Binary file saved in the same directory:\n{output_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

if __name__ == "__main__":
    convert_json_to_ybr()