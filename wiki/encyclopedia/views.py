import markdown2
from django.shortcuts import render
from markdown2 import Markdown
from . import util

def coverter(topic):
    words = util.get_entry(topic)
    converter_obj = markdown2.Markdown()
    if words == None:
        return None
    else:
        converter_obj.convert(words)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

