from django.urls import resolve, reverse
from django.test import TestCase
from ..views import home
from ..models import Pembekal


class HomeTests(TestCase):
    def setUp(self):
        self.pembekal = Pembekal.objects.create(pembekal='ABC S/B', alamat='sibu', telefon='1122')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_stoks_page(self):
        stoks_url = reverse('stoks', kwargs={'pk': self.pembekal.pk})
        self.assertContains(self.response, 'href="{0}"'.format(stoks_url))