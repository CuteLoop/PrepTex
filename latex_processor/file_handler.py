# File: latex_processor/file_handler.py

def read_latex_file(file_path):
    """Reads the content of a LaTeX file and returns it as a string."""
    with open(file_path, 'r') as file:
        return file.read()


def write_latex_file(file_path, content):
    """Writes the given content to a LaTeX file."""
    with open(file_path, 'w') as file:
        file.write(content)
