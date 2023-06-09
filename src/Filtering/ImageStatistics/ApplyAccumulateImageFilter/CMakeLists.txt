cmake_minimum_required(VERSION 3.16.3)

project(ApplyAccumulateImageFilter)

find_package(ITK REQUIRED)
include(${ITK_USE_FILE})

add_executable(${PROJECT_NAME} Code.cxx)
target_link_libraries(${PROJECT_NAME} ${ITK_LIBRARIES})

install(TARGETS ${PROJECT_NAME}
  DESTINATION bin/ITKSphinxExamples/Filtering/ImageStatistics
  COMPONENT Runtime
  )

install(FILES Code.cxx CMakeLists.txt
  DESTINATION share/ITKSphinxExamples/Code/Filtering/ImageStatistics/ApplyAccumulateImageFilter
  COMPONENT Code
  )

enable_testing()

foreach(i RANGE 0 2)
  add_test(NAME ApplyAccumulateImageFilterTest${i}
    COMMAND ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${PROJECT_NAME}
      ${CMAKE_CURRENT_BINARY_DIR}/HeadMRVolume.mha
      ${CMAKE_CURRENT_BINARY_DIR}/ApplyAccumulateImageFilterTestOutput${i}.mha
      ${i}
  )
endforeach()
