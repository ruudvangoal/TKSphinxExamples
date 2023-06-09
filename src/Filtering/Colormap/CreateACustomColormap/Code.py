#!/usr/bin/env python

# Copyright NumFOCUS
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        https://www.apache.org/licenses/LICENSE-2.0.txt
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import itk
import argparse

from distutils.version import StrictVersion as VS

if VS(itk.Version.GetITKVersion()) < VS("4.8.0"):
    print("ITK 4.8.0 is required (see example documentation).")
    sys.exit(1)

parser = argparse.ArgumentParser(description="Create A Custom Colormap.")
parser.add_argument("input_image")
parser.add_argument("output_image")
args = parser.parse_args()

PixelType = itk.UC
Dimension = 2

ImageType = itk.Image[PixelType, Dimension]

RGBPixelType = itk.RGBPixel[PixelType]
RGBImageType = itk.Image[RGBPixelType, Dimension]

ReaderType = itk.ImageFileReader[ImageType]
reader = ReaderType.New()
reader.SetFileName(args.input_image)

ColormapType = itk.CustomColormapFunction[PixelType, RGBPixelType]
colormap = ColormapType.New()

random = itk.MersenneTwisterRandomVariateGenerator.New()
random.SetSeed(0)

redChannel = []
greenChannel = []
blueChannel = []

for i in range(255):
    redChannel.append(random.GetUniformVariate(0.0, 1.0))
    greenChannel.append(random.GetUniformVariate(0.0, 1.0))
    blueChannel.append(random.GetUniformVariate(0.0, 1.0))

colormap.SetRedChannel(redChannel)
colormap.SetGreenChannel(greenChannel)
colormap.SetBlueChannel(blueChannel)

ColormapFilterType = itk.ScalarToRGBColormapImageFilter[ImageType, RGBImageType]
colormapFilter1 = ColormapFilterType.New()

colormapFilter1.SetInput(reader.GetOutput())
colormapFilter1.SetColormap(colormap)

WriterType = itk.ImageFileWriter[RGBImageType]
writer = WriterType.New()
writer.SetFileName(args.output_image)
writer.SetInput(colormapFilter1.GetOutput())

writer.Update()
