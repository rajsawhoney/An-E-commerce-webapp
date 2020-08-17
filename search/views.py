from django.shortcuts import render
from product.models import Product, Category
from django.views.generic import TemplateView
from django.db.models import Q
from cart.models import Cart
from django.contrib import messages
from accounts.models import UserModel
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.


class SearchResultView(TemplateView):
    template_name = "searchresult.html"

    def get_context_data(self, **kwargs):
        request = self.request
        querytxt = request.GET.get('q')
        catSelection = request.GET.get('catsel')
        context = super().get_context_data(**kwargs)

        if catSelection == '1':
            cat_lookups = Q(category__name__icontains='accessories')
        elif catSelection == '2':
            cat_lookups = Q(category__name__icontains='laptop')
        elif catSelection == '3':
            cat_lookups = Q(category__name__icontains='smartphone')
        elif catSelection == '4':
            cat_lookups = Q(category__name__icontains='camera')
        else:
            cat_lookups = (
                Q(category__name__icontains='accessories') |
                Q(category__name__icontains='laptop') |
                Q(category__name__icontains='smartphone') |
                Q(category__name__icontains='camera')
            )

        lookups = (Q(name__icontains=querytxt) |
                   Q(description__icontains=querytxt) |
                   Q(price_amount__icontains=querytxt) |
                   # search by related model names
                   Q(producttag__title__icontains=querytxt) |
                   # search by related model names
                   Q(category__name__icontains=querytxt) |
                   # search by related model names
                   Q(category__description__icontains=querytxt) |
                   Q(which_product__description__icontains=querytxt) |
                   Q(which_prod__description__icontains=querytxt)
                   # Q(answers__description__icontains = querytxt)

                   )
        context['products'] = Product.objects.filter(cat_lookups).filter(
            lookups).distinct()
        context["maincategory"] = Category.objects.all()
        cart_obj, new_obj = Cart.objects.get_create_cartId(self.request)
        context["cartItems"] = cart_obj.product.all()
        context["wishItems"] = cart_obj.wishedProduct.all()
        context["subTotal"] = cart_obj.subTotal
        context["total"] = cart_obj.totalSum
        if self.request.user.is_authenticated:
            context['userinfo'] = UserModel.objects.get(user=self.request.user)
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


def ajax_search(request):
    querytxt = request.GET.get('q')
    catSelection = request.GET.get('catsel')
    if catSelection == '1':
        cat_lookups = Q(category__name__icontains='accessories')
    elif catSelection == '2':
        cat_lookups = Q(category__name__icontains='laptop')
    elif catSelection == '3':
        cat_lookups = Q(category__name__icontains='smartphone')
    elif catSelection == '4':
        cat_lookups = Q(category__name__icontains='camera')
    else:
        cat_lookups = (
            Q(category__name__icontains='accessories') |
            Q(category__name__icontains='laptop') |
            Q(category__name__icontains='smartphone') |
            Q(category__name__icontains='camera')
        )

    lookups = (Q(name__icontains=querytxt) |
               Q(description__icontains=querytxt) |
               Q(price_amount__icontains=querytxt) |
               # search by related model names
               Q(producttag__title__icontains=querytxt) |
               # search by related model names
               Q(category__name__icontains=querytxt) |
               # search by related model names
               Q(category__description__icontains=querytxt) |
               Q(which_product__description__icontains=querytxt) |
               Q(which_prod__description__icontains=querytxt)
               # Q(answers__description__icontains = querytxt)

               )
    products = Product.objects.filter(cat_lookups).filter(
        lookups).distinct()

    if request.is_ajax():
        print("Its an ajax request for searching...")
        html = render_to_string('includes/search-result-snippet.html',
                                context={'products': products}, request=request)
        return JsonResponse({'search_data': html})

    return render(request, "searchresult.html", {'products': products})
