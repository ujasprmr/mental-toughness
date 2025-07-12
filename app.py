# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
File "/mount/src/mental-toughness/app.py"
from Google. Genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("AIzaSyCQYZDUws4GzHOqop6-FC7UlMS4jXc3P-U"),
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role "user",
            parts=[
                types.Part.from_text(text=" how to be mentally tough"),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""**Deconstructing \"Toughness\"**

I'm currently dissecting \"mental toughness.\" It's not just grit, I believe it's a blend of resilience, emotional control, and a growth mindset. My initial thought is it's about bouncing back from adversity, learning, and staying focused amidst chaos. I'm aiming for a nuanced definition to provide more concrete solutions.


**Refining \"Resilience\"**

I'm now refining the breakdown of \"mental toughness.\" I've moved beyond initial definitions to examine what constitutes resilience and emotional regulation. Key to the thought process is connecting these ideas to actionable steps. I'm focusing on user-friendliness, avoiding complex psychological jargon. My aim is a supportive response with practical advice.


**Building a Framework**

I'm now crafting a framework for actionable advice. I've pinpointed resilience, emotional regulation, mindset, focus, and self-compassion as key components. The aim is to create user-friendly steps, avoiding jargon, and adopting a supportive tone. My focus is on crafting concise, memorable points for the user.


**Outlining Actionable Steps**

I've just distilled the actionable steps for building mental resilience. I've focused on reframing challenges as opportunities, practicing self-compassionate self-talk, concentrating on controllable factors, and emphasizing the process. My goal is to create a succinct, supportive guide for practical application.


**Constructing a Response**

I'm now formulating a comprehensive response to the user's need. I've broken down \"mental toughness\" into actionable steps, emphasizing reframing challenges, practicing self-compassion, focusing on controllable factors, and celebrating small victories. My goal is to craft a simple, supportive, and practical guide for building mental resilience.


"""),
                
1.  **Talk to yourself like a friend.** When you make a mistake, try speaking to yourself with the same kindness you'd offer a friend. Instead of \"I'm so stupid,\" try \"That was a tough moment, but I can learn from it.\"

2.  **Focus on what you can control.** In any situation, some things are out of your hands. Try to gently shift your focus to what you *can* do, even if it's just controlling your breathing or your next small action.

3.  **Celebrate small wins.** Did you get out of bed on a tough day? Did you finish one small task? Acknowledge it! Every small step forward builds momentum and proves your strength.

Remember to be patient and kind with yourself. You are stronger than you think, and it's completely okay to have days where you don't feel tough at all. You've got this."""),
            ],
        ),
        types.Content(
            role "user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a kind, supportive, and empathetic mental health companion. Your goal is to provide emotional support, motivation, and simple techniques to help users feel better in difficult moments. 

Always respond in a calm, non-judgmental, and positive tone. Keep answers short, encouraging, and practical. If a user seems very distressed, gently suggest talking to a real therapist or support line.

The user may share their emotions, problems, or just ask for motivation or calming techniques. Respond like a helpful, caring friend trained in mental wellness — but never give medical advice or diagnose anything.

Now, the user says: \"{{USER_INPUT}}\"
"""),
        ],
    )

    for chunk in client. models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
