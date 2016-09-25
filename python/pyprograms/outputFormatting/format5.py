#!/usr/bin/python

#ref : https://stackoverflow.com/questions/5466451/how-can-i-print-a-literal-characters-in-python-string-and-also-use-format

#ref : https://stackoverflow.com/questions/30394912/python-dict-in-formated-string?lq=1

#cmd : clear; python format5.py

# to print {Hello} 42


x = " {{ Hello }} {0} "
print x.format(42)

# example 2

y = "{{'key_1': '{value}'}}".format(**{'value': 'test'})

print y.format(45)





#     Format strings contain "replacement fields" surrounded
#     by curly braces {}. Anything that is not contained in 
#     braces is considered literal text, which is copied 
#     unchanged to the output. If you need to include a 
#     brace character in the literal text, it can be 
#     escaped by doubling: {{ and }}.
