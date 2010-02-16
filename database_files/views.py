import base64
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_control
import mimetypes
from database_files.models import File
import os

@cache_control(max_age=86400)
def serve(request, name):
    pk, file_ext = os.path.splitext(name)
    try:
        pk = int(pk)
    except ValueError:
        raise Http404('Filename is not an integer')
    f = get_object_or_404(File, pk=pk)
    mimetype = mimetypes.guess_type(name)[0] or 'application/octet-stream'
    response = HttpResponse(base64.b64decode(f.content), mimetype=mimetype)
    response['Content-Length'] = f.size
    return response
