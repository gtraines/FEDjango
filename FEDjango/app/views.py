"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Welcome',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def services(request):
    """
    :param request:
    :return:
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/services.html',
        context_instance = RequestContext(request,
        {
            'title':'Services',
            'message':'Services provided by Friendly Element.'
            #'year':datetime.now().year,
        })
    )

def blog(request):
    """
    :param request:
    :return:
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        context_instance = RequestContext(request,
        {
            'title':'Blog',
            'message':'Friendly Element Blog.',
            'year':datetime.now().year,
        })
    )