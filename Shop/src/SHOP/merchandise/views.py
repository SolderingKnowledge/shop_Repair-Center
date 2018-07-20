from django.shortcuts import render
from .models import Merchandise
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.




def merchandise_list_view(request):                   #http://127.0.0.1:8000/merchandise_list_view/
    queryset = Merchandise.objects.all()
    context = {'object_list': queryset}
    return render(request, "index.html", context)



def merchandise_detail_view(request, id, *args, **kwargs):    #http://127.0.0.1:8000/merchandise_detail_view/1/
	instance = get_object_or_404(Merchandise, id=id)
	context = {'object': instance}
	return render(request, 'index.html', context)


