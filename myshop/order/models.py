from django.db import models
from django.core.validators import MaxValueValidator
from shop.models import Product
from django.utils.timezone import now

STATUS_CHOICES=(
    (0,'PENDING'),
    (1,'DELIVERY'),
    (3,'DONE')
)


class Order(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    province = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    index = models.IntegerField(validators=[MaxValueValidator(999999)])
    created = models.DateTimeField(auto_now_add=True)



    status = models.IntegerField(choices=STATUS_CHOICES,default=0)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('status','-created',)

    def __str__(self):
        return self.first_name
    def get_total_cost(self):
        return sum([i.price*i.quantity for i in self.item.all()])


class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='item',on_delete=models.CASCADE)
    item = models.ForeignKey(Product,related_name='order',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return self.item.name

    def get_cost(self):
        return self.quantity * self.price
