

# PrepTex
 **PrepTeX** is a Python tool designed to streamline exam preparation by automatically extracting key sections like theorems, lemmas, propositions, exercises, and examples from LaTeX documents. It helps students focus on the most important material, making it easier to revise, study, and practice for exams. By separating content into study-ready files, PrepTeX saves time and allows for efficient review of critical concepts and problems without solutions.  With a focus on modularity and ease of use, PrepTeX offers:  Command-line interface for quick extraction of LaTeX content. Support for customizable extraction of theorems and exercises. Test-driven development ensuring reliability and robustness.

## Features

- **Theorem and Lemma Extraction**: Automatically extract theorems, lemmas, and propositions from your LaTeX notes.
- **Exercises and Examples**: Separate exercises and examples (without solutions) into study-ready files.
- **Command-Line Interface (CLI)**: Easily extract and save content via simple commands.
- **Modular Design**: Organized and easy-to-extend code for future enhancements.
- **Test-Driven Development (TDD)**: Developed using a TDD approach, ensuring reliability.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/PrepTeX.git
   cd PrepTeX
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Extract theorems, lemmas, and propositions:

   ```bash
   python latex_processor.py --file data/sample.tex --output theorems_output.tex --type theorems
   ```

2. Extract exercises and examples:

   ```bash
   python latex_processor.py --file data/sample.tex --output exercises_output.tex --type exercises
   ```

## Test-Driven Development

PrepTeX was built with a test-first approach to ensure robustness. You can run tests using:

```bash
pytest
```

## Roadmap

- Add support for custom LaTeX environments.
- Expand extraction options to include user-defined sections.
- Improve the LaTeX parser for complex documents.

## Contributing

We welcome contributions! Feel free to submit a pull request or open an issue if you encounter any bugs or have feature suggestions.

## Acknowledgments

This project was built with the help of [GitHub Copilot](https://github.com/features/copilot) for code suggestions and [ChatGPT](https://openai.com/chatgpt) for development guidance and support.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
