import markdown2
from django.shortcuts import render
from . import util


def converter(topic):
    words = util.get_entry(topic)
    converter_obj = markdown2.Markdown()
    if words == None:
        return None
    else:
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

