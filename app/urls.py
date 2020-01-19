from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index),
    path('shows',views.to_all_shows),
    path('shows/new',views.add_new_show),
    path('shows/create',views.create_new_show),
    path('shows/<int:id>',views.show_page),
    path('shows/<int:id>/edit',views.edit_show_page),
    path('shows/<int:id>/update',views.update_show),
    path('shows/<int:id>/destroy',views.delete_show),
    ]
