from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import helpers

class NewImageForm(forms.Form):
    query = forms.CharField(widget = forms.TextInput(attrs={'class' : 'form-box'}), label= "Image name", required=False)
    amount = forms.IntegerField(widget = forms.TextInput(attrs={'class' : 'form-box'}), label= "Number of images (15 at most)", min_value = 1, max_value = 15)
    site = forms.URLField(label = "site to search in")

def index(request):
    return render(request, "ImageSearcher/index.html", {
        "form": NewImageForm
    })

def results(request):
    form = NewImageForm(request.POST)
    if form.is_valid():
        query = form.cleaned_data["query"]
        amount = form.cleaned_data["amount"]
        site = form.cleaned_data["site"]

        images, site = helpers.get_images(site, query)

        if images == "Url not found":
            return HttpResponse(images)

        return render(request, "ImageSearcher/results.html", {
            "images": images[:amount],
            "url": site
        })
    
    else:
        return render("GET", "ImageSearcher/index.html", {
            form: form
        })