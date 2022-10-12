import random


def get_choices():
  options = ["goz", "fard"]
  p_choice = input("Enter a choice (goz,fard):")
  c_choice = random.choice(options)
  choices = {"Player": p_choice, "Computer": c_choice}
  return choices

choices = get_choices()
print (choices)