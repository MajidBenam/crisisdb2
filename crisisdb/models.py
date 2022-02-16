from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
#from model_utils.models import StatusModel
from django.core.exceptions import ValidationError
from django.urls import reverse

from datetime import date

import uuid

from django.utils import translation

# This will include all the Polities in Seshat (Classic and CrisisDB)


APS = 'A;P*'
AP = 'A;P'
NFY = 'NFY'
UU = 'U*'
AA = 'A'
PP = 'P'
PS = 'P*'
AS = 'A*'
Certainty = (
    (APS, 'Absent Present Suspected'),
    (AP, 'Absent Present'),
    (UU, 'Unknown'),
    (AA, 'Absent'),
    (PP, 'Present'),
    (AS, 'Absent Suspected'),
    (PS, 'Present Suspected'),
    (NFY, 'Not Filled Yet'),
)

Tags = (
    ('TRS', 'Trusted'),
    ('DSP', 'Disputed'),
    ('SSP', 'Suspected'),
    ('IFR', 'Inferred'),
    ('UNK', 'Unknown'),
)


class Polity(models.Model):
    name = models.CharField(max_length=100)
    start = models.IntegerField(blank=True, null=True)
    end = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'polity'
        verbose_name_plural = 'polities'

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    polity = models.ForeignKey(Polity, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name


class Subsection(models.Model):
    name = models.CharField(max_length=100)
    sect = models.ForeignKey(
        'Section', on_delete=models.SET_NULL, null=True, related_name="subsection")

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name


class Reference(models.Model):
    """Model Representing a Reference"""
    title = models.CharField(
        max_length=200, help_text='Enter a book Genre Please...')
    year = models.IntegerField(
        blank=True, null=True, help_text="year of Publication")
    creator = models.CharField(
        max_length=100, help_text="Creator of pub")
    zotero_link = models.CharField(
        max_length=100, help_text="choose the 8-digit Zotero link")

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return "(%s_%s)" % (self.creator, self.year)


class Citation(models.Model):
    """Model representing a specific citation."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique Id for this particular citation")
    ref = models.ForeignKey(
        'Reference', on_delete=models.SET_NULL, null=True, related_name="citation")
    page_from = models.IntegerField(null=True, blank=True)
    page_to = models.IntegerField(null=True, blank=True)

    # class Meta:
    #     permissions = (("can_mark_returned", "Set book as returned"),
    #                    ("can_renew", "Can Renew A Book"),)

    def __str__(self) -> str:
        """String for representing the Model Object"""
        if self.page_from == self.page_to or ((not self.page_to) and self.page_from):
            return '({0}_{1}, p. {2})'.format(self.ref.creator, self.ref.year, self.page_from)
        elif self.page_from and self.page_to:
            return '({0}_{1}, pp. {2}-{3})'.format(self.ref.creator, self.ref.year, self.page_from, self.page_to)
        else:
            return '({0}_{1})'.format(self.ref.creator, self.ref.year)


class Rulertransition(models.Model):
    name = models.CharField(
        max_length=100, default="Ruler Transition")
    polity = models.ForeignKey(Polity, on_delete=models.SET_DEFAULT, default=1)
    predecessor = models.CharField(max_length=100, blank=True, null=True)
    successor = models.CharField(max_length=100, blank=True,  null=True)
    start_reign_predecessor = models.IntegerField(blank=True, null=True)
    end_reign_transition = models.IntegerField(blank=True, null=True)
    reign_number_predecessor = models.IntegerField(blank=True, null=True)

    contested = models.CharField(
        max_length=5, choices=Certainty, blank=True, null=True)
    overturn = models.CharField(
        max_length=5, choices=Certainty,  blank=True, null=True)
    assassination_predecessor = models.CharField(
        max_length=5, choices=Certainty, blank=True, null=True)
    intra_elite = models.CharField(
        max_length=5, choices=Certainty,  blank=True, null=True)
    military_revolt = models.CharField(
        max_length=5, choices=Certainty,  blank=True, null=True)
    popular_uprising = models.CharField(
        max_length=5, choices=Certainty,  blank=True, null=True)
    separatist_rebellion = models.CharField(
        max_length=5, choices=Certainty,  blank=True, null=True)
    external_invasion = models.CharField(
        max_length=5, choices=Certainty, blank=True, null=True)
    external_interference = models.CharField(
        max_length=5, choices=Certainty, blank=True, null=True)
    conflict_name = models.CharField(max_length=200, blank=True, null=True)
    transition_label = models.CharField(max_length=200, blank=True, null=True)

    description = models.TextField(
        blank=True, null=True, help_text="Add an Optional description or a personal comment above.")
    citations = ManyToManyField(
        Citation, help_text=mark_safe('Select one or more references for this fact. Hold CTRL to select multiple.'), blank=True,)
    finalized = models.BooleanField(default=False)
    tag = models.CharField(
        max_length=5, choices=Tags, blank=True, null=True)

    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'ruler transition'
        verbose_name_plural = 'ruler transitions'

    def clean(self):
        #b = Polity.objects.get(id=1)
        if self.polity == False:
            raise ValidationError('Please Enter a Polity Name.')
        elif self.end_reign_transition < self.start_reign_predecessor:
            raise ValidationError(
                'The start and the end do not match. Please fix it.')
        elif self.assassination_predecessor == 'P' and self.overturn == 'A':
            raise ValidationError(
                'In case of an assassination there must be an overturn. ')
        # elif b.start_date > self.start_reign_predecessor:
        #    raise ValidationError('The start and the end do not match the parent polity. Please fix it.')

    def display_citations(self):
        return '<br>'.join(['<a href="#"> ref: ' + citation.ref.title[:25]+' ... </a>' for citation in self.citations.all()[:2]])

    def get_absolute_url(self):
        """Returns the url to access a particular var instance"""
        return reverse('rulertransition-detail', args=[str(self.id)])
        # the above aczually uses self.id to create a customized url

    def __str__(self):
        return "%s: from %s to %s" % (self.polity, self.predecessor, self.successor)

# abstract class for use in other things:


class SeshatCommon(models.Model):
    polity = models.ForeignKey(Polity, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss", null=True)
    section = models.ForeignKey(
        Section, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss", blank=True, null=True,)
    subsection = models.ForeignKey(
        Subsection, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss", blank=True, null=True,)
    name = models.CharField(
        max_length=200,)
    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(blank=True, null=True)
    # exra vars will be added in between
    description = models.TextField(
        blank=True, null=True, help_text="Add an Optional description or a personal comment above.")
    citations = ManyToManyField(
        Citation, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss", help_text=mark_safe('Select one or more references for this fact. Hold CTRL to select multiple.'), blank=True,)
    finalized = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    tag = models.CharField(max_length=5, choices=Tags, default="TRS")

    class Meta:
        abstract = True
        ordering = ['polity']


class Majid(SeshatCommon):
    my_total_population = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name


class Agr_Prod_Pop(SeshatCommon):
    """Model Representing an Agricultural Production and Population Variable"""
    name = models.CharField(
        max_length=100, default="Agricultural Production and Population")
    total_population = models.IntegerField(blank=True, null=True)
    arable_land_per_capita = models.DecimalField(
        blank=True, null=True, decimal_places=2, max_digits=7, help_text="Arable Land per capita (mu)")

    class Meta:
        verbose_name = 'Agricultural production and population'
        verbose_name_plural = 'Agricultural production and populations'

    @property
    def display_citations(self):
        return ', '.join(['<a href="#">' + citation.__str__() + ' </a>' for citation in self.citations.all()[:2]])

    # I think it is for Admin site as well.
    #display_citations.short_description = 'Citations'

    def clean(self):
        if self.year_from > self.year_to:
            raise ValidationError({
                'year_from': 'The start year is bigger than the end year!',
            })
        if self.year_from < -10000 or self.year_from > date.today().year:
            raise ValidationError({
                'year_from': 'The start year is out of range!',
            })
        if self.year_to < -10000 or self.year_to > date.today().year:
            raise ValidationError({
                'year_to': 'The end year is out of range!',
            })

    def get_absolute_url(self):
        """Returns the url to access a particular var instance"""
        return reverse('Agr_Prod_Pop-detail', args=[str(self.id)])
        # the above aczually uses self.id to create a customized url

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name + " [for " + self.polity.name + " from " + str(self.year_from) + " to " + str(self.year_to) + "]"


class Agr_Productivity(models.Model):
    """Model Representing an Agricultural Productivity Variable"""
    polity = models.ForeignKey(Polity, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    name = models.CharField(
        max_length=100, default="Agricultural productivity")
    year = models.IntegerField(blank=True, null=True)
    total_amount_of_grain_yield = models.IntegerField(
        blank=True, null=True, help_text="Total amount of grain yield (in 1,000 catties), 1 catty = 1.1 pounds")
    total_size_of_grain_land = models.IntegerField(
        blank=True, null=True, help_text="Total size of grain land (1,000 mu)")
    total_number_of_farmers = models.IntegerField(
        blank=True, null=True, help_text="Total number of farmers (1,000)")
    grain_yield_per_mu = models.IntegerField(
        blank=True, null=True, help_text="Grain yield per mu")
    grain_yield_per_farmer = models.IntegerField(
        blank=True, null=True, help_text="Grain yield per farmer (catty), 1 catty = 1.1 pounds")
    grain_number_per_farmer = models.IntegerField(
        blank=True, null=True, help_text="Grain number per farmer (number of mouths fed)	Notes")

    description = models.TextField(
        blank=True, null=True, help_text="Add an Optional description or a personal comment above.")

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name + " (for " + self.polity.name + " in: " + str(self.year) + ")"


# Agricultural production per population
class Agr_Prod_Per_Pop(models.Model):
    """Model Representing an Agricultural Productivity Variable"""
    polity = models.ForeignKey(Polity, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    name = models.CharField(
        max_length=100, default="Agricultural production per population")
    year = models.IntegerField(blank=True, null=True)
    total_population = models.IntegerField(
        blank=True, null=True, help_text="Total Population (1,000)")
    agricultural_population = models.IntegerField(
        blank=True, null=True, help_text="Agricultural population (1,000)")
    arable_land = models.IntegerField(
        blank=True, null=True, help_text="Arable land (1,000 mu)")
    arable_land_per_farmer = models.DecimalField(
        blank=True, null=True, decimal_places=2, max_digits=7, help_text="Arable land per farmer(mu)")
    gross_grain_shared_per_agricultural_population = models.IntegerField(
        blank=True, null=True, help_text="Gross grain shared per agricultural population (catties per capita),1 catty = 1.1 pounds")
    net_grain_shared_per_agricultural_population = models.IntegerField(
        blank=True, null=True, help_text="Net grain shared per agricultural population (catties per capita), 1 catty = 1.1 pounds")
    Surplus = models.IntegerField(blank=True, null=True)

    description = models.TextField(
        blank=True, null=True, help_text="Add an Optional description or a personal comment above.")

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name + " (for " + self.polity.name + " in: " + str(self.year) + ")"
