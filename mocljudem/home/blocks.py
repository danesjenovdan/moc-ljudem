from wagtail import blocks


class LinkBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        label="Besedilo povezave",
    )
    url = blocks.URLBlock(
        required=True,
        label="Povezava, kamor vodi",
    )

    class Meta:
        icon = "link"
        label = "Povezava"


class StatusTypeBlock(blocks.ChoiceBlock):
    choices = [
        ("empty", "Prazen"),
        ("blue", "Moder"),
        ("green", "Zelen"),
        ("yellow", "Rumen"),
        ("red", "Rdeč"),
        ("violet", "Vijoličen"),
    ]
    default = "empty"

    class Meta:
        icon = "tag"
        label = "Tip statusa"
