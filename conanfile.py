from conans import ConanFile, CMake, tools


class BehleyoctreeConan(ConanFile):
    name = "BehleyOctree"
    version = "0.1"
    license = "MIT"
    author = "Richard Vock <vock@cs.uni-bonn.de>"
    url = "https://github.com/richard-vock/conan-behley-octree"
    description = "Efficient Radius Neighbor Search in Three-dimensional Point Clouds"
    topics = ("pointclouds")
    settings = "os"

    def source(self):
        self.run("git clone https://github.com/jbehley/octree.git")

    def package(self):
        self.copy("*.hpp", dst="include/BehleyOctree", keep_path=False)

    def package_id(self):
        self.info.header_only()

