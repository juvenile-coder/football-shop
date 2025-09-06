from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'title' : 'Moovr Sportswear',
        'name': 'Jefferson Tirza Liman',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)