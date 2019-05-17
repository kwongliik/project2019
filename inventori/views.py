from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewStokForm, NewInventoriForm
from .models import Pembekal, Stok, Inventori

def home(request):
    pembekals = Pembekal.objects.all()
    return render(request, 'home.html', {'pembekals': pembekals})

def stoks(request, pk):
    pembekal = get_object_or_404(Pembekal, pk=pk)   
    return render(request, 'stoks.html', {'pembekal': pembekal})

@login_required
def new_stok(request, pk):
    pembekal = get_object_or_404(Pembekal, pk=pk)

    if request.method == 'POST':
        form = NewStokForm(request.POST)
        if form.is_valid():
            stok = form.save(commit=False)
            stok.pembekal = pembekal
            stok.save()
            return redirect('stoks', pk=pembekal.pk)  # TODO: redirect to the created topic page
    else:
        form = NewStokForm()
    return render(request, 'new_stok.html', {'pembekal': pembekal, 'form': form})

def inventoris(request, pk, stok_pk):
    stok = get_object_or_404(Stok, pembekal__pk=pk, pk=stok_pk)
    return render(request, 'inventoris.html', {'stok': stok})

@login_required
def new_inventori(request, pk, stok_pk):
    stok = get_object_or_404(Stok, pembekal__pk=pk, pk=stok_pk)
    if request.method == 'POST':
        form = NewInventoriForm(request.POST)
        if form.is_valid():
            inventori = form.save(commit=False)
            inventori.stok = stok
            inventori.created_by = request.user
            inventori.save()
            return redirect('inventoris', pk=pk, stok_pk=stok_pk)
    else:
        form = NewInventoriForm()
    return render(request, 'new_inventori.html', {'stok': stok, 'form': form})

@method_decorator(login_required, name='dispatch')
class InventoriEditView(UpdateView):
    model = Inventori
    fields = ('inventori', 'harga', 'kuantiti')
    template_name = 'edit_inventori.html'
    pk_url_kwarg = 'inventori_pk'
    context_object_name = 'inventori'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        inventori = form.save(commit=False)
        inventori.updated_by = self.request.user
        inventori.updated_at = timezone.now()
        inventori.save()
        return redirect('inventoris', pk=inventori.stok.pembekal.pk, stok_pk=inventori.stok.pk)

@method_decorator(login_required, name='dispatch')
class InventoriDeleteView(DeleteView):
    model = Inventori
    template_name = 'delete_inventori.html'
    pk_url_kwarg = 'inventori_pk'
    context_object_name = 'inventori'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def get_success_url(self):
        # there is a ForeignKey from Stok to Inventori in your model
        return reverse_lazy('inventoris', kwargs={'pk': self.object.stok.pembekal.pk, 'stok_pk': self.object.stok.pk})