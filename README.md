# python-lec12-oct-13-24

## subjects learned:

1) Ternary: shortcut in conditions:

like in js:

```
desc=x%2==0?"even": "odd"
```

in python:

```
desc="even" if x%2==0 else "odd"
print(f"one line: {x} is {"even" if x%2==0 else "odd"}")
print(f"one line: {x} is {"negative" if x<0 else ("positive" if x>0 else "zero")}")
l1=[-4,1,200,-3,0,2,-3]
l1_1=["negative" if x<0 else ("positive" if x>0 else "zero") for x in l1]
```

## extra subjects:
