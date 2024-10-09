# File: latex_processor/formatter.py
# latex_processor/utils.py
def normalize_latex(content):
    """
    Normalize LaTeX content by stripping excessive newlines and spaces,
    and condensing multiple spaces into a single space.
    This ensures the content is normalized for comparison in tests.
    """
    import re
    lines = [line.strip() for line in content.splitlines() if line.strip()]  # Remove empty lines
    normalized = ' '.join(lines)  # Join lines with single spaces
    return re.sub(r'\s+', ' ', normalized)  # Replace multiple spaces with a single space



def format_extracted_content(theorems, exercises):
    """
    Formats extracted theorems and exercises into a valid LaTeX document.
    
    Args:
        theorems (list): A list of extracted theorems.
        exercises (list): A list of extracted exercises.
    
    Returns:
        str: A formatted LaTeX document as a string.
    """
    
    # Start building the LaTeX document
    document = r"\documentclass{article}\n\begin{document}\n"
    
    # Add theorems section if there are theorems
    if theorems:
        document += r"\section*{Theorems}\n"
        for theorem in theorems:
            document += r"\begin{theorem}\n" + theorem.strip() + r"\n\end{theorem}\n"
    
    # Add exercises section if there are exercises
    if exercises:
        document += r"\section*{Exercises}\n"
        for exercise in exercises:
            document += r"\begin{exercise}\n" + exercise.strip() + r"\n\end{exercise}\n"

    # Close the LaTeX document
    document += r"\end{document}"
    
    # Return the formatted document
    return document.strip()
