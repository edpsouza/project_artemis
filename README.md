# 🚀 Project Artemis

Project Artemis is a lightweight command-line interface (CLI) tool that interacts with Google's Gemini API to generate AI-powered content from user prompts. Designed for simplicity and extensibility, it enables quick experimentation with Gemini models directly from your terminal.

![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## ✨ Features

- 🔗 Connects to Gemini 2.0 Flash model via API
- 🧠 Accepts user prompts as command-line arguments
- 📊 Optional verbose mode for token usage insights
- 🔐 Loads API key securely from `.env` file
- ⚡ Uses `uv` for dependency resolution and environment management
- 🧩 Modular codebase for maintainability ('core' folder for config, API client. 'utils' folder for prompt parsing, and output formatting)

## 📦 Requirements

- Python 3.11+ (recommended: 3.11, as specified in `.python-version`)
- [uv](https://docs.astral.sh/uv/) installed (`pipx install uv`)
- A valid Gemini API key
- `.env` file with your API key

## 🛠 Installation

1. Clone the repository:
 ```bash
 git clone https://github.com/edpsouza/project_artemis.git
 cd project_artemis
```

2. Sync dependencies using uv:
```bash
uv venv
uv sync
```

4. Create a .env file and add your Gemini API key:
```bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

## 🚀 Usage

Start the interactive CLI:
```bash
uv run main.py
```
You will see:
```text
Welcome to Project Artemis! Type your prompt and press Enter.
Type 'exit' or 'quit' to end the session.
Add '--verbose' to the end of your prompt for detailed output.
```
Example prompts:
```text
Prompt: Write a short story about Artemis on the moon
Prompt: Summarise the history of AI --verbose
Prompt: exit
```

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
🧠✨ Made with curiosity and code by [Eduardo](https://github.com/edpsouza)
<<<<<<< HEAD
 



=======
>>>>>>> 20ae4a5 (Refactor CLI to interactive loop, modularise codebase, update README and .gitignore)
