from django.db import models


class MainBanner(models.Model):
    image = models.ImageField(upload_to='main_banners/')

    def __str__(self):
        return "Main Banner"


class ExclusiveOffers(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=512)

    def __str__(self):
        return "Exclusive Offer"


class OfferCard(models.Model):
    offer = models.ForeignKey(ExclusiveOffers, on_delete=models.CASCADE, related_name='offer_cards')
    title = models.CharField(max_length=256)
    package_slogan = models.CharField(max_length=256)
    offer_consept = models.CharField(max_length=256)
    starting_price = models.IntegerField()
    attribute_one = models.CharField(max_length=256)
    attribute_two = models.CharField(max_length=256)
    attribute_three = models.CharField(max_length=256)
    attribute_four = models.CharField(max_length=256)

    def __str__(self):
        return "Offer Card"


class ExclusiveOfferBanner(models.Model):
    title = models.TextField()

    def __str__(self):
        return "Exclusive Offer Banner"


class WhyChooseUs(models.Model):
    image = models.ImageField(upload_to='why_choose_us/')
    description = models.TextField()

    def __str__(self):
        return "Why Choose Us"


class Advantages(models.Model):
    obj = models.ForeignKey(WhyChooseUs, on_delete=models.CASCADE, related_name='advantages')
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title


class ServicesSection(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return "Services Section"


class ServiceCard(models.Model):
    service = models.ForeignKey(ServicesSection, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    attribute_one = models.CharField(max_length=256)
    attribute_two = models.CharField(max_length=256)
    attribute_three = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class ProjectsSection(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return "Projects Section"


class ProjectCard(models.Model):
    project = models.ForeignKey(ProjectsSection, on_delete=models.CASCADE, related_name='projects')
    card_image = models.ImageField(upload_to='projects/')
    title = models.CharField(max_length=256)
    card_info = models.CharField(max_length=256)
    description_image = models.ImageField(upload_to='projects/')
    description = models.TextField()

    def __str__(self):
        return self.title


class GallerySection(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return "Gallery Section"


class GalleryCard(models.Model):
    gallery = models.ForeignKey(GallerySection, on_delete=models.CASCADE, related_name='gallery_cards')
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class TestimonialsSection(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return "Testimonials Section"


class TestimonialCard(models.Model):
    testimonial = models.ForeignKey(TestimonialsSection, on_delete=models.CASCADE, related_name='testimonial_cards')
    stars = models.IntegerField()
    review = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    fullname = models.CharField(max_length=256)
    position = models.CharField(max_length=256)

    def __str__(self):
        return self.fullname


class ContactsSection(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    phone = models.CharField(max_length=256)
    email = models.EmailField()
    working_hours = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

    def __str__(self):
        return "Contacts Section"


class ContactFormServices(models.Model):
    contact = models.ForeignKey(ContactsSection, on_delete=models.CASCADE, related_name='services')
    service = models.CharField(max_length=256)

    def __str__(self):
        return self.service


class ClientFeedback(models.Model):
    service = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    phone = models.CharField(max_length=256)
    message = models.TextField()

    def __str__(self):
        return self.name