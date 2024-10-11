from django.shortcuts import render

# Create your views here.


def loginPage(request):
    title = 'Home Page'
    return render(request,'index.html',context={'title':title})

def aboutPage(request):
    title = 'About Page'
    return render(request,'about.html',context={'title':title})

def contactPage(request):
    locations = {
        'New_York': 'New York',
        'Los_Angeles': 'Los Angeles',
        'Chicago': 'Chicago',
        'Houston': 'Houston',
        'Miami': 'Miami'
    }
    title = 'Contact Page'
    return render(request,'contact.html',context={'title':title,'locations':locations})