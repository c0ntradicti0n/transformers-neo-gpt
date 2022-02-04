from transformers import pipeline
import os

model_name = os.environ["model_name"] if "model_name" in os.environ else 'EleutherAI/gpt-neo-125M'
generator = pipeline('text-generation', model=model_name)
length = os.environ["length"] if "length" in os.environ else 150

def f(intent=None, userinput=None, **other_kwargs):
    string = userinput if userinput else intent
    text = "".join(string.split()[:10]).replace('"', '').replace("[", '').replace("]", '')
    print ("text" + string + text)
    output = (generator(text, do_sample=True, min_length=length))
    print (f"Made this new idea {output}")
    return {
        "idea": output
    }
