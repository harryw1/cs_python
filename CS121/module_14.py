def first_even(int_list):
    for numbers in int_list:
        if numbers % 2 == 0:
            return numbers
    raise ValueError("No even numbers in list")
    
t = first_even([1,2,3,4,5,6,7])
assert t == 2, "Expected 2, got" + str(t)

t = first_even([8,4,2])
assert t == 8, "Expected 8, got" + str(t)

try:
    t = first_even([1,3,5,7])
    assert False, "This should not print"
except ValueError:
    print("ValueError: worked.")