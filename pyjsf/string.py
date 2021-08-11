class String:
    """Javascript methods for strings."""
    def char_at(string, index):
        """Returns the character at a specified index in a string."""
        return string[index]

    def trim(string):
        """Removes whitespace from both sides of a string."""
        return string.strip()

    def includes(string, value):
        """Checks if a string contains a specified value."""
        temp_bool = string.find(value)
        if temp_bool == -1:
            return False
        else:
            return True

    def starts_with(string, char):
        """Checks if a string starts with a specified charactor."""
        return string.startswith(char)

    def ends_with(string, char):
        """Checks if a string ends with a specified charactor."""
        return string.endswith(char)

    def multiline(*strings, end):
        """Takes lines of string and returns a multiline string.
        end: The lastest line of the string.
        """
        temp_string = ''
        for string in strings:
            temp_string += string + '\n'
        temp_string += end
        return temp_string
