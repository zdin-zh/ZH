from urllib.parse import unquote
from menu.views import *

from authentication.forms import PostForm

from smzh.models import BaseProfile,Post,Profile,Account

from django.views.generic import View
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect




class HomePageView(View):
      template_name ='home/home.html'

      def get(self, request): 

          form = PostForm()
                  
          response = ZedahServices.Test_User_Login(request)
          if not response:
           return  HttpResponseRedirect("/")

          template_name = 'home.html'
          user_obj = Profile.objects.filter(id=request.session['user_id'])
          userIdOfSession = (user_obj[0].username)
          data = {'username': request.session['username'], 'user': user_obj,'form': form}
          return render(request, template_name, data)

      def post(self, request):

          form = PostForm(request.POST, request.FILES)
          
          post = form.save()
              
          return redirect('upload')
          context = {
           "form": PostForm(),
           "alldata": Post.objects.all()
          }
          return render(request, "home.html", context)    
 
