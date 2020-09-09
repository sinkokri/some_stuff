#!/usr/bin/env python3
import re 

def rearrange(name):
    if not isinstance(name, str):
        raise TypeError(f'it has to be a name in formar "name, surname"')
    result=re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange("Maria, Petrova"))