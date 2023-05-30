import markdown2
from django.shortcuts import render
from . import util
import random


def converter(topic):
    words = util.get_entry(topic)
    converter_obj = markdown2.Markdown()
    return converter_obj.convert(words)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def content(request, topic):

    words = util.get_entry(topic)
    if words == None:
        return render(request, "encyclopedia/error.html", {
            "topic": topic
        })
    else:
        return render(request, "encyclopedia/content.html",{
            "topic": topic, "content": converter(topic)
        })


def random_page(request):
    topic_chosen = random.choice(util.list_entries())
    return render(request, "encyclopedia/content.html", {
        "topic": topic_chosen, "content": converter(topic_chosen)
    })


