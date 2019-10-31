from _ast import operator

from django.shortcuts import render

def homepage(request):
    return render(request , 'home.html', {'name':'Shubhanshu'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordcount = len(wordlist)
    countdict = {}
    for word in wordlist:
        if word in countdict:
            #increment and skip
            countdict[word] += 1
        else:
            #add to dictio
            countdict[word] = 1

    srtwclist = sorted(countdict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    return render(request , 'count.html', {'fulltext':fulltext,'wordcount':wordcount,'wclist':srtwclist} )
def about(request):
    return render(request, 'about.html')