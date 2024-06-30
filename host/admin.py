from django.contrib import admin

from host.models import Region, Studio, Game, GameMode, Release, Server


class StudioAdmin(admin.ModelAdmin):
    pass


class GameAdmin(admin.ModelAdmin):
    pass


class GameModeAdmin(admin.ModelAdmin):
    pass


class ReleaseAdmin(admin.ModelAdmin):
    pass


class RegionAdmin(admin.ModelAdmin):
    pass


class ServerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Studio, StudioAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GameMode, GameModeAdmin)
admin.site.register(Release, ReleaseAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Server, ServerAdmin)
