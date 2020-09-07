import os

from django.conf import settings
from django.http import HttpResponse
from django.template import loader
import static
from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage


def gallery(request):
    t = loader.get_template('gallery.html')
    html = t.render()
    return HttpResponse(html)


def home(request):
    t = loader.get_template('new.html')
    html = t.render()
    return HttpResponse(html)


def contact(request):
    t = loader.get_template('contact.html')
    html = t.render()
    return HttpResponse(html)


def learn(request):
    module_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(module_dir, 'static/course/a1.txt')
    file_path2 = os.path.join(module_dir, 'static/course/b1.txt')
    file_path3 = os.path.join(module_dir, 'static/course/c1.txt')
    content = open(file_path, 'r').read()
    content2 = open(file_path2, 'r').read()
    content3 = open(file_path3, 'r').read()
    t = loader.get_template('amoozesh.html')
    html = t.render({'content': content, 'content2': content2, 'content3': content3})
    return HttpResponse(html)
