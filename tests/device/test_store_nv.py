# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
@pytest.mark.parametrize("t_offset, voc_parameters, nox_parameters", [
    (-30.,                              # max allowed values
     (250, 1000, 1000, 3000, 5000, 1000),
     (250, 1000, 1000, 3000, 5000, 1000)),
    (30.,                               # min allowed values
     (1, 1, 1, 0, 10, 1),
     (1, 1, 1, 0, 10, 1)),
    (0.,                                # default values
     (100, 12, 12, 720, 50, 230),
     (1, 12, 12, 720, 50, 230)),
])
def test_nv(device, t_offset, voc_parameters, nox_parameters):
    """
    Test if store_nv_data() works as expected.
    """
    device.set_compensation_temperature_offset(t_offset)
    device.set_voc_tuning_parameters(*voc_parameters)
    device.set_nox_tuning_parameters(*nox_parameters)

    device.store_nv_data()

    assert device.get_compensation_temperature_offset() == t_offset
    assert device.get_voc_tuning_parameters() == voc_parameters
    assert device.get_nox_tuning_parameters() == nox_parameters

    # reset device and check that the value was stored in the nv-memory
    device.device_reset()

    assert device.get_compensation_temperature_offset() == t_offset
    assert device.get_voc_tuning_parameters() == voc_parameters
    assert device.get_nox_tuning_parameters() == nox_parameters
