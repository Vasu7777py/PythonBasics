
# python basics..
# printing and variables

print("Welcome.. to lazyCoder47 channel")

# python will handel all the data types automatically
i = 7			# python will see this as integer
				# any number with out decimal point (.) is integer
f = 4.7			# python will see this as floating point data
				# floating point data range 
				# (2.2250738585072014e-308(10^-308), 1.7976931348623157e+308(10^+308))
s = 'String'	# anything in '' or "", python will see this as string value

l = [i, f, s]	# anything in [] it is see as list
				# list is collection of values

# print is a function python uses to print data on screen...
# print function prints the given content line by line
# adds new line after printing by default

# if you add f or F before the string, it is said as fStrings
# in fStrings you can add variables inside the string
print(f"i : {i}, data type : {type(i)}")
# alternative way, if you dont want to use fStrings
print("i : " + str(i) + ", data type : " + str(type(i)) + " (alternative way)")

print(f"f : {f}, data type : {type(f)}")
print(f"s : {s}, data type : {type(s)}")
print(f"l = [i, f, s] : {l}, data type : {type(l)}")

# if you dont want to print line by line, u can mention it by passing 
# agrument to print function
print("Do love ", end = "😘 ")
print("PYTHON ??")
print("Python is simple and easy to learn than anyother programming language out there..", end = "\n\t")
print("Enjoy coding 👍")
