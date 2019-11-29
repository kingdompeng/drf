from django.shortcuts import render

# Create your views here.

from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile, Book

class BookAPIView1(APIView):
    """ 使用 Serializer """
    def get(self, request, format=None):
        APIkey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIKey=APIkey).first()
        if developer:
            balance = developer.money
            if balance > 0:
                isbn = self.request.query_params.get('isbn', 0)
                books = Book.objects.filter(isbn=isbn)
                books_serializer = BookSerializer(books, many=True)
                print(books_serializer)
                developer.money -= 1
                developer.save()
                return Response(books_serializer.data)
            else:
                return Response('兄弟，又到了需要充钱的时候！好开心啊！')
        else:
            return Response('查无此人啊')