from django.test import TestCase
from  todo.models import Todo

class TodoTestCase(TestCase):
    def setUp(self):
        """
        Setting up the data first
        """
        self.data1 = Todo.objects.create(title='samaale',slug='samaale',description='description weeye')
    
    def test_todo_model(self):
        '''
        testing the todo model if data1 created is instance of Todo table
        '''
        data = self.data1
        self.assertTrue(isinstance(data,Todo))

    def test_todo_model_str(self):
        '''
        Testing the str method of todo model to return title 
        '''
        data = self.data1
        self.assertEqual(str(data),self.data1.title)
    
    def test_todo_model_get_absolute_url(self):
        '''
        Testing the get_absolute_url method to return the url /todo/slug/
        '''
        self.assertEqual(self.data1.get_absolute_url(),'/todo/'+self.data1.slug+'/')
