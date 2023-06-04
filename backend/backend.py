import os
import openai

import tiktoken


from fastapi import FastAPI, WebSocket

openai.api_key = os.getenv('OPENAI_API_KEY')

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")



storyteller = """
            You are Evandor, the Fablemaster, a professional storyteller inventing fairytales for an audience (me). 
            You tell a infinite, neverending story that stays interesting all the time.
            You develop the story slowly from paragraph to paragraph. 
            You develop the characters with a lot of attention to details and give them chracteristic traits.
            You do not use to many stereotypes, instead form complex characters that have light and dark traits.
            You create a capturing intriguing story following best practices of story writing in subsequent steps. 

            First, state who you are and what is your mission.
            Let characters interact based on the given traits, leading to realistic dialogues.
            Inside the story you use a fair amount of literal speech.
            First, you describe the setting, where, and when is the story happening? 
            Explain the settings to orient the audience and yourself.             
            Write a maximum of 5 sentences in each iteration.
            Rember to tell an infinite story with no ending.
        """

HISTORY = [
    {"role": "system", 
     "content": """
     
     You are a guide telling an interactive free story where people can do anything they want.
     Ask me in what world the story is taking place. 
     I am the main character in your story, and I can act and talk to the characters in your story.
     When someone talks to me, you use litteral speech, then you ask me what I want to say or do.
     when I enter a new scene you desribe the environment with some detail.
     I cannot determine or predict the future.
     I cannot dictate the outcome of something.
     I cannot do things beyond my abilities, I am not almighty, you are determining what is posible and what not.
     Ask me what I want to do next, and don't assume any actions.
     If I suggest something might exists even though you did not talk about it in the past, please double check that it is factual, and possibly deny the request.
     There is a variety of races and groups, players can be anything.
     First you should ask me questions about the universe, followed by my character. What races are there, what specializations, age, gender, am I comming from a rich background, 
     poor, royal?? If I am a priest what deity do I serve? Mention the deities which are available. Ask this questions one by one and refine the ansers. 
     Then provide a summary of the main character and its abilitys and equiptment.
     Finally, let the game begin!
     """
    },
]



def get_answer(text):
    global HISTORY
    HISTORY.append({"role": "user", "content": text})

    print(len(HISTORY))

    print(f'N tokens: {len(encoding.encode(str(HISTORY)))}' )
    summarize_history()
    print(f'N tokens: {len(encoding.encode(str(HISTORY)))}' )


    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=HISTORY,
        #max_tokens=500

    )

    answer = completion.choices[0].message['content']
    HISTORY.append({"role": "assistant", "content": answer})

    
    return answer


def summarize_history():
    global HISTORY

    if len(HISTORY) >= 36:
        
        print('Summarizing history')
        # Generate summary only for messages from index 1 to 19
        summary_prompt = " ".join([message["content"] for message in HISTORY[1:20]]) + "\n\nSummarize this conversation:"

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a skilled summarizer. Please create a concise summary of the following conversation. take notes, use as little words as possible"}, 
                    {"role": "user", "content": summary_prompt}],
             max_tokens=500
        )

        summary = completion.choices[0].message['content']

        # Replace messages from index 1 to 19 with the summary
        HISTORY[1:40] = [{"role": "assistant", "content": summary}]


app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        text = await websocket.receive_text()
        answer = get_answer(text)
        await websocket.send_text(answer)