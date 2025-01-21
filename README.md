# Code explanation:

For the functions, I made it so that the functions only strictly allow floats to be used in the parameters for the sake of simplicity (on my end)

Both functions have typechecking to ensure that the parameters are floats. If the parameters are not floats, the functions will raise a TypeError. Additionally, the functions will raise a ValueError if the parameters are negative. To avoid division by zero in the second function, I added a check to see if the denominator (beta) is zero, in which case the function will raise a ValueError.

In the test file, I tested the functions with various test cases to ensure that the functions are working as intended. I tested the functions with positive and negative floats, as well as zero. I also tested the functions with the edge case of beta being zero in the second function. Since the functions could print out long decimal numbers, I used the math.isclose() function to check if the output is close to the expected value within a certain tolerance.