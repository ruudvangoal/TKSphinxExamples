cmake_minimum_required(VERSION 3.16.3)

project(IterativeHoleFilling)

find_package(ITK REQUIRED)
include(${ITK_USE_FILE})

add_executable(${PROJECT_NAME} Code.cxx)
target_link_libraries(${PROJECT_NAME} ${ITK_LIBRARIES})

install(TARGETS ${PROJECT_NAME}
  DESTINATION bin/ITKSphinxExamples/Segmentation/LabelVoting
  COMPONENT Runtime
  )

install(FILES Code.cxx CMakeLists.txt
  DESTINATION share/ITKSphinxExamples/Code/Segmentation/LabelVoting/IterativeHoleFilling
  COMPONENT Code
  )

enable_testing()

add_test(NAME IterativeHoleFillingTest
  COMMAND ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${PROJECT_NAME}
    ${CMAKE_CURRENT_BINARY_DIR}/BinaryThresholdImageFilter.png
    Output.png
    3 1 5
)
