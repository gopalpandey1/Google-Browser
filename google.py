import tkinter as tk
from tkinter import messagebox
import webbrowser
from googlesearch import search


########################## function to search ##################################

def search_google(event=None):
    for widget in links_frame.winfo_children():
        widget.destroy()
    query = search_entry.get()
    if query:
        try:
            count = 0
            for url in search(query):
                if count >= 10:
                    break
                link_button = tk.Button(links_frame, text=url, command=lambda url=url: webbrowser.open(url),bg='lightpink',fg='blue')
                link_button.pack(fill="x")
                count += 1
        except Exception as e:
            error_label = tk.Label(links_frame, text="Error: " + str(e),bg='lightpink',fg='red')
            error_label.pack()
    else:
        error_label = tk.Label(links_frame, text="Please enter a search query",bg='lightpink',fg='red')
        error_label.pack()

#################################################################




########################### GUI window ##########################

root = tk.Tk()
root.geometry('1200x700')
root.title("Google Search")
root.config(bg='Lightpink')

root.resizable(False,False)

search_label = tk.Label(root, text="Google Search",font=('Arial',30),justify='center',fg='blue',bg='lightpink')
search_label.pack( padx=30, pady=10)

search_entry = tk.Entry(root, width=45,font=   ('Arial',12),justify='center',borderwidth=(1),bg='lightblue')
search_entry.pack(padx=10, pady=18,ipady=7)
search_entry.focus_set()

search_button = tk.Button(root, text="Search",font=('Arial',12),justify='center', command=search_google,bg='lightblue')
search_button.pack( padx=6, pady=10)

links_frame = tk.Frame(root,bg='lightpink')
links_frame.pack(  padx=10, pady=10,ipadx=40,ipady=50)

root.bind("<Return>",search_google)

root.mainloop()