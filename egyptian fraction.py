#The first step is to find the largest possible unit fraction that is less than or equal to 6/14.
#This fraction is 1/3. The remaining fraction is 6/14 - 1/3 = 4/42.
#The largest possible unit fraction that is less than or equal to 4/42 is 1/11.
#The remaining fraction is 4/42 - 1/11 = 1/231.

def egyptian_fraction(numerator, denominator):
    fractions = []
    while numerator != 0:
        unit_fraction = (denominator + numerator - 1) // numerator
        fractions.append(unit_fraction)
        numerator = unit_fraction * numerator - denominator
        denominator *= unit_fraction
    return fractions

numerator = int(input())
denominator = int(input())

fractions = egyptian_fraction(numerator, denominator)

for fraction in fractions:
    print(fraction)

