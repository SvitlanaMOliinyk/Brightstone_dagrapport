class InvalidCsvError(Exception):
    """Raised when a CSV file is invalid.

    Inherits exception behavior from Exception class.
    """
    pass


class MissingColumnError(Exception):
    """Raised when a required column is missing from CSV file.

       Inherits exception behavior from Exception class.
       """
    pass
