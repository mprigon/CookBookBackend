from django.views.generic import ListView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


from .models import Dish
from .serializers import DishSerializer
from .permissions import IsAdminOrReadOnly


class DishAPIList(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class DishCategoryAPIList(generics.ListCreateAPIView):
    serializer_class = DishSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        catdish = self.kwargs['pk']
        return Dish.objects.filter(cat__id=catdish)


class DishAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # def get_queryset(self):
    #     dishid = self.kwargs['pk']
    #     print('Hello! dishid = ', dishid)
    #     dishSelected = Dish.objects.get(id=dishid)
    #     print('dishSelected = ', dishSelected)
    #     return Dish.objects.get(id=dishid)


class DishAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (IsAuthenticated, )


class DishAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (IsAdminOrReadOnly, )

class HomePageView(ListView):
    model = Dish
    template_name = 'home_page.html'
