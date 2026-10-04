from google import genai
from google.genai import types

client = genai.Client(api_key="AQ.Ab8RN6IfSfLXSXViNabiTEHnnZonDyFCEBP_5ex6nlRZZP52iw")

print("Chat starts here.... type 'endchat' to close")

userinput = input("User : ")

while userinput != 'endchat':
    systemoutput = client.models.generate_content(
        model='gemini-3.5-flash-lite',
        contents=userinput,
        config=types.GenerateContentConfig(
            system_instruction="Answer in 1 line, within 50 characters"
        ),
    )
    print("Startbot : ", systemoutput.text)
    userinput = input("User : ")