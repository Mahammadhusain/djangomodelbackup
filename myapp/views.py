from django.shortcuts import render,redirect
from django.apps import apps
from django.conf import settings
from django.core.management import call_command
from django.contrib import messages
import os
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
# Create your views here.
def BackupView(request):
    final_data_list =[{"app_name":app,"app_models":apps.all_models[app].keys()} for app in settings.INSTALLED_APPS if not app.startswith("django.")]
    directory = os.getcwd()
    path = directory
    try:
      backup_list = os.listdir(path+"\Backups")
    except Exception as e:
      messages.error(request,f'File path not found !')
      print('Not found')
      return redirect('/')

    if request.method == "POST":

      app_lbl = request.POST.get('select1')
      app_model = request.POST.get('select2')
      now = datetime.now()
      today_date = now.strftime("%d-%m-%y")
      today_time = now.strftime("(%I-%M-%p)")
      w= str(today_date+"_"+today_time)
      directory = os.getcwd()
      p = os.path.join(directory,f"Backups\{app_lbl}_{app_model}__{w}.json")
      with open(p, "w", encoding="utf-8") as fp:
        call_command(f"dumpdata",f"{app_lbl}.{app_model}", format="json", indent=3, stdout=fp)
        messages.success(request,f'({app_lbl}) | ({app_model}) Backup success')
        return redirect('/')


    context = {
      'final_data_list':final_data_list,
      'backup_list':backup_list,
    }
    return render(request,'index.html',context)


def RestoreView(request):
  if request.method == "POST":
    ContentType.objects.all().delete() 
    data_file = request.POST.get('restore')
    base_dir = os.getcwd()
    try:
      f_path = os.path.join(base_dir,'Backups',data_file)
      call_command("loaddata",f_path)
      messages.info(request,'Database restore success')
      return redirect('/')
    except Exception as e:
      messages.error(request,f'File path not found !')
      print('Not found')
      return redirect('/')

  context = {}
  return render(request,'index.html',context)