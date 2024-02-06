"""compass_regular_polygons.py: This program finds which regular polygons can be created
                                using a compass and straightedge. This code was written
                                to help with a homework assignment for MTH 116: Symmetry
                                and Shape."""

__author__ = "Trevor Hitchcock"

# returns list of prime factors
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# find all polygons able to be created with a straight edge and compass up to size max_sides
def findValidPolygons(max_sides):
    
    # valid fermat primes
    valid_factors = [2,3,5,17,257,65537]
    
    # empty initial list of valid polygons
    valid_polygons = []
    
    # start at 3, triangle first valid polygon
    for i in range(3,max_sides):
        primefactors = prime_factors(i)
        
        valid_set = True
        # for each prime in list of prime factors
        for prime in primefactors:
            # prime is not a fermat prime
            if prime not in valid_factors:
                valid_set = False
                break
            
        # remove 2s from primefactors
        # still works for 2*2*2... because [] == [] and valid_set == True
        no_twos_primefactors = [x for x in primefactors if x != 2]
        
        # if primefactors is equal to the primefactors without duplicates
        if(valid_set and no_twos_primefactors == sorted(list(set(no_twos_primefactors)))):
            # then it is a valid polygon
            valid_polygons.append(i)

    return valid_polygons

INPUT_MAX_SIDES = 100
print("N-sided polygons that can be created with a compass and straight edge (up to",INPUT_MAX_SIDES,"sides):")
print(findValidPolygons(INPUT_MAX_SIDES))