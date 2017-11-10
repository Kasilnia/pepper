from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView

from PIL import Image, ImageDraw, ImageFont

from utils.functions import random_words


WRONG_EXTENSION_MESSAGE = ('This image format is not supported. ' +
                           'Please try again.')
WRONG_TYPE_MESSAGE = ('You have chosen the wrong content type. ' +
                      'You should choose txt, json or html content type.')


class IndexView(TemplateView):
    template_name = 'index.html'


class ImageView(View):

    def get(self, request, text, width, height, extension, **kwargs):
        image_size = (int(width), int(height))
        image = Image.new('RGB', image_size, 'white')
        draw = ImageDraw.Draw(image)
        text_width, text_height = draw.textsize(text)
        text_position = ((int(width) - text_width) / 2,
                         (int(height) - text_height) / 2)
        draw.text(text_position, text, (0, 0, 0), align='center')
        response = HttpResponse(content_type='image/{}'.format(extension))
        try:
            image.save(response, extension)
        except KeyError:
            return HttpResponse(WRONG_EXTENSION_MESSAGE)
        return response


class WordView(View):

    def get(self, request, number, **kwargs):
        number = int(number)
        words_list = random_words(number)
        words = ' '.join(words_list)
        content_type = request.content_type
        if content_type == 'text/plain':
            return HttpResponse(words)
        elif content_type == 'text/html':
            return render(request, 'placeholders/word.html', {'words': words})
        elif content_type == 'application/json':
            return JsonResponse({'words': words_list})
        else:
            return HttpResponse(WRONG_TYPE_MESSAGE)


class ParagraphView(View):

    def get(self, request, number, **kwargs):
        number = int(number)
        paragraphs = []
        for i in range(number):
            paragraphs.append(' '.join(random_words(10)))
        content_type = request.content_type
        if content_type == 'text/plain':
            response = HttpResponse('<br/><br/>'.join(paragraphs))
        elif content_type == 'text/html':
            return render(request, 'placeholders/paragraph.html',
                          {'paragraphs': paragraphs})
        elif content_type == 'application/json':
            return JsonResponse({'paragraphs': paragraphs})
        else:
            response = HttpResponse(WRONG_TYPE_MESSAGE)
        return response
