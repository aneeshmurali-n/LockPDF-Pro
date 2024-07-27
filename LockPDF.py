# Copyright (c) 2024 Aneesh Murali Nariyampully [AMN]
import threading  # Threading module to run the PDF encryption and decryption in separate threads
from tkinter import *  # Import all the widgets and functions from the tkinter module to create the GUI
from tkinter import filedialog  # The filedialog module from the tkinter module to allow the user to select a PDF file
from tkinter.ttk import Progressbar  # Progressbar widget from the tkinter.ttk module for the progressbar
from PyPDF2 import PdfReader  # PdfReader class from the PyPDF2 module to read the contents of the PDF file
from PyPDF2 import PdfWriter  # PdfWriter class from the PyPDF2 module to write the extracted text to a new PDF file

pdf = None  # global variables
title = None

window = Tk()  # Creates a new Tk window
window.title("LockPDF Pro V1.0")  # Set the window title
window.geometry("600x130")  # Set the window dimension (width x height)
window.resizable(False, False)  # Make the window non-resizable
window.config(bg='#d5d5d5')  # set the window background color

window.iconbitmap(r'By_AMN_Ciiads.ico')  # Set the window icon


def destroy():  # Function to close the window when the user clicks the "X" button
    window.destroy()


window.wm_protocol("WM_DELETE_WINDOW", destroy)  # When the user clicks the "X" button call destroy Function


# function definition for browse pdf file
def browse_pdf():
    global pdf, title
    label["text"] = "Enter Your Password"  # Set the text of the label to "Enter Your Password"
    progressbar["value"] = 0  # Set the progressbar value to zero
    pdf = filedialog.askopenfile(  # Open a file dialog to browse the PDF file
        mode='rb', title="Browse Your Pdf File :)",
        filetype=[("Pdf File", "*.pdf")]
    )
    if pdf is None:  # If didn't browse the file,  and exit the function
        browse_pdf_button["text"] = "Browse PDF"  # Reset the browse button text to "Browse PDF"
        label["text"] = "Enter Your Password"  # Reset the label text to "Enter Your Password"
    else:
        browse_pdf_button["text"] = "PDF Browsed"  # Set the browse button text to "PDF Browsed"
        title = pdf.name  # get name of the pdf file path as string
        size = len(title)  # get length of the string
        title = title[:size - 4]  # remove last 4 char to remove ".pdf" & store that string to title variable


def encrypt_save():
    global pdf, title
    if browse_pdf_button["text"] == "PDF Browsed":
        out = PdfWriter()  # Creating a PdfWriter object to write the encrypted PDF.
        file = PdfReader(pdf)  # Creating a PdfReader object to read the original PDF file.
        if not file.is_encrypted or file.decrypt(''):  # check the file is encrypted or blank pswd
            label["text"] = "Encrypting..."
            num = len(file.pages)  # Getting the number of pages in the original PDF.
            for idx in range(num):  # Iterate through every page of the original file and add it to our new file.
                page = file.pages[idx]  # Get the page at index idx
                out.add_page(page)  # Add it to the output file
                update_progress(idx / num * 90)  # calling update_progress function
            password = textbox.get(1.0, "end-1c")  # Retrieving the password entered by the user in the text box.
            out.encrypt(password,
                        use_128bit=True)  # Encrypt the new file with the entered password 128 bit RC4 encryption
            with open(title + "_E.pdf",
                      "wb") as f:  # opening a new file f with the og name + "_E"
                label["text"] = "Saving Encrypted Copy..."
                out.write(f)  # Write our encrypted PDF to this file
            progressbar["value"] = 100
            label["text"] = "Finished!"
            browse_pdf_button["text"] = "Browse PDF"
            f.close()
        else:
            label["text"] = "It's an Encrypted PDF"
    else:
        label["text"] = "Please Browse PDF"


def first_thread():
    t1 = threading.Thread(target=encrypt_save)
    t1.daemon = True
    t1.start()


def second_thread():
    t2 = threading.Thread(target=decrypt_pdf)
    t2.daemon = True
    t2.start()


def decrypt_pdf():
    global pdf, title
    if browse_pdf_button["text"] == "PDF Browsed":
        out = PdfWriter()  # Creating a PdfWriter object to write the encrypted PDF.
        file = PdfReader(pdf)  # Creating a PdfReader object to read the original PDF file.
        password = textbox.get(1.0, "end-1c")  # Get the password entered by the user in the text box.
        if file.is_encrypted:  # check the file is encrypted
            label["text"] = "Decrypting..."
            try:
                file.decrypt(password)  # decrypt file with the entered password
                num = len(file.pages)  # Getting the number of pages in the original PDF.
                for idx in range(num):  # Iterate through every page of the original file and add it to our new file.
                    page = file.pages[idx]  # Get the page at index idx
                    out.add_page(page)  # Add it to the output file
                    update_progress(idx / num * 90)  # calling update_progress function
                with open(title + "_D.pdf", "wb") as f:  # opening a new file f with the og name + "_D"
                    label["text"] = "Saving Decrypted Copy..."
                    out.write(f)  # Write our encrypted PDF to this file
                progressbar["value"] = 100
                label["text"] = "Finished!"
                browse_pdf_button["text"] = "Browse PDF"
            except Exception as e:
                label["text"] = "Incorrect Password, " + f"{str(e)}"
        else:
            label["text"] = "It's not an Encrypted PDF"
    else:
        label["text"] = "Please Browse PDF"


# function to update the progress bar
def update_progress(progress):
    progressbar["value"] = progress
    window.update_idletasks()


def on_enter(event):  # When enter key is pressed
    return "break"


def on_alt_e(event):  # When Alt+e key is pressed call function encrypt_save()
    encrypt_save()


def on_alt_d(event):  # When Alt+d key is pressed call function decrypt_pdf()
    decrypt_pdf()


def on_alt_s(event):  # When Alt+s key is pressed call function browse_pdf()
    browse_pdf()


def on_alt_t(event):  # When Alt+t key is pressed call function to select textbox
    textbox.focus_set()


# Bind the Alt+e key event
window.bind("<Alt-e>", on_alt_e)

# Bind the Alt+d key event
window.bind("<Alt-d>", on_alt_d)

# Bind the Alt+s key event
window.bind("<Alt-s>", on_alt_s)

# Bind the Alt-t key event
window.bind("<Alt-t>", on_alt_t)

# Create a Progressbar
progressbar = Progressbar(window, length=600, mode='determinate')
progressbar.place(relx=0.5, rely=0.05, anchor="center")

# create a Label
label = Label(window, text="Enter Your Password", height=1, width=80, bg='#d5d5d5')
label.place(relx=0.5, rely=0.25, anchor="center")

# textbox
textbox = Text(window, height=1, width=72, bg='white', fg='black', bd='0', wrap='word', font=("Helvetica", 10))
textbox.place(relx=0.5, rely=0.45, anchor="center")
textbox.bind('<Return>', on_enter)  # Enter key is pressed while typing call on_enter to prevent new line

# browse pfd button
browse_pdf_button = Button(window, text="Browse PDF", height=1, width=20, bg='#00568e', fg='white', command=browse_pdf)
browse_pdf_button.place(relx=0.2, rely=0.7, anchor="center")

# decrypt PDF button
decrypt_pdf_button = Button(window, text="Decrypt PDF", height=1, width=20, bg='#00568e', fg='white', command=second_thread)
decrypt_pdf_button.place(relx=0.5, rely=0.7, anchor="center")

# encrypt and save pdf button
encrypt_save_button = Button(window, text="Encrypt PDF", height=1, width=20, bg='#00568e', fg='white', command=first_thread)
encrypt_save_button.place(relx=0.8, rely=0.7, anchor="center")

window.mainloop()
