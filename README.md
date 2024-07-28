# LockPDF-Pro
LockPDF Pro is a simple, lightweight software for encrypting and decrypting PDF files without altering the original copy. Operating entirely offline, it ensures document security from online threats. With a user-friendly interface, it allows easy addition or removal of passwords, maintaining the integrity and original content of your PDFs.

## Features

- **RC4 128-bit Encryption:** Secure your PDF files using robust encryption methods.
- **User-Friendly Interface:** Easy to navigate and use, making PDF security accessible to everyone.
- **Browse PDF:** Quickly browse and select PDF files for encryption or decryption.
- **Password Protection:** Set and manage passwords for your PDF files effortlessly.
- **Encrypt PDF:** Easily encrypt your PDF files to protect sensitive information.
- **Decrypt PDF:** Decrypt your PDF files when you need access.
- **Creates Encrypted/Decrypted Copies:** Ensures the original file remains untouched, and creates an encrypted or decrypted copy based on the selected operation: When encrypting, `_E` is added at the end of the file name, When decrypting, `_D` is added at the end of the file name.
- **Keyboard Shortcuts:**
  - **Alt + s:** Browse PDF
  - **Alt + t:** Focus password Textbox
  - **Alt + e:** Encrypt PDF
  - **Alt + d:** Decrypt PDF

## User Interface

LockPDF Pro V1.0 has a simple and intuitive interface:

- **Browse PDF:** Click this button to browse and select a PDF file.
- **Decrypt PDF:** Click this button to create a decrypted copy of the selected PDF file.
- **Encrypt PDF:** Click this button to create an encrypted copy of the selected PDF file.
- The progress bar at the top indicates the status of the encryption or decryption process.
- A text box in the middle allows you to input or focus on the password required for encryption or decryption.
- A message at the top displays the current status (e.g., "Finished!", "Saving Encrypted Copy...").

## Important Note

**Attention:** LockPDF Pro V1.0 does not preserve bookmarks or the table of contents when processing PDF files.

  
### Acknowledgment:
LockPDF Pro v1.0 incorporates the PyPDF2 library for PDF encryption and decryption,
and Tkinter, a standard GUI toolkit in Python, for creating the graphical user 
interface. We extend our gratitude to the developers and contributors of PyPDF2 
and Tkinter for their valuable contributions to the open-source community.
