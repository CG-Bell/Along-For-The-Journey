#Learning float
#a "floating point" is areal number that contains a decimal point ex: .0664

x = float(input("What's x?  "))
y = float(input("What's y?  "))

#You may also round numbers as follows:

z = round(x + y)
print(z)

#You may round down as:  z = round(x / y, 2) rounds to the two nearest decimal points

#You may also format to include comma (,) in the printed number: print(f"{z:,})