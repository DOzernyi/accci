import random

class FlashcardApp:
    def __init__(self, flashcard_sets):
        self.flashcard_sets = flashcard_sets
        self.score = 0
        self.wrong_answers = set()

    def start(self):
        print("Welcome to the Flashcard Learning App!")

        # Display available flashcard sets
        print("Available Flashcard Sets:")
        for i, flashcard_set in enumerate(self.flashcard_sets, 1):
            print("{}. {}".format(i, flashcard_set['name']))

        # Prompt user to choose a flashcard set
        while True:
            try:
                set_choice = int(input("Enter the number of the flashcard set you want to use: "))
                selected_set = self.flashcard_sets[set_choice - 1]['cards']
                break
            except (ValueError, IndexError):
                print("Invalid choice. Please enter a valid number.")

        flashcard_list = list(selected_set.items())
        random.shuffle(flashcard_list)  # Shuffle the flashcards

        while flashcard_list:
            current_flashcard = flashcard_list.pop(0)
            self.show_flashcard(current_flashcard)

            user_input = input("Your answer (enter 'q' to quit): ")

            if user_input.lower() == 'q':
                break

            if user_input.lower() == current_flashcard[1].lower():
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect. The correct answer is: {}".format(current_flashcard[1]))
                self.wrong_answers.add((current_flashcard[0], user_input))
            print()

        print("Game Over. Your Final Score: {}".format(self.score))
        if self.wrong_answers:
            print("\nList of Wrong Answers:")
            for question, user_answer in self.wrong_answers:
                print("Question: {}, Your Answer: {}".format(question, user_answer))

    def show_flashcard(self, flashcard):
        print("Question: {}".format(flashcard[0]))

if __name__ == "__main__":
    flashcard_sets = [
        {
            'name': 'Geography Set',
            'cards': {
                "What is the capital of France?": "Paris",
                "What is the largest mammal in the world?": "Blue Whale",
                "What is the square root of 25?": "5",
                # Add more flashcards as needed
            }
        },
        {
            'name': 'Science Set',
            'cards': {
                "Who is the author of 'Romeo and Juliet'?": "William Shakespeare",
                "What is the chemical symbol for gold?": "Au",
                "What is the largest planet in our solar system?": "Jupiter",
                # Add more flashcards as needed
            }
        },
        # Add more flashcard sets as needed
    ]

    app = FlashcardApp(flashcard_sets)
    app.start()
