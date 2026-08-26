from django.db import models
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from .blocks import LinkBlock, StatusTypeBlock


class BasePage(Page):
    meta_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
        verbose_name="Meta slika",
        help_text="Slika, ki bo prikazana pri deljenju strani na socialnih omrežjih.",
    )

    promote_panels = Page.promote_panels + [
        FieldPanel("meta_image"),
    ]

    class Meta:
        abstract = True


class HomePage(BasePage):
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

    @property
    def campaigns(self):
        return CampaignPage.objects.child_of(self).live()

    class Meta:
        verbose_name = "Domača stran"
        verbose_name_plural = "Domače strani"


class CampaignPage(BasePage):
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
            ("link", LinkBlock()),
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

    parent_page_types = ["home.HomePage"]

    @property
    def timelines(self):
        return TimelinePage.objects.child_of(self).live()

    class Meta:
        verbose_name = "Kampanja"
        verbose_name_plural = "Kampanje"


class TimelinePage(BasePage):
    icon = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
        verbose_name="Ikona",
        help_text="Ikona časovnice",
    )
    statuses = StreamField(
        [
            (
                "status",
                blocks.StructBlock(
                    [
                        (
                            "status_type",
                            StatusTypeBlock(),
                        ),
                        (
                            "title",
                            blocks.CharBlock(
                                required=True,
                                label="Naslov statusa",
                            ),
                        ),
                        (
                            "status_text",
                            blocks.CharBlock(
                                required=False,
                                label="Besedilo statusa",
                                help_text="Kratka besedilna oznaka, ki se prikaže pod naslovom",
                            ),
                        ),
                        (
                            "description",
                            blocks.RichTextBlock(
                                required=False,
                                label="Opis statusa",
                            ),
                        ),
                        (
                            "links",
                            blocks.StreamBlock(
                                [
                                    ("link", LinkBlock()),
                                ],
                                label="Povezave",
                                required=False,
                            ),
                        ),
                    ],
                    icon="radio-empty",
                    label="Status",
                ),
            ),
        ],
        null=True,
        blank=True,
        verbose_name="Statusi",
        help_text="Seznam statusov, ki se prikažejo v časovnici",
    )

    content_panels = Page.content_panels + [
        FieldPanel("icon"),
        FieldPanel("statuses"),
    ]

    parent_page_types = ["home.CampaignPage"]

    class Meta:
        verbose_name = "Časovnica"
        verbose_name_plural = "Časovnice"
