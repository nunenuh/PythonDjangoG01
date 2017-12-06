from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from provinsi.forms import ProvinceForm
from orm.models import Province

class TestView(View):
    def get(self, request):
        template = "provinsi/index.html"

        data =  {}
        return render(request, template, data)

class ListProvinceView(View):
    def get(self, request):
        template = "provinsi/index.html"
        form = ProvinceForm(request.POST or None)
        province_list = Province.objects.all()
        data =  {
            'form_mode':'add',
            'form': form,
            'province_list': province_list
        }
        return render(request, template, data)

class SaveProvinceView(View):
    def post(self, request):
        template = "provinsi/index.html"
        form = ProvinceForm(request.POST or None)
        if form.is_valid():
            prov = Province()
            prov.name = form.cleaned_data['name']
            prov.save()
            return redirect('provinsi:view')

        province_list = Province.objects.all()
        data =  {
            'form_mode':'add',
            'form': form,
            'province_list': province_list
        }
        return render(request, template, data)

class EditProvinceView(View):
    def get(self, request, id):
        template = "provinsi/index.html"

        form_data = {}
        prov = Province.objects.filter(id=id)
        if not prov.exists():
            return redirect('provinsi:view')
        
        prov = prov.first()
        form_data = {
                'id': prov.id,
                'name': prov.name,
        }
        form = ProvinceForm(initial=form_data)
        province_list = Province.objects.all()
        data =  {
            'form_mode':'edit',
            'id': id,
            'form': form,
            'province_list': province_list
        }
        return render(request, template, data)


class UpdateProvinceView(View):
    def post(self, request):
        template = "provinsi/index.html"
        form = ProvinceForm(request.POST or None)
        if form.is_valid():
            id = int(form.cleaned_data['id'])
            prov = Province.objects.get(pk=id)
            prov.name = form.cleaned_data['name']
            prov.save(force_update=True)
            return redirect('provinsi:view')

        province_list = Province.objects.all()
        data =  {
            'form_mode':'edit',
            'form': form,
            'province_list': province_list
        }
        return render(request, template, data)



class DeleteProvinceView(View):
    def get(self, request, id):
        prov = Province.objects.filter(id=id)
        if prov.exists():
            prov.first().delete()
        return redirect('provinsi:view')