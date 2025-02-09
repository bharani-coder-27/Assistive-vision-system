from image_processing import capture_image, detect_objects
from speech_processing import listen_and_transcribe, speak
from ai_integration import get_ai_suggestions

initial_context = "You are a guider for blind people. The user will ask about their surroundings, and you should provide appropriate guidance based on what is detected in the environment."

def main():
    print("System ready. Say 'What about the surroundings?' to get information about your surroundings.")
    
    while True:
        user_input = listen_and_transcribe()

        
        if user_input and "what about the surroundings" in user_input.lower():
            try:
                frame_rgb = capture_image()
                detected_objects = detect_objects(frame_rgb)
                
                feedback = []
                if detected_objects:
                    for obj, dist in detected_objects:
                        feedback.append(f"Object: {obj}, Distance: {dist:.2f} inches")
                else:
                    feedback.append("No significant objects detected directly in front of you.")
                
                feedback_text = " ".join(feedback)
                print(feedback_text)
                speak(feedback_text)

                
                prompt = f"{initial_context} The user asked about their surroundings, and here is what was detected: {feedback_text}. What further guidance can you provide?"
                ai_suggestions = get_ai_suggestions(prompt)
                print(ai_suggestions)
                speak(ai_suggestions)

            except Exception as e:
                print(f"Error: {e}")
                speak("Sorry, I could not capture the image. Please try again.")

        
        elif user_input:
            if "exit" in user_input.lower():
                print("Exiting...")
                break
            else:
                prompt = f"The user said: {user_input}. Provide guidance based on this input."
                ai_suggestions = get_ai_suggestions(prompt)
                print(ai_suggestions)
                speak(ai_suggestions)

if __name__ == "__main__":
    main()