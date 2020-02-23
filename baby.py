import random

questions = ["Why is the sky blue?: ", "How are babies born?: ", "What is your name?: "]

answer = input(random.choice(questions)).strip().lower()

while answer != "just because":
    answer = input("But why?: ").strip().lower()

print("Okie!")
