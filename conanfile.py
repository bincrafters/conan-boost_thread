#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostThreadConan(base.BoostBaseConan):
    name = "boost_thread"
    url = "https://github.com/bincrafters/conan-boost_thread"
    lib_short_names = ["thread"]
    cycle_group = "boost_cycle_group_c"
    options = {
        "shared": [True, False],
        "threadapi": ['default', 'win32', 'pthread']
    }
    default_options = "shared=False", "threadapi=default"
    b2_requires = ["boost_cycle_group_c"]

    def package_info_additional(self):
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("rt")

    def package_id_additional(self):
        self.info.header_only()
        self.info.settings.os = str(self.settings.os)
