from conans import ConanFile


class BoostThreadConan(ConanFile):
    name = "Boost.Thread"
    version = "1.65.1"
    url = "https://github.com/bincrafters/conan-boost-thread"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    requires =  "Boost.Level11Group/1.65.1@bincrafters/testing"
        
    #This library is part of one or more cyclic dependency groups within Boost.
    
    #All members of cyclic dependency groups must be built under single package per group for Conan.
    
    #The combination is performed in the package(s) listed in the requires field.
    
    #This package enables simple consumption of this library while abstracting away the cyclic dependency issues. 
