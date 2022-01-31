import tkinter as tk

window = tk.Tk()
window.title("Miles to Kilometers")

miles_entry = tk.Entry()
miles_entry.grid(row=0, column=1, padx=10, pady=10)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2, padx=10, pady=10)

is_equal_label = tk.Label(text="=")
is_equal_label.grid(row=1, column=0, padx=10, pady=10)

kilometers_result_label = tk.Label(text=" ")
kilometers_result_label.grid(row=1, column=1, padx=10, pady=10)

kilometers_label = tk.Label(text="Kilometers")
kilometers_label.grid(row=1, column=2, padx=10, pady=10)

calculate_button = tk.Button(text="Calculate", command=lambda: convert_miles_to_kilometers())
calculate_button.grid(row=2, column=1, padx=10, pady=10)


def convert_miles_to_kilometers():
    miles = float(miles_entry.get())
    kilometers = miles * 1.60934
    kilometers_result_label.config(text=round(kilometers, 2))


window.mainloop()
