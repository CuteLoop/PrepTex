from setuptools import setup, find_packages

setup(
    name='PrepTeX',
    version='0.1.0',
    description='A tool to extract theorems, exercises, and examples from LaTeX files for exam preparation',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/PrepTeX',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'prepex=cli:extract_latex',  # Points to cli.py
        ],
    },
    python_requires='>=3.6',
)
