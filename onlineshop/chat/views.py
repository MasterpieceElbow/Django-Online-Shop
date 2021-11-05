from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from shop.models import Category


@login_required
def category_chat_room(request, category_id):
    try:
        # retrieve category with given id
        category = Category.objects.get(id=category_id)
    except:
        # category doesn't exist
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {'category': category})
