a = range(-10, 105, 5)
c = "het vriest"
for x in a:
    if x < 35:
        c = "het vriest"
    else:
        c = "het vriest niet"
    b = int(5/9*(x-32))
    print( x, "Fahrenheit", "=", b, "graden", c)
