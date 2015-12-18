from scrapy.contrib.spiders import CrawlSpider


class YoutubeCrawler(CrawlSpider):

    name = "youtube"
    allowed_domains = ["youtube.com"]
    start_urls = [
        "https://www.youtube.com/watch?v=bAxlsajbcUg"
    ]

    def parse(self, response):

        visits = response.xpath("//div[@class='watch-view-count']\
            /text()").extract()[0]

        likes = response.xpath("//span[contains(@class, 'like-button-renderer')]\
            /span[position()=1]/button/span/text()").extract()[0]

        dislikes = response.xpath("//span[contains(@class, 'like-button-renderer')]\
            /span[position()=3]/button/span/text()").extract()[0]

        print "visits: %s" % visits
        print "likes: %s" % likes
        print "dislikes: %s" % dislikes
