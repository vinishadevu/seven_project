from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':200,'b':1000,'c':300}
    return render(request,'conditions.html',d)


def looping(request):
    d={'name':'vinni'}
    return render(request,'looping.html',d)