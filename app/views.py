from django.shortcuts import render

# Create your views here.
def built_in_filters(request):
    import datetime
    r=datetime.datetime.now()
    d={'data':'BaBUbasHA shaik','r':r,'d':2}
    return render(request,'built_in_filters.html',d)