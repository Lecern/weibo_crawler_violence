#!/usr/bin/env bash
current_date=`date +%Y-%m-%d`
python WeiboSearch/daily_word_cloud.py --date=${current_date}