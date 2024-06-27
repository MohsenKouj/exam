from django.urls import path,include
from pixe.views import *
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',post,name='post'),
    path('single/s-<int:ids>',single,name='single')
]

