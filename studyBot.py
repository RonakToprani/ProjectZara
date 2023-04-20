import openai

class Chatbot:
    def __init__(self, name, api_key):
        # Initialize chatbot's state
        self.state = "INITIAL"

        # Set up OpenAI API with API key
        openai.api_key = api_key

    def get_response(self, input_text):
        if self.state == "INITIAL":
            # Greet the user and prompt for input
            response = "Hey, I'm Zara, a friendly StudyBot designed to help you with homework problems. How could I assist you today?"
            self.state = "WAITING_INPUT"
        elif self.state == "WAITING_INPUT":
            
            # Send user input to OpenAI API to generate a response
            prompt = "You are a tutor that always responds in the Socratic style. You never give the student the answer, but always try to ask just the right question to help them learn to think for themselves. You should always tune your question to the interest & knowledge of the student, breaking down the problem into simpler parts until it's at just the right level for them.\n\nInput: " + input_text + "\nTutor:"
            api_response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.7
            ).choices[0].text.strip()
            response = "As a tutor who always responds in the Socratic style, I would ask: " + api_response
        else:
            # Return an error message and reset the chatbot's state
            response = "I'm sorry, there seems to be an issue. Please try again later."
            self.state = "INITIAL"
        return response
