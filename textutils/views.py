# I have created this file - Komal

from django.http import HttpResponse

# def index(request):
#     return HttpResponse('''<h1>Komal</h1>  <a href="https://www.codewithharry.com/"> codewithharry</a>''')
#
#
# def about(request):
#     return HttpResponse("About")

from django.shortcuts import render

# code for laying pipe
def index(request):
    return render(request, 'index2.html')

def analyze(request):
    # Get The Text
    djtext=request.POST.get('text','default')

    # check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    # check which checkbox is on
    if removepunc=="on":
        punctuations='''!()-[]{}:"';\,<>,/.@#$%^&*_'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':"Removed Punctuations",'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if fullcaps=="on":
         analyzed=""
         for char in djtext:
            analyzed=analyzed+char.upper()
         params={'purpose':'Change to Upper Case','analyzed_text':analyzed}
         djtext=analyzed
         # return render(request,'analyze.html',params)

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params={'purpose':'Remove New Line','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if extraspaceremover=="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'Remove Extra Space','analyzed_text':analyzed}
        # djtext=analyzed

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)