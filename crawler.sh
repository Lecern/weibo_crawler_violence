#!/usr/bin/env bash
source /etc/profile

cd /home/gao/project/weibo_crawler_violence/WeiboSearch/

/home/gao/.pyenv/shims/python /home/gao/project/weibo_crawler_violence/WeiboSearch/login.py >> /home/gao/project/weibo_crawler_violence/WeiboSearch/log/cookie.log
sleep 3
/home/gao/.pyenv/shims/python /home/gao/project/weibo_crawler_violence/WeiboSearch/run.py --start='2019-06-01' --end='2019-06-30' --ori >> /home/gao/project/weibo_crawler_violence/WeiboSearch/log/bash.log
sleep 3
/home/gao/.pyenv/shims/python /home/gao/project/weibo_crawler_violence/WeiboSearch/run.py --start='2020-01-01' --end='2020-06-30' --ori >> /home/gao/project/weibo_crawler_violence/WeiboSearch/log/bash.log
