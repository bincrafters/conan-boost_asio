#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostAsioConan(base.BoostBaseConan):
    name = "boost_asio"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_asio"
    lib_short_names = ["asio"]
    header_only_libs = ["asio"]
    b2_requires = [
        "boost_array",
        "boost_assert",
        "boost_bind",
        "boost_chrono",
        "boost_config",
        "boost_core",
        "boost_coroutine",
        "boost_date_time",
        "boost_function",
        "boost_regex",
        "boost_smart_ptr",
        "boost_system",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_utility"
    ]
