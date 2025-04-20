import pyautogui
import keyboard
import time

# Ensure fail-safe (move cursor to top-left to stop)
pyautogui.FAILSAFE = True

def track_cursor():
    """Track and print mouse coordinates for WhatsApp Web automation."""
    print("Tracking cursor position. Move mouse to desired spots.")
    print("Press 'q' to stop.")
    print("Suggested spots to check:")
    print("- Chrome icon (if opening browser)")
    print("- WhatsApp Web search bar (to type contact name)")
    print("- Message area (to drag-select messages)")
    print("- Click spot after copying (to deselect)")
    print("- Input box (to paste replies)")
    print("\nStarting in 3 seconds...")
    time.sleep(3)

    while not keyboard.is_pressed("q"):
        x, y = pyautogui.position()
        print(f"Cursor: X={x}, Y={y}")
        time.sleep(0.5)  # Update every 0.5 seconds
    print("Stopped tracking. Use these coordinates in whatsapp_bot.py.")

if __name__ == "__main__":  # Corrected entry point
    try:
        track_cursor()
    except KeyboardInterrupt:
        print("Stopped manually.")



# import requests

# api_key = "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"

# url = "https://openrouter.ai/api/v1/chat/completions"
# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }
# payload = {
#     "model": "openrouter/auto",
#     "messages": [
#         {"role": "system", "content": "You are a funny roasting bot."},
#         {"role": "user", "content": "Hey what's up loser?"}
#     ],
#     "temperature": 0.8,
#     "max_tokens": 100
# }

# response = requests.post(url, headers=headers, json=payload)
# print("Status Code:", response.status_code)
# print("Raw response:", response.text)




# import requests
# import json

# api_key = "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"

# url = "https://openrouter.ai/api/v1/chat/completions"
# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }
# payload = {
#     "model": "openai/gpt-3.5-turbo",
#     "messages": [
#         {"role": "system", "content": "You are a funny roast bot."},
#         {"role": "user", "content": "Why are you so dumb?"}
#     ],
#     "temperature": 0.8,
#     "max_tokens": 100
# }

# response = requests.post(url, headers=headers, json=payload)
# print("Status Code:", response.status_code)

# try:
#     data = response.json()
#     print(json.dumps(data, indent=2))  # Pretty print full response
# except Exception as e:
#     print("Failed to parse JSON:", e)
#     print("Raw content:", response.content)



