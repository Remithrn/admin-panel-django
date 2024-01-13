from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<int:pk>", views.detail_view, name="detail"),
    path("delete/<int:pk>", views.delete_view, name="delete"),
    path("edit/<int:pk>", views.edit_view, name="edit"),
    path('login/',views.login_view,name='login'),
    path('register',views.register,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('user/',views.admin_view,name='user'),
    path('detail_user/<int:pk>/',views.detail_user,name='user-detail'),
    path('edit_user/<int:pk>',views.edit_user,name='edit-user'),
    path('delete_user/<int:pk>',views.delete_user,name='delete-user'),
    path('error',views.error_page,name='error')
]
