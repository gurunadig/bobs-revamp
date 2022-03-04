from django.contrib import admin
from .models import Artist, Podcast, Radiolink, Blog

admin.site.register(Artist)
admin.site.register(Podcast)
admin.site.register(Blog)
admin.site.register(Radiolink)
