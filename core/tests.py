from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import Group

class MyTest(TestCase):
    fixtures = ["dumpdata.json"]

    def test_output_okay(self):
	    pass

#   def test_should_create_group(self):
#       group = Group.objects.get(pk=1)
#       self.assertEqual(group.name, "appusers")