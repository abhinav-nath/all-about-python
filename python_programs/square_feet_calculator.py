print("Input first dimension:")
l_ft_1 = int(input("Feet: "))
l_inch_1 = int(input("Inches: "))
l_ft_1 += l_inch_1 / 12
print("Length 1 : %f ft" % l_ft_1)

print("Input second dimension:")
l_ft_2 = int(input("Feet: "))
l_inch_2 = int(input("Inches: "))
l_ft_2 += l_inch_2 / 12
print("Length 2 : %f ft" % l_ft_2)

print("\nResult : %f sq ft" % (l_ft_1 * l_ft_2))