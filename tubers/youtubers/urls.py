from django.urls import path
from . import views

urlpatterns = [
    path('',views.youtubers, name="youtubers"),
    path('<int:id>',views.youtubers_detail, name="youtubers_detail"),
    path('search',views.search, name="search"),

    path('selection_for_login',views.selection_for_login,name="selection_for_login"),
    path('selection_for_register',views.selection_for_register,name="selection_for_register"),

    path('login_youtuber',views.login_youtuber,name="login_youtuber"),
    path('register_youtuber',views.register_youtuber,name="register_youtuber"),
    path('dashboard_youtuber',views.dashboard_youtuber,name="dashboard_youtuber"),
    path('dashboard_youtuber/<int:id>/edit_profile',views.EditProfileView.as_view(),name="edit_profile"),
    path('send_response',views.ytresponseview,name="ytresponseview"),
    path('logout_youtuber',views.logout_youtuber,name="logout_youtuber"),

]
