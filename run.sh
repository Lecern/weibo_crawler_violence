#!/usr/bin/env bash
source /etc/profile
cd /home/gao/project/weibo_crawler_violence/WeiboSearch/
/home/gao/.pyenv/shims/python /home/gao/project/weibo_crawler_violence/WeiboSearch/login.py >> /home/gao/project/weibo_crawler_violence/WeiboSearch/log/cookie.log
sleep 3
/home/gao/.pyenv/shims/python /home/gao/project/weibo_crawler_violence/WeiboSearch/run.py --ori >> /home/gao/project/weibo_crawler_violence/WeiboSearch/log/bash.log
sleep 3
/home/gao/.pyenv/shims/python /home/gao/project/weibo_crawler_violence/WeiboSearch/run.py --keyword="#面对家暴不再沉默#" --ori >> /home/gao/project/weibo_crawler_violence/WeiboSearch/log/bash.log
