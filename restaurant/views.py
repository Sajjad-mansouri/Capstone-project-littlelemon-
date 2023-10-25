from django.shortcuts import render
from rest_framework import generics,viewsets,permissions
from .serializers import MenuSerializer,BookingSerializser

from .models import Menu,Booking

# Create your views here.
def index(request):
	return render(request, 'index.html', {})


class MenuItemsView (generics.ListCreateAPIView):
	queryset=Menu.objects.all()
	serializer_class=MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
	queryset=Menu.objects.all()
	serializer_class=MenuSerializer	


class BookingViewSet(viewsets.ModelViewSet):
	serializer_class = BookingSerializser
	queryset = Booking.objects.all()
	permission_classes = [permissions.IsAuthenticated] 