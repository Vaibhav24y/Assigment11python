import tkinter as tk
import webbrowser
e = tk.Tk()
e.title("Enquiry ")
label = tk.Label(e, text="Course:")
entry = tk.Entry(e)
s_label = tk.Label(e, text="Where did you get information about us?")
s_var = tk.StringVar(e)
s_options = ["YouTube","Instagram","udemy","Other"]
s_dropdown = tk.OptionMenu(e, s_var, *s_options)
def formm():
    course = entry.get()
    source = s_var.get()
    if source == "YouTube":
        url = "https://example.com/faq/youtube"
    elif source == "Instagram":
        url = "https://example.com/faq/instagram"
    elif source == "udemy":
        url = "https://www.udemy.com/faq"
    else:
        url = "https://example.com/faq"
    webbrowser.open(url)
button = tk.Button(e, text="Search", command=formm,font=("Times New Roman",30))
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
s_label.grid(row=1, column=0)
s_dropdown.grid(row=1, column=1)
button.grid(row=2, column=0)
e.mainloop()