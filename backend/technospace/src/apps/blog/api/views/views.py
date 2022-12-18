from rest_framework import viewsets
from rest_framework import generics
from rest_framework.filters import SearchFilter
from src.apps.blog.api.serializers.serializers import BlogpostSerializer, CategorySerializer, SubscriptionSerializer, ContactSerializer
from src.apps.blog.models import BlogpostModel, CategoryModel, SubscriptionModel, ContactModel


class BlogpostView(viewsets.ModelViewSet):
    queryset = BlogpostModel.objects.all()
    serializer_class = BlogpostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']


class CategoryView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class SubscriptionCreateAPIView(generics.CreateAPIView):
    queryset = SubscriptionModel.objects.all()
    serializer_class = SubscriptionSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer