import re

text = "EUR 250.50"
match = re.search(r"(\d+\.\d+)",text)
if match:
    value = float(match.group(1))
    if value.is_integer():
        print(int(value))
    else:
        print(type(value))

        