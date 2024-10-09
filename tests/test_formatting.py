# File: tests/test_formatting.py
from latex_processor.formatter import format_extracted_content, normalize_latex  # Import the function

# Example from test_formatting.py
def test_format_single_theorem():
    extracted_theorems = ["This is a theorem."]
    extracted_exercises = []

    formatted_output = format_extracted_content(extracted_theorems, extracted_exercises)
    expected_output = r"""
    \documentclass{article}
    \begin{document}

    \section*{Theorems}
    \begin{theorem}
    This is a theorem.
    \end{theorem}

    \end{document}
    """

    assert normalize_latex(formatted_output) == normalize_latex(expected_output), "The formatted LaTeX output is not correct."

def normalize_latex(latex_string):
    """Removes unnecessary whitespace and normalizes LaTeX strings for comparison."""
    return "\n".join([line.strip() for line in latex_string.strip().splitlines()])

def test_format_single_theorem():
    extracted_theorems = ["This is a theorem."]
    extracted_exercises = []

    formatted_output = format_extracted_content(extracted_theorems, extracted_exercises)
    expected_output = r"""
    \documentclass{article}
    \begin{document}

    \section*{Theorems}
    \begin{theorem}
    This is a theorem.
    \end{theorem}

    \end{document}
    """
    assert normalize_latex(formatted_output) == normalize_latex(expected_output), "The formatted LaTeX output is not correct."

# Test 2: Formatting with multiple theorems and exercises
def test_format_multiple_theorems_and_exercises():
    extracted_theorems = ["Theorem 1.", "Theorem 2."]
    extracted_exercises = ["Exercise 1.", "Exercise 2."]

    formatted_output = format_extracted_content(extracted_theorems, extracted_exercises)
    expected_output = r"""
    \documentclass{article}
    \begin{document}

    \section*{Theorems}
    \begin{theorem}
    Theorem 1.
    \end{theorem}
    \begin{theorem}
    Theorem 2.
    \end{theorem}

    \section*{Exercises}
    \begin{exercise}
    Exercise 1.
    \end{exercise}
    \begin{exercise}
    Exercise 2.
    \end{exercise}

    \end{document}
    """
    
    assert normalize_latex(formatted_output) == normalize_latex(expected_output), "The formatted LaTeX output is not correct."

# Test 3: Handling empty inputs (no theorems or exercises)
def test_format_empty_content():
    extracted_theorems = []
    extracted_exercises = []

    formatted_output = format_extracted_content(extracted_theorems, extracted_exercises)
    expected_output = r"""
    \documentclass{article}
    \begin{document}

    \end{document}
    """
    
    assert normalize_latex(formatted_output) == normalize_latex(expected_output), "The formatted LaTeX output for empty content is not correct."

# Test 4: Formatting with only exercises
def test_format_only_exercises():
    extracted_theorems = []
    extracted_exercises = ["Exercise 1.", "Exercise 2."]

    formatted_output = format_extracted_content(extracted_theorems, extracted_exercises)
    expected_output = r"""
    \documentclass{article}
    \begin{document}

    \section*{Exercises}
    \begin{exercise}
    Exercise 1.
    \end{exercise}
    \begin{exercise}
    Exercise 2.
    \end{exercise}

    \end{document}
    """
    
    assert normalize_latex(formatted_output) == normalize_latex(expected_output), "The formatted LaTeX output is not correct."
