import tkinter as tk
from datetime import datetime

categories = ["Food", "Travel", "Grocery", "Rent", "Daily Expense", "Medical", "Misc.", "Other"]
expenses = {}

def add_expense():
    desc = desc_entry.get()
    amount = float(amount_entry.get())
    category = category_var.get()
    date = date_entry.get()
    if date == "":
        date = datetime.today().strftime('%Y-%m-%d')
    expenses.setdefault(category, {})
    expenses[category].setdefault(date, {})
    expenses[category][date][desc] = amount
    status_label.config(text="Expense added.")
    desc_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

def view_expenses():
    if len(expenses) == 0:
        status_label.config(text="No expenses to show.")
    else:
        total = 0
        expense_list.delete(0, tk.END)
        for category, dates in expenses.items():
            expense_list.insert(tk.END, "- {}:".format(category))
            for date, items in dates.items():
                expense_list.insert(tk.END, "    {}:".format(date))
                for desc, amount in items.items():
                    expense_list.insert(tk.END, "        {} (₹{:.2f})".format(desc, amount))
                    total += amount
        status_label.config(text="Total expenses: ₹{:.2f}".format(total))

def delete_expense():
    desc = desc_entry.get()
    category = category_var.get()
    date = date_entry.get()
    if date == "":
        date = datetime.today().strftime('%d-%m-%Y')
    if category in expenses and date in expenses[category] and desc in expenses[category][date]:
        del expenses[category][date][desc]
        status_label.config(text="Expense deleted.")
        desc_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
    else:
        status_label.config(text="Expense not found.")
        desc_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("1000x800")
root.config(bg="#565756")

button_frame = tk.Frame(root)

desc_label = tk.Label(root, text="Description:",)
desc_entry = tk.Entry(root)
amount_label = tk.Label(root, text="Amount:")
amount_entry = tk.Entry(root)
category_label = tk.Label(root, text="Category:")
category_var = tk.StringVar(value=categories[0])
category_menu = tk.OptionMenu(root, category_var, *categories)
date_label = tk.Label(root, text="Date (DD-MM-YY):")
date_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Expense", command=add_expense)
view_button = tk.Button(root, text="View Expenses", command=view_expenses)
delete_button = tk.Button(root, text="Delete Expense", command=delete_expense)
expense_list = tk.Listbox(root, width=40)
status_label = tk.Label(root, text="")
desc_label.config(bg="#565756",fg="#FFFFFF")
desc_entry.config(bg="#565756",fg="#FFFFFF")
amount_label.config(bg="#565756",fg="#FFFFFF")
amount_entry.config(bg="#565756",fg="#FFFFFF")
category_label.config(bg="#565756",fg="#FFFFFF")
category_menu.config(bg="#565756",fg="#FFFFFF")
date_label.config(bg="#565756",fg="#FFFFFF")
date_entry.config(bg="#565756",fg="#FFFFFF")
add_button.config(bg="#565756",fg="#FFFFFF")
view_button.config(bg="#565756",fg="#FFFFFF")
delete_button.config(bg="#565756",fg="#FFFFFF")
expense_list.config(bg="#565756",fg="#FFFFFF")
status_label.config(bg="#565756",fg="#FFFFFF")


desc_label.pack()
desc_entry.pack()
amount_label.pack()
amount_entry.pack()
category_label.pack()
category_menu.pack()
date_label.pack()
date_entry.pack()
add_button.place(relx=0.3, rely=0.5, anchor="center")
view_button.place(relx=0.5, rely=0.5, anchor="center")
delete_button.place(relx=0.7, rely=0.5, anchor="center")
expense_list.pack(anchor="center")
status_label.pack(anchor="center")

root.mainloop()