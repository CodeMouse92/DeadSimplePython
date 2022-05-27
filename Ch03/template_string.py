from string import Template
s = Template("$greeting, $user!")
print(s.substitute(greeting="Hi", user="Jason"))

s = Template("A ${thing}ify subscription costs $$$price/mo.")
print(s.substitute(thing="Code", price=19.95))
