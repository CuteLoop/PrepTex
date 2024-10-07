# File: cli/__init__.py

import click

@click.command()
def extract_latex():
    """A simple CLI command for PrepTeX."""
    click.echo("PrepTeX is working! Use this tool to extract theorems, exercises, and examples from LaTeX files.")

if __name__ == '__main__':
    extract_latex()
