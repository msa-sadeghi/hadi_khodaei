from django.shortcuts import render


def index(request):
    name = request.GET.get("name", "golang")
    print(request)
    return render(request, "reviews/base.html", {"name": name})
