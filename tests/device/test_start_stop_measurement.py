# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_svm41.device_errors import \
    Svm41CommandNotAllowedInCurrentState
import pytest
import time


@pytest.mark.needs_device
def test(device):
    """
    Test if start_measurement() and stop_measurement() work as expected.
    """

    # start continuous measurement and make sure it worked
    device.start_measurement()
    with pytest.raises(Svm41CommandNotAllowedInCurrentState):
        device.start_measurement()

    # stop and restart measurement
    device.stop_measurement()
    time.sleep(1.)
    device.start_measurement()
