def compareTo(s1, s2):
    """Recursive function to compare two strings lexicographically.
    Args:
        s1 (str): First string to compare.
        s2 (str): Second string to compare.
    
    Returns:
        int: Negative if s1 < s2, zero if s1 == s2, positive if s1 > s2.
    """
    if not s1 and not s2:
        return 0
    elif not s1:
        return -ord(s2[0])
    elif not s2:
        return ord(s1[0])
    elif s1[0] == s2[0]:
        return compareTo(s1[1:], s2[1:])
    else:
        return ord(s1[0]) - ord(s2[0])

if __name__ == "__main__":
    print("compareTo('hello', 'hello'):", compareTo('hello', 'hello'))
    print("compareTo('apple', 'banana'):", compareTo('apple', 'banana'))
    print("compareTo('banana', 'apple'):", compareTo('banana', 'apple'))