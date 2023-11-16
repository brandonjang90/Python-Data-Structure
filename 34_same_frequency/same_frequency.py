def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    counter1 = {}
    counter2 = {}
    lst1 = list(str(num1))
    lst2 = list(str(num2))

    for num in lst1:
        counter1[num] = counter1.get(num, 0) + 1
    for num in lst2:
        counter2[num] = counter2.get(num, 0) + 1
    
    if counter1 == counter2:
        return True
    else:
        return False