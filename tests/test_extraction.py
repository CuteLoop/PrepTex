# File: tests/test_extraction.py

import pytest

from latex_processor.extract_statements import extract_theorems, extract_exercises, validate_latex_syntax


# Test 1: Extracting a basic theorem environment
def test_extract_basic_theorem():
    content = r"""
    \documentclass{article}
    \begin{document}
    \begin{theorem}
    This is a basic theorem.
    \end{theorem}
    \end{document}
    """

    # Test that extract_theorems correctly identifies the theorem block
    extracted = extract_theorems(content)
    expected = ["This is a basic theorem."]
    assert extracted == expected, f"Expected {expected}, but got {extracted}"

# Test 2: Extracting multiple theorem environments
def test_extract_multiple_theorems():
    content = r"""
    \documentclass{article}
    \begin{document}
    \begin{theorem}
    First theorem.
    \end{theorem}

    \begin{theorem}
    Second theorem.
    \end{theorem}
    \end{document}
    """

    # Test multiple theorem extractions
    extracted = extract_theorems(content)
    expected = ["First theorem.", "Second theorem."]
    assert extracted == expected, f"Expected {expected}, but got {extracted}"

# Test 3: Extracting nested theorem-like environments
def test_extract_nested_theorem():
    content = r"""
    \documentclass{article}
    \begin{document}
    \begin{theorem}
    Theorem containing a proof.
    \begin{proof}
    This is a proof inside a theorem.
    \end{proof}
    \end{theorem}
    \end{document}
    """

    extracted = extract_theorems(content)
    expected = ["Theorem containing a proof.\n    \\begin{proof}\n    This is a proof inside a theorem.\n    \\end{proof}"]
    assert extracted == expected, f"Expected {expected}, but got {extracted}"

# Test 4: Extracting exercises
def test_extract_exercise():
    content = r"""
    \documentclass{article}
    \begin{document}
    \begin{exercise}
    This is an exercise.
    \end{exercise}
    \end{document}
    """

    # Test that extract_exercises correctly identifies the exercise block
    extracted = extract_exercises(content)
    expected = ["This is an exercise."]
    assert extracted == expected, f"Expected {expected}, but got {extracted}"

# Test 5: Extracting multiple exercises
def test_extract_multiple_exercises():
    content = r"""
    \documentclass{article}
    \begin{document}
    \begin{exercise}
    First exercise.
    \end{exercise}

    \begin{exercise}
    Second exercise.
    \end{exercise}
    \end{document}
    """

    extracted = extract_exercises(content)
    expected = ["First exercise.", "Second exercise."]
    assert extracted == expected, f"Expected {expected}, but got {extracted}"

# Test 6: Extracting examples
def test_extract_example():
    content = r"""
    \documentclass{article}
    \begin{document}
    \begin{example}
    This is an example.
    \end{example}
    \end{document}
    """

    extracted = extract_exercises(content)
    expected = ["This is an example."]
    assert extracted == expected, f"Expected {expected}, but got {extracted}"

# Test 7: Extracting with no theorems or exercises
def test_extract_no_theorems_or_exercises():
    content = r"""
    \documentclass{article}
    \begin{document}
    This is a document with no theorems or exercises.
    \end{document}
    """

    # No theorems or exercises should be found
    extracted_theorems = extract_theorems(content)
    extracted_exercises = extract_exercises(content)

    assert extracted_theorems == [], "Expected no theorems, but some were extracted."
    assert extracted_exercises == [], "Expected no exercises, but some were extracted."

# Test 8: Malformed LaTeX environments (missing \end{theorem})
def test_extract_malformed_theorem():
    content = r"""
    \documentclass{article}
    \begin{document}
    \begin{theorem}
    This is an incomplete theorem.
    \end{document}
    """

    # Malformed theorem should not be extracted or should raise an error depending on your handling
    with pytest.raises(SyntaxError):
        extract_theorems(content)


# Update the malformed LaTeX test in tests/test_extraction.py
def test_extract_malformed_theorem():
    content = r"""
    \documentclass{article}
    \begin{document}
    \begin{theorem}
    This is an incomplete theorem.
    \end{document}
    """

    # Malformed theorem should raise a SyntaxError
    with pytest.raises(SyntaxError):
        validate_latex_syntax(content, 'theorem')
