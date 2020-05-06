from bs4 import BeautifulSoup
html = """
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Quotes to Scrape</title>
<link href="/static/bootstrap.min.css" rel="stylesheet"/>
<link href="/static/main.css" rel="stylesheet"/>
</head>
<body>
<div class="container">
<div class="row header-box">
<div class="col-md-8">
<h1>
<a href="/" style="text-decoration: none">Quotes to Scrape</a>
</h1>
</div>
<div class="col-md-4">
<p>
<a href="/login">Login</a>
</p>
</div>
</div>
<div class="author-details">
<h3 class="author-title"></h3></div></div></body></html>
<p><strong>Born:</strong> <span class="author-born-date"></span> <span class="author-born-location"></span></p>
<p><strong>Description:</strong></p>
<div class="author-description">
</div>


<footer class="footer">
<div class="container">
<p class="text-muted">
                Quotes by: <a href="https://www.goodreads.com/quotes">GoodReads.com</a>
</p>
<p class="copyright">
                Made with <span class="sh-red">❤</span> by <a href="https://scrapinghub.com">Scrapinghub</a>
</p>
</div>
</footer>
"""
soup = BeautifulSoup(html, 'html.parser')
# print(soup.body.div)
# print(soup.find_all(class_ = 'special'))
# print(soup.find_all(attrs = { 'data-example': 'yes' }))
# print(soup.select('#first')[0])
print(soup.select('.author-born-date')[0])
# print(soup.select('[data-example]'))
# for item in soup.select('.special'):
    # print(item.get_text())
    # print(item.name)
    # print(item.attrs)
# print(type(soup))