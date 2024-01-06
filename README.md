```markdown
# Speech-to-Text ChatGPT Interface

## Introduction

This project is a speech-to-text interface that integrates with OpenAI's ChatGPT using the updated API. It allows users to interact with ChatGPT through spoken language, converting speech to text, querying ChatGPT, and receiving verbal responses.

## Features

- **Voice Recognition**: Utilizes Google's speech recognition to convert voice to text.
- **ChatGPT Integration**: Sends the text to ChatGPT and receives responses.
- **Flexible ChatGPT Models**: Supports various ChatGPT models available through OpenAI.
- **Environment Variable for API Key**: Securely manages the OpenAI API key using an environment variable.

## Requirements

- **Python**: Python 3.x is required.
- **OpenAI Python Package**: The `openai` package is used to interact with the OpenAI API.
- **Speech Recognition Package**: The `speech_recognition` package is required for converting spoken language to text.
- **Microphone**: A working microphone setup is necessary for capturing speech.
- **OpenAI API Key**: An API key from OpenAI is needed to use their GPT models.

## Setup and Installation

1. **Clone the Repository**:
   ```
   git clone [repository-url]
   ```

2. **Set Up Environment Variables**:
   - Obtain an OpenAI API key.
   - Set the `OPENAI_API_KEY` environment variable with your API key.

   For Unix/Linux:
   ```
   export OPENAI_API_KEY='your-api-key'
   ```

   For Windows:
   ```
   set OPENAI_API_KEY=your-api-key
   ```

3. **Install Dependencies**:
   - Install the necessary Python packages:
     ```
     pip install openai speechrecognition
     ```

## License

This project is released under the MIT License. This means it comes with permission for a wide range of uses with no restrictions on modifications or distribution.
```

### Explanation of Requirements

1. **Python 3.x**: The program is written in Python, and a current version of Python 3 is required to run the script.

2. **OpenAI Python Package**: This package (`openai`) is used to interact with the OpenAI API. It sends requests to the API and processes the responses.

3. **Speech Recognition Package**: The `speech_recognition` package is essential for the program to convert spoken language into text. This package supports various speech recognition engines, with Google's engine used in this project.

4. **Microphone**: A functional microphone is needed to capture your voice inputs.

5. **OpenAI API Key**: To use OpenAI's GPT models, an API key from OpenAI is required. This key must be set as an environment variable for security purposes. 
