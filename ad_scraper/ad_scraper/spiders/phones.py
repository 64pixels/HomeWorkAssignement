import scrapy
from ..items import AdScraperItem

class PhonesSpider(scrapy.Spider):
    name = "phones"
    allowed_domains = ["productindetail.com"]
    start_urls = ["https://www.productindetail.com"]
    url = "https://www.productindetail.com"
    page_number = 2

    def parse(self, response):
        phones_page = response.css("div.collapse.navbar-collapse").css("a.dropdown-item").attrib["href"]
        link = self.url+phones_page
        yield response.follow(link, callback=self.adsPage)


    def adsPage(self, response):
        ad_url_list = response.css("div.row.mt-5").css("a.text-decoration-none::attr(href)").getall()
        for item in ad_url_list:
            if 'pm' not in item:
                ad_url_list.remove(item)

        for item in ad_url_list:
            link = self.url+item
            yield response.follow(link, callback=self.scrapeAds)


    def scrapeAds(self, response):
        items = AdScraperItem()

        productName = response.css('li.breadcrumb-item.active small::text').get()
        brand = response.css('.link-dark.text-decoration-none small::text')[1].get()
        description = response.css('div.col-lg-12 p::text').get()
        imageURL = response.css('.img-fluid.mb-3::attr(src)').get()
        operatingSystem = response.css('div.div small::text')[7].get()
        displayTechnology = response.xpath('//*[@id="display"]/div[1]/table/tbody/tr[2]/td[1]/small/text()').get()
        
        items['productName'] = productName
        items['brand'] = brand
        items['description'] = description
        items['operatingSystem'] = operatingSystem
        items['displayTechnology'] = displayTechnology
        items['imageURL'] = imageURL
        
        yield items
            
        next_page = f'https://www.productindetail.com/phones/page-{self.page_number}'
        if next_page is not None:
                # Go to next page
                self.page_number+=1
                yield response.follow(next_page, callback=self.adsPage)




        # next_page = self.url + response.css("a.page-link")[-1].attrib["href"]

            # 'operatingSystem' : self.checkOperatingSystem(self, response),
            # 'displayTechnology' : self.checkDisplayTechnology(self, response),
            #sitas eilutes kai isitikinsim kad veikia be referensu
        


    # def checkOperatingSystem(self, response):
        
    #     table = response.xpath('//*[@class="table table-striped table-hover"]//tbody')[6]
    #     rows = table.xpath('//tr')
    #     operatingSystem = "None"

    #     for row in rows:
    #         if row.xpath('th//text()').get() == "OPERATING SYSTEM":
    #             operatingSystem = row.xpath('td//text()')[1].get()
    #             break

    #     return operatingSystem   


    # def checkDisplayTechnology(self, response):

    #     table = response.xpath('//*[@class="table table-striped table-hover"]//tbody')[1]
    #     rows = table.xpath('//tr')
    #     displayTechnology = "None"

    #     for row in rows:
    #         if row.xpath('th//text()').get() == "DISPLAY TECHNOLOGY":
    #             displayTechnology = row.xpath('td//text()')[1].get()
    #             break

    #     return displayTechnology
    

                        

#'operatingSystem' : response.css('div.div small::text')[7].get(),
#'displayTechnology' : response.xpath('//*[@id="display"]/div[1]/table/tbody/tr[2]/td[1]/small/text()').get(),
            


    # def scrapeAds(self, response):

    #     yield {
    #         'productName' : response.css('li.breadcrumb-item.active small::text').get(),
    #         'brand' : response.css('.link-dark.text-decoration-none small::text')[1].get(),
    #         'description' : response.css('div.col-lg-12 p::text').get(),
    #         'operatingSystem' : self.checkOperatingSystem(self, response),
    #         'displayTechnology' : self.checkDisplayTechnology(self, response),
    #         'imageURL': response.css('.img-fluid.mb-3::attr(src)').get()   
    #     }