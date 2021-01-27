from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Category,SubCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def dashboard(request):
    categories = Category.objects.all()
    top_items = Product.objects.all().order_by('-top')
    page = request.GET.get('page',1)
    
    paginator = Paginator(top_items, 12)
    
    try:
        top_items = paginator.page(page)
    except PageNotAnInteger:
        top_items = paginator.page(1)
    except EmptyPage:
        top_items = paginator.page(paginator.num_pages)
    
    nums = request.session.get('product',0)
    request.session['product']=nums+1

    ctx = {
        'categories':categories,
        'top_items':top_items,
    }
    return render(request, 'shop/dashboard.html',ctx)

def category(request,slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug = slug)
    subcategory = SubCategory.objects.filter(category = category)
    if request.method == 'POST':
        slugs = request.POST.getlist('slugs')
        products = Product.objects.filter(category__in = slugs)
    else:
        products = Product.objects.filter(category__in = subcategory.values_list('id',flat=True))
    page = request.GET.get('page',1)
    
    paginator = Paginator(products, 12)
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    ctx= {
        'categories':categories,
        'products':products,
        'subcategory':subcategory,
        'category':category,
    }
    return render(request, 'shop/category.html',ctx)

def subcategory(request,slug,subslug):
    subcategories = SubCategory.objects.filter(category__slug = slug)
    subcategory = subcategories.get(slug = subslug)
    products = Product.objects.filter(category = subcategory)
    categories = Category.objects.all()
    page = request.GET.get('page',1)
    
    paginator = Paginator(products, 12)
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    ctx= {
        'categories':categories,
        'products':products,
        'subcategory':subcategory,
        'subcategories':subcategories,
    }
    return render(request, 'shop/subcategory.html',ctx)

def item_view(request,slug,subslug,item_slug):
    item = get_object_or_404(Product,slug = item_slug)
    ctx = {
        'item':item
    }
    return render(request, 'shop/item_view.html',context=ctx)
