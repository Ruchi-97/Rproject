from django.contrib import admin
from myapp.models import level3data , level1data ,level2data,clickCount,answers,Scores,FinalScore


# Register your models here.
admin.site.register(level1data)
admin.site.register(level2data)
admin.site.register(level3data)
admin.site.register(clickCount)
admin.site.register(answers)
admin.site.register(Scores)
admin.site.register(FinalScore)

