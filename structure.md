
PrepTeX/
├── latex_processor/
│   ├── __init__.py                # Initializes the Python package
│   ├── extract_statements.py       # Logic to extract theorems, propositions, and lemmas
│   ├── extract_exercises.py        # Logic to extract exercises and examples
│   ├── file_handler.py             # Handles reading and writing LaTeX files
├── tests/
│   ├── test_file_handler.py        # Tests for reading and writing LaTeX files
│   ├── test_extraction.py          # Tests for extraction logic
│   ├── test_cli.py                 # Tests for CLI functionality
├── data/
│   ├── sample.tex                  # Example LaTeX file for testing
├── .gitignore                      # Ignores LaTeX build files, temp files, etc.
├── README.md                       # Project overview and instructions
├── roadmap.md                      # Detailed roadmap for development
├── requirements.txt                # Dependencies list for the project
├── setup.py                        # For setting up the package
├── LICENSE                         # Project license (e.g., MIT)
└── latex_processor.py              # Main script for the CLI to extract content
```

### Key Components:

- **`latex_processor/`**: Contains the core functionality for handling LaTeX files and extracting content.
- **`tests/`**: Includes unit tests for the TDD approach, covering all modules.
- **`data/`**: Contains sample `.tex` files for testing the tool.
- **`.gitignore`**: Excludes LaTeX build and temporary files from version control.
- **`README.md`**: Documentation that explains how to use the tool.
- **`roadmap.md`**: A developer roadmap outlining the tasks and goals.
- **`requirements.txt`**: Lists the Python dependencies required for the project.
- **`setup.py`**: Configures the Python package for installation.
- **`latex_processor.py`**: Provides the command-line interface for interacting with the tool.
