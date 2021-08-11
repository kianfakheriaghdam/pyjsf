class Array:
    """Javascript methods for arrays."""
    def is_array(value):
        """Checks whether a value is an array."""
        try:
            temp = iter(value)
            next(temp)
            return True
        except:
            return False
        
    def map(array, function):
        """Calls a function once for each array element
        and returns a new array with the results."""
        temp_array = []
        for value in array:
            temp_array.append(function(value))
        return temp_array

    def filter(array, function):
        """Calls a function once for each array element
        and returns a new array with the elements that passed the function."""
        temp_array = []
        for value in array:
            if function(value):
                temp_array.append(value)
        return temp_array

    def reduce(array, function):
        """Calls a function for an array elements
        and returns the result."""
        temp_value = array[0]
        for value in array[1:]:
            temp_value = function(temp_value, value)
        return temp_value

    def every(array, function):
        """Checks if all array elements passed a function."""
        for value in array:
            if not function(value):
                return False
        return True

    def some(array, function):
        """Checks if some array elements passed a function."""
        for value in array:
            if function(value):
                return True
        return False

    def index_of(array, value):
        """Search an array for an element value and returns it's index."""
        return array.index(value)

    def last_index_of(array, value):
        """Search from end to start of an array for an element value and returns it's index."""
        return len(array) - array[::-1].index(value) - 1

    def from_(string):
        """Turns a string into an array."""
        temp_array = []
        for char in string:
            temp_array.append(char)
        return temp_array

    def find(array, function):
        """Calls a function once for each array element
        and returns the first element that passed the function."""
        for value in array:
            if function(value):
                return value

    def find_index(array, function):
        """Calls a function once for each array element
        and returns the index of the first element that passed the function."""
        for value in array:
            if function(value):
                return array.index(value)

    def includes(array, value):
        """Checks if a array contains a specified element."""
        for element in array:
            if element == value:
                return True
        return False
