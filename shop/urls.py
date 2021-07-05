from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, PassChange, PassResest, SetPassword
urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>',
         views.productDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show-cart'),
    path('pluscart/', views.plus_cart, name='plus-cart'),
    path('minuscart/', views.minus_cart, name='minus-cart'),
    path('removecart/', views.remove_cart, name='remove-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path('ladies/', views.ladies, name='ladies'),
    path('ladies/<slug:data>', views.ladies, name='ladiesdata'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='shop/login.html',
                                                         authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(
        template_name='shop/passchange.html', form_class=PassChange, success_url='/passchangedone/'), name='passwordchange'),
    path('passchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='shop/passchangedone.html'), name='passchangedone'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='shop/pass_reset.html', form_class=PassResest), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='shop/pass_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='shop/pass_reset_confirm.html', form_class=SetPassword), name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='shop/pass_reset_complete.html'), name='password_reset_complete'),
    path('registration/', views.CustomerRegView.as_view(),
         name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
