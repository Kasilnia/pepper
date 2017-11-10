from django.conf.urls import url

from placeholders.views import IndexView, ImageView, WordView, ParagraphView


urlpatterns = [
    url(r'^image/(?P<text>.+)/(?P<width>\d+)x(?P<height>\d+)\.(?P<extension>\w+)$',  # noqa
        ImageView.as_view(), name='image'),
    url(r'^words/(?P<number>\d+)$',
        WordView.as_view(), name='words'),
    url(r'^paragraph/(?P<number>\d+)$',
        ParagraphView.as_view(), name='paragraph'),
    url(r'^$', IndexView.as_view(), name='index'),
]
