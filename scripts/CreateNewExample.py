#!/usr/bin/env python

""" Scripts to create a new example
"""

import os

group_name = raw_input( "Please enter a group: " )
module_name = raw_input( "Please enter a module: " )
class_name  = raw_input( "Please enter a class: " )
example_name = raw_input( "Please enter an example name: " )

# Collect directories
root_dir = os.path.abspath( "/Users/AJG23/GITROOT/ITKExamples" )
  # os.getcwd() ) #@ITK_EXAMPLE_SOURCE_DIR@ )

example_src_dir = os.path.join( root_dir, "src/Examples" )
example_dir = os.path.join( example_src_dir, group_name, module_name )

if not os.path.exists( example_dir )
   os.mkdir( example_dir )

example_base = os.path.join( example_dir, example_name )

example_rst = example_base + '.rst'
example_cxx = example_base + '.cxx'

# ---------------------------------------------------------
# Write rst file
f = open( example_rst, 'w' )
f.write( 'Title\n' )
f.write( '=====\n\n' )

f.write( '.. index::' )
f.write( '  single: ' + class_name + '\n\n')

f.write( 'Synopsis\n' )
f.write( '--------\n' )

synopsis = raw_input( 'Synopsis: ' )
f.write( synopsis )

f.write( 'Code\n' )
f.write( '----\n\n' )

f.write( 'C++\n' )
f.write( '...\n\n' )
f.write( '.. literalinclude:: ' + example_name + '.cxx\n\n' )

f.write( 'Results\n' )
f.write( '-------\n\n' )
f.write( '.. figure:: \n' )
f.write( '  :scale: 50%\n' )
f.write( '  :alt: Input image\n\n' )
f.write( '  Input image\n\n' )

f.write( '.. figure:: \n' )
f.write( '  :scale: 50%\n' )
f.write( '  :alt: Output image\n\n' )
f.write( '  Output image\n\n' )

f.write( 'Classes demonstrated\n' )
f.write( '--------------------\n\n' )

f.write( '.. doxygenclass: itk::' + class_name + '\n' )
f.write( '  :no-link:\n\n' )

f.write( '* \`' + class_name + ' detailed doxygen documentation\`_\n\n' )

f.write( '.. _' + class_name + ' detailed doxygen documentation:\n' )
f.write( '  http://www.itk.org/Doxygen/html/classitk_1_1' + class_name + '.html' )

# ---------------------------------------------------------
# Write cxx file

f = open( example_cxx, 'w' )
f.write( '// \#include \"itkImage.h\n' )
f.write( '// \#include \"itkImageFileReader.h\n' )
f.write( '// \#include \"itkImageFileWriter.h\n' )
f.write( '\#include \"itk' + class_name + '.h\n\n' )

f.write( 'int main( int argc, char* argv[]\n' )
f.write( '{\n' )
f.write( '  // const unsigned int Dimension = 2;\n\n' )

f.write( '  // typedef unsigned char                      PixelType;\n' )
f.write( '  // typedef itk::Image< PixelType, Dimension > ImageType;\n\n' )

f.write( '  // typedef itk::ImageFileReader< ImageType >  ReaderType;\n' )
f.write( '  // ReaderType::Pointer reader = ReaderType::New();\n' )
f.write( '  // reader->SetInputFileName( argv[1] );\n' )
f.write( '  // reader->Update();\n\n' )

f.write( '  // typedef itk::' + class_name + '<> FilterType;\n' )
f.write( '  // FilterType::Pointer filter = FilterType::New();\n' )
f.write( '  // filter->SetInput( reader->GetOutput() );\n' )
f.write( '  // filter->Update();\n\n' )

f.write( '  // typedef itk::ImageFileWrite< ImageType > WriteType;\n' )
f.write( '  // WriterType::Pointer writer = WriterType::New();\n' )
f.write( '  // writer->SetInput( filter->GetOutput() );\n' )
f.write( '  // writer->Update();\n\n' )

f.write( 'return EXIT_SUCCESS;\n' )
f.write( '}\n' )

# ---------------------------------------------------------
# Write CMakeLists.txt 

cmakefile = os.path.join( example_dir, 'CMakeLists.txt' )
f=open( cmakefile, 'w' )

f.write( 'cmake_minimum_required( VERSION 2.8 )\n\n' )

f.write( 'project( ' + example_name + ' )\n\n' )

f.write( 'find_package( ITK REQUIRED )\n\n' )

f.write( 'if( ${ITK_FOUND} )\n' )
f.write( '  include( ${ITK_USE_FILE} )\n' )
f.write( 'endif()\n\n' )

f.write( 'add_executable( ' + example_name + ' ' +  example_name + '.cxx )\n' )
f.write( 'target_link_libraries( ' + example_name + ' ${ITK_LIBRARIES} )\n\n' )

f.write( 'enable_testing()\n' )
f.write( 'add_test( ' + example_name + 'Test ' + example_name + ' )\n' )

