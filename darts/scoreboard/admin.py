from django.contrib import admin


from scoreboard.models import Event, Game, Game_Score, Player, Score, Team

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
