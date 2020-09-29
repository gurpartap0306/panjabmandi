from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view,name="login"),
<<<<<<< HEAD
    path("logout",views.logout_view,name="logout"),
    path("register",view.register,name="register")
=======
    path("logout", views.logout_view,name="logout"),
    path("register", views.register,name="register")
>>>>>>> 56c4f79f8128b23b40f4bf7a114e488618908a1c
]
