from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')


def f(intent=None, **other_kwargs):
    text = "".join(intent.split()[:10])
    print(generator(text, do_sample=True, min_length=50))
