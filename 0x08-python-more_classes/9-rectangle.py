#!/usr/bin/python3

"""Definition of class object ``Rectangle``"""


class Rectangle:
    """Class representing a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with width and height attributes.

        Args:
            width (int): the width of the rectangle. Defaults to 0.
            height (int): the height of the rectangle. Defaults to 0.
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns private instance attribute ``width``"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets private instance attribute ``width``

        Args:
            value (int): the value with which to set ``width``

        Raises:
            TypeError: if ``value`` is a non-integer
            ValueError: if ``value`` is negative
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Returns private instance attribute ``height``"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets private instance attribute ``height``

        Args:
            value (int): the value with which to set ``height``

        Raises:
            TypeError: if ``value`` is a non-integer
            ValueError: if ``value`` is negative
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns string representation of defined rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ''
        string = ''
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i < (self.__height - 1):
                string += '\n'
        return string

    def __repr__(self):
        """Returns repr representation of defined rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two instances of class Rectangle by area

        Returns: The bigger of the two, or ``rect_1`` if both are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        a, b = rect_1.area(), rect_2.area()
        if a >= b:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns new instance of Rectangle with uniform dimensions"""
        new = cls(size, size)
        return new
