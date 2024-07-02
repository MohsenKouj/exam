from django import template
from pixe.models import Post
register = template.Library()

@register.simple_tag()
def log():
    return 'just log'

@register.inclusion_tag('incl.htm')
def categoris():
    post = Post.objects.filter(status=True)
    return {'post': post}

@register.inclusion_tag('latest-post.html')
def latepost():
    post = Post.objects.filter(status=True).order_by('p_date').reverse()[:6]
    return {'post': post}
    
