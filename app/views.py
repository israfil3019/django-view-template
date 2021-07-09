from django.shortcuts import render
# from django.http import HttpResponse

# def home_view(request):
#     print(request.META)
#     return HttpResponse("Hello World!")


def home_view(request):
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }

    return render(request, "app/home.html", context)
