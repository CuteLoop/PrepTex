# File: latex_processor/extract_statements.py

import re

# Helper function to extract content between given LaTeX environments
def extract_latex_environment(content, environment):
    """
    Extracts content between \begin{<environment>} and \end{<environment>}.
    
    Args:
        content (str): The LaTeX content to search through.
        environment (str): The name of the LaTeX environment (e.g., 'theorem').
    
    Returns:
        List of strings, where each string is the content of a matched environment.
    """
    # Pattern to match \begin{environment} ... \end{environment}, ignoring leading/trailing whitespaces
    pattern = rf'\\begin{{{environment}}}(.*?)\\end{{{environment}}}'
    matches = re.findall(pattern, content, re.DOTALL)
    
    # Remove leading/trailing whitespace from each match
    return [match.strip() for match in matches]

# Function to extract theorems, lemmas, and propositions
def extract_theorems(content):
    """
    Extracts content from theorem-like environments: theorem, lemma, proposition.
    
    Args:
        content (str): The LaTeX content to search through.
    
    Returns:
        List of strings containing the content of all extracted theorem-like environments.
    """
    # Extract theorems, lemmas, and propositions
    theorems = extract_latex_environment(content, 'theorem')
    lemmas = extract_latex_environment(content, 'lemma')
    propositions = extract_latex_environment(content, 'proposition')

    # Combine results
    return theorems + lemmas + propositions

# Function to extract exercises and examples
def extract_exercises(content):
    """
    Extracts content from exercise-like environments: exercise, example.
    
    Args:
        content (str): The LaTeX content to search through.
    
    Returns:
        List of strings containing the content of all extracted exercise-like environments.
    """
    # Extract exercises and examples
    exercises = extract_latex_environment(content, 'exercise')
    examples = extract_latex_environment(content, 'example')

    # Combine results
    return exercises + examples

# File: latex_processor/extract_statements.py

# Helper function to validate LaTeX syntax
def validate_latex_syntax(content, environment):
    """
    Validates that \begin{environment} has a corresponding \end{environment}.
    
    Args:
        content (str): The LaTeX content to validate.
        environment (str): The name of the LaTeX environment to validate (e.g., 'theorem').
    
    Raises:
        SyntaxError: If there is a mismatch between \begin and \end tags.
    """
    begin_count = len(re.findall(rf'\\begin{{{environment}}}', content))
    end_count = len(re.findall(rf'\\end{{{environment}}}', content))
    
    if begin_count != end_count:
        raise SyntaxError(f"Missing \\end{{{environment}}} or \\begin{{{environment}}} in LaTeX content.")
