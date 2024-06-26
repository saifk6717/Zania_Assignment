# AI PDF Question Answering Agent

## Overview

This project creates an AI agent that leverages the capabilities of OpenAI's GPT-3.5-turbo model to extract answers based on the content of a large PDF document and post the results on Slack. The agent is designed to process PDF documents in chunks, handle user questions dynamically, and aggregate the responses for accurate answers.

## User Journey

1. The user inputs the PDF document.
2. The user inputs the questions to be answered.
3. The user asks the agent to "Answer the questions and post results on Slack."

## Features

- **PDF Parsing**: Extracts text from PDF files.
- **Chunk Processing**: Splits large text into manageable chunks to avoid exceeding the model's context limit.
- **OpenAI Integration**: Uses GPT-3.5-turbo for processing and answering questions.
- **Slack Integration**: Posts results to a specified Slack channel.
- **Interactive CLI**: Allows users to input questions dynamically and decide whether to post the answers to Slack.

## Supported Input File Types

- PDF

## Input Requirements

- **PDF File**: The document over which the questions will be answered.
- **Questions**: A list of questions to extract answers from the document.

## Ideal Output Format

The output is a structured JSON blob that pairs each question with its corresponding answer. If an answer cannot be confidently provided, the response will be "Data Not Available".

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and populate it with your API keys and tokens:
    ```plaintext
    OPENAI_API_KEY='Your Open API key'
    SLACK_BOT_TOKEN='Your Slack Bot token'
    SLACK_CHANNEL_ID=your-slack-channel-id
    ```

## Usage

1. Run the main application:
    ```sh
    python main.py
    ```

2. Follow the prompts to input your questions and decide whether to post the answers to Slack.

## Code Structure

- **config.py**: Loads API keys and tokens from environment variables.
- **pdf_parser.py**: Contains functions for extracting text from PDF and splitting it into chunks.
- **openai_api.py**: Contains function to get answers from OpenAI GPT-3.5-turbo.
- **slack_notifier.py**: Contains functions to post messages to Slack.
- **main.py**: The main script that handles user interaction and processes questions.

## Example Workflow

- Start the script with `python main.py`.
- Enter a question when prompted.
- Review the answer printed in the console.
- Decide whether to post the answer to Slack.
- Repeat or type 'exit' to quit the application.

## Improving Accuracy

Here are a few points on how the solution could be made more accurate:

1. **Enhanced Chunking**: Implement more sophisticated chunking to ensure that context is preserved across chunks.
2. **Contextual Awareness**: Use context windowing techniques to maintain the context from previous chunks when processing the next chunk.
3. **Answer Verification**: Implement a verification step where the model re-evaluates the aggregated answers for consistency and accuracy.
4. **Feedback Loop**: Allow users to provide feedback on the accuracy of answers and use this feedback to fine-tune the model.

## Demo

Please refer to the [video/demo] for a demonstration of the program in action.
