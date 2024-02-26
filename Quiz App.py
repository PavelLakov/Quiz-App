

import tkinter as tk
import random

# List of questions and their correct answers. Each entry is a dictionary.
questions_original = [
  # Each dictionary contains a question (key) and its answer (value).
  {"What is the capital of Germany?": "Berlin"},
  {"What is the capital of Bulgaria?": "Sofia"},
  {"what is the capital of Germany?": "Berlin"},
  {"what is the capital of Bulgaria?": "Sofia"},
  {"what is the capital of France?": "Paris"},
  {"what is the capital of Belgium?": "Brussels"},
  {"what is the capital of United Arab Emirates?": "Abu Dhabi"},
  {"what is the capital of Nigeria?": "Abuja"},
  {"what is the capital of Ghana?": "Accra"},
  {"what is the capital of Pitcairn Islands?": "Adamson"},
  {"what is the capital of Ethiopia?": "Addis Ababa"},
  {"what is the capital of Algeria?": "Algiers"},
  {"what is the capital of Niue?": "Alofi"},
  {"what is the capital of Jordan?": "Amman"},
  {"what is the capital of Netherlands?": "Amsterdam"},
  {"what is the capital of Andorra?": "Andorra la Vella"},
  {"what is the capital of Turkey?": "Ankara"},
  {"what is the capital of Madagascar?": "Antananarivo"},
  {"what is the capital of Samoa?": "Apia"},
  {"what is the capital of Turkmenistan?": "Ashgabat"},
  {"what is the capital of Eritrea?": "Asmara"},
  {"what is the capital of Kazakhstan?": "Astana"},
  {"what is the capital of Paraguay?": "Asunción"},
  {"what is the capital of Greece?": "Athens"},
  {"what is the capital of Cook Islands?": "Avarua"},
  {"what is the capital of Iraq?": "Baghdad"},
  {"what is the capital of Azerbaijan?": "Baku"},
  {"what is the capital of Mali?": "Bamako"},
  {"what is the capital of Brunei?": "Bandar Seri Begawan"},
  {"what is the capital of Thailand?": "Bangkok"},
  {"what is the capital of Central African Republic?": "Bangui"},
  {"what is the capital of Gambia?": "Banjul"},
  {"what is the capital of Saint Kitts and Nevis?": "Basseterre"},
  {"what is the capital of China?": "Beijing"},
  {"what is the capital of Lebanon?": "Beirut"},
  {"what is the capital of Serbia?": "Belgrade"},
  {"what is the capital of Belize?": "Belmopan"},
  {"what is the capital of Switzerland?": "Bern"},
  {"what is the capital of Kyrgyzstan?": "Bishkek"},
  {"what is the capital of Guinea-Bissau?": "Bissau"},
  {"what is the capital of Colombia?": "Bogotá"},
  {"what is the capital of Brazil?": "Brasília"},
  {"what is the capital of Slovakia?": "Bratislava"},
  {"what is the capital of Republic of the Congo?": "Brazzaville"},
  {"what is the capital of Barbados?": "Bridgetown"},
  {"what is the capital of Belgium?": "Brussels"},
  {"what is the capital of Romania?": "Bucharest"},
  {"what is the capital of Hungary?": "Budapest"},
  {"what is the capital of Argentina?": "Buenos Aires"},
  {"what is the capital of Burundi?": "Bujumbura"},
  {"what is the capital of Egypt?": "Cairo"},
  {"what is the capital of Australia?": "Canberra"},
  {"what is the capital of Venezuela?": "Caracas"},
  {"what is the capital of Saint Lucia?": "Castries"},
  {"what is the capital of French Guiana?": "Cayenne"},
  {"what is the capital of United States Virgin Islands?": "Charlotte Amalie"},
  {"what is the capital of Moldova?": "Chisinau"},

  # Add more questions here following the same format.
]


# This function copies the original questions list to refresh the available questions.
def reload_questions():
  return questions_original.copy()


# Initialize variables to store the current state of the quiz.
questions = reload_questions()  # Load the initial set of questions.
questions_answered = 0  # Keep track of how many questions have been answered.
current_question = {}  # Store the current question being asked.


# Function to select and display the next question.
def get_next_question():
  global current_question, questions_answered
  if not questions:  # Check if the questions list is empty.
    questions.extend(reload_questions())  # Reload questions if all have been asked.
  current_question = random.choice(questions)  # Randomly select a question.
  questions.remove(current_question)  # Remove the selected question to avoid repetition.

  # Update UI elements to show the new question and clear the previous answer.
  question_label.config(text=list(current_question.keys())[0])
  answer_entry.delete(0, tk.END)
  result_label.config(text="")
  root.bind('<Return>', check_answer)  # Rebind the Return key to check the answer.


# Function to check the user's answer against the correct answer.
def check_answer(event=None):
  global questions_answered
  # Get the user's answer and convert it to lowercase for case-insensitive comparison.
  user_answer = answer_entry.get().strip().lower()
  correct_answer = list(current_question.values())[0].lower()

  # Update the result label based on the correctness of the user's answer.
  if user_answer == correct_answer:
    result_label.config(text="Correct!")
  else:
    result_label.config(text=f"Incorrect. The correct answer is {list(current_question.values())[0]}.")

  questions_answered += 1  # Increment the count of answered questions.

  # Determine if it's time to ask the user if they want to continue after every 3 questions.
  if questions_answered % 3 == 0:
    root.after(1000, ask_continue)  # Delay before asking to continue.
  else:
    root.after(1000, get_next_question)  # Delay before showing the next question.


# Prompt the user to decide if they want to continue playing.
def ask_continue():
  result_label.config(text="Do you want to continue? Yes/No")
  answer_entry.delete(0, tk.END)
  root.bind('<Return>', handle_continue_response)  # Bind Return key to handle the user's response.


# Handle the user's decision to continue or not.
def handle_continue_response(event=None):
  response = answer_entry.get().strip().upper()  # Get and standardize the user's response.
  if response == "YES":
    root.after(300, get_next_question)  # Continue with next question.
  elif response == "NO":
    end_game()  # End the game if the user decides to stop.


# Function to end the game gracefully.
def end_game():
  result_label.config(text="Thank you for playing!")
  answer_entry.config(state='disabled')  # Disable the answer entry field.
  root.after(1700, root.destroy)  # Close the application after a short delay.


# Initialize the main application window.
root = tk.Tk()
root.title("Quiz Game")

# Configure the window size.
root.geometry("500x400")  # Width x Height

# Create and arrange the UI elements.
question_label = tk.Label(root, text="Press Enter to start", wraplength=400)
question_label.pack(pady=20)

answer_entry = tk.Entry(root)
answer_entry.pack()

result_label = tk.Label(root, text="", wraplength=400)
result_label.pack(pady=20)

# Bind the Return key to start the game or check the answer, depending on the game state.
root.bind('<Return>', lambda event: get_next_question() if not current_question else check_answer())

# Start the Tkinter event loop.
root.mainloop()
