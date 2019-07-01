from django.test import TestCase, Client
from django.urls import reverse, resolve
from property import views
from property.models import Property

class TestPropertyHomeView(TestCase):

    def setUp(self):

        self.url = reverse("property:home")

        self.client = Client()

    def test_page_status(self):

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'property/home.html')

    def test_view_fun(self):

        view = resolve(self.url)

        self.assertEqual(view.func.view_class, views.PropertyHomeView)
        

class TestPropertyListView(TestCase):

    def setUp(self):

        self.url = reverse("property:list")

        self.client = Client()

        self.response = self.client.get(self.url)

    def test_page_status(self):
    
        self.assertEqual(self.response.status_code, 200)

        self.assertTemplateUsed(self.response, 'property/property_list.html')

    def test_view_fun(self):

        view = resolve(self.url)

        self.assertEqual(view.func.view_class, views.PropertyListView)

    def test_property_object_count(self):

        objects_ = Property.objects.all()

        view_object = views.PropertyListView().get_queryset()

        self.assertEqual(len(objects_), len(view_object))

