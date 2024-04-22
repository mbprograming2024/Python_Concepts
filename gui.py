# import subprocess
# import tkinter as tk
# from tkinter import messagebox
#
#
# def submit_parameters():
#     ticket1 = entry_ticket1.get()
#     ticket2 = entry_ticket2.get()
#     user = entry_user.get()
#
#     # Construct the command string
#     command = f"python3 rest_bui.py -c jira.ini -v debug -l rest.log -s pass -t {ticket1} -x {ticket2} -k {user}"
#
#     # Print the command on the screen
#     print("Command to be executed:")
#     print(command)
#     try:
#         # Execute the command using subprocess
#         subprocess.Popen(command)
#         messagebox.showinfo("Script Running", "The script has been started.")
#     except Exception as e:
#         messagebox.showerror("Error", f"An error occurred: {str(e)}")
#
#
# # Create the main application window
# app = tk.Tk()
# app.title("Parameter Input")
#
# # Create labels and entry fields for each parameter
# label_ticket1 = tk.Label(app, text="Test_ID 1:")
# label_ticket1.grid(row=0, column=0)
# entry_ticket1 = tk.Entry(app)
# entry_ticket1.grid(row=0, column=1)
#
# label_ticket2 = tk.Label(app, text="Testexecution 2:")
# label_ticket2.grid(row=1, column=0)
# entry_ticket2 = tk.Entry(app)
# entry_ticket2.grid(row=1, column=1)
#
# label_user = tk.Label(app, text="Tester:")
# label_user.grid(row=2, column=0)
# entry_user = tk.Entry(app)
# entry_user.grid(row=2, column=1)
#
# # Create a submit button
# submit_button = tk.Button(app, text="Submit", command=submit_parameters)
# submit_button.grid(row=3, columnspan=2)
#
# # Run the application
# app.mainloop()
import tkinter as tk
from tkinter import messagebox
import subprocess


def submit_parameters():
    ticket1 = entry_ticket1.get()
    ticket2 = entry_ticket2.get()
    user = entry_user.get()

    # Construct the command to run rest_bui.py
    command = ["python3", "rest_bui.py", "-c", "jira.ini", "-v", "debug", "-l", "rest.log", "-s", "pass", "-t", ticket1,
               "-x", ticket2, "-k", user]

    try:
        # print(command)
        # Execute the command using subprocess and capture the output
        output = subprocess.check_output(command, universal_newlines=True)
        # Display the output in the text widget
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, output)
        messagebox.showinfo("Script Running", "The script has been started.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred: {e.output}")


# Create the main application window
app = tk.Tk()
app.title("Parameter Input")

# Create labels and entry fields for each parameter
label_ticket1 = tk.Label(app, text="Ticket 1:")
label_ticket1.grid(row=0, column=0)
entry_ticket1 = tk.Entry(app)
entry_ticket1.grid(row=0, column=1)

label_ticket2 = tk.Label(app, text="Ticket 2:")
label_ticket2.grid(row=1, column=0)
entry_ticket2 = tk.Entry(app)
entry_ticket2.grid(row=1, column=1)

label_user = tk.Label(app, text="User:")
label_user.grid(row=2, column=0)
entry_user = tk.Entry(app)
entry_user.grid(row=2, column=1)

# Create a submit button
submit_button = tk.Button(app, text="Submit", command=submit_parameters)
submit_button.grid(row=3, columnspan=2)

# Create a text widget to display output
text_output = tk.Text(app, height=15, width=50)
text_output.grid(row=4, columnspan=2)

# Run the application
app.mainloop()
