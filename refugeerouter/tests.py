from django.test import TestCase

# Create your tests here.
from refugeerouter.buiseness_logic import group_fits_in_flat
from refugeerouter.models import Refugee, Flat, Group


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


class GroupTest(TestCase):
    def test_create_object(self):
        r = Refugee.objects.create(last_name='Mustermann', first_name='Max', age=42,
                                   contact_data='tel: +42 4242 42424242', origin='city of god', origin_checked=False)
        r2 = Refugee.objects.create(last_name='Mustermann', first_name='Michael', age=42,
                                    contact_data='tel: +42 4242 42424242', origin='city of god', origin_checked=False)
        g = Group.objects.create(name='Group Foo', contact="+49 176 42424242", wish_city="Munich")
        r.group = g
        r.save()
        r2.group = g
        r2.save()
        assert g.refugee_set.count() == 2


class FlatTest(TestCase):

    def test_create_object(self):
        f = Flat.objects.create(owner_last_name='Owner', owner_first_name='Owner Firstname',
                                contact_data="+49 176 42424242", address='Foobar Street; Foobar City', max_male=0,
                                max_kids=2, max_adults=1, min_kids_age=0, max_kids_age=2)
        assert f.id != None

    def test_fit_group(self):
        f = Flat.objects.create(owner_last_name='Owner', owner_first_name='Owner Firstname',
                                contact_data="+49 176 42424242", address='Foobar Street; Foobar City', max_male=0,
                                max_kids=2, max_adults=1, min_kids_age=0, max_kids_age=2)
        f2 = Flat.objects.create(owner_last_name='Owner', owner_first_name='Owner Firstname',
                                contact_data="+49 176 42424242", address='Foobar Street; Foobar City', max_male=2,
                                max_kids=2, max_adults=2, min_kids_age=0, max_kids_age=2)
        r = Refugee.objects.create(last_name='Mustermann', first_name='Max', age=42,
                                   contact_data='tel: +42 4242 42424242', origin='city of god', origin_checked=False)
        r2 = Refugee.objects.create(last_name='Mustermann', first_name='Michael', age=42,
                                    contact_data='tel: +42 4242 42424242', origin='city of god', origin_checked=False)
        g = Group.objects.create(name='Group Foo', contact="+49 176 42424242", wish_city="Munich")
        r.group = g
        r.save()
        r2.group = g
        r2.save()
        assert group_fits_in_flat(group=g, flat=f) == False
        assert group_fits_in_flat(group=g, flat=f2) == True
