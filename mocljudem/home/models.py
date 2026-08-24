from django.db import models
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page


class HomePage(Page):
    logo = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
        verbose_name="Logotip",
        help_text="Slika, ki se prikaže v glavi strani",
    )
    hero_text = RichTextField(
        null=True,
        blank=True,
        verbose_name="Glavno besedilo",
        help_text="Glavno besedilo, ki se prikaže v hero sekciji strani",
    )
    hero_text_source = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Vir besedila",
        help_text="Malo besedilo, ki se prikaže pod glavnim besedilom v hero sekciji strani",
    )
    lead_text = RichTextField(
        null=True,
        blank=True,
        verbose_name="Opis",
        help_text="Opis, ki se prikaže pod hero sekcijo strani",
    )
    info_push = StreamField(
        [
            (
                "button",
                blocks.StructBlock(
                    [
                        (
                            "text",
                            blocks.RichTextBlock(
                                required=True,
                                label="Besedilo na gumbu",
                            ),
                        ),
                        (
                            "url",
                            blocks.URLBlock(
                                required=True,
                                label="Povezava",
                            ),
                        ),
                    ],
                    icon="link",
                    label="Gumb",
                ),
            ),
            (
                "notice",
                blocks.StructBlock(
                    [
                        (
                            "text",
                            blocks.RichTextBlock(
                                required=True,
                                label="Besedilo obvestila",
                            ),
                        ),
                    ],
                    icon="doc-full",
                    label="Obvestilo",
                ),
            ),
        ],
        null=True,
        blank=True,
        verbose_name="Info push",
        help_text="Elementi, ki so prikazani nad preostalo vsebino strani, npr. za obvestila ali akcije",
    )

    content_panels = Page.content_panels + [
        FieldPanel("logo"),
        FieldPanel("hero_text"),
        FieldPanel("hero_text_source"),
        FieldPanel("lead_text"),
        FieldPanel("info_push"),
    ]

    max_count = 1

    def get_context(self, request):
        context = super().get_context(request)
        context["campaigns"] = CampaignPage.objects.child_of(self).live()
        return context


class CampaignPage(Page):
    description = RichTextField(
        null=True,
        blank=True,
        verbose_name="Opis",
        help_text="Opis kampanje",
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
        verbose_name="Slika",
        help_text="Slika kampanje",
    )
    links = StreamField(
        [
            (
                "link",
                blocks.StructBlock(
                    [
                        (
                            "text",
                            blocks.CharBlock(
                                required=True,
                                label="Besedilo povezave",
                            ),
                        ),
                        (
                            "url",
                            blocks.URLBlock(
                                required=True,
                                label="Povezava, kamor vodi",
                            ),
                        ),
                    ],
                    icon="link",
                    label="Povezava",
                ),
            ),
        ],
        null=True,
        blank=True,
        verbose_name="Povezave",
        help_text="Povezave pod naslovom in opisom kampanje",
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("links"),
    ]

    parent_page_type = ["home.HomePage"]
