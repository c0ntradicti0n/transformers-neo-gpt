from transformers import pipeline
import os

model_name = os.environ["model_name"] if "model_name" in os.environ else 'EleutherAI/gpt-neo-125M'
generator = pipeline('text-generation', model=model_name)


def f(intent=None, userinput=None, **other_kwargs):
    string = query=userinput if userinput else intent
    text = "".join(intent.split()[:10])
    output = (generator(text, do_sample=True, min_length=50))
    print (f"Made this new idea {output}")
    return {
        "idea": output
    }
