from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from cart.cart import Cart
from .models import OrderItem, Order
from .forms import OrderForm
from shop.models import Product

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order,id=order_id)
    return render(request,'admin/orders/order/detail.html',{'order':order})

def create_order(request):
    cart = Cart(request)
    print(cart.__dict__)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            request.session['order']=order.id
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    item=item['product'],
                    price=item['product'].sell_price,
                    quantity=item['quantity']
                )
            cart.clear()
            return render(request,'order/orders.html')
    else:
        order = request.session.get('order')
        if order:
            try:
                order = Order.objects.get(id=order)
                form = OrderForm(instance=order)
            except Order.DoesNotExist:
                form = OrderForm()
            
        else:
            form = OrderForm()
    ctx = {
        'form':form,
        'cart':cart
    }
    return render(request,'order/create_order.html',context=ctx)