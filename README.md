A cool 10 liner that I use to check my answers while doing math homework.

I tend to use it in the REPL but you can use it in your applications too.

The derivative function takes a function and returns the derivative function of that function. This approach allows you to take second and third derivatives of the function. Derivatives are calculated using the central difference derivative formula.

The integral function takes the function that you're integrating and the lower and upper bounds of the integral, and returns a float representing the result of the integration. The function is using midpoint approximation to find the integral.

Note that both functions will return a result even when the derivative or the integral does not exist at a praticular point. For example the derivative of 1/x at zero.
