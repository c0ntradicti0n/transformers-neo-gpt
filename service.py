from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')


def f(intent=None, **other_kwargs):
    print(generator(intent, do_sample=True, min_length=50))
