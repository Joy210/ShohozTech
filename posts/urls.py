from django.urls import path

# Same App views
from . import views


urlpatterns = [
    path('lists/', views.posts_lists),
    path('create/', views.posts_create),
    path('details/<int:details_id>', views.posts_details, name='details'),
    path('update/<int:update_id>', views.posts_update, name='update'),
    # path('delete/<int:delete_id>', views.posts_delete, name='delete'),
]











