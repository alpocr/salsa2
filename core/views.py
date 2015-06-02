from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponse


from core.models import Record

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html', {})


@login_required
def calendar(request):
    return render(request, 'calendar.html', {})



class AddBookToCalendar(TemplateView):
    
    def post(self, request, *args, **kwargs):
        bookname = request.POST.get('bookname')
        read_from = request.POST.get('read_from')
        read_until = request.POST.get('read_until')
        obj, created = Record.objects.get_or_create(book=bookname, student=request.user,
                                                   read_from=read_from, read_until=read_until)
        if created:
            return HttpResponse()
        else:
            return HttpResponse(status=404)
        
        

class RecordList(ListView):
    model = Record
    template_name = "list.html"
    
    def get_queryset(self):
        return Record.objects.filter(student=self.request.user)
    