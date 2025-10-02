# 🚀 Project Artemis

Project Artemis is a lightweight command-line interface (CLI) tool that interacts with Google's Gemini API to generate AI-powered content from user prompts. Designed for simplicity and extensibility, it enables quick experimentation with Gemini models directly from your terminal.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## ✨ Features

- 🔗 Connects to Gemini 2.0 Flash model via API
- 🧠 Accepts user prompts as command-line arguments
- 📊 Optional verbose mode for token usage insights
- 🔐 Loads API key securely from `.env` file

## 📦 Requirements

- Python 3.8+
- A valid Gemini API key
- `.env` file with your API key

## 🛠 Installation

1. Clone the repository:
 ```bash
 git clone https://github.com/edpsouza/project_artemis.git
 cd project_artemis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file and add your Gemini API key:
```bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

## 🚀 Usage

Run the script with a prompt (example): 
```bash
python main.py "Write a short story about Artemis on the moon"
```
Enable verbose mode for detailed output:
```bash
python main.py "Summarise the history of AI" --verbose
```

## 🧪 Example Output
```text
User prompt: Summarise the history of AI

Artificial Intelligence (AI) began as a field in the 1950s...
Prompt tokens: 12
Response tokens: 87
```

## 🤝 Contributing

Pull requests are welcome! If you have ideas for new features, model integrations, or improvements to the CLI interface, feel free to fork and submit a PR.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## Made with curiosity and code by Eduardo
 
