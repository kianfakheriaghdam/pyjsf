# pyjsf
pyjsf contains some useful functions from javascript for python. these are function for strings, arrays(lists) and integers.

### Documention
We start up by importing all the functions from pyjsf
```Python
from pyjsf.string import String
from pyjsf.array import Array
from pyjsf.integer import Integer
```

### String functions
char_at() returns the character at a specified index in a string.
```Python
print(String.char_at('Hello world!', 0))
```
trim() removes whitespace from both sides of a string.
```Python
print(String.trim('  Hello world!  '))
```
includes() checks if a string contains a specified value.
```Python
print(String.includes('Hello world!', 'Hello'))
print(String.includes('Hello world!', 'Eggs and spams'))
```
starts_with() checks if a string starts with a specified charactor.
ends_with() checks if a string ends with a specified charactor.
```Python
print(String.starts_with('Hello world!', 'H'))
print(String.starts_with('Hello world!', '!'))

print(String.ends_with('Hello world!', '!'))
print(String.ends_with('Hello world!', 'H'))
```
multiline() Takes lines of string and returns a multiline string.
end is used to specify the lastest line of the string.
```Python
print(String.multiline('Hello', end='world!'))
print(String.multiline('Hello', 'Eggs and spams', end='world!'))
```

### Array functions
is_array() checks whether a value is an array.
```Python
print(Array.is_array(1))
print(Array.is_array(True))
print(Array.is_array('Hello world!')) # returns True because string is an array of chars.
print(Array.is_array([1, 2, 3]))
```
map() calls a function once for each array element and returns a new array with the results.
```Python
print(Array.map([1, 2, 3], lambda x: x * 2))
```
filter() calls a function once for each array element and returns a new array with the elements that passed the function.
```Python
print(Array.filter([1, 2, 3], lambda x: True if x > 1 else False))
```
reduce() calls a function for an array elements and returns the result.
```Python
print(Array.reduce([1, 2, 3], lambda x, y: x + y))
```
every() checks if all array elements passed a function.
```Python
print(Array.every([1, 2, 3], lambda x: True if x > 1 else False))
print(Array.every([2, 2, 3], lambda x: True if x > 1 else False))
```
some() checks if some array elements passed a function.
```Python
print(Array.some([1, 2, 3], lambda x: True if x > 1 else False))
print(Array.some([1, 1, 1], lambda x: True if x > 1 else False))
```
index_of() searchs an array for an element value and returns it's index.
```Python
print(Array.index_of([1, 2, 1], 1))
```
last_index_of() searchs from end to start of an array for an element value and returns it's index.
```Python
print(Array.last_index_of([1, 2, 1], 1))
```
from_() turns a string into an array.
```Python
print(Array.from_('Hello world!'))
```
find() calls a function once for each array element and returns the first element that passed the function.
```Python
print(Array.find([1, 2, 3], lambda x: True if x > 1 else False))
```
find_index() calls a function once for each array element and returns the index of the first element that passed the function.
```Python
print(Array.find_index([1, 2, 3], lambda x: True if x > 1 else False))
```
includes() checks if a array contains a specified element.
```Python
print(Array.includes([1, 2, 3], 1))
print(Array.includes([1, 2, 3], 4))
```

### Integer functions
is_integer() checks whether an object is an integer.
```Python
print(Integer.is_integer(1))
print(Integer.is_integer(1.1))
print(Integer.is_integer('Hello world!'))
print(Integer.is_integer([1, 2, 3]))
```
