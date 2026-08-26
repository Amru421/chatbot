# NoteBot Chatbot

NoteBot is a chatbot application that allows users to upload PDF documents and ask questions based on the content of those documents. It utilizes OpenAI's API to generate responses, making it a powerful tool for extracting information from notes and other text-based resources.

## Features

- Upload PDF files and extract text content.
- Ask questions related to the content of the uploaded documents.
- Generate responses using OpenAI's language model.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd notebot
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env` and fill in the necessary API keys and configurations.

## Usage

1. Run the application:
   ```
   streamlit run src/chatbot.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the NoteBot interface.

3. Upload a PDF file and start asking questions!

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.