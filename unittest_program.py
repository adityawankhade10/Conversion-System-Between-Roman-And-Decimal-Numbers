import unittest
from program import RomanToDecimalConverter
from program import DecimalToRomanConverter
from program import ConversionSystem

class TestRomanToDecimalConverter(unittest.TestCase):
    def setUp(self):
        self.converter = RomanToDecimalConverter()

    def test_single_numerals(self):
        self.assertEqual(self.converter.convert('I'), 1)
        self.assertEqual(self.converter.convert('V'), 5)
        self.assertEqual(self.converter.convert('X'), 10)

    def test_composite_numerals(self):
        self.assertEqual(self.converter.convert('III'), 3)
        self.assertEqual(self.converter.convert('IV'), 4)
        self.assertEqual(self.converter.convert('IX'), 9)
        self.assertEqual(self.converter.convert('LVIII'), 58)
        self.assertEqual(self.converter.convert('MCMXCIV'), 1994)

class TestDecimalToRomanConverter(unittest.TestCase):
    def setUp(self):
        self.converter = DecimalToRomanConverter()

    def test_single_values(self):
        self.assertEqual(self.converter.convert(1), 'I')
        self.assertEqual(self.converter.convert(5), 'V')
        self.assertEqual(self.converter.convert(10), 'X')

    def test_composite_values(self):
        self.assertEqual(self.converter.convert(3), 'III')
        self.assertEqual(self.converter.convert(4), 'IV')
        self.assertEqual(self.converter.convert(9), 'IX')
        self.assertEqual(self.converter.convert(58), 'LVIII')
        self.assertEqual(self.converter.convert(1994), 'MCMXCIV')

class TestConversionSystem(unittest.TestCase):
    def setUp(self):
        self.system = ConversionSystem()

    def test_roman_to_decimal(self):
        self.assertEqual(self.system.roman_to_decimal('III'), 3)
        self.assertEqual(self.system.roman_to_decimal('IV'), 4)
        self.assertEqual(self.system.roman_to_decimal('IX'), 9)
        self.assertEqual(self.system.roman_to_decimal('LVIII'), 58)
        self.assertEqual(self.system.roman_to_decimal('MCMXCIV'), 1994)

    def test_decimal_to_roman(self):
        self.assertEqual(self.system.decimal_to_roman(3), 'III')
        self.assertEqual(self.system.decimal_to_roman(4), 'IV')
        self.assertEqual(self.system.decimal_to_roman(9), 'IX')
        self.assertEqual(self.system.decimal_to_roman(58), 'LVIII')
        self.assertEqual(self.system.decimal_to_roman(1994), 'MCMXCIV')

if __name__ == '__main__':
    unittest.main()