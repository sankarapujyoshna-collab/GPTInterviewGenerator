GPT-Based Interview Question Generator
About the Project

This project is a simple Interview Question Generator developed using Python. It generates interview questions based on the technical domain selected by the user.

The main aim of this project is to help students prepare for interviews by providing random and relevant questions from different domains.

Domains Included
Python
Data Science
Machine Learning
Web Development
Features
Generates interview questions randomly.
Supports multiple technical domains.
Removes duplicate questions.
Handles invalid domain names.
Displays output in JSON format.
Technologies Used
Python
Random Module
JSON Module
Project Structure
GPTInterviewGenerator

│── interview_generator.py
│── README.md
How to Run the Project
Open the project folder in VS Code.
Open the terminal.
Run the following command:
python interview_generator.py
Select a domain by entering its name.
The program generates a random interview question.
Sample Output
Available Domains:

- Python
- Data Science
- Machine Learning
- Web Development

Enter Domain : Python

Generated Interview Question:

{
    "question": "What is inheritance?"
}
Conclusion

This project demonstrates the use of Python dictionaries, lists, random question generation, and JSON formatting to create a simple interview question generator. It is useful for interview preparation and can be extended by adding more domains and questions in the future.