# Conversion-System-Between-Roman-And-Decimal-Numbers

## Introduction

#### About

The Roman-Decimal Converter is a simple web application built using Python and the Tkinter library. It allows users to convert Roman numerals to decimal (integer) values and vice versa. This application leverages object-oriented programming principles to achieve modular and reusable code.

#### How to run/use the program

Ensure you have Python installed on your system.
Save the provided Python script (converter.py) in your working directory.
Open a terminal or command prompt.
Navigate to the directory where the script is saved.
Run the command: python converter.py
The application window will open, allowing you to input values and perform conversions.

## Functional overview and code analysis

The 

*#### Polymorphism

Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface. In my program:
The 'Converter class' defines a convert method which is implemented differently in 'RomanToDecimalConverter' and 'DecimalToRomanConverter'.

![image](https://github.com/adityawankhade10/Conversion-System-Between-Roman-And-Decimal-Numbers/assets/169479302/23cbefa9-440a-4fe4-9ac7-0888d16d9080)

*#### Abstraction
Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object. In this application:
The 'Converter class' abstracts the conversion logic by providing a common interface for conversion operations.

![image](https://github.com/adityawankhade10/Conversion-System-Between-Roman-And-Decimal-Numbers/assets/169479302/e77c5a7d-b0f3-4805-8561-d8ddd4139946)


*#### Inheritance
Inheritance allows one class to inherit attributes and methods from another class. In our application:
'RomanToDecimalConverter' and 'DecimalToRomanConverter' inherit from the 'Converter class'.

![image](https://github.com/adityawankhade10/Conversion-System-Between-Roman-And-Decimal-Numbers/assets/169479302/8acde5c1-1686-4d52-ab2a-0f18cb3db8fb)

*#### Encapsulation
Encapsulation is the concept of wrapping the data and methods that operate on the data within a single unit, often as a class, and restricting access to some of the object's components. In our application:
The conversion logic and data (e.g., Roman numeral values) are encapsulated within their respective classes.

![image](https://github.com/adityawankhade10/Conversion-System-Between-Roman-And-Decimal-Numbers/assets/169479302/e24b5f1e-6a28-4146-9759-3ea4e011967f)






















