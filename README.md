# chatbot

A simple python code for creating chatbots. Just clone, edit the data.yml file and import to your python program!

## How it works

This is a very simple idea - you add categories with keywords and question types. The code then tries to identify those in the input and retrieve a response, based on your rules in `data.yml` file.

A keyword is a word, which determines the important content of input. Eg. if you add a category called **greetings** with a keyword identifier *hello* and the input is a sentence *Hello, nice to meet you!*, the code will identify *hello* as a keyword from the **greetings** category and respond accordingly. See `data.yml` for more information.


## How to implement

Clone the repository or download `chatbot.py` and `data.yml`. Then, in your code, import using `import chatbot` and generate a response based on input using `chatbot.response(your_input)`.
You can then try to edit `data.yml` to add some behavior, for example add more categories, responses, identifiers or even more question types.


## Notes

This is my first public repository on github and it's just a small, fun project of mine, so don't expect anything amazing :-)
