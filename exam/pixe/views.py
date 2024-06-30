from django.shortcuts import render
from django.utils import timezone as tz
from django.http import Http404,HttpResponseNotFound
from .models import *
import datetime as dt

now = tz.now()
class dataAdapt:
    context = dict(post = list())
    def __init__(self,id,publisher,p_date,c_views,title,disc,image,category):
        self.id = id
        self.publisher = publisher
        self.p_date = p_date
        self.c_view = c_views
        self.title = title
        self.disc = disc
        self.image = image
        self.category = category

    def delete(self):
        del self.id
        del self.publisher
        del self.p_date
        del self.c_view
        del self.title
        del self.disc
        del self.image
        del self.category
 
       
# Create your views here.
def post(request):
    #rdate = now.year + now.month + now.day + now.hour + now.minute + now.second + now.microsecond
    rdate = now.timestamp()
    context = dict(post=list())
    p = Post.objects.all()
    for i in p:
        #ridate = i.p_date.year + i.p_date.month + i.p_date.day + i.p_date.hour + i.p_date.minute + i.p_date.second + i.p_date.microsecond
        ridate = i.p_date.timestamp()
        if ridate < rdate and i.status:
            context['post'].append(
                dataAdapt(i.id,i.publisher,i.p_date,i.c_view,i.title,i.disc,i.image,i.category)
            )
            context['rdate'] = rdate
            context['ridate'] = ridate
            
    return render(request, 'index.html',context)

def single(request,ids):
    p = Post.objects.get(id=ids)
    p.c_view += 1
    p.save()
    if now.timestamp() > p.p_date.timestamp() and p.status:
        context = {
            'post':Post.objects.get(id=ids),
            'nextp':Post.objects.get(id=ids+1),
            'prevp':Post.objects.get(id=ids-1),
            'comments':Comment.objects.all()
            }
        return render(request, 'single.html', context)
    else:
        
        return HttpResponseNotFound(request)
        
        
