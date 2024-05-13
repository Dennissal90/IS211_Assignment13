def gcd(a, b):
    """Recursive function to find the Greatest Common Divisor (GCD) using Euclid's algorithm.
    Args:
        a (int): First integer.
        b (int): Second integer, should not be zero initially.
    
    Returns:
        int: The GCD of the two integers.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    # Example to test the GCD function
    print("GCD(48, 18):", gcd(48, 18))