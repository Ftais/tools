#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import datetime
import time


def get_unix_timestamp():
    return int(time.time())

def get_milli_unix_timestamp():
    return int(round(time.time() * 1000))


def date_to_timestamp(strftime=None, date=None):
    strftime = '%Y-%m-%d %H:%M:%S' if strftime is None else strftime
    if date == None:
        return int(time.time())
    else:
        date = datetime.utcnow().strftime(strftime) if date is None else date
    timestamp = time.strptime(date, strftime)
    timestamp = int(time.mktime(timestamp))
    return timestamp


def timestamp_to_date(strftime=None, timestamp=None):
    strftime = '%Y-%m-%d %H:%M:%S' if strftime is None else strftime
    timestamp = int(time.time()) if timestamp is None else timestamp
    date = time.localtime(timestamp)
    date = time.strftime(strftime, date)
    return date


if __name__ == '__main__':
    print(get_unix_timestamp())
    print(get_milli_unix_timestamp())
    print(date_to_timestamp(date="2020-03-14 0:0:0"))
    print(date_to_timestamp(strftime="%Y-%m-%dT%H:%M:%S"))
    print(timestamp_to_date(timestamp=1584154137))
    print(timestamp_to_date(strftime='%Y-%m-%dT%H:%M:%S'))
