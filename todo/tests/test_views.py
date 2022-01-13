from django.test import TestCase
from unittest import skip
from django.contrib.auth.models import User
from todo.models import Todo
from django.test import Client
from django.urls import reverse

# @skip('demostrating skipping')
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass
class TestViewResponse(TestCase):
    def setUp(self):
        self.c = Client()
        self.data1 = Todo.objects.create(title='maame',slug='maame',description='samaale')
    
    def test_url_allowed_hosts(self):
        '''
        Testing url response
        '''
        response = self.c.get('/')
        self.assertEqual(response.status_code,200)
    
    def test_todo_detail_status(self):
        '''
        Testing todo detail page
        '''
        response = self.c.get(reverse('todo:todo_detail',args=[self.data1.slug]))
        self.assertEqual(response.status_code,200)
    
    def test_todo_create_status(self):
        '''
        Testing todo create page
        '''
        response = self.c.get(reverse('todo:todo_create'))
        self.assertEqual(response.status_code,200)
    
    def test_todo_delete_status(self):
        '''
        Testing todo delete page
        '''
        response = self.c.post(reverse('todo:todo_delete',args=[self.data1.slug]))
        self.assertEqual(response.status_code,302)
    
    def test_todo_update_status(self):
        '''
        Testing todo update page
        '''
        response = self.c.get(reverse('todo:todo_update', args=[self.data1.slug]))
        self.assertEqual(response.status_code,200)
    
    def test_todo_create_post(self):
        '''
        Testing todo create post
        '''
        response = self.c.post(reverse('todo:todo_create'),{'title':'samaale','slug':'samaale','description':'caaalami'})
        self.assertEqual(response.status_code,200)

    def test_todo_update_post(self):
        '''
        Testing todo update post
        '''
        response = self.c.post(reverse('todo:todo_update',args=[self.data1.slug]),{'title':'samaale','slug':'samaale','description':'caaalami'})
        self.assertEqual(response.status_code,200)

    def test_todo_delete_post(self):
        '''
        Testing todo delete post
        '''
        response = self.c.delete(reverse('todo:todo_delete',args=[self.data1.slug]))
        self.assertEqual(response.status_code,200)