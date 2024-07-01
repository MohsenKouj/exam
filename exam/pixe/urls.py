from django.urls import path,include
from pixe.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',post,name='post'),
    path('single/s-<int:ids>',single,name='single'),
    path('category/<str:name>',post,name='category'),
    path('publisher/<str:namep>',post,name='publisher'),
]
