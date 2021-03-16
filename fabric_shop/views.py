from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *
from .forms import *
from django.core.paginator import Paginator


class IndexView(View):
    def get(self, request):
        return render(request, 'fabric_shop/index.html')


class CartView(View):
    def get(self, request):
        return render(request, 'fabric_shop/cart.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'fabric_shop/contact.html')


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'fabric_shop/categories.html', context={"categories": categories})


class CategoryView(View):
    def get(self, request, category):
        products_list = Product.objects.filter(category__name=str(category))
        paginator = Paginator(products_list, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'fabric_shop/category.html', context={"products": page_obj})


class SingleProduct(View):
    def get(self, request, product_id):
        single_product = Product.objects.filter(id=product_id)
        return render(request, 'fabric_shop/single-product2.html', context={"single_product": single_product})

    @login_required
    def post(self, request, product_id):
        User.objects.get()
        single_product = get_object_or_404(Product, pk=product_id)
        order_form = OrderForm(request.POST)
        if not order_form.is_valid():
            return HttpResponseBadRequest("Bad request")

        data = order_form.cleaned_data
        order = OrderProduct(**data)
        order.save()
        return render(request, 'fabric_shop/single-product2.html', context={"single_product": single_product})

#
# class RegistrationView(View):
#     def post(self, request):
#         if request.method == "POST":
#             form = AuthUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 username = form.changed_data.get('username')
#                 return redirect('home')
#         else:
#             form = AuthUserForm()
#         return render(request, 'mylogin.html', {'form': form})

class LoginUserView(TemplateView):
    template_name = "fabric_shop/mylogin.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)


class RegisterUserView(TemplateView):
    template_name = "fabric_shop/regist.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)


class LogoutUserView(View):

    def get(self, request):
        logout(request)
        return redirect(reverse("home"))
