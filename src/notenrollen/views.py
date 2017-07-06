from .settings import RES_BASE_DIR, XSLT_DIR
from os.path import join
from django.http import HttpResponse
from django.shortcuts import render
# from django.template.loader import render_to_string


xslt_path = join(XSLT_DIR, "gen_catalogue_html.xslt")
cataloge_index_path = join(RES_BASE_DIR, "all_objects.xml")
basex_uri = "http://basex:8984"

# base64( <user>:<passwd> ) :
login_data = "YWRtaW46YWRtaW4="

def index_page(request, **args):
    context = {}
    return render(request, "index.html", context )

def explore(request, **args):
    context = {}
    return render(request, "explore.html", context )

def search(request, **args):
    context = {}
    return render(request, "search.html", context )

def quiz(request, **args):
    context = {}
    return render(request, "quiz.html", context )

def search_database(request, **args):
    keyword = args['keyword']
    # TODO: 1. calculate xpath expression
    # TODO: 2. apply this expression on database

    xmldata= '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><TODO> </TODO>'

    # TODO: 3. send database response (xml) to client
    return HttpResponse(xmldata, content_type='application/xml')

def gen_catalogue(request, **args):
    from lxml import etree
    import requests as httplib

    transformation = etree.XSLT(etree.parse(xslt_path))
    url = basex_uri + "/rest/notenrollen/all_objects.xml"
    headers={"Authorization": "Basic YWRtaW46YWRtaW4=", "request": "/" }
    response = httplib.get(url=url, headers=headers)
    source_xml = etree.XML( response.text )

    # source_xml = etree.parse(cataloge_index_path)
    catalog_html = transformation(source_xml, **args)

    context = {
        'catalog_html' : catalog_html
    }

    return render(request, "main.html", context )
