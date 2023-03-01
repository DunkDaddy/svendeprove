from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(PostNummer)
admin.site.register(Person)
admin.site.register(Handlinger)
admin.site.register(Handling_Junctions)
admin.site.register(Rapport)
admin.site.register(Rapport_junctions)
admin.site.register(PointGrade)
admin.site.register(Permissions)
admin.site.register(Uddel_Permissions)
admin.site.register(Settings)
admin.site.register(WorkSector)
