from django.test import TestCase

# Create your tests here.
from refugeerouter.models import Refugee, Flat


class RefugeeTest(TestCase):
    def test_create_object(self):
        r = Refugee.objects.create(last_name='Mustermann', first_name='Max', gender=Refugee.GENDER_MALE, age=42,
                                   contact_data='tel: +42 4242 42424242', origin='city of god', origin_checked=False)
        assert r.id != None


class FlatTest(TestCase):
    def test_create_object(self):
        f = Flat.objects.create(rooms=3, shared_kitchen=False, shared_bath=True, owner_last_name="Wurzel",
                                owner_first_name="Hans", address="Blafooweg 17, 11111 Berlin",
                                contact_data="+49 176 42424242", max_adults=5, min_kids_age=4)
        assert f.id != None
