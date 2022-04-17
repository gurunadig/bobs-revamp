from django.contrib import admin
from .models import Artist, Podcast, Radiolink, Blog, Bobstv, Carousel

admin.site.register(Artist)
admin.site.register(Podcast)
admin.site.register(Blog)
admin.site.register(Radiolink)
admin.site.register(Bobstv)
admin.site.register(Carousel)
