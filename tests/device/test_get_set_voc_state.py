# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest
import time


@pytest.mark.needs_device
def test_voc_state(device):
    """
    Test if get_voc_state() and set_voc_state() work as expected.
    """
    device.start_measurement()
    state = device.get_voc_state()
    assert type(state) is bytes
    assert len(state) == 8

    device.stop_measurement()
    time.sleep(1.)
    device.set_voc_state(state)
