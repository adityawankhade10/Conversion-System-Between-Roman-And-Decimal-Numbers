import tkinter as tk
from tkinter import messagebox


class Converter:
    def convert(self, input):
        raise NotImplementedError("Subclasses must implement abstract method")


class RomanToDecimalConverter(Converter):
    def convert(self, roman):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        decimal = 0
        prev_value = 0
        for numeral in reversed(roman):
            value = roman_numerals[numeral]
            if value < prev_value:
                decimal -= value
            else:
                decimal += value
            prev_value = value
        return decimal


class DecimalToRomanConverter(Converter):
    def convert(self, decimal):
        roman_numerals = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        roman = ''
        for value, numeral in roman_numerals.items():
            while decimal >= value:
                roman += numeral
                decimal -= value
        return roman


class ConversionSystem:
    def __init__(self):
        self._roman_to_decimal_converter = RomanToDecimalConverter()
        self._decimal_to_roman_converter = DecimalToRomanConverter()

    def roman_to_decimal(self, roman):
        return self._roman_to_decimal_converter.convert(roman)

    def decimal_to_roman(self, decimal):
        return self._decimal_to_roman_converter.convert(decimal)


def save_to_file(result):
    with open("conversion_results.txt", "a") as file:
        file.write(result + "\n")


def convert():
    input_value = entry.get()
    try:
        if input_type.get() == "Roman to Decimal":
            output = conversion_system.roman_to_decimal(input_value)
        elif input_type.get() == "Decimal to Roman":
            output = conversion_system.decimal_to_roman(int(input_value))
        result_label.config(text=str(output))

        # Save the result to a file
        save_to_file(f"Input: {input_value}, Output: {output}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")


root = tk.Tk()
root.title("Roman-Decimal Converter")

instruction_label = tk.Label(root, text="Enter the value:", font=("Arial", 12))
instruction_label.pack(pady=5)

entry = tk.Entry(root, width=20, font=("Arial", 12))
entry.pack(pady=5)

input_type = tk.StringVar()
input_type.set("Roman to Decimal")
radio_roman = tk.Radiobutton(root, text="Roman to Decimal", variable=input_type, value="Roman to Decimal",
                             font=("Arial", 12))
radio_roman.pack()
radio_decimal = tk.Radiobutton(root, text="Decimal to Roman", variable=input_type, value="Decimal to Roman",
                               font=("Arial", 12))
radio_decimal.pack()

convert_button = tk.Button(root, text="Convert", command=convert, font=("Arial", 12))
convert_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=5)

root.configure(background="#f0f0f0")
instruction_label.configure(background="#f0f0f0")
result_label.configure(background="#f0f0f0")

window_width = 300
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

conversion_system = ConversionSystem()

root.mainloop()
