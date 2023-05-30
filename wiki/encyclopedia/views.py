import markdown2
from django.shortcuts import render
from . import util
import random
from django import forms


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
        return render(request, "encyclopedia/content.html", {
            "topic": topic, "content": converter(topic)
        })


def random_page(request):
    topic_chosen = random.choice(util.list_entries())
    return render(request, "encyclopedia/content.html", {
        "topic": topic_chosen, "content": converter(topic_chosen)
    })


def search_box(request):
    similar_entries = []
    if request.method == "POST":
        search_received = request.POST['q']
        # cross-checking with lower to make sure upper/lower case does not matter
        if search_received.lower() in (name.lower() for name in util.list_entries()):
            return render(request, "encyclopedia/content.html", {
                "topic": search_received, "content": converter(search_received)
            })
        # This block is for checking if the entry is a substring of a page that already exists
        for entry in util.list_entries():
            if search_received.lower() in entry.lower() and search_received != "":
                similar_entries.append(entry)
        return render(request, "encyclopedia/similar.html", {
            "similar_entries": similar_entries,
            "size": len(similar_entries)
        })
