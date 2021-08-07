from django.test import TestCase
from TqlCook.models import Recipe

# Create your tests here.
class TqlCookModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Recipe.objects.create(id=9, name='Beef', ingredient='beef', method='heat', views=12, images="123.jpg")

    def test_name_label(self):
        recipe = Recipe.objects.get(id=9)
        field_label=recipe._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_id_label(self):
        recipe = Recipe.objects.get(id=9)
        field_label = recipe._meta.get_field('id').verbose_name
        self.assertEquals(field_label, 'id')

    def test_ingredient_label(self):
        recipe = Recipe.objects.get(id=9)
        field_label=recipe._meta.get_field('ingredient').verbose_name
        self.assertEquals(field_label,'ingredient')

    def test_views_label(self):
        recipe = Recipe.objects.get(id=9)
        field_label=recipe._meta.get_field('views').verbose_name
        self.assertEquals(field_label,'views')