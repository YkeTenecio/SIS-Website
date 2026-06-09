from django.db import models

# ── Shared choices ────────────────────────────────────────────────────────────

class YearChoices(models.TextChoices):
    FYFS = 'FYFS', 'First Year | First Sem'
    FYSS = 'FYSS', 'First Year | Second Sem'
    FYS  = 'FYS',  'First Year | Summer'
    SYFS = 'SYFS', 'Second Year | First Sem'
    SYSS = 'SYSS', 'Second Year | Second Sem'
    SYS  = 'SYS', 'Second Year | Summer'
    M    = 'M',    'Major'
    POS = 'POS', 'Program of Study'


class SDSProgChoices(models.TextChoices):
    COMDEV   = 'COMDEV',   'Community Development'
    ECONDEV  = 'ECONDEV',  'Economic Development'
    ENVIED   = 'ENVIED',   'Environmental Education'
    ENVIENGG = 'ENVIENGG', 'Environmental Engineering'
    RESMGT   = 'RESMGT',   'Resource Management'
    RUP      = 'RUP',      'Rural and Urban Planning'
    PCT      = 'PCT',      'Peace and Conflict Transformation'


class TitleChoices(models.TextChoices):
    PHD   = 'PhD',   'PhD'
    DISDS = 'DiSDS', 'DiSDS'
    MSC   = 'MSc',   'MSc'


# ── Home ──────────────────────────────────────────────────────────────────────

class Home_Event(models.Model):
    title       = models.CharField(max_length=255)
    description = models.TextField()
    event_date  = models.DateField()

    def __str__(self):
        return self.title


class Home_Announcement(models.Model):
    title   = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

# ── Environmental Science subjects ────────────────────────────────────────────
# EPM, ER, and PhDES collapsed into one model with a program_type field.

class EnviSubject(models.Model):
    class ProgramType(models.TextChoices):
        EPM   = 'EPM',   'MSES Environmental Planning and Management'
        ER    = 'ER',    'MSES Environmental Research'
        PHDES = 'PHDES', 'PhD Environmental Science'

    program_type = models.CharField(max_length=10, choices=ProgramType.choices)
    year         = models.CharField(max_length=32, choices=YearChoices.choices)
    subject      = models.CharField(max_length=100, blank=True, null=True)
    POS_link     = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name        = 'Environmental Science Subject'
        verbose_name_plural = 'Environmental Science Subjects'

    def __str__(self):
        return f"{self.get_program_type_display()} | {self.get_year_display()} - {self.subject}"


# ── SDS subjects ──────────────────────────────────────────────────────────────
# All 6 SDS models (MSDS, MSSDS, DSDSw, DSDSwo, PhDSDSw, PhDSDSwo)
# collapsed into one model with a program_type field.

class SDSSubject(models.Model):
    class ProgramType(models.TextChoices):
        MSDS     = 'MSDS',     'Master in Sustainable Development Studies'
        MSSDS    = 'MSSDS',    'Master of Science in Sustainable Development Studies'
        DSDSW    = 'DSDSW',    'Doctor in SDS (with bridging)'
        DSDSWO   = 'DSDSWO',   'Doctor in SDS (without bridging)'
        PHDSDSW  = 'PHDSDSW',  'PhD SDS (with bridging)'
        PHDSDSWO = 'PHDSDSWO', 'PhD SDS (without bridging)'

    program_type = models.CharField(max_length=10, choices=ProgramType.choices)
    prog         = models.CharField(max_length=32, choices=SDSProgChoices.choices)
    year         = models.CharField(max_length=32, choices=YearChoices.choices)
    subject      = models.CharField(max_length=100, blank=True, null=True)
    POS_link     = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name        = 'SDS Subject'
        verbose_name_plural = 'SDS Subjects'

    def __str__(self):
        return f"{self.get_program_type_display()} | {self.get_year_display()} - {self.prog} - {self.subject}"


# ── Data Science subjects ─────────────────────────────────────────────────────

class MDS(models.Model):
    year    = models.CharField(max_length=32, choices=YearChoices.choices)
    subject      = models.CharField(max_length=100, blank=True, null=True)
    POS_link     = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name        = 'MDS Subject'
        verbose_name_plural = 'MDS Subjects'

    def __str__(self):
        return f"{self.get_year_display()} - {self.subject}"


# ── Faculty & Staff ───────────────────────────────────────────────────────────

class Faculties(models.Model):
    class Category(models.TextChoices):
        FACULTY   = 'FACULTY',   'Faculty'
        AFFILIATE = 'AFFILIATE', 'Affiliate'
        STAFF     = 'STAFF',     'Staff'

    class Department(models.TextChoices):
        ENVISCI    = 'ENVISCI',    'Environmental Science'
        SUSTAINDEV = 'SUSTAINDEV', 'Sustainable Development'
        DATASCI    = 'DATASCI',    'Data Science'

    class Position(models.TextChoices):
        DEAN        = 'DEAN',        'Dean'
        ASSTDEAN    = 'ASSTDEAN',    'Assistant Dean'
        CHAIRPERSON = 'CHAIRPERSON', 'Chairperson'
        PRGCOORD    = 'PRGCOORD',    'Program Coordinator'

    class Rank(models.TextChoices):
        PROF       = 'Prof',      'Professor'
        ASSOC_PROF = 'Assoc Prof', 'Associate Professor'
        ASSOC_LEC  = 'Asoc Lec', 'Associate Lecturer'
        ASST_PROF  = 'Asst Prof', 'Assistant Professor'
        LEC        = 'Lec',       'Lecturer'

    name       = models.CharField(max_length=225, unique=True)
    category   = models.CharField(max_length=12, choices=Category.choices)
    department = models.CharField(max_length=12, choices=Department.choices)
    position   = models.CharField(max_length=12, choices=Position.choices, blank=True, null=True)
    rank       = models.CharField(max_length=12, choices=Rank.choices, blank=True, null=True)
    title      = models.CharField(max_length=12, choices=TitleChoices.choices, blank=True, null=True)
    image_url  = models.URLField(blank=True, null=True)
    email      = models.EmailField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return self.name


# ── Research ──────────────────────────────────────────────────────────────────

class Agendas(models.Model):
    title   = models.CharField(max_length=200)
    content = models.CharField(max_length=600)

    def __str__(self):
        return self.title


# ── Resources ─────────────────────────────────────────────────────────────────

class Resources(models.Model):
    class Type(models.TextChoices):
        GUIDES    = 'Downloadable Guides', 'Downloadable Guides'
        ADMISSION = 'Admission Related',   'Admission Related'
        PROPOSAL  = 'Proposal Forms',      'Proposal Forms'
        DEFENSE   = 'Defense Forms',       'Defense Forms'
        COMPRE    = 'Comprehensive Exam',  'Comprehensive Exam'
        REGISTRAR = 'Registrar Forms',     'Registrar Forms'
        ETHICS    = 'Research Ethics',     'Research Ethics'
        QUALITY   = 'Quality Assurance',   'Quality Assurance'
        LINKAGES  = 'Linkages',            'Linkages'

    TYPE_ORDER = [
        Type.GUIDES, Type.ADMISSION, Type.PROPOSAL, Type.DEFENSE,
        Type.COMPRE, Type.REGISTRAR, Type.ETHICS, Type.QUALITY, Type.LINKAGES,
    ]
    
    type       = models.CharField(max_length=32, choices=Type.choices)
    resource   = models.CharField(max_length=600)
    links      = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.resource    