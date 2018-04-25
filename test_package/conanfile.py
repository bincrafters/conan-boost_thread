#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools, RunEnvironment
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def requirements(self):
        boost_deps = ['assert', 'atomic', 'bind', 'chrono', 'concept_check', 'config', 'container', 'container_hash', 'core', 'exception', 'function', 'intrusive', 'io', 'iterator', 'move', 'mpl', 'optional', 'predef', 'preprocessor', 'smart_ptr', 'static_assert', 'system', 'thread', 'throw_exception', 'tuple', 'type_traits', 'utility', 'winapi']
        for lib in boost_deps:
            self.requires("boost_" + lib + "/1.67.0@" + self.user + "/" + self.channel)
        if False:
            if not tools.os_info.is_windows:
                self.requires("openmpi/3.0.0@bincrafters/stable")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        with tools.environment_append(RunEnvironment(self).vars):
            if self.settings.os == "Windows":
                self.run(os.path.join("bin", "test_package"))
            else:
                self.run("DYLD_LIBRARY_PATH=%s %s" % (os.environ['DYLD_LIBRARY_PATH'], os.path.join("bin", "test_package")))
