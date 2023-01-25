#!/usr/bin/python3
class Square:
	def __init__(_Square, size=0):
		_Square.__size = size
	
		if not isinstance(_Square.__size, int):	
			raise TypeError("size must be an integer")
		elif _Square.__size < 0:
			raise ValueError("size must be >= 0")
	def area(self):
		return self.__size * self.__size
	def size(self):
		return self.__size
	def size(self,value):
		if not isinstance(self.__value, int):
			raise TypeError("size must be an integer")
		elif self.__value < 0:
			raise ValueError("size must be >= 0")
