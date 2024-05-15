from django.db.models import Count

from .models import Category, Job


def load_job(params = {}):
    q = Job.objects.all()
    kw = params.get('kw')
    if kw:
        q = q.objects.filter(name__icontains=kw)
    cate = params.get('cate_id')
    if cate:
        q = q.objects.filter(category_id=cate)
def count_job_by_cat():
    return Category.objects.annotate(count = Count('job__id')).values('id', 'name', 'count')
