from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound
from .models import *
import datetime as dt

now = dt.datetime.now()
class dataAdapt:
    context = dict(post = list())
    def __init__(self,id,publisher,date_modified,c_views,title,disc):
        self.id = id
        self.publisher = publisher
        self.date_modified = date_modified
        self.c_view = c_views
        self.title = title
        self.disc = disc

    def delete(self):
        del self.id
        del self.publisher
        del self.date_modified
        del self.c_view
        del self.title
        del self.disc
 
       
# Create your views here.
def post(request):
    #rdate = now.year + now.month + now.day + now.hour + now.minute + now.second + now.microsecond
    rdate = now.timestamp()
    context = dict(post=list())
    p = Post.objects.all()
    for i in p:
        #ridate = i.date_modified.year + i.date_modified.month + i.date_modified.day + i.date_modified.hour + i.date_modified.minute + i.date_modified.second + i.date_modified.microsecond
        ridate = i.date_modified.timestamp()
        if ridate < rdate:
            context['post'].append(
                dataAdapt(i.id,i.publisher,i.date_modified,i.c_view,i.title,i.disc)
            )
            context['rdate'] = rdate
            context['ridate'] = ridate
            
    return render(request, 'index.html',context)

def single(request,ids):
    p = Post.objects.get(id=ids)
    p.c_view += 1
    p.save()
    if now.timestamp() > p.date_modified.timestamp():
        context = {
            'post':Post.objects.get(id=ids),
            'comments':Comment.objects.all()
            }
        return render(request, 'single.html', context)
    else:
        
        return HttpResponseNotFound(request)
        
        
