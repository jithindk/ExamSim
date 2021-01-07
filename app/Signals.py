from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import F
from .models import Module, Question, Result, Taken

@receiver(post_save, sender=Module)
def Module_CountUP(sender, instance, created, **kwargs):
    if created:
        c = instance.course
        c.modules=F('modules')+1
        c.save()

@receiver(post_delete, sender=Module)
def Module_CountDown(sender, instance, **kwargs):
    c = instance.course
    c.modules=F('modules')-1
    c.save()

@receiver(post_save, sender=Question)
def Question_CountUP(sender, instance, created, **kwargs):
    if created:
        m = instance.module
        m.questions=F('questions')+1
        m.save()

@receiver(post_delete, sender=Question)
def Question_CountDown(sender, instance, **kwargs):
    m = instance.module
    m.questions=F('questions')-1
    m.save()

@receiver(post_save, sender= Result)
def Enroll_Course(sender, instance, created, **kwargs):
    if created:
        if not Taken.objects.filter(user=instance.user, course=instance.module.course).exists():
            Taken.objects.create(user=instance.user, course=instance.module.course)