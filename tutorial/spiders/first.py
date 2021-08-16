import scrapy 
from ..items import TutorialItem

class FirstWebsite(scrapy.Spider):
    name="firstwebsite"
    page_number= 1
    start_urls= ["https://traveltriangle.com/tour-packages/nepal/page/1"]


    def parse(self, response):

        item=TutorialItem()
        all =response.xpath('//div[@class="clearfix row p8 bb radius2"]')
        for row in all:
                   
            title =row.xpath('div[2]/div/h3/a/span/text()').extract_first()
            duration = row.xpath('div[2]/div[2]/span/span').extract_first()
            price =row.xpath('div[2]/div[3]/div/h4/text()').extract_first()
            discount =row.xpath('div[2]/div[3]/div/span/span[2]/span/text()').extract_first()
            types =row.xpath('div[2]/div[4]/div/div/div/div/label/text()').extract_first()
            citi =row.xpath('div[2]/div[4]/div/div[2]/ul').extract_first()
            item['title']=title
            item['duration']= duration
            item['price']= price
            item['types']=types
            item['citi']=citi
            item['discount']=discount
            yield item
        next_page= 'https://traveltriangle.com/tour-packages/nepal/page/'+str(FirstWebsite.page_number)        
        if FirstWebsite.page_number<=3 :
            FirstWebsite.page_number=FirstWebsite.page_number+1
            print(FirstWebsite.page_number)
            yield response.follow(next_page, callback=self.parse)
            