# !/usr/bin/python
# -*- coding:utf-8 -*-
# @Time : 2022/6/20 21:18
# @Author : wangjie
# @File : test_alarms.py
# @project : SensoroApi

import pytest

from common.http_method import BaseApi
from pageApi.alarms import Alarms
from utils.time_utils import TimeUtil


class TestAlarms:
    """测试预警"""

    @pytest.mark.run(order=1)
    def test_get_alarms_list(self, get_token_v2, set_global_data):
        """获取预警列表"""
        headers = {'Authorization': f'Bearer {get_token_v2}'}
        params = {
            'page': 1,
            'size': 20,
            'startTime': TimeUtil.get_current_time_unix(),
            'endTime': TimeUtil.get_seven_days_ago_time_unix()
        }
        r = Alarms().get_alarms_list(headers=headers, params=params)
        alarms_id = BaseApi.get_json(r)['data']['list'][0]['id']
        set_global_data('alarms_id', alarms_id)
        message = BaseApi.get_json(r)['message']
        assert message == 'SUCCESS'

    def test_get_alarms_details(self, get_token_v2, get_global_data):
        headers = {'Authorization': f'Bearer {get_token_v2}'}
        alarms_id = get_global_data('alarms_id')
        print('取出来的：', alarms_id)
        r = Alarms().get_alarms_details(alarms_id, headers=headers)
        message = BaseApi.get_json(r)['message']
        assert message == 'SUCCESS'
