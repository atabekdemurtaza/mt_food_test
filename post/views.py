from post.models import Post 
from post.serializers import PostSerializer
from rest_framework import generics 

class ListPost(generics.ListAPIView):

	queryset = Post.objects.all()
	serializer_class = PostSerializer 

class DetailPost(generics.RetrieveAPIView):

	queryset = Post.objects.all()
	serializer_class = PostSerializer

