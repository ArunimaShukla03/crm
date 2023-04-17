from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/", views.registerPage, name="register"),

    path("login/", views.loginPage, name="login"),

    path("logout/", views.logoutUser, name="logout"),

    path("", views.home, name="home"),

    path("user/", views.userPage, name="user-page"),

    path("account/", views.accountSettings, name="account"),

    path("products/", views.products, name="products"),

    path("customer/<str:pk>/", views.customer, name="customer"),

    path("create_order/<str:pk_customer>", views.createOrder, name="create_order"),

    path("update_order/<str:pk_test>/", views.updateOrder, name="update_order"),

    path("delete_order/<str:primary_key>", views.deleteOrder, name="delete_order"),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

    # "reset/" is the URL endpoint that triggers the password reset process.

    # "<uidb64>" is the unique identifier that is used to identify the user requesting the password reset.

    # "<token>" is the one-time token that is generated and sent to the user's email for security purposes.

    # When you click on the link containing the token, "auth_views.PasswordResetConfirmView" view verifies the validity of the token and allows the user to reset their password.

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]