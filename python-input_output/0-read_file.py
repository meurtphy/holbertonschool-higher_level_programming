def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    :param filename: Name of the file to be read.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
