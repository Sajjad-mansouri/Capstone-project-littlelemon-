from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register(r'tables', views.BookingViewSet)
#api
urlpatterns=[
    
    path('menu', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),

    #booking
    path('booking/', include(router.urls)),
]