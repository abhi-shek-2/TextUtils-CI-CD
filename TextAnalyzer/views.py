from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import render
from datetime import datetime
from TextAnalyzer.models import Contact
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Message has been sent')
    return render(request, 'contact.html')


def analyze(request):
    a=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    captialize=request.POST.get('captialize','off')
    Newlineremover=request.POST.get('Newlineremover','off')
    Spaceremover=request.POST.get('Spaceremover','off')
    Charcount=request.POST.get('Charcount','off')
    numberremover=request.POST.get('numberremover','off')
    # analyzed= a
    if removepunc == "on":
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~|/'''
        analyzed= ""
        for char in a:
            if char not in punctuations:
                analyzed = analyzed+char
        params={'purpose':'Removed punctuations',"analyzed_text":analyzed}
        a= analyzed
        # return render(request,'analyze.html',params)

    if(captialize=="on"):
        analyzed= ""
        for char in a:
            analyzed= analyzed + char.upper()
        params={'purpose':'captialize ',"analyzed_text":analyzed}
        a= analyzed
        # return render(request,'analyze.html',params)

    if(Newlineremover=="on"):
        analyzed= ""
        for char in a:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params={'purpose':'Newlineremover ',"analyzed_text":analyzed}
        a= analyzed
        # return render(request,'analyze.html',params)

    if(numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in a:
            if char not in numbers:
                analyzed = analyzed + char
        
        params = {'purpose': 'numberremover', 'analyzed_text': analyzed}
        a = analyzed

    if(Spaceremover=="on"):
        analyzed= ""
        for index,char in enumerate(a):
            if a[index] == " " and a[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params={'purpose':'Spaceremover ',"analyzed_text":analyzed}
        a= analyzed
        # return render(request,'analyze.html',params)

    if(Charcount=="on"):
        analyzed = len(a)
        params={'purpose':'Charcount ',"analyzed_text":analyzed}

    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in a:
            if char not in numbers:
                analyzed = analyzed + char
        
        params = {'purpose': 'numberremover', 'analyzed_text': analyzed}
        a = analyzed

    if(removepunc != "on" and captialize!="on" and Newlineremover!="on" and Spaceremover!="on" and Charcount!="on" and numberremover!="on"):
        return HttpResponse("Error,Try again")

    return render(request,'analyze.html',params)
