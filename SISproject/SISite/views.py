from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import (
    Home_Event, Home_Announcement,
    EnviSubject, SDSSubject, MDS,
    Faculties, Agendas, Resources,
)

def admission(request):
    return render(request, 'admission.html')

def faqs(request):
    return render(request, 'faqs.html')

# ── Helper functions ──────────────────────────────────────────────────────────

def get_envi_context(program_type):
    """Return semester-split context for a given EnviSubject program_type."""
    qs = EnviSubject.objects.filter(program_type=program_type)

    pos = qs.filter(year='POS').first()
    return {
        'fyfs': qs.filter(year='FYFS'),
        'fyss': qs.filter(year='FYSS'),
        'fys':  qs.filter(year='FYS'),
        'syfs': qs.filter(year='SYFS'),
        'syss': qs.filter(year='SYSS'),
        'm':    qs.filter(year='M'),
        'download_url': pos.POS_link if pos else '#',
    }



def get_sds_context(program_type):
    """Return per-track, per-semester context for a given SDSSubject program_type."""
    qs = SDSSubject.objects.filter(program_type=program_type)
    tracks    = ['COMDEV', 'ECONDEV', 'ENVIED', 'ENVIENGG', 'RESMGT', 'RUP', 'PCT']
    semesters = ['FYFS', 'FYSS', 'FYS', 'SYFS', 'SYSS', 'M']
    sem_keys  = ['fyfs', 'fyss', 'fys', 'syfs', 'syss', 'm']

    context = {}
    for track in tracks:
        track_qs = qs.filter(prog=track)
        for sem, key in zip(semesters, sem_keys):
            context[f'{track.lower()}_{key}'] = track_qs.filter(year=sem)
        pos = track_qs.filter(year='POS').first()
        context[f'{track.lower()}_download_url'] = pos.POS_link if pos else '#'
    
    return context


# ── Home ──────────────────────────────────────────────────────────────────────

def home(request):
    context = {
        'events':        Home_Event.objects.all().order_by('-event_date')[:3],
        'announcements': Home_Announcement.objects.all().order_by('-id')[:3],
    }
    return render(request, 'home.html', context)


# ── About ─────────────────────────────────────────────────────────────────────

def about_overview(request):
    return render(request, 'aboutus-overview.html')


def about_history(request):
    return render(request, 'aboutus-history.html')


def about_vismiss(request):
    return render(request, 'aboutus-vismiss.html')


def about_dean(request):
    context = {
        'deans':    Faculties.objects.filter(position=Faculties.Position.DEAN),
        'asstdean': Faculties.objects.filter(position=Faculties.Position.ASSTDEAN),
        'chair':    Faculties.objects.filter(position=Faculties.Position.CHAIRPERSON),
    }
    return render(request, 'aboutus-dean.html', context)


# ── Programs — overview pages ─────────────────────────────────────────────────

def programs(request):
    context = {
        'deans': Faculties.objects.filter(position=Faculties.Position.DEAN),
    }
    return render(request, 'programs.html', context)


# ENVI

def programsenvi(request):
    try:
        chair = Faculties.objects.get(department='ENVISCI', position=Faculties.Position.CHAIRPERSON)
    except ObjectDoesNotExist:
        chair = None
    context = {'chair': chair}
    return render(request, 'programs-envi.html', context)


def enviepm(request):
    context = get_envi_context(EnviSubject.ProgramType.EPM)
    return render(request, 'programs-envi-epm.html', context)


def envier(request):
    context = get_envi_context(EnviSubject.ProgramType.ER)
    return render(request, 'programs-envi-er.html', context)


def enviphd(request):
    context = get_envi_context(EnviSubject.ProgramType.PHDES)
    return render(request, 'programs-envi-phdes.html', context)


# SDS

def programssds(request):
    try:
        chair = Faculties.objects.get(department='SUSTAINDEV', position=Faculties.Position.CHAIRPERSON)
    except ObjectDoesNotExist:
        chair = None
    context = {'chair': chair}
    return render(request, 'programs-sds.html', context)


def msds(request):
    context = get_sds_context(SDSSubject.ProgramType.MSDS)
    return render(request, 'programs-sds-msds.html', context)


def mssds(request):
    context = get_sds_context(SDSSubject.ProgramType.MSSDS)
    return render(request, 'programs-sds-mssds.html', context)


def dsdsw(request):
    context = get_sds_context(SDSSubject.ProgramType.DSDSW)
    return render(request, 'programs-sds-dsdswith.html', context)


def dsdswo(request):
    context = get_sds_context(SDSSubject.ProgramType.DSDSWO)
    return render(request, 'programs-sds-dsdswithout.html', context)


def phdsdsw(request):
    context = get_sds_context(SDSSubject.ProgramType.PHDSDSW)
    return render(request, 'programs-sds-phdsdswith.html', context)


def phdsdswo(request):
    context = get_sds_context(SDSSubject.ProgramType.PHDSDSWO)
    return render(request, 'programs-sds-phdsdswithout.html', context)


# DS

def programsds(request):
    try:
        chair = Faculties.objects.get(department='DATASCI', position=Faculties.Position.CHAIRPERSON)
    except ObjectDoesNotExist:
        chair = None
    context = {'chair': chair}
    return render(request, 'programs-ds.html', context)


def mds(request):
    qs = MDS.objects.all()

    pos = qs.filter(year='POS').first()

    context = {
        'fyfs': qs.filter(year='FYFS'),
        'fyss': qs.filter(year='FYSS'),
        'fys':  qs.filter(year='FYS'),
        'syfs': qs.filter(year='SYFS'),
        'syss': qs.filter(year='SYSS'),
        'm':    qs.filter(year='M'),
        'download_url': pos.POS_link if pos else '#',
    }
    return render(request, 'programs-ds-mds.html', context)


# ── Students ──────────────────────────────────────────────────────────────────

def students(request):
    return render(request, 'students.html')


# ── Faculty & Staff ───────────────────────────────────────────────────────────

def facultyhome(request):
    return render(request, 'facultystaff-home.html')


def faculty(request):
    context = {
        'facul': Faculties.objects.filter(category=Faculties.Category.FACULTY),
    }
    return render(request, 'facultystaff-faculty.html', context)


def staff(request):
    context = {
        'staff': Faculties.objects.filter(category=Faculties.Category.STAFF),
    }
    return render(request, 'facultystaff-staff.html', context)


def affil(request):
    context = {
        'affil': Faculties.objects.filter(category=Faculties.Category.AFFILIATE),
    }
    return render(request, 'facultystaff-affiliates.html', context)


# ── Research ──────────────────────────────────────────────────────────────────

def research(request):
    return render(request, 'research.html')


def agendas(request):
    context = {
        'agendas': Agendas.objects.all(),
    }
    return render(request, 'research-agendas.html', context)


# ── Resources ─────────────────────────────────────────────────────────────────

def resources(request):
    all_resources = Resources.objects.all().order_by('resource')

    grouped = {}
    for type_key in Resources.TYPE_ORDER:
        items = [r for r in all_resources if r.type == type_key]
        display_label = dict(Resources.Type.choices)[type_key]
        if items:
            grouped[display_label] = items

    context = {'grouped_resources': grouped}
    return render(request, 'resources.html', context)