import os

# Directories and files to be created
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
    'tests/test_repository_structure.py',  # Current test
    'data/sample.tex',
    '.gitignore',
    'README.md',
    'roadmap.md',
    'requirements.txt',
    'setup.py',
    'latex_processor.py',
]

# Create directories if they don't exist
for directory in expected_directories:
    os.makedirs(directory, exist_ok=True)

# Create files if they don't exist
for file in expected_files:
    file_dir = os.path.dirname(file)
    if file_dir:  # Only create parent directory if it is not an empty string
        os.makedirs(file_dir, exist_ok=True)
    
    # Create the file if it doesn't exist
    if not os.path.exists(file):
        with open(file, 'w') as f:
            if file.endswith('.py'):
                f.write("# Python script\n")
            elif file == "README.md":
                f.write("# PrepTeX\n\nProject description goes here.\n")
            elif file == ".gitignore":
                f.write("# Ignore LaTeX build files\n*.aux\n*.log\n*.out\n")
            elif file == "roadmap.md":
                f.write("# Roadmap\n\nDetailed development roadmap.\n")
            elif file == "requirements.txt":
                f.write("# Add project dependencies here\n")
            elif file == "setup.py":
                f.write("# Setup script for project\n")
            elif file == "data/sample.tex":
                f.write("% Sample LaTeX file for testing\n")
            else:
                f.write("# Placeholder file\n")

print("Repository structure created successfully.")