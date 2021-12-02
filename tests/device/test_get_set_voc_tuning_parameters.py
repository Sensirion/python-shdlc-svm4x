# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test_voc_tuning_parameters(device):
    """
    Test if set_voc_tuning_parameters() and get_voc_tuning_parameters() work
    as expected.
    """
    device.set_voc_tuning_parameters(110, 16, 42, 90, 40, 200)
    voc_index_offset, learning_time_offset_hours, learning_time_gain_hours, \
        gating_max_duration_minutes, \
        std_initial, gain_factor = device.get_voc_tuning_parameters()
    assert voc_index_offset == 110
    assert learning_time_offset_hours == 16
    assert learning_time_gain_hours == 42
    assert gating_max_duration_minutes == 90
    assert std_initial == 40
    assert gain_factor == 200
