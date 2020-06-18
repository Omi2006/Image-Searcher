from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import helpers

class NewImageForm(forms.Form):
    query = forms.CharField(widget = forms.TextInput(attrs={'class' : 'form-box'}) ,label= "Image name")
    amount = forms.IntegerField(widget = forms.TextInput(attrs={'class' : 'form-box'}), label= "Number of images (15 at most)", min_value = 1, max_value = 15)

def index(request):
    return render(request, "ImageSearcher/index.html", {
        "form": NewImageForm
    })

def results(request):
    form = NewImageForm(request.POST)
    if form.is_valid():
        query = form.cleaned_data["query"]
        amount = form.cleaned_data["amount"]

        images, url = helpers.get_images(query)

        return render(request, "ImageSearcher/results.html", {
            "images": images[:amount],
            "url": url
        })