from django.shortcuts import render
#from .models import Menu

def index(request):
    return render(request, "index.html", {})

#def menu(request):
#    menu_data = Menu.objects.all()
#    main_data = {"menu": menu_data}
#    return render(request, "menu.html", {"menu": main_data})
