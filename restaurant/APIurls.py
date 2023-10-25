from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router=DefaultRouter()
router.register(r'tables', views.BookingViewSet)
#api
urlpatterns=[
    
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),

    #booking
    path('booking/', include(router.urls)),

    #auth-token
    path('api-token-auth/', obtain_auth_token),
]