import tkinter as tk

def meters_to_feet(meters):
    feet = meters * 3.28084
    return feet

def meters_to_miles(meters):
    miles = meters * 0.000621371
    return miles

def feet_to_meters(feet):
    meters = feet / 3.28084
    return meters

def feet_to_miles(feet):
    miles = feet / 5280.0
    return miles

def miles_to_meters(miles):
    meters = miles / 0.000621371
    return meters

def miles_to_feet(miles):
    feet = miles * 5280.0
    return feet

def convert():
    choice = choice_var.get()

    if choice == 1:
        meters = float(entry_input.get())
        feet = meters_to_feet(meters)
        result_label.config(text=f"{meters} meters is equal to {feet} feet.")
    elif choice == 2:
        meters = float(entry_input.get())
        miles = meters_to_miles(meters)
        result_label.config(text=f"{meters} meters is equal to {miles} miles.")
    elif choice == 3:
        feet = float(entry_input.get())
        meters = feet_to_meters(feet)
        result_label.config(text=f"{feet} feet is equal to {meters} meters.")
    elif choice == 4:
        feet = float(entry_input.get())
        miles = feet_to_miles(feet)
        result_label.config(text=f"{feet} feet is equal to {miles} miles.")
    elif choice == 5:
        miles = float(entry_input.get())
        meters = miles_to_meters(miles)
        result_label.config(text=f"{miles} miles is equal to {meters} meters.")
    elif choice == 6:
        miles = float(entry_input.get())
        feet = miles_to_feet(miles)
        result_label.config(text=f"{miles} miles is equal to {feet} feet.")
    else:
        result_label.config(text="Invalid choice. Please select a valid option (1/2/3/4/5/6).")

root = tk.Tk()
root.title("Unit Converter - Length")
input_label = tk.Label(root, text="Enter length:")
input_label.pack()
entry_input = tk.Entry(root)
entry_input.pack()
choice_label = tk.Label(root, text="Select conversion type:")
choice_label.pack()
choice_var = tk.IntVar()
choices = [("Meters to Feet", 1), ("Meters to Miles", 2),
           ("Feet to Meters", 3), ("Feet to Miles", 4),
           ("Miles to Meters", 5), ("Miles to Feet", 6)]

for text, value in choices:
    radio_button = tk.Radiobutton(root, text=text, variable=choice_var, value=value)
    radio_button.pack()
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
