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

#### Polymorphism

Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface. In my program:
The 'Converter class' defines a convert method which is implemented differently in 'RomanToDecimalConverter' and 'DecimalToRomanConverter'.

![image](https://github.com/adityawankhade10/Conversion-System-Between-Roman-And-Decimal-Numbers/assets/169479302/23cbefa9-440a-4fe4-9ac7-0888d16d9080)

#### Abstraction

Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object. In this application:
The 'Converter class' abstracts the conversion logic by providing a common interface for conversion operations.

![image](https://github.com/adityawankhade10/Conversion-System-Between-Roman-And-Decimal-Numbers/assets/169479302/e77c5a7d-b0f3-4805-8561-d8ddd4139946)


#### Inheritance

Inheritance allows one class to inherit attributes and methods from another class. In our application:
'RomanToDecimalConverter' and 'DecimalToRomanConverter' inherit from the 'Converter class'.

![image](https://github.com/adityawankhade10/Conversion-System-Between-Roman-And-Decimal-Numbers/assets/169479302/8acde5c1-1686-4d52-ab2a-0f18cb3db8fb)

#### Encapsulation

Encapsulation is the concept of wrapping the data and methods that operate on the data within a single unit, often as a class, and restricting access to some of the object's components. In our application:
The conversion logic and data (e.g., Roman numeral values) are encapsulated within their respective classes.

![image](https://github.com/adityawankhade10/Conversion-System-Between-Roman-And-Decimal-Numbers/assets/169479302/e24b5f1e-6a28-4146-9759-3ea4e011967f)


#### Factory Pattern

The Factory Pattern is used in scenarios where we need different types of objects with varying behaviors and characteristics. In our application, the ConversionSystem class acts as a factory for creating the appropriate converter object based on the conversion type.

![image](https://github.com/adityawankhade10/Conversion-System-Between-Roman-And-Decimal-Numbers/assets/169479302/d1cd8104-5c4a-46e2-9626-85d14736a64d)

How it works: The ConversionSystem initializes instances of RomanToDecimalConverter and DecimalToRomanConverter and provides methods to access these converters.

Why it is suitable: This pattern is suitable here as it centralizes the creation of converter objects and provides a clean interface for performing conversions.

#### Strategy Pattern

The Strategy Pattern is used to define a family of algorithms, encapsulate each one, and make them interchangeable. It allows the algorithm to vary independently from clients that use it. In your application, the different conversion strategies (Roman to Decimal and Decimal to Roman) are encapsulated within separate classes that implement a common interface (Converter).

![image](https://github.com/adityawankhade10/Conversion-System-Between-Roman-And-Decimal-Numbers/assets/169479302/3f8d1b06-6f90-41ce-b2a0-3b139119cee7)

How it works: The Converter class provides a common interface (convert method) for different conversion strategies. The RomanToDecimalConverter and DecimalToRomanConverter classes implement this interface with specific conversion algorithms.

Why it is suitable: This pattern is suitable because it encapsulates the different conversion algorithms, allowing them to be used interchangeably without changing the client code.


## Results and Summary

#### Results

The application successfully converts Roman numerals to decimals and decimals to Roman numerals. Each result is displayed on the interface and saved to a text file.

#### Conclusions

The Roman-Decimal Converter application effectively demonstrates the use of object-oriented programming principles and design patterns. It is modular, reusable, and easy to extend.

#### How to extend the application?

To extend the application, you can:

- Add more validation to handle incorrect inputs more gracefully.

- Implement additional conversion systems, such as binary or hexadecimal.

- Enhance the user interface with more features and better aesthetics.

- Add functionality to clear the input and output fields.

- Provide an option to view the history of conversions from the conversion_results.txt file directly within the application.
















