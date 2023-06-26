from django.urls import path
from . import views

urlpatterns = [
    path('messages/get/', views.get_messages, name='get_messages'),
    path('messages/create/', views.create_message, name='create_message'),
      path('messages/delete/', views.delete_messages, name='delete_messages'),
  
]


# from . import views
# from django.urls import  path,include
# from rest_framework import routers

# router=routers.DefaultRouter()
# router.register(r'messages',views.get_messages),
# router.register(r'messages',views.create_message),


# urlpatterns=[
#     path('',include(router.urls))
# ]
