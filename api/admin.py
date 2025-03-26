from django.contrib import admin
from .models import *

class OfferCardInline(admin.StackedInline):
    model = OfferCard
    extra = 0

class AdvantagesInline(admin.StackedInline):
    model = Advantages
    extra = 0

class ServiceCardInline(admin.StackedInline):
    model = ServiceCard
    extra = 0

class ProjectCardInline(admin.StackedInline):
    model = ProjectCard
    extra = 0

class GalleryCardInline(admin.StackedInline):
    model = GalleryCard
    extra = 0

class TestimonialCardInline(admin.StackedInline):
    model = TestimonialCard
    extra = 0

class ContactFormServicesInline(admin.StackedInline):
    model = ContactFormServices
    extra = 0


@admin.register(MainBanner)
class MainBannerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not MainBanner.objects.exists()

@admin.register(ExclusiveOffers)
class ExclusiveOffersAdmin(admin.ModelAdmin):
    inlines = [OfferCardInline]

@admin.register(ExclusiveOfferBanner)
class ExclusiveOfferBannerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not ExclusiveOfferBanner.objects.exists()

@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    inlines = [AdvantagesInline]

@admin.register(ServicesSection)
class ServicesSectionAdmin(admin.ModelAdmin):
    inlines = [ServiceCardInline]

@admin.register(ProjectsSection)
class ProjectsSectionAdmin(admin.ModelAdmin):
    inlines = [ProjectCardInline]

@admin.register(GallerySection)
class GallerySectionAdmin(admin.ModelAdmin):
    inlines = [GalleryCardInline]

@admin.register(TestimonialsSection)
class TestimonialsSectionAdmin(admin.ModelAdmin):
    inlines = [TestimonialCardInline]

@admin.register(ContactsSection)
class ContactsSectionAdmin(admin.ModelAdmin):
    inlines = [ContactFormServicesInline]


@admin.register(ClientFeedback)
class ClientFeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')