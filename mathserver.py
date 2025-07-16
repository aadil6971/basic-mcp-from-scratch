from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    """_summary_
    Add to numbers
    """
    return a+b

@mcp.tool()
def multiple(a:int,b:int)-> int:
    """Multiply two numbers"""
    return a*b

@mcp.tool()
def subtract(a:int,b:int)->int:
    """Subtract two numbers"""
    return a-b

@mcp.tool()
def divide(a:int,b:int)->float:
    """Divide two numbers"""
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a/b

@mcp.tool()
def power(a:int,b:int)->int:
    """Raise a to the power of b"""
    return a**b
@mcp.tool()
def square_root(a:int)->float:
    """Calculate the square root of a number"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a**0.5
@mcp.tool()
def factorial(n:int)->int:
    """Calculate the factorial of a number"""
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__=="__main__":
    mcp.run(transport="stdio")