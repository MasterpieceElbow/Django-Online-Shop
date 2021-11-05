from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector
from .models import Category, Product
from cart.forms import CartAddProductForm
from .recommender import Recommender
from .forms import ReviewForm, SearchForm
from django.db.models.functions import Greatest
from django.contrib.postgres.search import TrigramSimilarity


def category_list(request):
    categories = Category.objects.filter(active=True)
    return render(request,
                  'shop/category/list.html',
                  {'categories': categories})


def list_by_category(request, slug):
    categories = Category.objects.filter(active=True)
    if slug:
        category = get_object_or_404(Category, slug=slug, active=True)
        products = category.products.filter(available=True)
    return render(request,
                  'shop/product/list.html',
                  {'categories': categories,
                   'category': category,
                   'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    reviews = product.reviews.all()
    views = product.views
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        product.views = F('views') + 1
        product.save()

    form = ReviewForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'reviews': reviews,
                   'cart_product_form': cart_product_form,
                   'recommended_products': recommended_products,
                   'form': form,
                   'views': views})


def category_product_search(request):
    form = SearchForm()
    query = None
    results_category = []
    results_product = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results_category = Category.objects.annotate(
                similarity=TrigramSimilarity('name', query),
            ).filter(
                active=True, similarity__gt=0.1
            ).order_by('-similarity')
            results_product = Product.objects.annotate(
                similarity=Greatest(TrigramSimilarity('name', query), TrigramSimilarity('description', query)),
            ).filter(
                available=True, similarity__gt=0.1
            ).order_by('-similarity')
    return render(request,
                  'shop/search.html',
                  {'form': form,
                   'query': query,
                   'results_category': results_category,
                   'results_product': results_product})
