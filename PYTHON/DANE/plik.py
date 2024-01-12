# -*- coding: utf-8 -*-
# import packages:
import json
import openai

openai.api_key = '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'

def get_content(in_prompt):
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=in_prompt,
                                        temperature=0,
                                        max_tokens=3900)
    return response

if __name__ == "__main__":
    # in_prompt = input("Insert text: ")

    questions_list = ["How to learn Python?",
                     "What is your favorite film?",
                     "Can you write a program?"]
    answers_list = []

    for i in questions_list:
        content_json = get_content(i)
        content_text = content_json["choices"][0]["text"]
        answers_list.append(content_text)

    # Result as text
    for j in answers_list:
        print(j)

