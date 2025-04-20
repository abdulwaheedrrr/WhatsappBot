import pyautogui
import pyperclip
import time
import keyboard
import requests
import re
import json

# Your OpenRouter API key
api_key = "INTER_YOUR_KEY_HERE"
# Make sure to replace with your actual API key

# Enable PyAutoGUI fail-safe
pyautogui.FAILSAFE = True

def is_last_message_from_sender(chat_log, your_name="Your Name"):
    """Check if the latest message is from another user (not you)."""
    messages = chat_log.strip().split("\n")
    for line in reversed(messages):
        if re.match(r"\d{1,2}:\d{2}(?: [AP]M)?, \d{2}/\d{1,2}/\d{4} .+:", line):
            if your_name in line:
                return False
            return True
    return False

def generate_response(chat_history):
    """Generate a roasting reply using OpenRouter API."""
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "openai/gpt-3.5-turbo",  # Specific model known to work
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are Abdul Waheed, a coder from Kashmir who speaks Urdu and English. "
                        "You roast people in a funny, friendly way like a CS student in a WhatsApp group chat. "
                        "Respond with a short, witty text message (no timestamps or sender prefixes). "
                        "Use emojis and keep it savage but chill."
                    )
                },
                {"role": "user", "content": chat_history}
            ],
            "temperature": 0.8,
            "max_tokens": 100
        }

        response = requests.post(url, headers=headers, json=payload)
        print("Status Code:", response.status_code)  # Debugging output
        print("Full Response:", response.text)      # Debugging output

        # Attempt to parse the response JSON
        data = response.json()
        return data["choices"][0]["message"]["content"]
    
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print("Raw Response Text:", response.text)
        return "Error in JSON parsing. Check the API response format."
    except Exception as e:
        print(f"API Error: {e}")
        return "Arre, your messages are buggier than my old C++ code! Try again!"

def chatbot():
    """Main loop: Automate WhatsApp Web and reply with roasts."""
    # Your screen coordinates (adjust for your system)
    taskbar_icon_x, taskbar_icon_y = 1063, 1051
    search_bar_x, search_bar_y = 997, 168
    select_start_x, select_start_y = 1400, 151
    select_end_x, select_end_y = 1865, 917
    click_after_copy_x, click_after_copy_y = 1396, 489
    input_box_x, input_box_y = 1551, 979

    print("Opening WhatsApp Web...")
    pyautogui.click(taskbar_icon_x, taskbar_icon_y)
    time.sleep(1)

    contact_name = "scom"
    pyautogui.click(search_bar_x, search_bar_y)
    time.sleep(2)
    pyautogui.typewrite(contact_name)
    pyautogui.press("enter")
    time.sleep(1)

    print("Chatbot running. Press 'q' to stop.")
    while not keyboard.is_pressed("q"):
        try:
            # Copy chat text
            pyautogui.moveTo(select_start_x, select_start_y)
            pyautogui.dragTo(select_end_x, select_end_y, duration=1.0, button="left")
            time.sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            time.sleep(1)
            pyautogui.click(click_after_copy_x, click_after_copy_y)
            time.sleep(1)

            chat_history = pyperclip.paste()
            print("Chat History:", chat_history)

            if is_last_message_from_sender(chat_history, your_name="Your Name"):
                print("Last message is from another user!")

                response = generate_response(chat_history)
                print("Generated Roast:", response)

                pyperclip.copy(response)
                pyautogui.click(input_box_x, input_box_y)
                time.sleep(1)
                pyautogui.hotkey("ctrl", "v")
                time.sleep(0.5)
                pyautogui.press("enter")
                time.sleep(1)
            else:
                print("No new message from another user.")

            time.sleep(2)
        except Exception as e:
            print(f"Error in loop: {e}")
            time.sleep(10)

    print("Chatbot stopped.")

if __name__ == "__main__":
    try:
        chatbot()
    except KeyboardInterrupt:
        print("Chatbot stopped manually.")