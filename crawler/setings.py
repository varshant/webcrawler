BOT_NAME = 'crawler'
SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

# Enable concurrency for efficiency
CONCURRENT_REQUESTS = 16  
DOWNLOAD_DELAY = 1  # Adjust based on website restrictions
ROBOTSTXT_OBEY = True
DEPTH_LIMIT = 2 

# Middleware and pipelines (if needed)
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

# Output format settings
FEEDS = {
    'data/output.json': {"format": "json", "encoding": "utf-8"},
}
