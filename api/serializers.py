from rest_framework import serializers
from .models import MainBanner, ExclusiveOfferBanner, ExclusiveOffers, WhyChooseUs, ServicesSection, ProjectsSection, \
    GallerySection, TestimonialsSection, ContactsSection, ClientFeedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFeedback
        fields = '__all__'


class FlatHomePageDTO(serializers.Serializer):
    main_banner_image = serializers.SerializerMethodField()

    exclusive_offers = serializers.SerializerMethodField()

    exclusive_offer_banner_title = serializers.SerializerMethodField()

    why_choose_us_image = serializers.SerializerMethodField()
    why_choose_us_description = serializers.SerializerMethodField()
    advantages = serializers.SerializerMethodField()

    services_title = serializers.SerializerMethodField()
    services_description = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()

    projects_title = serializers.SerializerMethodField()
    projects_description = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()

    gallery_title = serializers.SerializerMethodField()
    gallery_description = serializers.SerializerMethodField()
    gallery = serializers.SerializerMethodField()

    testimonials_title = serializers.SerializerMethodField()
    testimonials_description = serializers.SerializerMethodField()
    testimonials = serializers.SerializerMethodField()

    contacts_title = serializers.SerializerMethodField()
    contacts_description = serializers.SerializerMethodField()
    contacts_phone = serializers.SerializerMethodField()
    contacts_email = serializers.SerializerMethodField()
    contacts_working_hours = serializers.SerializerMethodField()
    contacts_address = serializers.SerializerMethodField()
    contact_services = serializers.SerializerMethodField()

    # ----------------------------
    def get_main_banner_image(self, obj):
        banner = MainBanner.objects.first()
        return banner.image.url if banner else None

    def get_exclusive_offer_banner_title(self, obj):
        banner = ExclusiveOfferBanner.objects.first()
        return banner.title if banner else ""

    def get_exclusive_offers(self, obj):
        offers = ExclusiveOffers.objects.prefetch_related('offer_cards').first()
        return {
                "title": offers.title,
                "description": offers.description,
                "cards": [
                    {
                        'id': c.id,
                        "title": c.title,
                        "package_slogan": c.package_slogan,
                        "offer_consept": c.offer_consept,
                        "starting_price": c.starting_price,
                        "attribute_one": c.attribute_one,
                        "attribute_two": c.attribute_two,
                        "attribute_three": c.attribute_three,
                        "attribute_four": c.attribute_four,
                    } for c in offers.offer_cards.all()
                ]
            }

    def get_why_choose_us_image(self, obj):
        section = WhyChooseUs.objects.first()
        return section.image.url if section else None

    def get_why_choose_us_description(self, obj):
        section = WhyChooseUs.objects.first()
        return section.description if section else ""

    def get_advantages(self, obj):
        section = WhyChooseUs.objects.first()
        return [
            {
                "id": adv.id,
                "title": adv.title,
                "description": adv.description
            } for adv in section.advantages.all()
        ] if section else []

    def get_services_title(self, obj):
        section = ServicesSection.objects.first()
        return section.title if section else ""

    def get_services_description(self, obj):
        section = ServicesSection.objects.first()
        return section.description if section else ""

    def get_services(self, obj):
        section = ServicesSection.objects.first()
        return [
            {   'id': s.id,
                "title": s.title,
                "description": s.description,
                "attribute_one": s.attribute_one,
                "attribute_two": s.attribute_two,
                "attribute_three": s.attribute_three,
            } for s in section.services.all()
        ] if section else []

    def get_projects_title(self, obj):
        section = ProjectsSection.objects.first()
        return section.title if section else ""

    def get_projects_description(self, obj):
        section = ProjectsSection.objects.first()
        return section.description if section else ""

    def get_projects(self, obj):
        section = ProjectsSection.objects.first()
        return [
            {   "id": p.id,
                "title": p.title,
                "card_image": p.card_image.url,
                "card_info": p.card_info,
                "description_image": p.description_image.url,
                "description": p.description,
            } for p in section.projects.all()
        ] if section else []

    def get_gallery_title(self, obj):
        section = GallerySection.objects.first()
        return section.title if section else ""

    def get_gallery_description(self, obj):
        section = GallerySection.objects.first()
        return section.description if section else ""

    def get_gallery(self, obj):
        section = GallerySection.objects.first()
        return [
            {   "id": g.id,
                "title": g.title,
                "image": g.image.url
            } for g in section.gallery_cards.all()
        ] if section else []

    def get_testimonials_title(self, obj):
        section = TestimonialsSection.objects.first()
        return section.title if section else ""

    def get_testimonials_description(self, obj):
        section = TestimonialsSection.objects.first()
        return section.description if section else ""

    def get_testimonials(self, obj):
        section = TestimonialsSection.objects.first()
        return [
            {   "id": t.id,
                "fullname": t.fullname,
                "position": t.position,
                "stars": t.stars,
                "review": t.review,
                "image": t.image.url
            } for t in section.testimonial_cards.all()
        ] if section else []

    def get_contacts_title(self, obj):
        section = ContactsSection.objects.first()
        return section.title if section else ""

    def get_contacts_description(self, obj):
        section = ContactsSection.objects.first()
        return section.description if section else ""

    def get_contacts_phone(self, obj):
        section = ContactsSection.objects.first()
        return section.phone if section else ""

    def get_contacts_email(self, obj):
        section = ContactsSection.objects.first()
        return section.email if section else ""

    def get_contacts_working_hours(self, obj):
        section = ContactsSection.objects.first()
        return section.working_hours if section else ""

    def get_contacts_address(self, obj):
        section = ContactsSection.objects.first()
        return section.address if section else ""

    def get_contact_services(self, obj):
        section = ContactsSection.objects.first()
        return [
            {
                "id": s.id,
                "service": s.service
            } for s in section.services.all()
        ] if section else []
