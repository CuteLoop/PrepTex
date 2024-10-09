import subprocess
import sys
import os
import shutil
import venv
from pathlib import Path

# Define paths
VENV_DIR = Path("test_env")

def create_virtualenv(venv_dir):
    """Create a virtual environment for testing."""
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(venv_dir)
    assert venv_dir.exists(), f"Virtual environment was not created at {venv_dir}"

def run_in_virtualenv(venv_dir, command):
    """Run a command within the virtual environment."""
    activate_script = venv_dir / "bin" / "activate" if os.name != 'nt' else venv_dir / "Scripts" / "activate"
    full_command = f'{activate_script} && {command}'
    
    # Ensure we're running the command in the correct directory
    cwd = Path().resolve()  # Ensure current working directory is where setup.py is located
    print(f"Running command: {full_command} in {cwd}")  # Debugging print
    result = subprocess.run(full_command, shell=True, capture_output=True, text=True, cwd=cwd)
    print(f"stdout: {result.stdout}")  # Add print for stdout
    print(f"stderr: {result.stderr}")  # Add print for stderr
    return result

def test_package_installation():
    """
    Test that the package installs correctly.
    If the package is not installed, install it.
    """
    if VENV_DIR.exists():
        shutil.rmtree(VENV_DIR)  # Clean up if virtualenv exists

    # Step 1: Create the virtual environment
    create_virtualenv(VENV_DIR)

    # Step 2: Test if the package is installed
    result = run_in_virtualenv(VENV_DIR, f"{sys.executable} -m pip show PrepTeX")
    
    if "WARNING: Package(s) not found" in result.stderr:
        # Step 3: Install the package if it's not installed
        result = run_in_virtualenv(VENV_DIR, f"{sys.executable} -m pip install -e .")
        assert result.returncode == 0, f"Package installation failed: {result.stderr}"
    
    # Check again after installation
    result = run_in_virtualenv(VENV_DIR, f"{sys.executable} -m pip show PrepTeX")
    print("Package Info after installation:", result.stdout)  # Debug print
    assert "Name: PrepTeX" in result.stdout, "Package installation failed"

def test_dependencies_installed():
    """
    Test if the required dependencies (e.g., 'click') are installed.
    """
    result = run_in_virtualenv(VENV_DIR, f"{sys.executable} -m pip show click")
    assert result.returncode == 0, "Dependency 'click' is not installed"

def test_cli_entry_point():
    """
    Test that the CLI entry point is available and '--help' works.
    """
    result = run_in_virtualenv(VENV_DIR, "prepex --help")
    print(f"CLI stdout: {result.stdout}")  # Debug print for CLI output
    print(f"CLI stderr: {result.stderr}")  # Debug print for CLI errors
    assert result.returncode == 0, f"CLI command failed: {result.stderr}"
    assert "Usage:" in result.stdout, "CLI help command did not return expected output"

def teardown_module(module):
    """
    Clean up the virtual environment after the tests.
    """
    if VENV_DIR.exists():
        shutil.rmtree(VENV_DIR)
