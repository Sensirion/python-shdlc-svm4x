# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_svm41.response_types import AirQualityVoc, \
    AirQualityNox, Humidity, Temperature
from sensirion_shdlc_svm41.device_errors import \
    Svm41CommandNotAllowedInCurrentState
import pytest
import time


@pytest.mark.needs_device
def test(device):
    """
    Test if read_measured_values() returns the expected values.
    """
    device.start_measurement()
    time.sleep(1.)

    # check the read values
    humidity, temperature, air_quality_voc, air_quality_nox =\
        device.read_measured_values()
    assert type(humidity) is Humidity
    assert type(humidity.ticks) is int
    assert type(humidity.percent_rh) is float
    assert type(temperature) is Temperature
    assert type(temperature.ticks) is int
    assert type(temperature.degrees_celsius) is float
    assert type(temperature.degrees_fahrenheit) is float
    assert type(air_quality_voc) is AirQualityVoc
    assert type(air_quality_voc.voc_index) is float
    assert type(air_quality_nox) is AirQualityNox
    assert type(air_quality_nox.nox_index) is float
    # use default formatting for printing output:
    print("{}, {}, {}, {}".format(humidity,
                                  temperature,
                                  air_quality_voc,
                                  air_quality_nox))

    # stop the measurement and check for proper exception if called again
    device.stop_measurement()
    with pytest.raises(Svm41CommandNotAllowedInCurrentState):
        device.read_measured_values()


@pytest.mark.needs_device
def test_initial_state(device):
    """
    Test if read_measured_values() returns the expected
    exception if called without starting the measurement first.
    """
    with pytest.raises(Svm41CommandNotAllowedInCurrentState):
        device.read_measured_values()
