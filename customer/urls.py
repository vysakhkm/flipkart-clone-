from django.urls import path
from customer import views
urlpatterns=[
    path("register/",views.SignupView.as_view(),name="signup"),
    path("",views.LoginView.as_view(),name="signin"),
    path("home/",views.HomeView.as_view(),name="home"),
    path("products/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
    path("products/<int:id>/carts/add",views.AddtocartView.as_view(),name="cart-add"),
    path("customer/carts/all",views.CartListView.as_view(),name="cart-list"),
    path("carts/<int:id>/change",views.CartRemoveview.as_view(),name="cart-change"),
    path("orders/add/<int:id>",views.MakeOrderView.as_view(),name="create-order"),
    path("customer/order/all",views.OrderView.as_view(),name="order-list")
    
]