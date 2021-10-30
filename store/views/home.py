from django.shortcuts import render, redirect ,HttpResponseRedirect
from store.models.product import Product
from store.models.categories import Category
from django.views import View


# Creating my views here
class Index(View):

    def post(self , request):
       product = request.POST.get('product')
       return redirect('homepage')


    def get(self , request):
        products = None

        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()

        data = {}
        data['prod'] = products
        data['categories'] = categories


        print('you are: ', request.session.get('email'))
        print(data)
        #print(products)

        #print(data.get('products'))
        a=Product.get_all_products()
        b=Product.objects.get(name='Magic Moments')
        print(b.name)
        #print(products.name)



        return render(request, 'index.html', data)


def ceo(request):
    return render(request, 'ceo.html')


def company(request):
    return render(request, 'company.html')


def help(request):
    return render(request, 'help.html')



