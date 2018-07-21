from django.shortcuts import render
from django.db.models import Q
from .models import Merchandise
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.




def merchandise_list_view(request):                   #http://127.0.0.1:8000/merchandise_list_view/
    queryset = Merchandise.objects.all()
    context = {'merchandises': queryset}
    query = request.GET.get("q")
    if query:
    	queryset = queryset.filter(
                Q(title__icontains=query)
            ).distinct()
    	return render(request, 'list.html', {
                'merchandises': queryset,
            })
    return render(request, "list.html", context)




def merchandise_detail_view(request, id, *args, **kwargs):    #http://127.0.0.1:8000/merchandise_detail_view/1/
	instance = get_object_or_404(Merchandise, id=id)
	context = {'object': instance}
	return render(request, 'detail.html', context)


