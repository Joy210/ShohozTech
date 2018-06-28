from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.http import HttpResponseRedirect

# Same App importing
from .models import Post
from .forms import PostForm


# Function-Based views
def posts_create(request):
    """Creating Posts using model form"""
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'form': form}
    return render(request, 'posts/post_form.html', context)


def posts_details(request, details_id):
    """Displaying single item"""
    instance = get_object_or_404(Post, id=details_id)
    context = {
        'title': instance.title,
        'instance': instance,
    }
    template = 'posts/details.html'
    return render(request, template, context)


def posts_lists(request):
    """Displaying all items"""
    queryset = Post.objects.all()
    context = {
        'title': 'List',
        'object_list': queryset,
    }
    template = 'posts/index.html'
    return render(request, template, context)


def posts_update(request, update_id):
    """Updating individual item"""
    instance = get_object_or_404(Post, id=update_id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': instance.title,
        'instance': instance,
        'form': form,
    }
    return render(request, 'posts/post_form.html', context)


# def posts_delete(request):
#     pass





















