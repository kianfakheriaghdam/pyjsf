class Integer:
    """Javascript methods for integers."""
    def is_integer(value):
        """Checks whether an object is an integer."""
        try:
            int(str(value))
            return True
        except:
            return False
