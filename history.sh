#!/usr/bin/env bash
source /etc/profile
if [[ $# -lt 3 ]]
then
    echo "Missing variable."
    exit 1
fi

cd /home/gao/project/WeiboCrawler/WeiboSearch/

/home/gao/.pyenv/shims/python /home/gao/project/WeiboCrawler/WeiboSearch/login.py >> /home/gao/project/WeiboCrawler/WeiboSearch/log/cookie.log
sleep 3
/home/gao/.pyenv/shims/python /home/gao/project/WeiboCrawler/WeiboSearch/run.py --start=${1} --end=${2} >> /home/gao/project/WeiboCrawler/WeiboSearch/log/bash.log
sleep 3
/home/gao/.pyenv/shims/python /home/gao/project/WeiboCrawler/WeiboSearch/run.py --keyword="冠状病毒" --start=${1} --end=${2} >> /home/gao/project/WeiboCrawler/WeiboSearch/log/bash.log
sleep 3
/home/gao/.pyenv/shims/python /home/gao/project/WeiboCrawler/WeiboSearch/run.py --keyword="新冠肺炎" --start=${1} --end=${2}>> /home/gao/project/WeiboCrawler/WeiboSearch/log/bash.log
sleep 3
/home/gao/.pyenv/shims/python /home/gao/project/WeiboCrawler/WeiboSearch/daily_word_cloud.py --date=${3} >> /home/gao/project/WeiboCrawler/WeiboSearch/log/upload_image.log