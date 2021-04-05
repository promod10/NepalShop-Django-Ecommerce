from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.
DISTRICT_CHOICES = (
    ('Bhojpur', 'Bhojpur'),
    ('Dhankuta', 'Dhankuta'),
    ('Ilam', 'Ilam'),
    ('Jhapa', 'Jhapa'),
    ('Khotang', 'Khotang'),
    ('Morang', 'Morang'),
    ('Okhaldhunga', 'Okhaldhunga'),
    ('Panchthar', 'Panchthar'),
    ('Sankhuwasabha', 'Sankhuwasabha'),
    ('Solukhumbu', 'Solukhumbu'),
    ('Sunsari', 'Sunsari'),
    ('Taplejung', 'Taplejung'),
    ('Terhathum', 'Terhathum'),
    ('Udayapur', 'Udayapur'),
    # Provice No.2
    ('Bara', 'Bara'),
    ('Dhanusa', 'Dhanusa'),
    ('Mahottari', 'Mahottari'),
    ('Parsa', 'Parsa'),
    ('Rautahat', 'Rautahat'),
    ('Saptari', 'Saptari'),
    ('Sarlahi', 'Sarlahi'),
    ('Siraha', 'Siraha'),
    # Provice No.3
    ('Bhaktapur', 'Bhaktapur'),
    ('Chitwan', 'Chitwan'),
    ('Dhading', 'Dhading'),
    ('Dolakha', 'Dolakha'),
    ('Kathmandu', 'Kathmandu'),
    ('Kavrepalanchok', 'Kavrepalanchok'),
    ('Lalitpur', 'Lalitpur'),
    ('Makwanpur', 'Makwanpur'),
    ('Nuwakot', 'Nuwakot'),
    ('Ramechhap', 'Ramechhap'),
    ('Rasuwa', 'Rasuwa'),
    ('Sindhuli', 'Sindhuli'),
    ('Sindhupalchok', 'Sindhupalchok'),
    # Provice No.4
    ('Baglung', 'Baglung'),
    ('Gorkha', 'Gorkha'),
    ('Kaski', 'Kaski'),
    ('Lamjung', 'Lamjung'),
    ('Manang', 'Manang'),
    ('Mustang', 'Mustang'),
    ('Myagdi', 'Myagdi'),
    ('Nawalpur', 'Nawalpur'),
    ('Parbat', 'Parbat'),
    ('Syangja', 'Syangja'),
    ('Tanahun', 'Tanahun'),
    # Provice No.5
    ('Arghakhanchi', 'Arghakhanchi'),
    ('Banke', 'Banke'),
    ('Bardiya', 'Bardiya'),
    ('Dang', 'Dang'),
    ('Eastern Rukum', 'Eastern Rukum'),
    ('Gulmi', 'Gulmi'),
    ('Kapilvastu', 'Kapilvastu'),
    ('Palpa', 'Palpa'),
    ('Parasi', 'Parasi'),
    ('Pyuthan', 'Pyuthan'),
    ('Rolpa', 'Rolpa'),
    ('Rupandehi', 'Rupandehi'),
    # Provice No.6
    ('Dailekh', 'Dailekh'),
    ('Dolpa', 'Dolpa'),
    ('Humla', 'Humla'),
    ('Jajarkot', 'Jajarkot'),
    ('Jumla', 'Jumla'),
    ('Kalikot', 'Kalikot'),
    ('Mugu', 'Mugu'),
    ('Salyan', 'Salyan'),
    ('Surkhet	', 'Surkhet	'),
    ('Western Rukum', 'Western Rukum'),
    # Province No.7
    ('Achham', 'Achham'),
    ('Baitadi', 'Baitadi'),
    ('Bajhang', 'Bajhang'),
    ('Bajura', 'Bajura'),
    ('Dadeldhura', 'Dadeldhura'),
    ('Darchula', 'Darchula'),
    ('Doti', 'Doti'),
    ('Kailali', 'Kailali'),
    ('Kanchanpur', 'Kanchanpur'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    district = models.CharField(choices=DISTRICT_CHOICES, max_length=100)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('G', 'Gents'),
    ('LD', 'Ladies'),
    ('F', 'Footware'),
    ('B', 'Bags'),

)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=4)
    product_image = models.ImageField(upload_to='product_img')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=50, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price
