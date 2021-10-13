# Lambda - one liner anonymous function

def add(a, b):
    return a + b


# not a correct way of writing lambda
# if we are binding it with a name then
# better define a regular function
minus = lambda a, b: a - b

print("add", add(2, 5))
print("minus", minus(8, 3))

# correct way to execute a lambda
print("minus", (lambda a, b: a - b)(8, 3))

# incorrect
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("    rick", "gRimes   "))

# correct way
print((lambda fn, ln: fn.strip().title() + " " + ln.strip().title())("    rick", "gRimes   "))
