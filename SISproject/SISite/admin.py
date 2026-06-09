from django.contrib import admin

from .models import (
    Home_Event, Home_Announcement,
    EnviSubject, SDSSubject, MDS,
    Faculties, Agendas, Resources,
)


# ── Home ──────────────────────────────────────────────────────────────────────

@admin.register(Home_Event)
class HomeEventAdmin(admin.ModelAdmin):
    list_display  = ('title', 'event_date')
    search_fields = ('title',)
    ordering      = ('-event_date',)


@admin.register(Home_Announcement)
class HomeAnnouncementAdmin(admin.ModelAdmin):
    list_display  = ('title',)
    search_fields = ('title',)

# ── Subjects ──────────────────────────────────────────────────────────────────

@admin.register(EnviSubject)
class EnviSubjectAdmin(admin.ModelAdmin):
    list_display  = ('program_type', 'year', 'subject')
    list_filter   = ('program_type', 'year')
    search_fields = ('subject',)
    ordering      = ('program_type', 'year')


@admin.register(SDSSubject)
class SDSSubjectAdmin(admin.ModelAdmin):
    list_display  = ('program_type', 'prog', 'year', 'subject')
    list_filter   = ('program_type', 'prog', 'year')
    search_fields = ('subject',)
    ordering      = ('program_type', 'prog', 'year')


@admin.register(MDS)
class MDSAdmin(admin.ModelAdmin):
    list_display  = ('year', 'subject')
    list_filter   = ('year',)
    search_fields = ('subject',)
    ordering      = ('year',)


# ── Faculty & Staff ───────────────────────────────────────────────────────────

@admin.register(Faculties)
class FacultiesAdmin(admin.ModelAdmin):
    list_display  = ('name', 'category', 'department', 'position', 'rank')
    list_filter   = ('category', 'department')
    search_fields = ('name',)
    ordering      = ('category', 'name')


# ── Research ──────────────────────────────────────────────────────────────────

@admin.register(Agendas)
class AgendasAdmin(admin.ModelAdmin):
    list_display  = ('title',)
    search_fields = ('title', 'content')


# ── Resources ─────────────────────────────────────────────────────────────────

@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display  = ('resource', 'type', 'created_at')
    list_filter   = ('type',)
    search_fields = ('resource',)
    ordering      = ('type',)