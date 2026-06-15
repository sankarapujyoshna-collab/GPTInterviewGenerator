import random
import json

questions = {

    "Python": [

        "What is Python?",
        "What is a list in Python?",
        "Explain lambda functions.",
        "What is inheritance?",
        "What is exception handling?",
        "What is Python?"      
    ],

    "Data Science": [

        "What is Data Science?",
        "What is data cleaning?",
        "Explain normalization.",
        "What is feature engineering?",
        "What is data visualization?"

    ],

    "Machine Learning": [

        "Explain overfitting in Machine Learning.",
        "What is supervised learning?",
        "What is unsupervised learning?",
        "What is cross validation?",
        "What is confusion matrix?"

    ],

    "Web Development": [

        "What is HTML?",
        "What is CSS?",
        "What is JavaScript?",
        "What is REST API?",
        "What is responsive design?"

    ]

}

print("\nAvailable Domains:")

for i in questions:

    print("-", i)


domain = input("\nEnter Domain : ")

domain = domain.title()


if domain in questions:

    questions[domain] = list(

        set(

            questions[domain]

        )

    )

    q = random.choice(

        questions[domain]

    )

    result = {

        "question": q

    }

    print("\nGenerated Interview Question:\n")

    print(

        json.dumps(

            result,

            indent=4

        )

    )

else:

    print("\nInvalid Domain")
