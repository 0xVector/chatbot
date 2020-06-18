# main chatbot file
import re
from random import choice
from unidecode import unidecode
import yaml


def normalize(text_input):
    return ''.join(
        c for c in unidecode(text_input).lower() if ord(c) in range(97, 123) or ord(c) == 32).lstrip().rstrip()


def find_whole_word(w):
    return re.compile(r'\b({0})\b'.format(re.escape(w))).search


def response(text_input):  # main function

    foundQuestionType, foundCategory = None, None

    text_input = normalize(text_input)

    for question_type in question_types:
        for identifier in question_types[question_type]:
            match = find_whole_word(identifier)(text_input)
            if match:
                foundQuestionType = question_type

    for category in categories:
        for identifier in categories[category]:
            match = find_whole_word(identifier)(text_input)
            if match:
                foundCategory = category

    if foundCategory is not None:  # we have some category

        # if we also have a question type and there is a response for it
        if foundQuestionType is not None and foundQuestionType in data["categories"][foundCategory]["responses"]:
            generated_response = choice(data["categories"][foundCategory]["responses"][foundQuestionType])

        else:  # use a default response
            generated_response = choice(data["categories"][foundCategory]["responses"]["default"])

    else:
        generated_response = choice(data["error_responses"])  # return random error response

    return generated_response


# ===  loading the yml file  ===

with open("data.yml") as file:
    data = yaml.full_load(file)

    # dicts which contain category and identifiers for that category
    question_types = {}
    categories = {}

    # loop through all question types
    for question_type in data["question_types"]:
        question_types[question_type] = []  # add a new list for identifiers

        # loop through all identifiers for that q. type
        for identifier in data["question_types"][question_type]["identifiers"]:
            question_types[question_type].append(identifier)  # add that identifier

    # the same with categories
    for category in data["categories"]:
        categories[category] = []
        for identifier in data["categories"][category]["identifiers"]:
            categories[category].append(identifier)

# delete unnecessary stuff (we keep data so we don't have to load it again)
del file, category, question_type, identifier

#  ======

if __name__ == "__main__":
    while True:
        print(response(input()))
