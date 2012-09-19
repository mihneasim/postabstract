
from django.utils.translation import ugettext_lazy as _


EXTRA_MODEL_FIELDS = (
    # Four-item sequence for one field injected.
    (
        # field
        "mezzanine.blog.models.BlogPost.abstract",
        # Dotted path to field class.
        "mezzanine.core.fields.RichTextField",
        # Positional args for field class.
        (_("Abstract"),),
        # Keyword args for field class.
        {'default': '',},
    ),
)
