from django.contrib import admin

# Register your models here.
from finder.models import Site, Tag, Matches

admin.site.register(Site)
admin.site.register(Tag)
admin.site.register(Matches)