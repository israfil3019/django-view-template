from django.shortcuts import render
# from django.http import HttpResponse

# def home_view(request):
#     print(request.META)
#     return HttpResponse("Hello World!")


def home_view(request):
    context = {
        "first_name": "İsrafil",
        "last_name": "T",
    }
    return render(request, "app/home.html", context)
