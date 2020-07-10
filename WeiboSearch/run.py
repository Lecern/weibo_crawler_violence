import argparse
from datetime import datetime, timedelta

from scrapy import cmdline

now_date = datetime.now().strftime("%Y-%m-%d")
one_day_ago = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
two_days_ago = (datetime.now() - timedelta(2)).strftime("%Y-%m-%d")
parser = argparse.ArgumentParser()
parser.add_argument("--start", type=str, default=two_days_ago)
parser.add_argument("--end", type=str, default=one_day_ago)
parser.add_argument("--ori", type=int, default=1)
parser.add_argument("--keyword", type=str)
args = parser.parse_args()

execute = 'scrapy crawl weibo_spider -s LOG_ENABLED=0'
if args:
    execute += ' -a start={} -a end={} -a ori={}'.format(args.start, args.end, args.ori)
if args.keyword:
    execute += ' -a keyword={}'.format(args.keyword)

cmdline.execute(execute.split())
