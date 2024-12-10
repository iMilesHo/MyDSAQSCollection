cmake_minimum_required(VERSION 3.10)
project(LeetCodeSolution CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add GoogleTest
# Make sure you have GTest installed or add it as a submodule.
# If installed via a package manager:
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

include_directories(include)

# Create library from Solution files
add_library(SolutionLib src/Solution.cpp)

# Create test executable
add_executable(runTests tests/test_solution.cpp)
target_link_libraries(runTests PRIVATE SolutionLib GTest::GTest GTest::Main)

enable_testing()
add_test(NAME runTests COMMAND runTests)