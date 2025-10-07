import datetime
import json
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  
    category = request.GET.get("category", "all")

    if filter_type != "all":
        product_list = Product.objects.filter(user=request.user)
        if category != "all":
            product_list = product_list.filter(category=category)
    else:
        product_list = Product.objects.all()
        if category != "all":
            product_list = product_list.filter(category=category)

    context = {
        'title': 'Moovr Sportswear',
        'name': request.user.username,
        'class': 'PBP B',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        "categories": Product.CATEGORY_CHOICES,
        "current_filter": filter_type,
    }
    
    return render(request, "main.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.select_related('user').all()

    data = [
        {
            'id': product.id,
            'name': product.name,
            'price': float(product.price) if product.price is not None else 0,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else 'Anonymous',
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': float(product.price) if product.price is not None else 0,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else 'Anonymous',
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Jika request dari AJAX
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "success": True,
                    "redirect_url": "/login/"
                })
            # Jika request biasa (non-AJAX)
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                # Gabungkan error jadi 1 string
                errors = []
                for field, msg_list in form.errors.items():
                    errors.append(f"{field}: {', '.join(msg_list)}")
                return JsonResponse({
                    "success": False,
                    "message": " ".join(errors)
                })

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        # Jika AJAX request
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            if user is not None:
                login(request, user)
                return JsonResponse({
                    "success": True,
                    "redirect_url": "/"
                })
            else:
                return JsonResponse({
                    "success": False,
                    "message": "Invalid username or password."
                })

        # Kalau bukan AJAX (fallback normal)
        if user is not None:
            login(request, user)
            return redirect("main:show_main")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('main:show_main')

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return JsonResponse({
        'status': 'success',
        'message': 'Product added successfully',
        'product': {
            'id': new_product.id,
            'name': new_product.name,
            'price': float(new_product.price) if new_product.price is not None else 0,
            'description': new_product.description,
            'category': new_product.category,
            'thumbnail': new_product.thumbnail,
            'is_featured': new_product.is_featured,
            'user_id': request.user.id,
            'user_username': request.user.username,
        }
    })

def get_product_json(request, id):
    product = get_object_or_404(Product, pk=id)
    return JsonResponse({
        'id': product.id,
        'name': product.name,
        'price': float(product.price) if product.price is not None else 0,
        'description': product.description,
        'category': product.category,
        'thumbnail': product.thumbnail,
        'is_featured': product.is_featured,
        'user_id': product.user.id if product.user else None,
        'user_username': product.user.username if product.user else 'Anonymous'
    })

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id)
        
        # Check ownership
        if product.user != request.user:
            return JsonResponse({'status': 'error', 'message': 'Permission denied'}, status=403)

        # Update fields manually
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.description = request.POST.get("description")
        product.category = request.POST.get("category")
        product.thumbnail = request.POST.get("thumbnail")
        product.is_featured = request.POST.get("is_featured") == 'on'
        
        product.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Product updated successfully',
            'product': {
                'id': product.id,
                'name': product.name,
                'price': float(product.price) if product.price is not None else 0,
                'description': product.description,
                'category': product.category,
                'thumbnail': product.thumbnail,
                'is_featured': product.is_featured,
                'user_id': product.user.id,
                'user_username': product.user.username,
            }
        })
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id)
        
        # Check ownership
        if product.user != request.user:
            return JsonResponse({'status': 'error', 'message': 'Permission denied'}, status=403)
            
        product.delete()
        return JsonResponse({'status': 'success', 'message': 'Product deleted successfully'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)