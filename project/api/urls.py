from django.urls import path
from rest_framework import routers

from .views import PostView, posts_get, post_del, posts_list, post_put, post_add, post_update

# router = routers.DefaultRouter()
# router.register(r'posts', PostView)
#
# urlpatterns = router.urls

urlpatterns = [
    path('', PostView.as_view({'get': 'list'})),
    path('posts', posts_get),
    path('posts/<int:pk>', posts_list),
    path('post_del/<int:pk>', post_del),
    path('post_add/', post_add),
    path('post_put/<int:pk>', post_put),
    path('post_patch/<int:pk>', post_update)
]
