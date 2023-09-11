from django.http import HttpResponse
from django_nextjs.render import render_nextjs_page

async def index(request):
    return await render_nextjs_page(request, "nextjs_app/src/app/page.tsx")