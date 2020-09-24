from django.shortcuts import render
from django.core import serializers
from django import views, http
from .models import User
# Create your views here.


class ViewBase(views.generic.TemplateView):
    pass


class IndexView(ViewBase):
    template_name = 'main/index.html'


class RadarView(ViewBase):
    template_name = 'main/radar.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["key"] = "INPUT YOUR GOOGLE MAP JAVASCRIPT API KEY"
        return ctx


class RegisterView(ViewBase):
    template_name = 'main/register.html'


class Regist(views.View):

    def post(self, request: http.HttpRequest):
        user = User()
        user.Name = request.POST['name']
        user.Status = request.POST['status']
        user.Size = float(request.POST['size'].__str__())
        user.Latitude = float(request.POST['latitude'].__str__())
        user.Longitude = float(request.POST['longitude'].__str__())
        user.save()
        return render(request, 'main/complete.html', context={
            "message": "登録完了"
        })


class GetUsersView(views.View):

    def get(self, request):
        data = serializers.serialize("json", User.objects.all())
        return http.HttpResponse(content=data)