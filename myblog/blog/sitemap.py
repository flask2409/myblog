from django.contrib.sitemaps import Sitemap
from blog.models import Post


class SitemapXML(Sitemap):
    
    changefreq = 'weekly'
    
    priority = 0.5

    def items(self):
        
        return Post.objects.filter().order_by('pk')

    def lastmod(self, obj):
        
        return obj.date

    def location(self, obj):
       
        return "/post/%s/" % obj.id