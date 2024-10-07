# File: tests/test_file_handler.py

import os
import pytest
from latex_processor.file_handler import read_latex_file, write_latex_file

# Test 1: Reading LaTeX files
def test_read_latex_file():
    sample_content = r"""
    \documentclass{article}
    \begin{document}
    \section{Test}
    This is a test document.
    \end{document}
    """

    # Create a temporary LaTeX file for reading
    file_path = 'data/test_read_latex_file.tex'
    with open(file_path, 'w') as file:
        file.write(sample_content)
    
    # Test that the content is read correctly
    content = read_latex_file(file_path)
    assert content == sample_content, "Content read does not match expected content"

    # Clean up
    os.remove(file_path)


# Test 2: Writing LaTeX files
def test_write_latex_file():
    sample_content = r"""
    \documentclass{article}
    \begin{document}
    \section{Test}
    This is a test document.
    \end{document}
    """

    # Define the path for the test LaTeX file
    file_path = 'data/test_write_latex_file.tex'

    # Write the content to the LaTeX file
    write_latex_file(file_path, sample_content)

    # Check that the content was written correctly
    with open(file_path, 'r') as file:
        written_content = file.read()
    assert written_content == sample_content, "Content written does not match expected content"

    # Clean up
    os.remove(file_path)


# Test 3: Handling empty LaTeX files
def test_read_empty_latex_file():
    empty_file_path = 'data/test_empty_file.tex'
    
    # Create an empty file
    with open(empty_file_path, 'w') as file:
        pass
    
    # Read from the empty file and ensure content is empty
    content = read_latex_file(empty_file_path)
    assert content == "", "Reading an empty file should return an empty string"

    # Clean up
    os.remove(empty_file_path)


# Test 4: Handling non-existent file errors
def test_read_non_existent_file():
    non_existent_file = 'data/non_existent_file.tex'
    
    # Check if the function raises a FileNotFoundError for non-existent files
    with pytest.raises(FileNotFoundError):
        read_latex_file(non_existent_file)


# Test 5: Writing to a non-existent directory
def test_write_to_non_existent_directory():
    file_path = 'non_existent_dir/test_write_latex_file.tex'
    
    # Ensure the function raises a FileNotFoundError or handles the error correctly
    with pytest.raises(FileNotFoundError):
        write_latex_file(file_path, "This is a test content")
