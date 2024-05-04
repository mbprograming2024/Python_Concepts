# Python sets support various operations commonly used in set theory,
# such as union, intersection, difference, and symmetric difference.

set1 = {1,2,3}
set2 = {3,4,5}

# union = '|' , unic parameter from both set and return one set

union = set1 | set2
print(union)

#Intersection (&): Returns a new set containing only the elements present in both sets.

intersection = set1 & set2
print(intersection)

#Difference (-): Returns a new set containing elements present in the first set but not in the second set.

diff = set1-set2
print(diff)
diff = set2-set1
print(diff)

# Symmetric Difference (^): Returns a new set containing elements present in either set, but not in both.

symetric_diff = set1 ^ set2
print(symetric_diff)


# Subset (<=) and Superset (>=): Tests whether one set is a subset or superset of another.

set3 = {1,2,3}
set4 = {1,2}

print(set3 <= set4)
print(set3 >= set4)

# Proper Subset (<) and Proper Superset (>): Similar to subset and superset, but strict.
set3 = {1,2,3}
set4 = {1,2}

print(set3<set4)
print(set3>set4)




