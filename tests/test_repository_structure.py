import os

def test_repository_structure():
    # Define expected files and directories
    expected_directories = [
        'latex_processor/',
        'tests/',
        'data/',
    ]
    
    expected_files = [
        'latex_processor/__init__.py',
        'latex_processor/extract_statements.py',
        'latex_processor/extract_exercises.py',
        'latex_processor/file_handler.py',
        'tests/test_file_handler.py',
        'tests/test_extraction.py',
        'tests/test_cli.py',
        "tests/test_repository_structure.py",
        'data/sample.tex',
        '.gitignore',
        'README.md',
        'roadmap.md',
        'requirements.txt',
        'setup.py',
        #'latex_processor.py',
    ]
    
    # Check if the directories exist
    for directory in expected_directories:
        assert os.path.isdir(directory), f"Missing directory: {directory}"
    
    # Check if the files exist
    for file in expected_files:
        assert os.path.isfile(file), f"Missing file: {file}"

