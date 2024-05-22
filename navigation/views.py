from django.shortcuts import render
import datetime
# Create your views here.

def about(request):
    d = {'author': 'novo', 'age': 10, 'list':['python', 'is', 'best'], 'date':datetime.datetime.now(), 'courses': [
        {
            'id': 1,
            'name': 'Python',
            'fee': 1000
        },
        {
            'id': 2,
            'name': 'C++',
            'fee': 5000
            
        },
        {
            'id': 3,
            'name': 'Django',
            'fee': 6000
        },
    ]}
    return render(request,'navigation/about.html', context=d)

def contact(request):
    return render(request,'navigation/contact.html')