from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from kogni.models import scenariy,Node_log, Node_men, Node_mar
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


import sys
sys.path.insert(0, 'fixed_nirm3')
from fixed_nirm3.recount import main,main1,main2



class KogniView(TemplateView):
    template_name = 'kogni/home.html'


def ska(requset):
    output = main()
    return HttpResponse('Работает')

def home (request):
    karti_list = scenariy.objects.all()
    paginator = Paginator(karti_list, 3)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        karti = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        karti = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        # если страница первая то отображает базовый путь
        karti = paginator.page(paginator.num_pages)
    if page == '1':
        return redirect('kogni:home', permanent=True)
    context = {
        'title':'Выбор карты',
        'karti': karti,
     }
    return render(request,'kogni/home.html', context)



def karti_detail (request, karti_id):
    karti_item = get_object_or_404(scenariy, pk=karti_id)
    context = {
        'page_header': karti_item.title,
        'karti_item': karti_item,
    }
    return render(request,'kogni/kogni_detail.html', context)
    #return HttpResponse ('Karti detail page' + karti_id)


def my_view(request):
    output = main()
    return render(request, 'kogni/sim7.html')

def my_react11(request):
    output = main1()
    return render(request, 'kogni/react_11.html')

def my_react12(request):
    output = main2()
    return render(request, 'kogni/react_12.html')


def gorin (request):
    return render(request, 'kogni/gorin.html')


def my_int(request):
    context = {
        'manag':Node_men.objects.all(),
    }
    return render(request, 'kogni/int_test.html', context)
