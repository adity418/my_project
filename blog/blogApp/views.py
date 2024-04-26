from django.shortcuts import render
from rest_framework import generics
from blogApp.models import Category, Blog
from blogApp.serializers import CategorySerializer, BlogSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.OrderingFilter]

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.OrderingFilter]


    

"""Create your views here."""
# class CategoryListView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class BlogListView(generics.ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class CategoryList(APIView):

#     def get(self,request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories,many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class CategoryDetail(APIView):

#     def get_object(self,pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise Http404
        
#     def get(self,request,pk):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(category,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request,pk):
#         category = self.get_object(pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class BlogList(APIView):

#     def get(self,request):
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs,many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class BlogDetail(APIView):

#     def get_object(self,pk):
#         try:
#             return Blog.objects.get(pk=pk)
#         except Blog.DoesNotExist:
#             raise Http404
        
#     def get(self,request,pk):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request,pk):
#         blog = self.get_object(pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)