from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Note,Bin
from django.utils import timezone
from django.urls import reverse

def index(request,id):
    if request.method=='GET':
        ''' This will return a page with all past notes
        with a option to delete a note or add a note'''
        user=User.objects.get(pk=id)

        note_list=user.note_set.all()
        return render(request,'notes/index.html',{'note_list':note_list,'userid':id})
    else:
        return HttpResponse("Hey! A Error might Had Occured !")

def add(request,id):
    if request.method=='GET':
        ''' For opening a page to add a new note.'''
        return render(request,'notes/add.html',{'userid':id})
    else:
        if(request.POST['upload']):
            title=request.POST['title']
            note=request.POST['note']
            upload=request.POST['uplaod']
            user=User.objects.get(pk=id)
            note= user.note_set.create(title=title,datetime=timezone.now(),note=note, upload=upload,editdate=timezone.now())
            note.save()
            userid=user.id
            return HttpResponseRedirect(reverse('notes:index', args=[user.id]))

        else:
            title=request.POST['title']
            note=request.POST['note']
            user=User.objects.get(pk=id)
            note= user.note_set.create(title=title,datetime=timezone.now(),note=note, editdate=timezone.now())
            note.save()
            userid=user.id
            return HttpResponseRedirect(reverse('notes:index', args=[user.id]))

def delete(request,userid,noteid):
    if request.method=='GET':
        user=User.objects.get(pk=userid)
        note=user.note_set.get(pk=noteid)
        bin_note=user.bin_set.create(note=note.note,title=note.title,datetime=note.datetime, deletedate=timezone.now())
        bin_note.save()
        note.delete()
        return HttpResponseRedirect(reverse('notes:index', args=[userid]))
    else:
        return HttpResponse("It seems you are at the Wrong Page!")

def edit(request,userid,noteid):
    if request.method=='GET':
        user=User.objects.get(pk=userid)
        note=Note.objects.get(pk=noteid)
        title=note.title
        note=note.note

        return render(request,'notes/edit.html',{'userid':userid,'noteid':noteid,'note':note,'title':title})

    else:
        title=request.POST['title']
        note=request.POST['note']
        old=Note.objects.get(pk=noteid)
        old.note= note
        old.title=title
        old.editdate=timezone.now()
        old.save()
        return HttpResponseRedirect(reverse('notes:index' ,args=[userid]) )

def bin(request,userid):
    if request.method=='GET':
        user=User.objects.get(pk=userid)
        bin_note_list=user.bin_set.all()
        return render(request,'notes/bin.html',{'bin_note_list':bin_note_list,'userid':userid})

def undo(request,userid,noteid):
    if request.method=="GET":
        bin_note=Bin.objects.get(pk=noteid)
        user=User.objects.get(pk=userid)
        note=user.note_set.create(title=bin_note.title,note=bin_note.note,datetime=bin_note.datetime, editdate=timezone.now())
        note.save()
        bin_note.delete()
        return HttpResponseRedirect(reverse('notes:index',args=[userid]))

def bin_delete(request,userid,noteid):
    if request.method=="GET":
        bin_note=Bin.objects.get(pk=noteid)
        bin_note.delete()
        return HttpResponseRedirect(reverse('notes:bin', args=[userid]))

# Create your views here.
