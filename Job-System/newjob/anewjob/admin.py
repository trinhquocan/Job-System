from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.safestring import mark_safe
from .models import Category, Job, User,Tag
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .dao import count_job_by_cat

# Register your models here.


class JobTagInlineAdmin(admin.TabularInline):
    model = Job.tags.through
class JobForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Job
        fields = '__all__'
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']



class JobAppAdminSite(admin.AdminSite):
    site_header = "HỆ THỐNG VIỆT LÀM TRỰC TUYẾN"
    def get_urls(self):
        return [
                   path('job-stats/', self.stats_view)
               ] + super().get_urls()

    def stats_view(self, request):
        stats = count_job_by_cat()
        return TemplateResponse(request, 'admin/stats_view.html',context={
            'stats': stats
        })
class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description']
    search_fields = ['subject']
    list_filter = ['id', 'subject']
    form = JobForm
    inlines = [JobTagInlineAdmin]
    readonly_fields = ['ava']
    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }
    def ava(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=obj.image.name)
            )


admin_site = JobAppAdminSite(name="myapp")
admin_site.register(Category, CategoryAdmin)
admin_site.register(Job, JobAdmin)
admin_site.register(Tag)
admin_site.register(User)
