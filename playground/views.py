from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import Q, F
from django.db.models.aggregates import Count, Sum, Avg, Min, Max
from store.models import Collection, Product, OrderItem, Order
from django.db import transaction



# Create your views here.
def say_hello(request):
    #create a collection
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()
    # collection.id

    #update a collection
    # collection = Collection.objects.get(pk=11)
    # collection.title = 'Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()

    #or
    #Collection.objects.filter(pk=11).update(title='Video Games', featured_product=Product(pk=1))
    #delete a collection
    # collection = Collection.objects.get(pk=11)
    # collection.delete()

    #multiple delete
    # Collection.objects.filter(pk__gt=10).delete()

    #Transaction
    # with transaction.atomic():
    with transaction.atomic():
        try:
            order = Order()
            order.customer_id = 1
            order.save()
            order_item = OrderItem()
            order_item.order = order
            order_item.product_id = 1
            order_item.quantity = 1
            order_item.unit_price = 100
            order_item.save()
        except Exception as e:
            print(f'Error occurred: {e}')
        #collection = Collection.objects.get(pk=11)
        #collection.delete()

    #queryset = Product.objects.filter(inventory=F('collection__id'))
    #product = Product.objects.values_list('id', 'title', 'unit_price', 'collection__title')
    # product = Product.objects.filter(id__in=Product.objects.values('collection_id').distinct())
    # product = Product.objects.select_related('collection').all()
    #product = Product.objects.prefetch_related('promotion').select_related('collection').all()
    result = Product.objects.filter(collection__id=3).aggregate(count=Count('id'), min_price=Min('unit_price'), max_price=Max('unit_price'), avg_price=Avg('unit_price'), total_inventory=Sum('inventory'))
    product = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('placed_at').all()
    return render(request, 'hello.html', { 'name': 'Tanvir', 'value': product.count(), 'products': list(product), 'result': result }) 