from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Pembekal, Stok, Inventori
from ..views import inventoris


class InventorisTests(TestCase):
    def setUp(self):
        pembekal = Pembekal.objects.create(pembekal='cemerlang s/b', alamat='sibu', telefon='112233')
        user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        stok = Stok.objects.create(stok='alatulis', pembekal=pembekal)
        Inventori.objects.create(inventori='pencil', stok=stok, harga=2.00, created_by=user)
        url = reverse('inventoris', kwargs={'pk': pembekal.pk, 'stok_pk': stok.pk})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/pembekal/1/stok/1/')
        self.assertEquals(view.func, inventoris)