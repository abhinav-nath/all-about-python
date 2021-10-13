def add(a, b):
    return a + b


minus = lambda a, b: a - b

print("add", add(2, 5))
print("minus", minus(8, 3))  # one liner anonymous function

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("    rick", "gRimes   "))
