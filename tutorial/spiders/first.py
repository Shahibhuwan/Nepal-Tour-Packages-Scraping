import scrapy 
from ..items import TutorialItem
import w3lib.html

class FirstWebsite(scrapy.Spider):
    name="firstwebsite"
    
    page_number= 1
    start_urls= ["https://traveltriangle.com/tour-packages/nepal/page/1"]


    # def parse(self, response):

    #     item=TutorialItem()
        # all =response.xpath('//div[@class="clearfix row p8 bb radius2"]')
        # for row in all:
                   
        #     title =row.xpath('div[2]/div/h3/a/span/text()').extract_first()
        #     duration = row.xpath('div[2]/div[2]/span/span').extract_first()
        #     price =row.xpath('div[2]/div[3]/div/h4/text()').extract_first()
        #     discount =row.xpath('div[2]/div[3]/div/span/span[2]/span/text()').extract_first()
        #     types =row.xpath('div[2]/div[4]/div/div/div/div/label/text()').extract_first()
        #     citi =row.xpath('div[2]/div[4]/div/div[2]/ul').extract_first()
        #     item['title']=title
        #     item['duration']= duration
        #     item['price']= price
        #     item['types']=types
        #     item['citi']=citi
        #     item['discount']=discount
        #     yield item
        # next_page= 'https://traveltriangle.com/tour-packages/nepal/page/'+str(FirstWebsite.page_number)        
        # if FirstWebsite.page_number<=3 :
        #     FirstWebsite.page_number=FirstWebsite.page_number+1
        #     print(FirstWebsite.page_number)
        #     yield response.follow(next_page, callback=self.parse)
    def parse(self, response):
        products = response.xpath('//div[@class="clearfix row p8 bb radius2"]')
        item=TutorialItem()
        for product in products:
            url_inside =product.xpath('div[2]/div/h3/a/@href').get()
            
            item['url'] =response.urljoin(url_inside)#product.xpath('div[2]/div/h3/a/@href').get() 
            
            yield response.follow(url = item['url'], meta = {'item': item}, callback=self.parse_additional_info) 
        next_page= 'https://traveltriangle.com/tour-packages/nepal/page/'+str(FirstWebsite.page_number)        
        if FirstWebsite.page_number<=3 :
            FirstWebsite.page_number=FirstWebsite.page_number+1
            print(FirstWebsite.page_number)
            yield response.follow(next_page, callback=self.parse)
#scrapy.Request() instead of response.follow
    def parse_additional_info(self, response):
        # page = response.url.split('/')[-1]
        # filename = f'tours-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
              

        filename = response.url.split("/")[-1][:13] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        item = response.meta['item']
        item['name'] = response.xpath('//div[@class="clearfix row"]/div[3]/div/div/h1/span/text()').extract_first().strip()
        #span[@class="iblock mr8"]
       # item['description1'] = response.xpath('//div[@class="clearfix p15 border mt8 pt24"]/div/div[1]/label/h3/text()[2]').extract_first()
        item['day1']=w3lib.html.remove_tags(response.xpath('//div[@class="clearfix p15 border mt8 pt24"]/div/div[1]/label/h3').extract_first())#//div[@class="clearfix p15 border mt8 pt24"]/div/div[1]/div/div/div[2]
        item['day2']=w3lib.html.remove_tags(response.xpath('//div[@class="clearfix p15 border mt8 pt24"]/div/div[2]/label/h3').extract_first()) #//div[@class="clearfix p15 border mt8 pt24"]/div/div[2]/div/div/div[2]
        item['day3'] = w3lib.html.remove_tags(response.xpath('//div[@class="clearfix p15 border mt8 pt24"]/div/div[3]/label/h3').extract_first())#//div[@class="clearfix p15 border mt8 pt24"]/div/div[3]/div/div/div[2]

        item['day4']=w3lib.html.remove_tags(response.xpath('//div[@class="clearfix p15 border mt8 pt24"]/div/div[4]/label/h3').extract_first())#//div[@class="clearfix p15 border mt8 pt24"]/div/div[4]/div/div/div[2]
        item['hotels']= str(response.xpath('//div[@class="hotel-card bb pt15 pb15"] /div/div[2]/div/div/h3/text()').extract_first()) +',' + str(response.xpath('//div[@class="hotel-card bb pt15 pb15"][2]/div/div[2]/div/div/h3/text()').extract_first())
        item['price'] =w3lib.html.remove_tags(response.xpath('//div[@class="pdp-right-block fleft iblock row pl15 ml15"]/div[2]/div/div/div/div/div/h4/span/text()').get())
        item['types'] = w3lib.html.remove_tags(response.xpath('//div[@class="clearfix p15 border"]/div/div[3]/div/span/span[2]/text()').get())
        item['citi'] = w3lib.html.remove_tags(response.xpath('//div[@class="pdp-right-block fleft iblock row pl15 ml15"]/div/div/div/div[2]/div/ul').extract_first())
        # item['discount']=response.xpath('')
        yield item


        # euro = Selector(response).xpath('//strong[@class="special-price"]/span[@class="euros"]/text()').extract()[0]
        # cent = Selector(response).xpath('//strong[@class="special-price"]/span[@class="cents"]/text()').extract()[0]