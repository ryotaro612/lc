include_directories(${PROJECT_SOURCE_DIR}/src)

add_executable(missing_ranges_test missing_ranges.cc)
target_link_libraries(missing_ranges_test missing_ranges gtest_main)
gtest_discover_tests(missing_ranges_test)

add_executable(next_closest_time_test next_closest_time.cc)
target_link_libraries(next_closest_time_test next_closest_time gtest_main)
gtest_discover_tests(next_closest_time_test)

add_executable(find_and_replace_in_string_test find_and_replace_in_string.cc)
target_link_libraries(find_and_replace_in_string_test find_and_replace_in_string gtest_main)
gtest_discover_tests(find_and_replace_in_string_test)

add_executable(trapping_rain_water_test trapping_rain_water.cc)
target_link_libraries(trapping_rain_water_test trapping_rain_water gtest_main)
gtest_discover_tests(trapping_rain_water_test)

add_executable(backspace_string_compare_test backspace_string_compare.cc)
target_link_libraries(backspace_string_compare_test backspace_string_compare gtest_main)
gtest_discover_tests(backspace_string_compare_test)