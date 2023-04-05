# OpenAI Text Prompt UI

This project provides a simple and elegant user interface for sending text prompts to the OpenAI API and displaying the generated responses. The project consists of a Flask backend that communicates with the OpenAI API and a frontend built with HTML, CSS, and JavaScript.

## Prerequisites

- Python 3.6 or higher
- Node.js (for serving the frontend)
- An OpenAI API key (Sign up for an account at [OpenAI](https://beta.openai.com/signup/) and obtain an API key)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Sreekiranar/open_ai_text_prompt_ui.git
    cd openai-text-prompt-ui
    ```

2. Install the required Python packages:

    ```bash
    pip install flask openai
    ```

3. Install the `http-server` package for serving the frontend:

    ```bash
    npm install -g http-server
    ```

## Configuration

Update the `app.py` file with your OpenAI API key:

```python
import os
import openai

# Configure the OpenAI API
openai.api_key = "enter-your-api-key"
```

Replace `enter-your-api-key` with your actual OpenAI API key.

## Usage

- Start the Flask server:

    ```python
    python app.py
    ```

- In a separate terminal, navigate to the project's directory and start the frontend server:

    ```bash
    http-server -p 8000
    ```

- Open your browser and navigate to <http://localhost:8000>. You should see the UI where you can enter a text prompt, submit it, and view the prompt and the response from the OpenAI API.

## Project Structure

- app.py: The Flask server that communicates with the OpenAI API.
- index.html: The HTML file for the frontend UI.
- styles.css: The CSS file for styling the frontend UI.
- main.js: The JavaScript file for handling user input and interaction with the Flask server.

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit/).
