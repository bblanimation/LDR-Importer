# Copyright (C) 2019 Christopher Gearhart
# chris@bblanimation.com
# http://bblanimation.com/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# System imports
import bpy
import numpy as np
import colorsys

# Addon imports
# from .general import *


def getABSMaterial(key):
    if not hasattr(getABSMaterial, 'color_mapping'):
        colors = {}
        colors["black"] = "ABS Plastic Black"
        colors["blue"] = "ABS Plastic Blue"
        colors["bright_green"] = "ABS Plastic Bright Green"
        colors["bright_light_orange"] = "ABS Plastic Bright Light Orange"
        colors["bright_pink"] = "ABS Plastic Bright Pink"
        colors["brown"] = "ABS Plastic Brown"
        colors["light_yellow"] = "ABS Plastic Cool Yellow"
        colors["dark_azure"] = "ABS Plastic Dark Azur"
        colors["dark_blue"] = "ABS Plastic Dark Blue"
        colors["dark_brown"] = "ABS Plastic Dark Brown"
        colors["dark_green"] = "ABS Plastic Dark Green"
        colors["dark_gray"] = "ABS Plastic Dark Grey"
        colors["dark_purple"] = "ABS Plastic Dark Purple"
        colors["dark_red"] = "ABS Plastic Dark Red"
        colors["dark_tan"] = "ABS Plastic Dark Tan"
        colors["chrome_gold"] = "ABS Plastic Gold"
        colors["green"] = "ABS Plastic Green"
        colors["lavender"] = "ABS Plastic Lavender"
        colors["light_blue"] = "ABS Plastic Light Blue"
        colors["light_flesh"] = "ABS Plastic Light Flesh"
        colors["light_gray"] = "ABS Plastic Light Grey"
        colors["light_pink"] = "ABS Plastic Light Pink"
        colors["lime"] = "ABS Plastic Lime"
        colors["medium_dark_flesh"] = "ABS Plastic Medium Dark Flesh"
        colors["magenta"] = "ABS Plastic Magenta"
        colors["medium_lavender"] = "ABS Plastic Medium Lavender"
        colors["orange"] = "ABS Plastic Orange"
        colors["purple"] = "ABS Plastic Purple"
        colors["red"] = "ABS Plastic Red"
        colors["sand_blue"] = "ABS Plastic Sand Blue"
        colors["sand_green"] = "ABS Plastic Sand Green"
        colors["chrome_silver"] = "ABS Plastic Silver"
        colors["tan"] = "ABS Plastic Tan"
        colors["dark_turquoise"] = "ABS Plastic Teal"
        colors["trans_dark_blue"] = "ABS Plastic Trans-Blue"
        colors["trans_neon_orange"] = "ABS Plastic Trans-Bright Orange"
        colors["trans_clear"] = "ABS Plastic Trans-Clear"
        colors["trans_green"] = "ABS Plastic Trans-Green"
        colors["trans_light_blue"] = "ABS Plastic Trans-Light Blue"
        colors["trans_bright_green"] = "ABS Plastic Trans-Light Green"
        colors["trans_orange"] = "ABS Plastic Trans-Orange"
        colors["trans_red"] = "ABS Plastic Trans-Red"
        colors["trans_yellow"] = "ABS Plastic Trans-Yellow"
        colors["white"] = "ABS Plastic White"
        colors["yellow"] = "ABS Plastic Yellow"
        getABSMaterial.color_mapping = colors
    # The following colors do not exist in the ABS Plastic Materials palette
    # dark_pink
    # light_turquoise
    # salmon
    # pink
    # light_green
    # light_violet
    # dark_blue_violet
    # very_light_orange
    # light_purple
    # reddish_brown
    # light_bluish_gray
    # dark_bluish_gray
    # medium_blue
    # medium_green
    # dark_flesh
    # blue_violet
    # flesh
    # light_salmon
    # violet
    # medium_violet
    # medium_lime
    # aqua
    # light_lime
    # light_orange
    # very_light_bluish_gray
    # bright_light_blue
    # rust
    # bright_light_yellow
    # sky_blue
    # maersk_blue
    # medium_azure
    # light_aqua
    # yellowish_green
    # olive_green
    # sand_red
    # medium_dark_pink
    # earth_orange
    # sand_purple
    # fabuland_brown
    # medium_orange
    # dark_orange
    # very_light_gray
    # chrome_antique_brass
    # chrome_black
    # chrome_blue
    # chrome_green
    # chrome_pink
    # pearl_white
    # pearl_very_light_gray
    # pearl_light_gray
    # flat_silver
    # pearl_dark_gray
    # metal_blue
    # pearl_light_gold
    # pearl_gold
    # flat_dark_gold
    # copper
    # metallic_silver
    # metallic_green
    # metallic_gold
    # metallic_black
    # metallic_dark_gray
    # milky_white
    # glow_in_dark_opaque
    # glow_in_dark_trans
    # glitter_trans_dark_pink
    # glitter_trans_clear
    # glitter_trans_purple
    # speckle_black_silver
    # speckle_black_gold
    # speckle_black_copper
    # speckle_dark_bluish_gray_silver
    # trans_black
    # trans_neon_yellow
    # trans_yellow
    # trans_neon_green
    # trans_medium_blue
    # trans_very_light_blue
    # trans_light_purple
    # trans_purple
    # trans_dark_pink
    # trans_pink
    # rubber_yellow
    # rubber_trans_yellow
    # rubber_trans_clear
    # rubber_black
    # rubber_blue
    # rubber_red
    # rubber_orange
    # rubber_light_gray
    # rubber_dark_blue
    # rubber_purple
    # rubber_lime
    # rubber_light_bluish_gray
    # rubber_flat_silver
    # rubber_white
    # main_colour
    # edge_colour
    # trans_black_ir_lens
    # magnet
    # electric_contact_alloy
    # electric_contact_copper
    if key not in getABSMaterial.color_mapping:
        return None
    else:
        return getABSMaterial.color_mapping[key]


def getColors():
    if not hasattr(getColors, 'colors'):
        colors = {}
        colors["ABS Plastic Black"] = [0.019, 0.018, 0.017, 1.0]
        colors["ABS Plastic Blue"] = [0.000, 0.122, 0.468, 1.0]
        colors["ABS Plastic Bright Green"] = [0.006, 0.296, 0.047, 1.0]
        colors["ABS Plastic Bright Light Orange"] = [0.984, 0.445, 0.000, 1.0]
        colors["ABS Plastic Bright Pink"] = [0.863, 0.082, 0.235, 1.0]
        colors["ABS Plastic Brown"] = [0.165, 0.048, 0.024, 1.0]
        colors["ABS Plastic Cool Yellow"] = [1.000, 0.831, 0.205, 1.0]
        colors["ABS Plastic Dark Azur"] = [0.162, 0.407, 0.658, 1.0]
        colors["ABS Plastic Dark Blue"] = [0.012, 0.038, 0.089, 1.0]
        colors["ABS Plastic Dark Brown"] = [0.068, 0.033, 0.025, 1.0]
        colors["ABS Plastic Dark Green"] = [0.007, 0.065, 0.036, 1.0]
        colors["ABS Plastic Dark Grey"] = [0.078, 0.100, 0.093, 1.0]
        colors["ABS Plastic Dark Purple"] = [0.093, 0.051, 0.258, 1.0]
        colors["ABS Plastic Dark Red"] = [0.220, 0.020, 0.022, 1.0]
        colors["ABS Plastic Dark Tan"] = [0.328, 0.231, 0.127, 1.0]
        colors["ABS Plastic Gold"] = [0.718, 0.522, 0.129, 1.0]
        colors["ABS Plastic Green"] = [0.000, 0.216, 0.005, 1.0]
        colors["ABS Plastic Lavender"] = [0.485, 0.397, 0.680, 1.0]
        colors["ABS Plastic Light Blue"] = [0.060, 0.323, 0.604, 1.0]
        colors["ABS Plastic Light Flesh"] = [0.930, 0.558, 0.397, 1.0]
        colors["ABS Plastic Light Grey"] = [0.347, 0.376, 0.386, 1.0]
        colors["ABS Plastic Light Pink"] = [0.922, 0.407, 0.701, 1.0]
        colors["ABS Plastic Lime"] = [0.366, 0.491, 0.003, 1.0]
        colors["ABS Plastic Medium Dark Flesh"] = [0.423, 0.175, 0.065, 1.0]
        colors["ABS Plastic Magenta"] = [0.392, 0.019, 0.150, 1.0]
        colors["ABS Plastic Medium Lavender"] = [0.361, 0.178, 0.479, 1.0]
        colors["ABS Plastic Orange"] = [1.000, 0.209, 0.006, 1.0]
        colors["ABS Plastic Purple"] = [0.246, 0.022, 0.147, 1.0]
        colors["ABS Plastic Red"] = [0.503, 0.012, 0.015, 1.0]
        colors["ABS Plastic Sand Blue"] = [0.156, 0.235, 0.301, 1.0]
        colors["ABS Plastic Sand Green"] = [0.165, 0.296, 0.202, 1.0]
        colors["ABS Plastic Silver"] = [0.168, 0.168, 0.168, 1.0]
        colors["ABS Plastic Tan"] = [0.716, 0.539, 0.301, 1.0]
        colors["ABS Plastic Teal"] = [0.000, 0.292, 0.283, 1.0]
        colors["ABS Plastic Trans-Blue"] = [0.000, 0.423, 0.745, 0.4]
        colors["ABS Plastic Trans-Bright Orange"] = [1.000, 0.314, 0.000, 0.4]
        colors["ABS Plastic Trans-Clear"] = [0.5, 0.5, 0.5, 0.1]
        colors["ABS Plastic Trans-Green"] = [0.000, 0.533, 0.084, 0.4]
        colors["ABS Plastic Trans-Light Blue"] = [0.386, 0.855, 1.000, 0.4]
        colors["ABS Plastic Trans-Light Green"] = [0.888, 1.000, 0.012, 0.4]
        colors["ABS Plastic Trans-Orange"] = [1.000, 0.474, 0.122, 0.4]
        colors["ABS Plastic Trans-Red"] = [0.956, 0.000, 0.000, 0.4]
        colors["ABS Plastic Trans-Yellow"] = [1.000, 0.896, 0.017, 0.4]
        colors["ABS Plastic Trans-Yellowish Clear"] = [0.880, 0.839, 0.730, 0.2]
        colors["ABS Plastic White"] = [0.947, 0.896, 0.815, 1.0]
        colors["ABS Plastic Yellow"] = [0.973, 0.584, 0.000, 1.0]
        # # gamma correct RGB values
        # for key in colors:
        #     colors[key] = gammaCorrect(colors[key], 2)
        getColors.colors = colors
    return getColors.colors


def findNearestBrickColorName(rgba, transWeight, matObj=None):
    if rgba is None:
        return ""
    colors = getColors().copy()
    if matObj is not None:
        for k in getColors().keys():
            if k not in matObj.data.materials.keys():
                colors.pop(k, None)
    return findNearestColorName(rgba, transWeight, colors)


def distance(c1, c2, aWt=1):
    r1, g1, b1, a1 = c1
    r2, g2, b2, a2 = c2
    # a1 = c1[3]
    # # r1, g1, b1 = rgb_to_lab(c1[:3])
    # r1, g1, b1 = colorsys.rgb_to_hsv(r1, g1, b1)
    # a2 = c2[3]
    # # r2, g2, b2 = rgb_to_lab(c2[:3])
    # r2, g2, b2 = colorsys.rgb_to_hsv(r1, g1, b1)
    # diff =  0.33 * ((r1 - r2)**2)
    # diff += 0.33 * ((g1 - g2)**2)
    # diff += 0.33 * ((b1 - b2)**2)
    # diff += 1.0 * ((a1 - a2)**2)
    diff =  0.30 * ((r1 - r2)**2)
    diff += 0.59 * ((g1 - g2)**2)
    diff += 0.11 * ((b1 - b2)**2)
    diff += aWt * ((a1 - a2)**2)
    return diff


def findNearestColorName(rgba, transWeight, colorNames):
    mindiff = None
    mincolorname = ""
    for colorName in colorNames:
        diff = distance(rgba, colorNames[colorName], transWeight)
        if mindiff is None or diff < mindiff:
            mindiff = diff
            mincolorname = colorName
    return mincolorname
