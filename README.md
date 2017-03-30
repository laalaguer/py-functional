## Functional Programming in Python 2.7 (3.x)
Funtional Python, which is already supported in Python. It language supports feature like filter(), map() and reduce().

## Problem Solving & Knowledge Points
### 1.1 Word Frequency (no side effect)
`wordfq.py` : How to get frequency of words in a file? As Java programmers we want to objectnize things and as procedure programmers we want to make things do one step and then another. May it be transform, filter. We learn from this `wordfq.py` how we did wrongly about functional programming and we introduce the key feature of it: don't mutate the argument object and return a new state if possible. AKA. no side effects.

### 1.2 Index of Any (tool intro)
`indexofany.py`: Given a string, and a list of key chars, find the occurance of chars in the string. This lesson gives us a taste of list comprehension in Python. `list comprehension` is a Pythonic way of filtering objects in a collection. (or transform objects)

### 1.3 Convert Names (streamline your operations)
`convertname.py`: functional programmer wants their functions to be 'pipes' and data to be wather. Data flow through functions as water flow through conjuction pipes. In real world, we do calculation in steps, do f(x) then, let g(f(x)). In this example, we filter() out bad names, then capitalize() remained good names. Apart from 'stream line', we remember use pure functions as the building blocks of any pipe line. (no side effect)

### 1.4 Find Aliquot Number (first full FP program)
`aliquotNum.py`: Our first FP program. The target is to classify a number based on its aliquot sum. This is a good example of pure FP as it is based on two fundemental ideas: 1. no side effect. 2. streamline operations. But it also have problems: high memory footprint and no cache accelerations! We will fix it in next version.

### 1.5 Find Aliquot Number (improved version, Generator pattern, Lazy evaluation)
`aliquotNum2.py`: improved aliquot FP program, we use generators to reduce memory footprint. Generators behaves like a list, (which you can iterate on it one by one), but instead of generate a full list at once, you can fit in a generator, and let it give you "next" value each time you visit it.

