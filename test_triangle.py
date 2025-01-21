from triangle import triangleArea, angle_alpha
from math import isclose

def test_triangleArea():
	# Regular cases
	assert triangleArea(3.0, 4.0, 5.0) == 6.0
	assert triangleArea(5.0, 12.0, 13.0) == 30.0
	assert triangleArea(7.0, 24.0, 25.0) == 84.0

	# edge cases
	assert triangleArea(0.0, 0.0, 0.0) == 0.0
	assert isclose(triangleArea(100.0, 100.0, 100.0), 4330.12, rel_tol=1e-2) 

	# Invalid inputs
	try:
		triangleArea("a", 4, 5)
	except TypeError as e:
		assert str(e) == "Input must be of type float."
	# ValueError
	try:
		triangleArea(-3.0, 4.0, 5.0)
	except ValueError as e:
		assert str(e) == "Input must be a positive float."

def test_angle_alpha():
	# angle alpha takes 3 arguments: a, b, and beta; it solves for alpha
	assert isclose(angle_alpha(3.0, 4.0, 90.0), 48.59, rel_tol=1e-2)
	assert isclose(angle_alpha(5.0, 12.0, 90.0), 24.62, rel_tol=1e-2)

	# edge cases
	assert isclose(angle_alpha(7.0, 24.0, 179.0), 0.29, rel_tol=1e-2)

	# Invalid inputs
	try:
		angle_alpha("a", 4.0, 5.0)
	except TypeError as e:
		assert str(e) == "Input must be of type float."
	# ZeroDivisionError
	try:
		angle_alpha(3.0, 4.0, 0.0)
	except ZeroDivisionError as e:
		assert str(e) == "float division by zero"
	# ValueError
	try:
		angle_alpha(-3.0, 4.0, 5.0)
	except ValueError as e:
		assert str(e) == "Input must be a positive float."
