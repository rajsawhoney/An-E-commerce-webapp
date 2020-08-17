from plyer import notification, battery, email, camera, tts, wifi, camera
import plyer.platforms.win.notification
from django.forms import modelformset_factory
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from reviews.forms import ReviewForm
from reviews.models import Review
from django.views.generic.edit import CreateView, View, UpdateView
from .models import Category, Product, ProductImage
from accounts.models import UserModel
from specialoffers.models import Offer
from cart.models import Cart
from django.contrib.auth import get_user_model, login
from django.utils.decorators import method_decorator

from django.contrib import messages
from questions_ans.models import QuestionAns
from .forms import RvwForm, QnAnsForm

from django.utils.translation import gettext_lazy as _
# Create your views here.

from django.views.generic import TemplateView, DetailView
from django.http.response import HttpResponse, JsonResponse
from product.forms import ProductModelForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.forms import UserForm, UserProfileForm
from django.template.loader import render_to_string


class CategoryListView(TemplateView):
    template_name = "category_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["maincategory"] = Category.objects.all()
        cart_obj, new_obj = Cart.objects.get_create_cartId(self.request)
        context["cartItems"] = cart_obj.product.all()
        context["wishItems"] = cart_obj.wishedProduct.all()
        if self.request.user.is_authenticated:
            context['userinfo'] = UserModel.objects.get(user=self.request.user)
        else:
            context['userinfo'] = self.request.user
        return context


class CategoryView(TemplateView):
    template_name = "category_view.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request = self.request
        catdata = self.request.path
        for cat in Category.objects.all():
            if cat.name in catdata.split('/'):  # Awesome logic here
                catdata = cat
                break
        context["maincategory"] = Category.objects.all()
        context['category'] = Product.objects.filter(
            category__name__icontains=catdata).distinct()
        context['query_category'] = catdata
        cart_obj, new_obj = Cart.objects.get_create_cartId(self.request)
        context["cartItems"] = cart_obj.product.all()
        context["wishItems"] = cart_obj.wishedProduct.all()
        context["subTotal"] = cart_obj.subTotal
        context["total"] = cart_obj.totalSum
        if self.request.user.is_authenticated:
            context['userinfo'] = UserModel.objects.get(user=self.request.user)
        else:
            context['userinfo'] = self.request.user

        rec = messages.get_messages(self.request)
        data = []
        for d in rec:
            data.append(d)

        if len(data) > 0:
            context["ptype"] = int(str(data[0]))
            context["name"] = data[1]
            context["imgurl"] = data[2]
            context["qty"] = int(str(data[3]))
        return context


class HomeView(TemplateView):
    template_name = "index.html"
    notification.notify(title="Test Notification!",
                        message=f"Remaining charge:{battery.get_state()['percentage']}", app_name='nepaliamazon', app_icon=None, timeout=20, ticker="notification arrived!", toast=False)

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["maincategory"] = Category.objects.all()
        context['offers'] = Offer.objects.all()

        tags = ['new', 'top', 'hot']  # Shortcuts for below codes
        for tag in tags:
            context[f'{tag}_products'] = Product.objects.filter(
                product_tag=tag).distinct()
            for cat in context["maincategory"]:
                context[f'{tag}_{cat}'] = Product.objects.get_category(
                    tag, cat)

        if self.request.method == "POST":
            user_form = UserForm(self.request.POST)
            user_profile_form = UserProfileForm(
                self.request.POST, self.request.FILES)
            if user_form.is_valid() and user_profile_form.is_valid():
                user = user_form.save()
                profile = user_profile_form.save(commit=False)
                profile.user = user
                profile.save()
                registered = True
                login(self.request, user)
                return redirect('product:product_list')
            else:
                print(user_form.errors, user_profile_form.errors)
        else:
            user_form = UserForm()
            user_profile_form = UserProfileForm()

        context['user_form'] = user_form
        context['user_profile_form'] = user_profile_form

        # FOR ONLY NEW PRODUCTS
        # context['new_products'] = Product.objects.filter(product_tag='new')
        # context['new_category1'] = Product.objects.get_category('new',"LAPTOP")        # For
        # context['new_category2'] = Product.objects.get_category('new',"SMARTPHONE")    # New
        # context['new_category3'] = Product.objects.get_category('new',"CAMERA")        # Products
        # context['new_category4'] = Product.objects.get_category('new',"ACCESSORIES")   # only

        # FOR ONLY TOP PRODUCTS
        # context['top_products'] = Product.objects.filter(product_tag='top')
        # context['top_category1'] = Product.objects.get_category('top',"LAPTOP")        # For
        # context['top_category2'] = Product.objects.get_category('top',"SMARTPHONE")    # Top
        # context['top_category3'] = Product.objects.get_category('top',"CAMERA")        # Products
        # context['top_category4'] = Product.objects.get_category('top',"ACCESSORIES")   # only

        # FOR ONLY TOP PRODUCTS
        # context['hot_products'] = Product.objects.filter(product_tag='hot')
        # context['hot_category1'] = Product.objects.get_category('hot',"LAPTOP")        # For
        # context['hot_category2'] = Product.objects.get_category('hot',"SMARTPHONE")    # Hot
        # context['hot_category3'] = Product.objects.get_category('hot',"CAMERA")        # Products
        # context['hot_category4'] = Product.objects.get_category('hot',"ACCESSORIES")   # only

        # Filter and pass context for top selling products and hot deals
        cart_obj, new_obj = Cart.objects.get_create_cartId(self.request)
        context["cartItems"] = cart_obj.cartitem_set.all()
        context["wishItems"] = cart_obj.wishedProduct.all()
        context["subTotal"] = cart_obj.subTotal
        context["total"] = cart_obj.totalSum
        if self.request.user.is_authenticated:
            context['userinfo'] = UserModel.objects.get(user=self.request.user)
        else:
            context['userinfo'] = self.request.user

        rec = messages.get_messages(self.request)
        data = []
        for d in rec:
            data.append(d)
        if len(data) > 0:
            context["ptype"] = int(str(data[0]))
            context["name"] = data[1]
            context["imgurl"] = data[2]
            context["qty"] = int(str(data[3]))

        return context


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "product-detail.html"
#     context_object_name = 'thisProduct'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         product = Product.objects.get(id=1)
#         context['productImages'] = product.images.all()[0]
#         return context


# class ReviewCreate(CreateView):
#     model=Review
#     fields="__all__"
#     template_name = 'blank.html'....


def ProductDetailView(request, pk):
    product = get_object_or_404(Product, slug=pk)
    productImage = product.images.all()
    productReviews = Review.objects.filter(reviews=product).order_by("-id")
    progress_bar1, progress_bar2, progress_bar3, progress_bar4, progress_bar5 = 0, 0, 0, 0, 0
    if product.rating1count or product.rating2count or product.rating3count or product.rating4count or product.rating5count:
        ratingSum = product.rating1count + product.rating2count + \
            product.rating3count + product.rating4count + product.rating5count
        progress_bar5 = int(product.rating5count*100/ratingSum)
        progress_bar4 = int(product.rating4count*100/ratingSum)
        progress_bar3 = int(product.rating3count*100/ratingSum)
        progress_bar2 = int(product.rating2count*100/ratingSum)
        progress_bar1 = int(product.rating1count*100/ratingSum)

    relatedProducts = Product.objects.all()[:4]  # just for examples
    questions = QuestionAns.objects.filter(
        product=product, answer=None).order_by("-id")

    greetingtxt = _(
        'हामी नेपाली येमेज़नको तर्फबाट तपाइलाई हार्दिक स्वागत गर्दछौ ।')

    cart_obj, new_obj = Cart.objects.get_create_cartId(request)
    cartItems = cart_obj.cartitem_set.all()
    wishItems = cart_obj.wishedProduct.all()
    subTotal = cart_obj.subTotal
    total = cart_obj.totalSum
    if request.user.is_authenticated:
        userinfo = UserModel.objects.get(user=request.user)
    else:
        userinfo = request.user

    return render(request, 'product-detail.html', {
        'maincategory': Category.objects.all(),
        'product': product,
        'productImage': productImage,
        'relatedProducts': relatedProducts,
        'productReviews': productReviews,
        'questions': questions,
        'transtxt': greetingtxt,
        'cartItems': cartItems,
        'wishItems': wishItems,
        'subTotal': subTotal,
        'total': total,
        'cart_obj': cart_obj,
        'userinfo': userinfo,
        'progress_bar1': progress_bar1,
        'progress_bar2': progress_bar2,
        'progress_bar3': progress_bar3,
        'progress_bar4': progress_bar4,
        'progress_bar5': progress_bar5,
    })


def TestIndex(request):
    return HttpResponse("<h1> This is a test Response!!! </h1>")


class ProductCreateView(View):

    @method_decorator(login_required)
    def get(self, request):
        print("I am Inside Get method!!!")
        if self.request.user.is_superuser:  #
            form = ProductModelForm()
            template = 'product-create.html'
        context = {'form': form, }
        return render(request, template, context)

    @method_decorator(login_required)
    def post(self, request):
        print("I am Inside Post method!!!")
        if self.request.user.is_superuser:  #
            form = ProductModelForm(
                self.request.POST, self.request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.get_absolute_url())
        context = {'form': form, }
        template = 'product-create.html'
        return render(request, template, context)


# class ProductCreateView(CreateView):
#     model = Product
#     template_name = "product-create.html"
#     form_class = ProductModelForm

#     def form_valid(self, form):
#         return HttpResponseRedirect('product:product_list')
