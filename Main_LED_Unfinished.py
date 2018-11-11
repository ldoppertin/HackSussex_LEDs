#!/usr/bin/python

# Simple strand test for Adafruit Dot Star RGB LED strip.
# This is a basic diagnostic tool, NOT a graphics demo...helps confirm
# correct wiring and tests each pixel's ability to display red, green
# and blue and to forward data down the line.  By limiting the number
# and color of LEDs, it's reasonably safe to power a couple meters off
# USB.  DON'T try that with other code!

import time
from dotstar import Adafruit_DotStar
import random

numpixels = 1152 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
strip    = Adafruit_DotStar(numpixels, 2000000)

# Alternate ways of declaring strip:
#  Adafruit_DotStar(npix, dat, clk, 1000000) # Bitbang @ ~1 MHz
#  Adafruit_DotStar(npix)                    # Use SPI (pins 10=MOSI, 11=SCLK)
#  Adafruit_DotStar(npix, 32000000)          # SPI @ ~32 MHz
#  Adafruit_DotStar()                        # SPI, No pixel buffer
#  Adafruit_DotStar(32000000)                # 32 MHz SPI, no pixel buf
# See image-pov.py for explanation of no-pixel-buffer use.
# Append "order='gbr'" to declaration for proper colors w/older DotStar strips)

strip.begin()           # Initialize pins for output
strip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

# Runs 10 LEDs at a time along strip, cycling through red, green and blue.
# This requires about 200 mA for all the 'on' pixels + 1 mA per 'off' pixel.


array_LED = [334, 339, 191, 329, 326, 192, 233, 183, 256, 175, 127, 151, 193, 35, 167, 324, 143, 101, 261, 345, 225, 199, 327, 3, 2, 182, 338, 224, 200, 166, 100, 262, 258, 196, 259, 6, 159, 135, 1, 335, 134, 217, 194, 198, 332, 240, 347, 190, 197, 103, 195, 64, 241, 263, 16, 348, 383, 266, 17, 158, 209, 7, 150, 207, 174, 201, 354, 350, 142, 204, 260, 36, 352, 9, 102, 242, 129, 203, 333, 382, 216, 4, 257, 133, 265, 19, 24, 250, 68, 5, 208, 271, 32, 344, 131, 267, 71, 373, 108, 128, 69, 273, 132, 341, 205, 40, 202, 18, 268, 206, 119, 141, 328, 342, 270, 111, 33, 15, 12, 148, 351, 218, 109, 37, 140, 130, 214, 275, 232, 325, 264, 10, 31, 70, 213, 210, 139, 170, 281, 337, 279, 51, 211, 138, 110, 117, 222, 283, 359, 367, 13, 226, 269, 21, 379, 346, 171, 274, 56, 137, 331, 289, 87, 25, 212, 22, 168, 172, 116, 124, 215, 48, 243, 42, 169, 287, 23, 248, 136, 234, 276, 74, 181, 304, 43, 320, 220, 38, 249, 353, 118, 272, 282, 126, 291, 330, 223, 277, 11, 30, 73, 49, 380, 147, 219, 79, 176, 381, 26, 178, 50, 297, 85, 149, 228, 29, 221, 355, 374, 349, 284, 360, 125, 280, 189, 28, 343, 146, 0, 84, 290, 27, 145, 180, 20, 41, 47, 368, 357, 83, 340, 39, 292, 114, 227, 285, 161, 187, 229, 231, 86, 375, 362, 58, 153, 144, 34, 45, 298, 236, 46, 179, 230, 44, 78, 361, 300, 278, 363, 165, 295, 113, 92, 244, 308, 356, 61, 94, 251, 235, 313, 163, 293, 238, 52, 95, 177, 59, 91, 239, 57, 288, 93, 152, 311, 72, 184, 358, 323, 65, 82, 99, 378, 162, 237, 309, 106, 364, 299, 286, 80, 247, 303, 164, 245, 53, 188, 75, 185, 296, 301, 371, 105, 60, 98, 121, 155, 307, 336, 319, 246, 370, 89, 294, 67, 154, 366, 63, 96, 112, 156, 369, 77, 252, 186, 316, 312, 173, 255, 123, 306, 317, 157, 302, 66, 372, 315, 115, 365, 120, 97, 377, 104, 160, 254, 318, 253, 54, 122, 314, 81, 107, 310, 90, 76, 321, 62, 88, 322, 55, 384, 743, 400, 735, 751, 392, 416, 727, 408, 424, 759, 432, 576, 600, 767, 575, 574, 440, 518, 613, 551, 592, 566, 584, 608, 558, 638, 719, 623, 550, 401, 586, 577, 542, 585, 567, 393, 734, 526, 601, 519, 402, 726, 578, 527, 557, 611, 617, 534, 605, 559, 704, 573, 579, 603, 533, 647, 543, 621, 710, 535, 587, 649, 639, 449, 582, 712, 425, 433, 388, 385, 525, 627, 517, 580, 541, 657, 548, 441, 386, 631, 417, 450, 565, 713, 451, 583, 549, 591, 709, 516, 618, 589, 633, 588, 389, 693, 524, 632, 720, 394, 572, 648, 640, 765, 708, 452, 564, 596, 458, 590, 664, 448, 453, 390, 391, 599, 721, 630, 609, 556, 612, 725, 532, 410, 642, 459, 665, 762, 460, 614, 682, 456, 677, 728, 418, 607, 512, 520, 597, 455, 764, 496, 619, 602, 707, 466, 610, 653, 705, 595, 540, 676, 760, 730, 742, 666, 409, 615, 454, 514, 457, 387, 395, 646, 464, 673, 521, 750, 672, 706, 515, 635, 469, 462, 513, 744, 755, 695, 641, 397, 463, 546, 604, 656, 675, 442, 467, 523, 399, 465, 398, 689, 471, 461, 699, 752, 651, 740, 723, 650, 690, 681, 745, 470, 547, 468, 486, 703, 531, 724, 426, 747, 669, 477, 637, 396, 545, 645, 472, 701, 674, 403, 475, 522, 684, 758, 434, 714, 555, 654, 659, 474, 737, 430, 662, 478, 414, 422, 691, 732, 530, 447, 748, 663, 661, 487, 479, 698, 482, 667, 529, 696, 528, 680, 606, 481, 484, 539, 438, 404, 683, 731, 473, 561, 644, 670, 616, 736, 480, 766, 624, 636, 729, 483, 419, 668, 658, 692, 660, 536, 476, 620, 738, 717, 411, 413, 439, 405, 485, 685, 643, 756, 406, 446, 412, 749, 671, 1129, 700, 754, 626, 488, 501, 746, 739, 678, 594, 407, 497, 427, 722, 444, 429, 538, 652, 1120, 697, 562, 687, 598, 753, 716, 715, 1137, 763, 537, 554, 733, 900, 761, 628, 741, 679, 655, 415, 436, 757, 445, 571, 686, 443, 552, 570, 1145, 702, 694, 510, 544, 1132, 851, 629, 437, 1146, 887, 634, 1148, 843, 688, 431, 593, 823, 420, 491, 871, 899, 811, 435, 421, 423, 560, 569, 1130, 494, 563, 428, 553, 1150, 506, 898, 912, 854, 894, 872, 507, 846, 842, 816, 1051, 903, 504, 1139, 824, 1036, 503, 508, 806, 511, 493, 1122, 940, 805, 847, 1045, 880, 844, 1131, 498, 1046, 869, 492, 895, 852, 1140, 1037, 490, 1087, 825, 1121, 944, 902, 495, 1079, 1063, 1149, 865, 840, 1070, 812, 945, 939, 1124, 885, 848, 1078, 1084, 901, 817, 1053, 1055, 489, 853, 1113, 804, 1086, 1069, 1071, 870, 1038, 947, 1083, 502, 830, 1141, 1123, 1076, 904, 807, 938, 813, 1138, 841, 1085, 1023, 893, 863, 831, 797, 928, 1088, 1061, 1054, 808, 1068, 1077, 1047, 881, 1142, 1082, 877, 505, 1115, 849, 1044, 1114, 1074, 500, 1060, 509, 818, 1116, 1075, 1006, 499, 1015, 866, 1067, 1022, 1105, 1112, 796, 1062, 1035, 999, 1039, 1052, 794, 905, 882, 850, 937, 1081, 826, 1031, 983, 959, 829, 929, 883, 809, 1133, 1125, 1066, 795, 941, 857, 1013, 1059, 936, 1134, 819, 958, 814, 946, 1042, 906, 1107, 1007, 1020, 839, 1072, 1089, 997, 886, 821, 1043, 1030, 1016, 920, 799, 930, 822, 793, 1029, 810, 1064, 1080, 864, 1097, 890, 855, 1073, 933, 792, 1034, 1004, 875, 1147, 1011, 955, 1005, 949, 1117, 1106, 1065, 827, 1014, 989, 876, 931, 1017, 1144, 1010, 992, 934, 815, 889, 798, 845, 1050, 838, 993, 1098, 932, 1118, 1058, 922, 1049, 1021, 954, 1090, 918, 787, 874, 1028, 820, 1018, 1009, 988, 935, 867, 1057, 801, 791, 1126, 862, 1135, 1001, 957, 1143, 1091, 1003, 1041, 1056, 917, 994, 953, 776, 914, 1002, 1008, 942, 788, 1136, 790, 1101, 982, 888, 828, 800, 1099, 981, 956, 837, 1019, 784, 868, 1027, 1040, 879, 964, 921, 1100, 985, 979, 861, 1127, 943, 1048, 803, 777, 1000, 952, 916, 802, 948, 990, 909, 860, 1110, 1128, 923, 913, 963, 987, 782, 966, 924, 1111, 915, 836, 783, 1109, 1032, 951, 1012, 971, 970, 859, 785, 986, 1033, 789, 778, 1102, 950, 925, 998, 969, 911, 978, 1093, 926, 1108, 786, 907, 995, 927, 996, 962, 972, 834, 775, 892, 960, 1104, 779, 975, 773, 1026, 910, 980, 977, 833, 961, 973, 878, 1103, 774, 1096, 1024, 991, 891, 780, 832, 965, 908, 1094, 1092, 984, 974, 896, 781, 772, 1025, 770, 967, 835, 897, 976, 1095, 968, 771, 768]
aspect_ratio = [18,63]
#print(len(array_LED))

def turn_to_2d(aspect_ratio,array_LED):
    count = 0
    result = [[array_LED[count] for x in range(aspect_ratio[0])] for y in range(aspect_ratio[1])]

    for x in range(aspect_ratio[1]):
        for y in range (aspect_ratio[0]):
            result[x][y] = array_LED[count]
            count+=1
    return result

matrix = turn_to_2d(aspect_ratio, array_LED)

head  = 0               # Index of first 'on' pixel
tail  = -len(matrix)+2           # Index of last 'off' pixel
tail_plus = 20
color = 0xFFFFFF        # 'On' color (starts red)
unit1 = []
unit2 = []
unit3 = []
unit4 = []
unit5 = []
unit6 = []
units = [unit1,unit2,unit3,unit4,unit5,unit6]
unit_pairs = [(unit1,unit2), (unit3,unit4), (unit5,unit6)]
on = 384
off = 370
value = 190
led = 0


for unit in units:
    for i in range(192):
	unit.append(led)
        led += 1


while True:                              # Loop forever

    '''
    all_leds = []
    for a, b in unit_pairs:
        u_leds = []
        #for x in all_leds:
        #    strip.setPixelColor(x,0)
        for i in range(3):
            for x in range(on):
            #print(unit[0][0], unit[1][-1])
                led = random.randint(a[0], b[-1])
                strip.setPixelColor(led, color)
                u_leds.append(led)
                all_leds.append(led)
	    
            #for led in u_leds:
            #    strip.setPixelColor(led, color)
            strip.show()
            time.sleep(1.0 /20)
 
               
	#strip.show()
		#for led in all_leds:
		#	strip.setPixelColor(led, 0)
	
        #for x in range(off):
	#    led = random.choice(u_leds)
	#    strip.setPixelColor(led, 0)

	    
	    strip.show()
        time.sleep(1.0 /10)
                
        for i in range(3):
            for x in range(value):
                led2 = random.choice(u_leds)
                strip.setPixelColor(led2,0)
            strip.show()
            time.sleep(1.0 /20)
        
        for x in all_leds:
            strip.setPixelColor(x,0)
    
    '''



    for led in matrix[head]:
        strip.setPixelColor(led, color) # Turn on 'head' pixel
    #for plus in range(tail_plus):
    #    if tail + plus >= 0:
     #       tail = 0
    for led in matrix[tail]:
        #if led >= numpixels:
            #tail = 0
        strip.setPixelColor(led, 0)     # Turn off 'tail'

    strip.show()                     # Refresh strip
    #time.sleep(1.0 / 100)             # Pause 20 milliseconds (~50 fps)





    head += 1                        # Advance head position
    if(matrix[head] >= matrix[-1]):           # Off end of strip?
		head    = 0              # Reset to start
		color >>= 8              # Red->green->blue->black
		if(color == 0): color = 0xFF0000 # If black, reset to red

    tail += 1                        # Advance tail position
    if(matrix[tail] >= matrix[-1]): tail = 0  # Off end? Reset




