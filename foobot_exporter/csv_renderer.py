from django.utils.encoding import smart_text
from rest_framework import renderers

class CsvRenderer(renderers.BaseRenderer):
    media_type = 'text/csv'
    format = 'csv'

    def render(self, data, media_type=None, renderer_context=None):
        return data.encode(self.charset)