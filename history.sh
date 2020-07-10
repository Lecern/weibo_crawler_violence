#!/usr/bin/env bash
source /etc/profile
if [[ $# -lt 3 ]]
then
    echo "Missing variable."
    exit 1
fi

cd /home/gao/project/weibo_crawler_violence/WeiboSearch/

/home/gao/.pyenv/shims/python /home/gao/project/weibo_crawler_violence/WeiboSearch/login.py >> /home/gao/project/weibo_crawler_violence/WeiboSearch/log/cookie.log
sleep 3
/home/gao/.pyenv/shims/python /home/gao/project/weibo_crawler_violence/WeiboSearch/run.py --start=${1} --end=${2} >> /home/gao/project/weibo_crawler_violence/WeiboSearch/log/bash.log
sleep 3
/home/gao/.pyenv/shims/python /home/gao/project/weibo_crawler_violence/WeiboSearch/run.py --keyword="#面对家暴不再沉默#" --start=${1} --end=${2} >> /home/gao/project/weibo_crawler_violence/WeiboSearch/log/bash.log
