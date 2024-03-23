import tkinter as tk
import tkinter.messagebox
import time

def show_reminder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Display reminder dialog
    tkinter.messagebox.showinfo("Reminder", "It's time to brush your teeth!")
    print("Alarm set for every ten minutes. Press Ctrl+C to exit.")

    # Destroy the hidden root window to avoid tkinter-related issues
    root.destroy()

def main():
    while True:
        show_reminder()
        # Wait for 10 minutes
        time.sleep(10 * 60)

if __name__ == "__main__":
    main()
