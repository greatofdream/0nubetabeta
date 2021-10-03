cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(FeldmanCousin CXX)
set(CMAKE_BUILD_TYPE Release)

find_package(ROOT)
include(${ROOT_USE_FILE})
include_directories(${ROOT_INCLUDE_DIR})

add_library(FC SHARED fc.cpp)
target_link_libraries(FC PUBLIC ${ROOT_LIBRARIES})
install(TARGETS FC
    LIBRARY DESTINATION lib)