
import json

_dict = {
    "name": "0",
    "age": ""
}

for k,v in _dict.items():
    _dict[k]=(input(f'HI! please write your {k}:\n'))

# print(_dict)
for k,v in _dict.items():
    print(f"{k}:{v}")

