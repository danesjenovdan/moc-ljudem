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
                                required=True, help_text="Besedilo na gumbu"
                            ),
                        ),
                        (
                            "url",
                            blocks.URLBlock(
                                required=True, help_text="Povezava, kamor gumb vodi"
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
                                required=True, help_text="Besedilo obvestila"
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
