from typing import Any
from django.shortcuts import render
from django.utils import timezone as tz
from django.http import Http404,HttpResponseNotFound
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
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
def post(request,name=None,namep=None):
    #rdate = now.year + now.month + now.day + now.hour + now.minute + now.second + now.microsecond
    rdate = now.timestamp()
    p = Post.objects.filter(status=1)
    
    if name:
        p = p.filter(category__name=name)
    elif namep:
        p = p.filter(publisher=namep)
    ps = Paginator(p,3)
    
    try:
        pn = request.GET.get('pages')
    except PageNotAnInteger:
        pn = 1
    except EmptyPage:
        pn = 1
        
        
    p = ps.get_page(pn)
    return render(request, 'index.html',{'posts': p,'pages':ps})



def single(request,ids):
    class id_:
        i = []
        def I(self):
            return self.i
        def index(self,indx):
            if indx == "down":
                return -2
            elif indx == "up":
                return -1
            else:
                return self.i[indx]
    id_ = id_()
    ps = Post.objects.filter(status=True)
    for i in ps:
        if i.p_date.timestamp() < now.timestamp():
            id_.i.append(i)
    p = Post.objects.get(id=ids)
    p.c_view += 1
    p.save()
    realindex = id_.i.index(p)

    def conc(l,rindex):
        if rindex > l.__len__()-1:
            return "up"
        elif rindex < 0:
            return "down"
        else:
            return rindex
    
        
    if now.timestamp() > p.p_date.timestamp() and p.status:
        context = {
            'post':Post.objects.get(id=ids),
            'nextp':id_.index(conc(id_.i,realindex+1)),
            'prevp':id_.index(conc(id_.i,realindex-1)),
            'comments':Comment.objects.all(),
            }
        return render(request, 'single.html', context)
    else:
        
        return HttpResponseNotFound(request)
        
        
def cat(request,name):
    p = Post.objects.filter(status=1)
    p = p.filter(category__name=name)
    return render(request, 'index.html',{'post':p})

def search_post(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(disc__contains=s)
            
    return render(request, 'index.html',{'post':posts})

def loging(request):
    return render(request, 'login-form.html')