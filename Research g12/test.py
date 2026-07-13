import google.genai as genai

client = genai.Client(api_key="AQ.Ab8RN6J7CZxd3T-UCaKQzoFF_1rsD4yZbP8kuE-08WaF2KuDvQ")

try:
    response = client.models.generate_content(
        model='gemini-3.1-flash-lite',  # Switched to a lighter, less busy model
        contents='Write a haiku about learning how to code in Python.',
    )
    print("\n--- SUCCESS! ---")
    print(response.text)
    print("----------------\n")

except Exception as e:
    print("\n--- ERROR ---")
    print(e)
    print("-------------\n")