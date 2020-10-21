from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")


def amazon(request):
    import urllib.request
    import random
    import requests
    from bs4 import BeautifulSoup as bs
    import yagmail

    #This is a bowser user-agent list user-agent's are listed here as string
    browser_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1', 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', 'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996', 'Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10', 'Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/28.2725; U; ru) Presto/2.8.119 Version/11.10', 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) OPiOS/10.2.0.93022 Mobile/11D257 Safari/9537.53', 'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4', 'Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30', 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP', 'Mozilla/5.0 (Linux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP', 'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; Microsoft; Lumia 950)', 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977', 'Mozilla/5.0 (BB10; Kbd) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.3.3.2205 Mobile Safari/537.35+', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:59.0) Gecko/20100101 Firefox/59.0']
    #This is a bowser referer stored in list
    ref = ['https://www.amazon.com.br/', 'https://en.wikipedia.org/wiki/Lady_Gaga', 'http://www.tutorsinindia.com/', 'https://bel-india.com/', 'https://brandservices.amazon.com/', 'https://moz.com/top500', 'https://amazon-presse.de/', 'https://insider.razer.com/index.php?threads/which-mouse-should-i-get.49833/', 'https://www.iamin.in/', 'https://www.audible.in/', 'https://play.google.com/store/apps/details?id=in.amazon.mShop.android.shopping&hl=en_US', 'https://www.aboutamazon.in/']
    # url = input("Url: ")  #This input field will take url what users want to scrape
    a = random.choice(browser_agent) #random choice function to pick a random users agent every time the code runs
    b = random.choice(ref)
    headers = {
        'user-agent': a,
        'referer': b
    }
    url = request.POST["amazon_url"] #it's amazon url scrapper
    url = url
    if "amazon.in" in url:
        a = requests.get(url, headers=headers, params={
        "api_key": "NPUVAPJM6F1X64JC1Q6WWBBPHLRM6PUK21SBHHGO5KY2M85M8YC3PAEJNKJ9N84P977IS3J98CKUE2YE", #This is proxy api from scrapingbee.com
        "url": url,
        "premium_proxy": "true", 
        "country_code":"in",
        },).content
        c = bs(a, "html.parser")
        product_image = c.find("img", class_="a-hidden", src=True)
        product_image = product_image["src"]
        amazon_product_title = c.find('h1')   #This will print the amazon price
        amazon_product_title = amazon_product_title.text
        amazon_product_title = amazon_product_title.strip('\n')
        if len(amazon_product_title) >= 60:
            amazon_product_title = amazon_product_title[0:61]
        else:
            amazon_product_title = amazon_product_title
        amazon_product_price = c.find('span', attrs={'class': 'buyingPrice'})
        amazon_product_price = amazon_product_price.text #This is amazon price
        r = random.randint(1, 896557987668767865) #This will randomly generate a number which will be used in image name
        urllib.request.urlretrieve(product_image, f"static\images\{r}.png")
        # set to the path to your file
        filename = f"static\images\{r}.png"
        random_word = ["Latest offer from Amazon", "New Loot offer from Amazon", "Bumper Offer from Amazon", "Loot Now Offer from Amazon"]
        random_word = random.choice(random_word)
        offer = url
        content = f"""
        <p style="text-align:center;"><img src={product_image} height="175"/"></p>
        <h1 style="text-align: center;">Amazon {amazon_product_title} Rs.{amazon_product_price}</h1>
        <p>Looking for Amazon deals and offers checkout <today></today> {random_word} get {amazon_product_title} at rs.{amazon_product_price} only.
        <p><font color="green">Follow below steps to avail this bumper offer from Amazon.</font></p>
        <h2 style="text-align: center;">
        How to Buy {amazon_product_title}</h2>
        <ol><li>First of all visit Amazon <a href="{offer}" rel="nofollow" target="_blank">offer page</a></li> 
        <li>Read <a href="{offer}" rel="nofollow" target="_blank">product</a> information if you are interested in reading</li>
        <li>Add the product to cart</li>
        <li>Now go to the checkout page or click buy now</li>
        <li>You will be redirected to the Amazon login page, Login using your Amazon credential</li>
        <li>If you don’t have an account then create one it’s free</li>
        <li>After that enter your product delivery address</li>
        <li>Now Amazon will ask you to pay the money</li>
        <li>Pay money or choose Cod(cash on delivery</li>
        <li>Confirm the order, You will receive the product in your doorstep within a few days.</li>
        <li>We will love to hear from you regarding this deal so comment and share. Please share our site with your Friends, share in Your Whatsapp, Telegram, Facebook Group keep visitng <a href="https://indisale.in/">Indisale</a>.</li></ol>
        <text align="center"><h3>Copy Below Text and Paste In Seo Description</h3>
        <b>Get {amazon_product_title} limited time offer Rs.{amazon_product_price}only.</b></text>
        [category "Amazon Deals Offers"]
        """
        #initializing the server connection
        yag = yagmail.SMTP(user='hampu786@gmail.com', password='bokachoda420@@')
        #sending the email
        yag.send(to='zire368buke@post.wordpress.com', subject="Amazon"+' '+amazon_product_title, contents=content, attachments=filename)
        success = ("Post Published successfully")
        return HttpResponse(success)
    elif "flipkart" in url:
        import requests as req
        import random
        from bs4 import BeautifulSoup as bs
        import yagmail
        import re
        import urllib.request
        url = url
        product_type = "PC monitor"
        offer = url
        url = req.get(url)
        # url = url.content
        url = url.content
        soup = bs(url, "html.parser")
        a = soup.find_all("span", class_="_35KyD6")#This one is for product Title
        a = a[0]
        a = a.text
        b = soup.find("div", attrs = {'class': "_1vC4OE _3qQ9m1"}).text
        #This will print the product price
        b = b[1:]
        image = soup.find("div", attrs={"class": "_2_AcLJ", "style": re.compile('.jpeg')})
        image = image["style"]
        image = image[21:]
        image = image[:-1]
        r = random.randint(200, 896557987668767865) #This will randomly generate a number which will be used in image name
        urllib.request.urlretrieve(image, f"static\images\{r}.png")
        # set to the path to your file
        images = f"static\images\{r}.png"
        random_word = ["Today latest offer", "Bumper sale offer", "Today hot offer", "Exclusive offer"]
        random_word = random.choice(random_word)
        content = f'''<p>Looking for Flipkart deals and offers of {product_type} checkout {random_word} on {a} at rs.{b} only.
        <p><font color="green">Follow below steps to avail this bumper offer from Flipkart.</font></p>
        <h2 style="text-align:center">How to Buy {a}</h2>
        <ol><li>First of all visit Flipkart <a href="{offer}" target="_blank" rel="nofollow">offer page</a></li>  
        <li>Read <a href="{offer}" target="_blank" rel="nofollow">product</a> information if you are interested in reading</li>
        <li>Add the product to cart</li>
        <li>Now go to the checkout page or click buy now</li>
        <li>You will be redirected to the Flipkart login page, Login using your Flipkart credential</li>
        <li>If you don’t have an account then create one it’s free</li>
        <li>After that enter your product delivery address</li>
        <li>Now Flipkart will ask you to pay the money</li>
        <li>Pay money or choose Cod(cash on delivery</li>
        <li>Confirm the order, You will receive the product in your doorstep within a few days.</li>
        <li>We will love to hear from you regarding this deal so comment and share. Please share our site with your Friends, share in Your Whatsapp, Telegram, Facebook Group keep visitng <a href="https://indisale.in/">Indisale</a>.</li>
        </ol>
        [category "Flipkart Deals Offer"]'''
        yag = yagmail.SMTP(user='hampu786@gmail.com', password='bokachoda420@@')
        #sending the email
        yag.send(to='zire368buke@post.wordpress.com', subject='Flipkart'+ ' '+ a, contents=content, attachments=images)
        result = "Email sent successfully"
        return HttpResponse(result)
    elif "snapdeal" in url:
        import requests as req
        from bs4 import BeautifulSoup
        import yagmail
        import urllib.request
        a = url
        offer = a
        a = req.get(a).content
        b = BeautifulSoup(a, 'html.parser')
        product_title = b.find("p", class_="product-title").text
        product_price = b.find("span", class_="payBlkBig").text
        product_features = (b.find("div", attrs = {"class": "spec-body p-keyfeatures"})).text
        images = b.find('img', class_="hidden", src=True)
        images = images["src"]
        r = random.randint(200, 896557987668767865) #This will randomly generate a number which will be used in image name
        urllib.request.urlretrieve(images, f"static\images\{r}.png")
        # set to the path to your file
        images = f"static\images\{r}.png"
        content = f'''<p style="text-align:center;"><img src="{images}" height="175"/"></p>
        <h1 style="text-align: center;">Snapdeal {product_title} Rs.{product_price}</h1>
        <p>Looking for deals and offers checkout today snapdeal offer get {product_title} at rs.{product_price} only.
        <p>This product have {product_features} so it's a great deal checkout soon because products stocks are limited.</P>
        <p><font color="green">Follow below steps to avail this bumper offer from Snapdeal.</font></p>
        <h2 style="text-align: center;">
        How to Buy {product_title}</h2>
        <p>
        <ol><li>First of all visit Snapdeal <a href="{offer}">offer page</a></li> 
        <li>Read <a href="{offer}">product</a> information if you are interested in reading</li>
        <li>Add the product to cart</li>
        <li>Now go to the checkout page or click buy now</li>
        <li>You will be redirected to the Snapdeal sites login page, Login using your Snapdeal's account credential</li>
        <li>If you don’t have an account then create one it’s free</li>
        <li>After that enter your product delivery address</li>
        <li>Now Snapdeal will ask you to pay the product's total money</li>
        <li>Pay money or choose Cod(cash on delivery</li>
        <li>Confirm the order, You will receive the product in your doorstep within a few days.</li>
        <li>We will love to hear from you regarding this deal so comment and share. Please share our site with your Friends, share in Your Whatsapp, Telegram, Facebook Group keep visitng <a href="https://indisale.in/">Indisale</a>.</li></ol></p>
        [category "Snapdeal Deals Offer"]'''
        yag = yagmail.SMTP(user='hampu786@gmail.com', password='bokachoda420@@')
        #sending the email
        yag.send(to='zire368buke@post.wordpress.com', subject='Snapdeal'+ ' '+ product_title, contents=content, attachments=images)
        result = "Email sent successfully"
        return HttpResponse(result)
    elif "paytmmall" in url:
        import requests
        from bs4 import BeautifulSoup as bs
        import urllib.request
        import random
        import yagmail
        url = url
        offer = url
        product_title = requests.get(url)#Passing the paytmaall url here
        product_title = product_title.content
        soup = bs(product_title, "html.parser")
        a = soup.find("h1", class_="NZJI").text #This is product title
        product_price = soup.find("span", class_="_1V3w").text #This is product price
        image = soup.find("img", attrs={"class": "fPC9", "src": True}) #This will scrape product main image
        image = image["src"]
        r = random.randint(200, 896557987668767865) #This will randomly generate a number which will be used in image name
        urllib.request.urlretrieve(image, f"static\images\{r}.png")
        # set to the path to your file
        images = f"static\images\{r}.png"
        random_word = ["today Paytmmall", "Today Exclusive", "huge discount", "mega sale"]
        random_word = random.choice(random_word)
        content = f'''<p>Looking for Paytmmall's deals and offers checkout {random_word} offers get {a} at rs.{product_price} only.
        <p><font color="blue">Follow below steps to avail this bumper offer from Paytmmall.</font></p>
        <h2 style="text-align: center;">
        How to Buy {a}</h2>
        <p>
        <ol><li>First of all visit Paytmmall <a href="{offer}" target="_blank" rel="nofollow">offer page</a></li> 
        <li>Read <a href="{offer}" target="_blank" rel="nofollow">product</a> information if you are interested in reading</li>
        <li>Add the product to cart</li>
        <li>Now go to the checkout page or click buy now</li>
        <li>You will be redirected to the Paytmmall login page, Login using your Paytmmall credential</li>
        <li>If you don’t have an account then create one it’s free</li>
        <li>After that enter your product delivery address</li>
        <li>Now Paytmmall will ask you to pay the money</li>
        <li>Pay money or choose Cod(cash on delivery</li>
        <li>Confirm the order, You will receive the product in your doorstep within a few days.</li>
        <li>We will love to hear from you regarding this deal so comment and share. Please share our site with your Friends, share in Your Whatsapp, Telegram, Facebook Group keep visitng <a href="https://indisale.in/">Indisale</a>.</li></ol></p>
        [category "Paytmall Deals Offers"]'''
        yag = yagmail.SMTP(user='hampu786@gmail.com', password='bokachoda420@@')
        #sending the email
        yag.send(to='zire368buke@post.wordpress.com', subject='Paytmmall'+ ' '+ a, contents=content, attachments=images)
        result = "Email sent successfully of Paytmall"
        return HttpResponse(result)