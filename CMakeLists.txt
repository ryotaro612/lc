cmake_minimum_required(VERSION 3.16.3)

set(CMAKE_CXX_FLAGS "-D=_debug -std=c++14 -Wall -ftrapv")

include(FetchContent)
FetchContent_Declare(
  googletest
  # Specify the commit you depend on and update it regularly.
  URL https://github.com/google/googletest/archive/609281088cfefc76f9d0ce82e1ff6c30cc3591e5.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

project(lc)
include(GoogleTest)
enable_testing()
add_subdirectory(src)
add_subdirectory(test)
