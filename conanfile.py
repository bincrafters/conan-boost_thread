from conans import ConanFile, tools, os

class BoostThreadConan(ConanFile):
    name = "Boost.Thread"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/thread"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "thread"
    requires =  "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Atomic/1.64.0@bincrafters/testing", \
                      "Boost.Bind/1.64.0@bincrafters/testing", \
                      "Boost.Chrono/1.64.0@bincrafters/testing", \
                      "Boost.Concept_Check/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Container/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Date_Time/1.64.0@bincrafters/testing", \
                      "Boost.Exception/1.64.0@bincrafters/testing", \
                      "Boost.Function/1.64.0@bincrafters/testing", \
                      "Boost.Functional/1.64.0@bincrafters/testing", \
                      "Boost.Intrusive/1.64.0@bincrafters/testing", \
                      "Boost.Io/1.64.0@bincrafters/testing", \
                      "Boost.Move/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Optional/1.64.0@bincrafters/testing", \
                      "Boost.Predef/1.64.0@bincrafters/testing", \
                      "Boost.Preprocessor/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.System/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Tuple/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Utility/1.64.0@bincrafters/testing", \
                      "Boost.Winapi/1.64.0@bincrafters/testing"

                      #assert1 atomic4 bind3 chrono8 concept_check5 config0 container7 core2 date_time11 exception5 function5 functional5 intrusive6 io1 move3 mpl5 optional5 predef0 preprocessor0 smart_ptr4 static_assert1 system3 throw_exception2 tuple4 type_traits3 utility5 winapi1
                      
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)

    def package_id(self):
        self.info.header_only()