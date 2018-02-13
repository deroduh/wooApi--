import json
import re

from woocommerce import API

from datetime import datetime, timezone



def wooApi(interval):
    wcapi = API(
        url="http://test1.ru/",
        consumer_key="ck_fe23641c34472977e0e22bfd52a7807126065bd4",
        consumer_secret="cs_9534d46244517804a1b261c66ea98988f455a723",
        wp_api=True,
        version="wc/v2",
        query_string_auth=True
    )

    p_order = re.compile('\'date_created_gmt\': \'\w+-\w+-\w+:\w+:\w+\'')
    p_order_time_gmt = re.compile('\w+-\w+-\w+:\w+:\w+')


    orders = wcapi.get("orders").json()

    orders_time = p_order_time_gmt.findall(str(p_order.findall(str(orders))))

    new_order_count = 0
    for time in orders_time:
        datetime_object = datetime.strptime(str(time), '%Y-%m-%dT%H:%M:%S')
        if (datetime.utcnow() - datetime_object).seconds <3600:
            new_order_count +=1

    return new_order_count


















