# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_svm41.response_types import Humidity, Temperature
from sensirion_shdlc_svm41.device_errors import \
    Svm41CommandNotAllowedInCurrentState
import pytest
import time


@pytest.mark.needs_device
def test(device):
    """
    Test if read_measured_values_raw() returns the expected values.
    """
    device.start_measurement()
    time.sleep(1.)

    # check the read values
    raw_humidity, raw_temperature, raw_voc_ticks, raw_nox_ticks = \
        device.read_measured_values_raw()
    # raw types
    assert type(raw_humidity) is Humidity
    assert type(raw_humidity.ticks) is int
    assert type(raw_humidity.percent_rh) is float
    assert type(raw_temperature) is Temperature
    assert type(raw_temperature.ticks) is int
    assert type(raw_temperature.degrees_celsius) is float
    assert type(raw_temperature.degrees_fahrenheit) is float
    assert type(raw_voc_ticks) is int
    assert type(raw_nox_ticks) is int

    # use default formatting for printing output:
    print("temperature={}, humidity={}, [raw] voc ticks={}, [raw] nox ticks={}"
          .format(raw_humidity, raw_temperature, raw_voc_ticks, raw_nox_ticks))

    # stop the measurement and check for proper exception if called again
    device.stop_measurement()
    with pytest.raises(Svm41CommandNotAllowedInCurrentState):
        device.read_measured_values_raw()


@pytest.mark.needs_device
def test_initial_state(device):
    """
    Test if read_measured_values_raw() returns the expected
    exception if called without starting the measurement first.
    """
    with pytest.raises(Svm41CommandNotAllowedInCurrentState):
        device.read_measured_values_raw()
