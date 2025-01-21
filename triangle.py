import math

def triangleArea(a:float, b:float, c:float):
	"""Calculate triangle area using Heron's formula.

	Args:
		a (float): One side of the triangle.
		b (float): One side of the triangle.
		c (float): One side of the triangle.

	Returns:
		float: The area of the triangle.
	"""
	# Check if input is of type float
	if not (isinstance(a, float) and isinstance(b, float) and isinstance(c, float)):
		raise TypeError("Input must be of type float.")
	if a < 0 or b < 0 or c < 0:
		raise ValueError("Input must be a positive float.")
	s = (a + b + c) / 2
	return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def angle_alpha(a:float, b:float, beta:float):
	"""Calculate the angle alpha of a triangle using the law of sines.

	Args:
		a (float): One side of the triangle.
		b (float): One side of the triangle.
		beta (float): The angle beta of the triangle.

	Returns:
		float: The angle alpha of the triangle.
	"""
	# Check if input is of type float
	if not (isinstance(a, float) and isinstance(b, float) and isinstance(beta, float)):
		raise TypeError("Input must be of type float.")
	if a < 0 or b < 0 or beta < 0:
		raise ValueError("Input must be a positive float.")
	if beta == 0:
		raise ZeroDivisionError("float division by zero")
	return math.degrees(math.asin((a * math.sin(math.radians(beta))) / b))
