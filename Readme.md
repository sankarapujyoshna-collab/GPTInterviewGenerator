# GPT-Based Interview Question Generator

## Project Description

The GPT-Based Interview Question Generator is a simple Python project developed to generate interview questions for different technical domains. The user can select a domain such as Python, Data Science, Machine Learning, or Web Development, and the program generates a relevant interview question randomly.

This project uses Python dictionaries to store domain-wise questions and the `random` module to select questions dynamically. It also handles duplicate questions by removing repeated entries and checks for invalid domain names to avoid incorrect outputs.

The generated question is displayed in JSON format, making the output structured and easy to understand. This project is useful for students preparing for technical interviews and can be extended further by adding more domains and interview questions.

## Features

* Generates interview questions randomly.
* Supports multiple technical domains.
* Removes duplicate questions.
* Handles invalid domain names.
* Displays output in JSON format.

## Domains Supported

* Python
* Data Science
* Machine Learning
* Web Development

## Technologies Used

* Python
* Random Module
* JSON Module

## Project Structure

```text
GPTInterviewGenerator

│── interview_generator.py
│── README.md
```

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python interview_generator.py
```

4. Enter the domain name.
5. The program generates a random interview question.

## Output

```json
{
    "question": "Explain overfitting in Machine Learning."
}
```

## Conclusion

This project demonstrates the use of Python dictionaries, lists, random question generation, and JSON formatting to create a simple interview question generator. It helps users practice technical interview questions and can be enhanced in the future by adding more domains and questions.
