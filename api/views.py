from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import validators
import urllib
import xmltodict

class RSSFeed(APIView):
    def post(self, req, format=None):

        website_url = req.data['url']
        req_xml_feed = req.data['xml']
        req_json_feed = req.data['json']
        rss_feed = {}
        json_feed = {}

        if not validators.url(website_url):
            return Response({"message": "Invalid URL Format"}, status=400)

        if website_url[-1] == "/":
            suffix = "feed"

        else:
            suffix = "/feed"

        rss_url = website_url + suffix
        rss_feed = urllib.request.urlopen(rss_url).read()

        if req_json_feed:
            json_feed = xmltodict.parse(rss_feed, process_namespaces=True)


        print(rss_feed)
        print(json_feed)

        return Response({"message": "URL Works", "url_tested": website_url, "xml": rss_feed if req_xml_feed else {}, "json": json_feed}, status=200)
