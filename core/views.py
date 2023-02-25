from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    posts_page = Paginator(Post.objects.filter(published=True), 2)
    page = request.GET.get('page')
    posts = posts_page.get_page(page)
    aux = 'x' * posts.paginator.num_pages

    print(type(posts.paginator.num_pages))
    return render(request,'core/home.html', {'posts':posts, 'aux':aux})

# Detalle del Post
def post(request, post_id):
    # post = Post.objects.get(id=post_id)
    try:
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'core/detail.html', {'post':post})
    except:
        return render(request, 'core/404.html')

# Filtrado por Categoría
def category(request, category_id):
    try:
        category = get_object_or_404(Category, id=category_id)
        return render(request, 'core/category.html', {'category':category})    
    except:
        return render(request, 'core/404.html')

# Filtrado por Author
def author(request, author_id):
    try:
        author = get_object_or_404(User, id=author_id)
        return render(request, 'core/author.html', {'author':author})
    except:
        return render(request, 'core/404.html')

def dates(request, month_id, year_id):

    meses = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre',
    }

    if month_id > 12 or month_id < 1:
        return render(request, 'core/404.html')

    posts = Post.objects.filter(published=True, created__month=month_id, created__year=year_id)
    return render(request, 'core/dates.html', {'posts':posts, 'month':meses[month_id], 'year':year_id})