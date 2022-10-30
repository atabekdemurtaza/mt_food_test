from django.test import TestCase
from post.models import Post 

class PostModelTest(TestCase):

	@classmethod 
	def setUpTestData(cls):

		Post.objects.create(title='first post', body='a body here')

	def test_title_content(self):

		post = Post.objects.get(id=1)
		expected_object_name = f'{post.title}'
		self.assertEquals(expected_object_name, 'first post')

	def test_body_content(self):

		post = Post.objects.get(id=1)
		expected_object_name = f'{post.body}'
		self.assertEquals(expected_object_name, 'a body here')