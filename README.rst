What is postabstract?
======================
A quick demo of Mezzanine's way of injecting custom fields in existing models.
`postabstract` injects a rich text field for post abstract, named `abstract`.

Requirements
======================

This worked for me with Django 1.4.1 and Mezzanine 1.2.4

Installation
======================

1. Place 'postabastract' in INSTALLED_APPS of your django projects' settings
   file.
#. Place following code in settings file::

    EXTRA_MODEL_FIELDS = () # or replace with existing value
    from postabstract import inject
    EXTRA_MODEL_FIELDS += inject.EXTRA_MODEL_FIELDS

#. Run migration::

    python manage.py migrate mezzanine.blog

#. Aaand you're done! You should see the abstract field in your django admin
   for each blog post, just before the featured image (or description). You can
   now extend/overextend "blog_post_list.html" and change::

    {% editable page.richtextpage.content %}
    {{ blog_post.description_from_content|safe }}
    {% endeditable %}

   to

    {% editable blog_post.abstract %}
    {{ blog_post.abstract|richtext_filter|safe }}
    {% endeditable %}

   You may also add this to "blog_post_detail.html" overextension.
