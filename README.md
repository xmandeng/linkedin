# LinkedIn Scraper Project Setup

This README provides step-by-step instructions to set up the development environment for the LinkedIn Scraper project using pyenv, Poetry, and Git.

## Prerequisites

- Git
- pyenv
- pip (for installing Poetry)

## Setup Instructions

### 1. Install Python 3.11.4 using pyenv

```bash
pyenv install 3.11.4
```

### 2. Create a new virtual environment

```bash
pyenv virtualenv 3.11.4 linkedin
```

### 3. Activate the virtual environment

```bash
pyenv activate linkedin
```

### 4. Install Poetry

```bash
pip install poetry
```

### 5. Clone the repository

```bash
git clone git@github.com:xmandeng/linkedin.git
cd linkedin
```

### 6. Install project dependencies

```bash
poetry install
```

### 7. Verify the setup

```bash
python --version  # Should output Python 3.11.4
poetry --version  # Should output the installed Poetry version
```

## Development

After completing the setup, you can start developing the LinkedIn Scraper project. Use Poetry to manage dependencies and run scripts defined in the `pyproject.toml` file.

## Ethical Use and Disclaimer

This LinkedIn Scraper is an experimental project and should be used responsibly and ethically. Please ensure that your use of this tool complies with LinkedIn's terms of service, applicable laws, and respects user privacy. The authors of this project are not responsible for any misuse or any consequences arising from the use of this tool.

## Troubleshooting

If you encounter any issues during setup, please check the following:

- Ensure pyenv is properly installed and configured in your shell.
- Verify that you have the correct permissions to clone the repository.
- If Poetry installation fails, try using pip3 instead of pip.

For any other issues, please open an issue in the GitHub repository.

## Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) file for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.