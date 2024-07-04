import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DR64 - PDF MERGER")

        self.file1_path = ""
        self.file2_path = ""

        self.create_widgets()

    def create_widgets(self):
        # Create file selection buttons
        self.select_file1_button = tk.Button(self.root, text="Select PDF 1", command=self.select_file1)
        self.select_file1_button.pack(pady=5)

        self.file1_status = tk.Label(self.root, text="", fg="green")
        self.file1_status.pack()

        self.select_file2_button = tk.Button(self.root, text="Select PDF 2", command=self.select_file2)
        self.select_file2_button.pack(pady=5)

        self.file2_status = tk.Label(self.root, text="", fg="green")
        self.file2_status.pack()

        # Create merge button
        self.merge_button = tk.Button(self.root, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack(pady=20)

    def select_file1(self):
        self.file1_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.file1_path:
            filename = os.path.basename(self.file1_path)
            self.file1_status.config(text=f"✔ {filename} selected")

    def select_file2(self):
        self.file2_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.file2_path:
            filename = os.path.basename(self.file2_path)
            self.file2_status.config(text=f"✔ {filename} selected")

    def merge_pdfs(self):
        if not self.file1_path or not self.file2_path:
            messagebox.showwarning("Warning", "Please select both PDF files.")
            return

        merger = PdfMerger()
        merger.append(self.file1_path)
        merger.append(self.file2_path)

        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_path:
            merger.write(output_path)
            merger.close()
            messagebox.showinfo("Success", f"Merged PDF saved as: {output_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
