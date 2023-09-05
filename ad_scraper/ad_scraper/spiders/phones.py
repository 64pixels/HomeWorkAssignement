import scrapy
from ..items import AdScraperItem

class PhonesSpider(scrapy.Spider):
    name = "phones"
    allowed_domains = ["productindetail.com"]
    start_urls = ["https://www.productindetail.com"]
    url = "https://www.productindetail.com"
    page_number = 2


    #This function is used to get from main page of the website 
    # to page with all mobile phones
    def parse(self, response):
        phones_page = response.css("div.collapse.navbar-collapse").css("a.dropdown-item").attrib["href"]
        link = self.url+phones_page
        yield response.follow(link, callback=self.adsPage)


    #This function extracts hrefs from "/phones" page to a list ,
    # then the first loop removes the ones that will not take us to phone details.
    # second loop merges start url with extracted href. By doing this we get urls of every phone 
    # on page one of "phones" category. Finally, spider enters phone's link and call scraper function "def scrapeAds(self, response)"
    def adsPage(self, response):
        ad_url_list = response.css("div.row.mt-5").css("a.text-decoration-none::attr(href)").getall()
        for item in ad_url_list:
            if 'pm' not in item:
                ad_url_list.remove(item)

        for item in ad_url_list:
            link = self.url+item
            yield response.follow(link, callback=self.scrapeAds)


    #This function extracts all desired information about devices and adds them to items objects "containers" 
    # 
    def scrapeAds(self, response):
        #initialize class object
        items = AdScraperItem()

        #extract data
        productName = response.css('li.breadcrumb-item.active small::text').get()
        brand = response.css('.link-dark.text-decoration-none small::text')[1].get()
        description = response.css('div.col-lg-12 p::text').get()
        imageURL = response.css('.img-fluid.mb-3::attr(src)').get()
        operatingSystem = response.css('div.div small::text')[7].get()
        displayTechnology = response.xpath('//*[@id="display"]/div[1]/table/tbody/tr[2]/td[1]/small/text()').get()
        
        #Assign values to object
        items['productName'] = productName
        items['brand'] = brand
        items['description'] = description
        items['operatingSystem'] = operatingSystem
        items['displayTechnology'] = displayTechnology
        items['imageURL'] = imageURL
        
        yield items
        
        #Go to next page of ads and callback to function "def adsPage(self, response)"
        next_page = f'https://www.productindetail.com/phones/page-{self.page_number}'
        if next_page is not None:
                # Go to next page
                self.page_number+=1
                yield response.follow(next_page, callback=self.adsPage)

