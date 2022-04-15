from tkinter import *
from datetime import date

########################################################################################################################################################################################################################################################################################################################

def close():
    root.destroy()  

def dateCheck(x):
    a = str(date.today())
    a = a.split("-")
    if int(a[1]) >= 1 or int(a[0]) > 2022:
        if int(a[2]) >= 4 or int(a[1]) > 1 or int(a[0]) > 2022:
            J1.config(state=DISABLED, bg="red")
            J2.config(state=DISABLED, bg="red")
            J3.config(state=DISABLED, bg="red")
            J4.config(state=DISABLED, bg="red")
            J5.config(state=DISABLED, bg="red")
            J6.config(state=DISABLED, bg="red")
            J7.config(state=DISABLED, bg="red")
            J8.config(state=DISABLED, bg="red")
            J9.config(state=DISABLED, bg="red")
            J10.config(state=DISABLED, bg="red")
            J11.config(state=DISABLED, bg="red")
            J12.config(state=DISABLED, bg="red")
            J13.config(state=DISABLED, bg="red")
        if int(a[2]) >= 11 or int(a[1]) > 1 or int(a[0]) > 2022:
            J14.config(state=DISABLED, bg="red")
            J15.config(state=DISABLED, bg="red")
            J16.config(state=DISABLED, bg="red")
            J17.config(state=DISABLED, bg="red")
            J18.config(state=DISABLED, bg="red")
            J19.config(state=DISABLED, bg="red")
            J20.config(state=DISABLED, bg="red")
            if x == "a":
                J21.config(state=DISABLED, bg="red")
        if int(a[2]) >= 18 or int(a[1]) > 1 or int(a[0]) > 2022:
            J21.config(state=DISABLED, bg="red")
            J22.config(state=DISABLED, bg="red")
            J23.config(state=DISABLED, bg="red")
            J24.config(state=DISABLED, bg="red")
            J25.config(state=DISABLED, bg="red")
            J26.config(state=DISABLED, bg="red")
            J27.config(state=DISABLED, bg="red")
            if x == "i":
                J28.config(state=DISABLED, bg="red")
        if int(a[2]) > 25 or int(a[1]) > 1 or int(a[0]) > 2022:
            J28.config(state=DISABLED, bg="red")
            J29.config(state=DISABLED, bg="red")
            J30.config(state=DISABLED, bg="red")
            J31.config(state=DISABLED, bg="red")
            F1.config(state=DISABLED, bg="red")
            F2.config(state=DISABLED, bg="red")
            F3.config(state=DISABLED, bg="red")
            if x == "a":
                F4.config(state=DISABLED, bg="red")
    if int(a[1]) >= 2 or int(a[0]) > 2022:
        if int(a[2]) > 1 or int(a[1]) > 2 or int(a[0]) > 2022:
            F4.config(state=DISABLED, bg="red")
            F5.config(state=DISABLED, bg="red")
            F6.config(state=DISABLED, bg="red")
            F7.config(state=DISABLED, bg="red")
            F8.config(state=DISABLED, bg="red")
            F9.config(state=DISABLED, bg="red")
            F10.config(state=DISABLED, bg="red")
            if x == "i":
                F11.config(state=DISABLED, bg="red")
        if int(a[2]) >= 8 or int(a[1]) > 2 or int(a[0]) > 2022:
            F11.config(state=DISABLED, bg="red")
            F12.config(state=DISABLED, bg="red")
            F13.config(state=DISABLED, bg="red")
            F14.config(state=DISABLED, bg="red")
            F15.config(state=DISABLED, bg="red")
            F16.config(state=DISABLED, bg="red")
            F17.config(state=DISABLED, bg="red")
            if x == "a":
                F18.config(state=DISABLED, bg="light grey")
        if int(a[2]) >= 15 or int(a[1]) > 2 or int(a[0]) > 2022:
            F18.config(state=DISABLED, bg="red")
            F19.config(state=DISABLED, bg="red")
            F20.config(state=DISABLED, bg="red")
            F21.config(state=DISABLED, bg="red")
            F22.config(state=DISABLED, bg="red")
            F23.config(state=DISABLED, bg="red")
            F24.config(state=DISABLED, bg="red")
            if x == "i":
                F25.config(state=DISABLED, bg="red")
        if int(a[2]) >= 22 or int(a[1]) > 2 or int(a[0]) > 2022:
            F25.config(state=DISABLED, bg="red")
            F26.config(state=DISABLED, bg="red")
            F27.config(state=DISABLED, bg="red")
            F28.config(state=DISABLED, bg="red")
            M1.config(state=DISABLED, bg="red")
            M2.config(state=DISABLED, bg="red")
            M3.config(state=DISABLED, bg="red")
            if x == "a":
                M4.config(state=DISABLED, bg="red")
    if int(a[1]) >= 3 or int(a[0]) > 2022:
        if int(a[2]) >= 1 or int(a[1]) > 3 or int(a[0]) > 2022:
            M4.config(state=DISABLED, bg="red")
            M5.config(state=DISABLED, bg="red")
            M6.config(state=DISABLED, bg="red")
            M7.config(state=DISABLED, bg="red")
            M8.config(state=DISABLED, bg="red")
            M9.config(state=DISABLED, bg="red")
            M10.config(state=DISABLED, bg="red")
            if x == "i":
                M11.config(state=DISABLED, bg="red")
        if int(a[2]) >= 8 or int(a[1]) > 3 or int(a[0]) > 2022:
            M11.config(state=DISABLED, bg="red")
            M12.config(state=DISABLED, bg="red")
            M13.config(state=DISABLED, bg="red")
            M14.config(state=DISABLED, bg="red")
            M15.config(state=DISABLED, bg="red")
            M16.config(state=DISABLED, bg="red")
            M17.config(state=DISABLED, bg="red")
            if x == "a":
                M18.config(state=DISABLED, bg="red")
        if int(a[2]) >= 15 or int(a[1]) > 3 or int(a[0]) > 2022:
            M18.config(state=DISABLED, bg="red")
            M19.config(state=DISABLED, bg="red")
            M20.config(state=DISABLED, bg="red")
            M21.config(state=DISABLED, bg="red")
            M22.config(state=DISABLED, bg="red")
            M23.config(state=DISABLED, bg="red")
            M24.config(state=DISABLED, bg="red")
            if x == "i":
                M25.config(state=DISABLED, bg="red")
        if int(a[2]) >= 22 or int(a[1]) > 3 or int(a[0]) > 2022:
            M25.config(state=DISABLED, bg="red")
            M26.config(state=DISABLED, bg="red")
            M27.config(state=DISABLED, bg="red")
            M28.config(state=DISABLED, bg="red")
            M29.config(state=DISABLED, bg="red")
            M30.config(state=DISABLED, bg="red")
            M31.config(state=DISABLED, bg="red")
            if x == "a":
                A1.config(state=DISABLED, bg="red")
        if int(a[2]) >= 29 or int(a[1]) > 3 or int(a[0]) > 2022:
            A1.config(state=DISABLED, bg="red")
            A2.config(state=DISABLED, bg="red")
            A3.config(state=DISABLED, bg="red")
            A4.config(state=DISABLED, bg="red")
            A5.config(state=DISABLED, bg="red")
            A6.config(state=DISABLED, bg="red")
            A7.config(state=DISABLED, bg="red")
            if x == "i":
                A8.config(state=DISABLED, bg="red")
        if int(a[1]) >= 4 or int(a[0]) > 2022:
            if int(a[2]) >= 5 or int(a[1]) > 4 or int(a[0]) > 2022:
                A8.config(state=DISABLED, bg="red")
                A9.config(state=DISABLED, bg="red")
                A10.config(state=DISABLED, bg="red")
                A11.config(state=DISABLED, bg="red")
                A12.config(state=DISABLED, bg="red")
                A13.config(state=DISABLED, bg="red")
                A14.config(state=DISABLED, bg="red")
                if x == "a":
                    A15.config(state=DISABLED, bg="red")
            if int(a[2]) >= 12 or int(a[1]) > 4 or int(a[0]) > 2022:
                A15.config(state=DISABLED, bg="red")
                A16.config(state=DISABLED, bg="red")
                A17.config(state=DISABLED, bg="red")
                A18.config(state=DISABLED, bg="red")
                A19.config(state=DISABLED, bg="red")
                A20.config(state=DISABLED, bg="red")
                A21.config(state=DISABLED, bg="red")
                if x == "i":
                    A22.config(state=DISABLED, bg="red")
            if int(a[2]) >= 19 or int(a[1]) > 4 or int(a[0]) > 2022:
                A22.config(state=DISABLED, bg="red")
                A23.config(state=DISABLED, bg="red")
                A24.config(state=DISABLED, bg="red")
                A25.config(state=DISABLED, bg="red")
                A26.config(state=DISABLED, bg="red")
                A27.config(state=DISABLED, bg="red")
                A28.config(state=DISABLED, bg="red")
                if x == "a":
                    A29.config(state=DISABLED, bg="red")
            if int(a[2]) >= 26 or int(a[1]) > 4 or int(a[0]) > 2022:
                A29.config(state=DISABLED, bg="red")
                A30.config(state=DISABLED, bg="red")
                MA1.config(state=DISABLED, bg="red")
                MA2.config(state=DISABLED, bg="red")
                MA3.config(state=DISABLED, bg="red")
                MA4.config(state=DISABLED, bg="red")
                MA5.config(state=DISABLED, bg="red")
                if x == "i":
                    MA6.config(state=DISABLED, bg="red")
        if int(a[1]) >= 5 or int(a[0]) > 2022:
            if int(a[2]) >= 3 or int(a[1]) > 5 or int(a[0]) > 2022:
                MA6.config(state=DISABLED, bg="red")
                MA7.config(state=DISABLED, bg="red")
                MA8.config(state=DISABLED, bg="red")
                MA9.config(state=DISABLED, bg="red")
                MA10.config(state=DISABLED, bg="red")
                MA11.config(state=DISABLED, bg="red")
                MA12.config(state=DISABLED, bg="red")
                if x == "a":
                    MA13.config(state=DISABLED, bg="red")
            if int(a[2]) >= 10 or int(a[1]) > 5 or int(a[0]) > 2022:
                MA13.config(state=DISABLED, bg="red")
                MA14.config(state=DISABLED, bg="red")
                MA15.config(state=DISABLED, bg="red")
                MA16.config(state=DISABLED, bg="red")
                MA17.config(state=DISABLED, bg="red")
                MA18.config(state=DISABLED, bg="red")
                MA19.config(state=DISABLED, bg="red")
                if x == "i":
                    MA20.config(state=DISABLED, bg="red")
            if int(a[2]) >= 17 or int(a[1]) > 5 or int(a[0]) > 2022:
                MA20.config(state=DISABLED, bg="red")
                MA21.config(state=DISABLED, bg="red")
                MA22.config(state=DISABLED, bg="red")
                MA23.config(state=DISABLED, bg="red")
                MA24.config(state=DISABLED, bg="red")
                MA25.config(state=DISABLED, bg="red")
                MA26.config(state=DISABLED, bg="red")
                if x == "a":
                    MA27.config(state=DISABLED, bg="red")
            if int(a[2]) >= 24 or int(a[1]) > 5 or int(a[0]) > 2022:
                MA27.config(state=DISABLED, bg="red")
                MA28.config(state=DISABLED, bg="red")
                MA29.config(state=DISABLED, bg="red")
                MA30.config(state=DISABLED, bg="red")
                MA31.config(state=DISABLED, bg="red")
                JU1.config(state=DISABLED, bg="red")
                JU2.config(state=DISABLED, bg="red")
                if x == "i":
                    JU3.config(state=DISABLED, bg="red")
            if int(a[2]) >= 31 or int(a[1]) > 5 or int(a[0]) > 2022:
                JU3.config(state=DISABLED, bg="red")
                JU4.config(state=DISABLED, bg="red")
                JU5.config(state=DISABLED, bg="red")
                JU6.config(state=DISABLED, bg="red")
                JU7.config(state=DISABLED, bg="red")
                JU8.config(state=DISABLED, bg="red")
                JU9.config(state=DISABLED, bg="red")
                if x == "a":
                    JU10.config(state=DISABLED, bg="red")
        if int(a[1]) >= 6 or int(a[0]) > 2022:
            if int(a[2]) >= 7 or int(a[1]) > 6 or int(a[0]) > 2022:
                JU10.config(state=DISABLED, bg="red")
                JU11.config(state=DISABLED, bg="red")
                JU12.config(state=DISABLED, bg="red")
                JU13.config(state=DISABLED, bg="red")
                JU14.config(state=DISABLED, bg="red")
                JU15.config(state=DISABLED, bg="red")
                JU16.config(state=DISABLED, bg="red")
                if x == "i":
                    JU17.config(state=DISABLED, bg="red")
            if int(a[2]) >= 14 or int(a[1]) > 6 or int(a[0]) > 2022:
                JU17.config(state=DISABLED, bg="red")
                JU18.config(state=DISABLED, bg="red")
                JU19.config(state=DISABLED, bg="red")
                JU20.config(state=DISABLED, bg="red")
                JU21.config(state=DISABLED, bg="red")
                JU22.config(state=DISABLED, bg="red")
                JU23.config(state=DISABLED, bg="red")
                if x == "a":
                    JU24.config(state=DISABLED, bg="red")
            if int(a[2]) >= 21 or int(a[1]) > 6 or int(a[0]) > 2022:
                JU24.config(state=DISABLED, bg="red")
                JU25.config(state=DISABLED, bg="red")
                JU26.config(state=DISABLED, bg="red")
                JU27.config(state=DISABLED, bg="red")
                JU28.config(state=DISABLED, bg="red")
                JU29.config(state=DISABLED, bg="red")
                JU30.config(state=DISABLED, bg="red")
                if x == "i":
                    JUL1.config(state=DISABLED, bg="red")
            if int(a[2]) >= 28 or int(a[1]) > 6 or int(a[0]) > 2022:
                JUL1.config(state=DISABLED, bg="red")
                JUL2.config(state=DISABLED, bg="red")
                JUL3.config(state=DISABLED, bg="red")
                JUL4.config(state=DISABLED, bg="red")
                JUL5.config(state=DISABLED, bg="red")
                JUL6.config(state=DISABLED, bg="red")
                JUL7.config(state=DISABLED, bg="red")
                if x == "a":
                    JUL8.config(state=DISABLED, bg="red")
        if int(a[1]) >= 7 or int(a[0]) > 2022:
            if int(a[2]) >= 5 or int(a[1]) > 7 or int(a[0]) > 2022:
                JUL8.config(state=DISABLED, bg="red")
                JUL9.config(state=DISABLED, bg="red")
                JUL10.config(state=DISABLED, bg="red")
                JUL11.config(state=DISABLED, bg="red")
                JUL12.config(state=DISABLED, bg="red")
                JUL13.config(state=DISABLED, bg="red")
                JUL14.config(state=DISABLED, bg="red")
                if x == "i":
                    JUL15.config(state=DISABLED, bg="red")
            if int(a[2]) >= 12 or int(a[1]) > 7 or int(a[0]) > 2022:
                JUL15.config(state=DISABLED, bg="red")
                JUL16.config(state=DISABLED, bg="red")
                JUL17.config(state=DISABLED, bg="red")
                JUL18.config(state=DISABLED, bg="red")
                JUL19.config(state=DISABLED, bg="red")
                JUL20.config(state=DISABLED, bg="red")
                JUL21.config(state=DISABLED, bg="red")
                if x == "a":
                    JUL22.config(state=DISABLED, bg="red")
            if int(a[2]) >= 19 or int(a[1]) > 7 or int(a[0]) > 2022:
                JUL22.config(state=DISABLED, bg="red")
                JUL23.config(state=DISABLED, bg="red")
                JUL24.config(state=DISABLED, bg="red")
                JUL25.config(state=DISABLED, bg="red")
                JUL26.config(state=DISABLED, bg="red")
                JUL27.config(state=DISABLED, bg="red")
                JUL28.config(state=DISABLED, bg="red")
                if x == "i":
                    JUL29.config(state=DISABLED, bg="red")
            if int(a[2]) >= 26 or int(a[1]) > 7 or int(a[0]) > 2022:
                JUL29.config(state=DISABLED, bg="red")
                JUL30.config(state=DISABLED, bg="red")
                JUL31.config(state=DISABLED, bg="red")
                AU1.config(state=DISABLED, bg="red")
                AU2.config(state=DISABLED, bg="red")
                AU3.config(state=DISABLED, bg="red")
                AU4.config(state=DISABLED, bg="red")
                if x == "a":
                    AU5.config(state=DISABLED, bg="red")
        if int(a[1]) >= 8 or int(a[0]) > 2022:
            if int(a[2]) >= 2 or int(a[1]) > 8 or int(a[0]) > 2022:
                AU5.config(state=DISABLED, bg="red")
                AU6.config(state=DISABLED, bg="red")
                AU7.config(state=DISABLED, bg="red")
                AU8.config(state=DISABLED, bg="red")
                AU9.config(state=DISABLED, bg="red")
                AU10.config(state=DISABLED, bg="red")
                AU11.config(state=DISABLED, bg="red")
                if x == "i":
                    AU12.config(state=DISABLED, bg="red")
            if int(a[2]) >= 9 or int(a[1]) > 8 or int(a[0]) > 2022:
                AU12.config(state=DISABLED, bg="red")
                AU13.config(state=DISABLED, bg="red")
                AU14.config(state=DISABLED, bg="red")
                AU15.config(state=DISABLED, bg="red")
                AU16.config(state=DISABLED, bg="red")
                AU17.config(state=DISABLED, bg="red")
                AU18.config(state=DISABLED, bg="red")
                if x == "a":
                    AU19.config(state=DISABLED, bg="red")
            if int(a[2]) >= 16 or int(a[1]) > 8 or int(a[0]) > 2022:
                AU19.config(state=DISABLED, bg="red")
                AU20.config(state=DISABLED, bg="red")
                AU21.config(state=DISABLED, bg="red")
                AU22.config(state=DISABLED, bg="red")
                AU23.config(state=DISABLED, bg="red")
                AU24.config(state=DISABLED, bg="red")
                AU25.config(state=DISABLED, bg="red")
                if x == "i":
                    AU26.config(state=DISABLED, bg="red")
            if int(a[2]) >= 23 or int(a[1]) > 8 or int(a[0]) > 2022:
                AU26.config(state=DISABLED, bg="red")
                AU27.config(state=DISABLED, bg="red")
                AU28.config(state=DISABLED, bg="red")
                AU29.config(state=DISABLED, bg="red")
                AU30.config(state=DISABLED, bg="red")
                AU31.config(state=DISABLED, bg="red")
                S1.config(state=DISABLED, bg="red")
                if x == "a":
                    S2.config(state=DISABLED, bg="red")
            if int(a[2]) >= 30 or int(a[1]) > 8 or int(a[0]) > 2022:
                S2.config(state=DISABLED, bg="red")
                S3.config(state=DISABLED, bg="red")
                S4.config(state=DISABLED, bg="red")
                S5.config(state=DISABLED, bg="red")
                S6.config(state=DISABLED, bg="red")
                S7.config(state=DISABLED, bg="red")
                S8.config(state=DISABLED, bg="red")
                if x == "i":
                    S9.config(state=DISABLED, bg="red")
        if int(a[1]) >= 9 or int(a[0]) > 2022:
            if int(a[2]) >= 6 or int(a[1]) > 9 or int(a[0]) > 2022:
                S9.config(state=DISABLED, bg="red")
                S10.config(state=DISABLED, bg="red")
                S11.config(state=DISABLED, bg="red")
                S12.config(state=DISABLED, bg="red")
                S13.config(state=DISABLED, bg="red")
                S14.config(state=DISABLED, bg="red")
                S15.config(state=DISABLED, bg="red")
                if x == "a":
                    S16.config(state=DISABLED, bg="red")
            if int(a[2]) >= 13 or int(a[1]) > 9 or int(a[0]) > 2022:
                S16.config(state=DISABLED, bg="red")
                S17.config(state=DISABLED, bg="red")
                S18.config(state=DISABLED, bg="red")
                S19.config(state=DISABLED, bg="red")
                S20.config(state=DISABLED, bg="red")
                S21.config(state=DISABLED, bg="red")
                S22.config(state=DISABLED, bg="red")
                if x == "i":
                    S23.config(state=DISABLED, bg="red")
            if int(a[2]) >= 20 or int(a[1]) > 9 or int(a[0]) > 2022:
                S23.config(state=DISABLED, bg="red")
                S24.config(state=DISABLED, bg="red")
                S25.config(state=DISABLED, bg="red")
                S26.config(state=DISABLED, bg="red")
                S27.config(state=DISABLED, bg="red")
                S28.config(state=DISABLED, bg="red")
                S29.config(state=DISABLED, bg="red")
                if x == "a":
                    S30.config(state=DISABLED, bg="red")
            if int(a[2]) >= 27 or int(a[1]) > 9 or int(a[0]) > 2022:
                S30.config(state=DISABLED, bg="red")
                O1.config(state=DISABLED, bg="red")
                O2.config(state=DISABLED, bg="red")
                O3.config(state=DISABLED, bg="red")
                O4.config(state=DISABLED, bg="red")
                O5.config(state=DISABLED, bg="red")
                O6.config(state=DISABLED, bg="red")
                if x == "i":
                    O7.config(state=DISABLED, bg="red")
        if int(a[1]) >= 10 or int(a[0]) > 2022:
            if int(a[2]) >= 4 or int(a[1]) > 10 or int(a[0]) > 2022:
                O7.config(state=DISABLED, bg="red")
                O8.config(state=DISABLED, bg="red")
                O9.config(state=DISABLED, bg="red")
                O10.config(state=DISABLED, bg="red")
                O11.config(state=DISABLED, bg="red")
                O12.config(state=DISABLED, bg="red")
                O13.config(state=DISABLED, bg="red")
                if x == "i":
                    O14.config(state=DISABLED, bg="red")
            if int(a[2]) >= 11 or int(a[1]) > 10 or int(a[0]) > 2022:
                O14.config(state=DISABLED, bg="red")
                O15.config(state=DISABLED, bg="red")
                O16.config(state=DISABLED, bg="red")
                O17.config(state=DISABLED, bg="red")
                O18.config(state=DISABLED, bg="red")
                O19.config(state=DISABLED, bg="red")
                O20.config(state=DISABLED, bg="red")
                if x == "a":
                    O21.config(state=DISABLED, bg="red")
            if int(a[2]) >= 18 or int(a[1]) > 10 or int(a[0]) > 2022:
                O21.config(state=DISABLED, bg="red")
                O22.config(state=DISABLED, bg="red")
                O23.config(state=DISABLED, bg="red")
                O24.config(state=DISABLED, bg="red")
                O25.config(state=DISABLED, bg="red")
                O26.config(state=DISABLED, bg="red")
                O27.config(state=DISABLED, bg="red")
                if x == "i":
                    O28.config(state=DISABLED, bg="red")
            if int(a[2]) >= 25 or int(a[1]) > 10 or int(a[0]) > 2022:
                O28.config(state=DISABLED, bg="red")
                O29.config(state=DISABLED, bg="red")
                O30.config(state=DISABLED, bg="red")
                O31.config(state=DISABLED, bg="red")
                N1.config(state=DISABLED, bg="red")
                N2.config(state=DISABLED, bg="red")
                N3.config(state=DISABLED, bg="red")
                if x == "a":
                    N4.config(state=DISABLED, bg="red")
        if int(a[1]) >= 11 or int(a[0]) > 2022:
            if int(a[2]) >= 1 or int(a[1]) > 11 or int(a[0]) > 2022:
                N4.config(state=DISABLED, bg="red")
                N5.config(state=DISABLED, bg="red")
                N6.config(state=DISABLED, bg="red")
                N7.config(state=DISABLED, bg="red")
                N8.config(state=DISABLED, bg="red")
                N9.config(state=DISABLED, bg="red")
                N10.config(state=DISABLED, bg="red")
                if x == "i":
                    N11.config(state=DISABLED, bg="red")
            if int(a[2]) >= 8 or int(a[1]) > 11 or int(a[0]) > 2022:
                N11.config(state=DISABLED, bg="red")
                N12.config(state=DISABLED, bg="red")
                N13.config(state=DISABLED, bg="red")
                N14.config(state=DISABLED, bg="red")
                N15.config(state=DISABLED, bg="red")
                N16.config(state=DISABLED, bg="red")
                N17.config(state=DISABLED, bg="red")
                if x == "a":
                    N18.config(state=DISABLED, bg="red")
            if int(a[2]) >= 15 or int(a[1]) > 11 or int(a[0]) > 2022:
                N18.config(state=DISABLED, bg="red")
                N19.config(state=DISABLED, bg="red")
                N20.config(state=DISABLED, bg="red")
                N21.config(state=DISABLED, bg="red")
                N22.config(state=DISABLED, bg="red")
                N23.config(state=DISABLED, bg="red")
                N24.config(state=DISABLED, bg="red")
                if x == "i":
                    N25.config(state=DISABLED, bg="red")
            if int(a[2]) >= 22 or int(a[1]) > 11 or int(a[0]) > 2022:
                N25.config(state=DISABLED, bg="red")
                N26.config(state=DISABLED, bg="red")
                N27.config(state=DISABLED, bg="red")
                N28.config(state=DISABLED, bg="red")
                N29.config(state=DISABLED, bg="red")
                N30.config(state=DISABLED, bg="red")
                D1.config(state=DISABLED, bg="red")
                if x == "i":
                    D2.config(state=DISABLED, bg="red")
            if int(a[2]) >= 29 or int(a[1]) > 11 or int(a[0]) > 2022:
                D2.config(state=DISABLED, bg="red")
                D3.config(state=DISABLED, bg="red")
                D4.config(state=DISABLED, bg="red")
                D5.config(state=DISABLED, bg="red")
                D6.config(state=DISABLED, bg="red")
                D7.config(state=DISABLED, bg="red")
                D8.config(state=DISABLED, bg="red")
                if x == "a":
                    D9.config(state=DISABLED, bg="red")
        if int(a[1]) >= 12 or int(a[0]) > 2022:
            if int(a[2]) >= 6 or int(a[1]) > 12 or int(a[0]) > 2022:
                D9.config(state=DISABLED, bg="red")
                D10.config(state=DISABLED, bg="red")
                D11.config(state=DISABLED, bg="red")
                D12.config(state=DISABLED, bg="red")
                D13.config(state=DISABLED, bg="red")
                D14.config(state=DISABLED, bg="red")
                D15.config(state=DISABLED, bg="red")
                if x == "i":
                    D16.config(state=DISABLED, bg="red")
            if int(a[2]) >= 13 or int(a[1]) > 12 or int(a[0]) > 2022:
                D16.config(state=DISABLED, bg="red")
                                     
#################################################################################################################################################################################################################################################################################

def output(m, d, t):
    if t == "application":
        if m == 1:
            if d == 14 or d == 15 or d == 16 or d == 17 or d == 18 or d == 19 or d == 20 or d == 21:
                Sdate = "Friday January 14th | 5:01pm"
                Edate = "Friday January 21st | 4:59pm"
                Sby = "Monday January 10th | 11:00pm"
                SbH = "Tuesday January 11th | 2:00pm"
                Acab = "Thursday January 13th | 10:00am"
                Aadhoc = "Thursday January 13th | 5:00pm"
                NSD = "Friday January 28th | 5:01pm"
                NED = "Friday February 4th | 4:59pm"
            if d == 28 or d == 29 or d == 30 or d == 31:
                Sdate = "Friday January 28th | 5:01pm"
                Edate = "Friday February 4th | 4:59pm"
                Sby = "Monday January 24th | 11:00pm"
                SbH = "Tuesday January 25th | 2:00pm"
                Acab = "Thursday January 27th | 10:00am"
                Aadhoc = "Thursday January 27th | 5:00pm"
                NSD = "Friday February 11th | 5:01pm"
                NED = "Friday February 18th | 4:59pm"
        if m == 2:
            if d == 1 or d == 2 or d == 3 or d == 4:
                Sdate = "Friday January 28th | 5:01pm"
                Edate = "Friday February 4th | 4:59pm"
                Sby = "Monday January 24th | 11:00pm"
                SbH = "Tuesday January 25th | 2:00pm"
                Acab = "Thursday January 27th | 10:00am"
                Aadhoc = "Thursday January 27th | 5:00pm"
                NSD = "Friday February 11th | 5:01pm"
                NED = "Friday February 18th | 4:59pm"
            if d == 11 or d == 12 or d == 13 or d == 14 or d == 15 or d == 16 or d == 17 or d == 18:
                Sdate = "Friday February 11th | 5:01pm"
                Edate = "Friday February 18th | 4:59pm"
                Sby = "Monday February 7th | 11:00pm"
                SbH = "Tuesday February 8th | 2:00pm"
                Acab = "Thursday February 10th | 10:00am"
                Aadhoc = "Thursday February 10th | 5:00pm"
                NSD = "Friday February 25th | 5:01pm"
                NED = "Friday March 4th | 4:59pm"
            if d == 25 or d == 26 or d == 27 or d == 28:
                Sdate = "Friday February 25th | 5:01pm"
                Edate = "Friday March 4th | 4:59pm"
                Sby = "Monday February 21st | 11:00pm"
                SbH = "Tuesday February 22nd | 2:00pm"
                Acab = "Thursday February 24th | 10:00am"
                Aadhoc = "Thursday February 24th | 5:00pm"
                NSD = "Friday March 11th | 5:01pm"
                NED = "Friday March 18th | 4:59pm"
        if m == 3:
            if d == 1 or d == 2 or d == 3 or d == 4:
                Sdate = "Friday February 25th | 5:01pm"
                Edate = "Friday March 4th | 4:59pm"
                Sby = "Monday February 21st | 11:00pm"
                SbH = "Tuesday February 22nd | 2:00pm"
                Acab = "Thursday February 24th | 10:00am"
                Aadhoc = "Thursday February 24th | 5:00pm"
                NSD = "Friday March 11th | 5:01pm"
                NED = "Friday March 18th | 4:59pm"
            if d == 11 or d == 12 or d == 13 or d == 14 or d == 15 or d == 16 or d == 17 or d == 18:
                Sdate = "Friday March 11th | 5:01pm"
                Edate = "Friday March 18th | 4:59pm"
                Sby = "Monday March 7th | 11:00pm"
                SbH = "Tuesday March 8th | 2:00pm"
                Acab = "Thursday March 10th | 10:00am"
                Aadhoc = "Thursday March 10th | 5:00pm"
                NSD = "Friday March 27th | 5:01pm"
                NED = "Friday April 1st | 4:59pm"
            if d == 27 or d == 28 or d == 29 or d == 30 or d == 31:
                Sdate = "Sunday March 27th | 5:01pm"
                Edate = "Friday April 1st | 4:59pm"
                Sby = "Monday March 21st | 11:00pm"
                SbH = "Tuesday March 22nd | 2:00pm"
                Acab = "Thursday March 24th | 10:00am"
                Aadhoc = "Thursday March 24th | 5:00pm"
                NSD = "Friday April 8th | 5:01pm"
                NED = "Friday April 13th | 4:59pm"
        if m == 4:
            if d == 1:
                Sdate = "Sunday March 27th | 5:01pm"
                Edate = "Friday April 1st | 4:59pm"
                Sby = "Monday March 21st | 11:00pm"
                SbH = "Tuesday March 22nd | 2:00pm"
                Acab = "Thursday March 24th | 10:00am"
                Aadhoc = "Thursday March 24th | 5:00pm"
                NSD = "Friday April 8th | 5:01pm"
                NED = "Friday April 13th | 4:59pm"
            if d == 8 or d == 9 or d == 10 or d == 11 or d == 12 or d == 13:
                Sdate = "Friday April 8th | 5:01pm"
                Edate = "Friday April 13th | 4:59pm"
                Sby = "Monday April 4th | 11:00pm"
                SbH = "Tuesday April 5th | 2:00pm"
                Acab = "Thursday April 7th | 10:00am"
                Aadhoc = "Thursday April 7th | 5:00pm"
                NSD = "Friday April 22nd | 5:01pm"
                NED = "Friday April 29th | 4:59pm"
            if d == 22 or d == 23 or d == 24 or d == 25 or d == 26 or d == 27 or d == 28 or d == 29:
                Sdate = "Friday April 22nd | 5:01pm"
                Edate = "Friday April 29th | 4:59pm"
                Sby = "Monday April 18th | 11:00pm"
                SbH = "Tuesday April 19th | 2:00pm"
                Acab = "Thursday April 21st | 10:00am"
                Aadhoc = "Thursday April 21st | 5:00pm"
                NSD = "Friday May 6th | 5:01pm"
                NED = "Friday May 13th | 4:59pm"
        if m == 5:
            if d == 6 or d == 7 or d == 8 or d == 9 or d == 10 or d == 11 or d == 12 or d == 13:
                Sdate = "Friday May 6th | 5:01pm"
                Edate = "Friday May 13th | 4:59pm"
                Sby = "Monday May 2nd | 11:00pm"
                SbH = "Tuesday May 3rd | 2:00pm"
                Acab = "Thursday May 5th | 10:00am"
                Aadhoc = "Thursday May 5th | 5:00pm"
                NSD = "Friday May 20th | 5:01pm"
                NED = "Friday May 27th | 4:59pm"
            if d == 20  or d == 21  or d == 22  or d == 23  or d == 24  or d == 25  or d == 26  or d == 27:
                Sdate = "Friday May 20th | 5:01pm"
                Edate = "Friday May 27th | 4:59pm"
                Sby = "Monday May 16th | 11:00pm"
                SbH = "Tuesday May 17th | 2:00pm"
                Acab = "Thursday May 19th | 10:00am"
                Aadhoc = "Thursday May 19th | 5:00pm"
                NSD = "Friday June 3rd | 5:01pm"
                NED = "Friday June 10th | 4:59pm"
        if m == 6:
            if d == 3 or d == 4 or d == 5 or d == 6 or d == 7 or d == 8 or d == 9 or d == 10:
                Sdate = "Friday June 3rd | 5:01pm"
                Edate = "Friday June 10th | 4:59pm"
                Sby = "Monday May 30th | 11:00pm"
                SbH = "Tuesday May 31st | 2:00pm"
                Acab = "Thursday June 2nd | 10:00am"
                Aadhoc = "Thursday June 2nd | 5:00pm"
                NSD = "Friday June 19th | 5:01pm"
                NED = "Friday June 24th | 4:59pm"
            if d == 19 or d == 20 or d == 21 or d == 22 or d == 23 or d == 24:
                Sdate = "Friday June 19th | 5:01pm"
                Edate = "Friday June 24th | 4:59pm"
                Sby = "Monday June 13th | 11:00pm"
                SbH = "Tuesday June 14th | 2:00pm"
                Acab = "Thursday June 16th | 10:00am"
                Aadhoc = "Thursday June 16th | 5:00pm"
                NSD = "Friday July 1st | 5:01pm"
                NED = "Friday July 8th | 4:59pm"
        if m == 7:
            if d == 1 or d == 2 or d == 3 or d == 4 or d == 5 or d == 6 or d == 7 or d == 8:
                Sdate = "Friday July 1st | 5:01pm"
                Edate = "Friday July 8th | 4:59pm"
                Sby = "Monday June 27th | 11:00pm"
                SbH = "Tuesday June 28th | 2:00pm"
                Acab = "Thursday June 30th | 10:00am"
                Aadhoc = "Thursday June 30th | 5:00pm"
                NSD = "Friday July 15th | 5:01pm"
                NED = "Friday July 22nd | 4:59pm"
            if d == 15 or d == 16 or d == 17 or d == 18 or d == 19 or d == 20 or d == 21 or d == 22:
                Sdate = "Friday July 15th | 5:01pm"
                Edate = "Friday July 22nd | 4:59pm"
                Sby = "Monday July 11th | 11:00pm"
                SbH = "Tuesday July 12th | 2:00pm"
                Acab = "Thursday July 14th | 10:00am"
                Aadhoc = "Thursday July 14th | 5:00pm"
                NSD = "Friday July 29th | 5:01pm"
                NED = "Friday August 5th | 4:59pm"
            if d == 29 or d == 30 or d == 31:
                Sdate = "Friday July 29th | 5:01pm"
                Edate = "Friday August 5th | 4:59pm"
                Sby = "Monday July 25th | 11:00pm"
                SbH = "Tuesday July 26th | 2:00pm"
                Acab = "Thursday July 28th | 10:00am"
                Aadhoc = "Thursday July 28th | 5:00pm"
                NSD = "Friday July 12th | 5:01pm"
                NED = "Friday August 19th | 4:59pm"
        if m == 8:
            if d == 1 or d == 2 or d == 3 or d == 4 or d == 5:
                Sdate = "Friday July 29th | 5:01pm"
                Edate = "Friday August 5th | 4:59pm"
                Sby = "Monday July 25th | 11:00pm"
                SbH = "Tuesday July 26th | 2:00pm"
                Acab = "Thursday July 28th | 10:00am"
                Aadhoc = "Thursday July 28th | 5:00pm"
                NSD = "Friday July 12th | 5:01pm"
                NED = "Friday August 19th | 4:59pm"
            if d == 12 or d == 13 or d == 14 or d == 15 or d == 16 or d == 17 or d == 18 or d == 19:
                Sdate = "Friday August 12th | 5:01pm"
                Edate = "Friday August 19th | 4:59pm"
                Sby = "Monday August 8th | 11:00pm"
                SbH = "Tuesday August 9th | 2:00pm"
                Acab = "Thursday August 11th | 10:00am"
                Aadhoc = "Thursday August 11th | 5:00pm"
                NSD = "Friday August 26th | 5:01pm"
                NED = "Friday September 2nd | 4:59pm"
            if d == 26 or d == 27 or d == 28 or d == 29 or d == 30 or d == 31:
                Sdate = "Friday August 26th | 5:01pm"
                Edate = "Friday September 2nd | 4:59pm"
                Sby = "Monday August 22nd | 11:00pm"
                SbH = "Tuesday August 23rd | 2:00pm"
                Acab = "Thursday August 25th | 10:00am"
                Aadhoc = "Thursday August 25th | 5:00pm"
                NSD = "Friday September 9th | 5:01pm"
                NED = "Friday September 16th | 4:59pm"
        if m == 9:
            if d == 1 or d == 2:
                Sdate = "Friday August 26th | 5:01pm"
                Edate = "Friday September 2nd | 4:59pm"
                Sby = "Monday August 22nd | 11:00pm"
                SbH = "Tuesday August 23rd | 2:00pm"
                Acab = "Thursday August 25th | 10:00am"
                Aadhoc = "Thursday August 25th | 5:00pm"
                NSD = "Friday September 9th | 5:01pm"
                NED = "Friday September 16th | 4:59pm"
            if d == 9 or d == 10 or d == 11 or d == 12 or d == 13 or d == 14 or d == 15 or d == 16:
                Sdate = "Friday September 9th | 5:01pm"
                Edate = "Friday September 26th | 4:59pm"
                Sby = "Monday September 5th | 11:00pm"
                SbH = "Tuesday September 6th | 2:00pm"
                Acab = "Thursday September 8th | 10:00am"
                Aadhoc = "Thursday September 8th | 5:00pm"
                NSD = "Friday September 23rd | 5:01pm"
                NED = "Friday September 30th | 4:59pm"
            if d == 23 or d == 24 or d == 25 or d == 26 or d == 27 or d == 28 or d == 29 or d == 30:
                Sdate = "Friday September 23rd | 5:01pm"
                Edate = "Friday September 30th | 4:59pm"
                Sby = "Monday September 19th | 11:00pm"
                SbH = "Tuesday September 20th | 2:00pm"
                Acab = "Thursday September 22nd | 10:00am"
                Aadhoc = "Thursday September 22nd | 5:00pm"
                NSD = "Friday October 14th | 5:01pm"
                NED = "Friday October 21st | 4:59pm"
        if m == 10:
            if d == 14 or d == 15 or d == 16 or d == 17 or d == 18 or d == 19 or d == 20 or d == 21:
                Sdate = "Friday October 14th | 5:01pm"
                Edate = "Friday October 21st | 4:59pm"
                Sby = "Monday October 10th | 11:00pm"
                SbH = "Tuesday October 11th | 2:00pm"
                Acab = "Thursday October 13th | 10:00am"
                Aadhoc = "Thursday October 13th | 5:00pm"
                NSD = "Friday October 28th | 5:01pm"
                NED = "Friday November 4th | 4:59pm"
            if d == 28  or d == 29 or d == 30 or d == 31:
                Sdate = "Friday October 28th | 5:01pm"
                Edate = "Friday November 4th | 4:59pm"
                Sby = "Monday October 24th | 11:00pm"
                SbH = "Tuesday October 25th | 2:00pm"
                Acab = "Thursday October 27th | 10:00am"
                Aadhoc = "Thursday October 27th | 5:00pm"
                NSD = "Friday November 11th | 5:01pm"
                NED = "Friday November 18th | 4:59pm"
        if m == 11:
            if d == 1 or d == 2 or d == 3 or d == 4:
                Sdate = "Friday October 28th | 5:01pm"
                Edate = "Friday November 4th | 4:59pm"
                Sby = "Monday October 24th | 11:00pm"
                SbH = "Tuesday October 25th | 2:00pm"
                Acab = "Thursday October 27th | 10:00am"
                Aadhoc = "Thursday October 27th | 5:00pm"
                NSD = "Friday November 11th | 5:01pm"
                NED = "Friday November 18th | 4:59pm"
            if d == 11 or d == 12 or d == 13 or d == 14 or d == 15 or d == 16 or d == 17 or d == 18:
                Sdate = "Friday November 11th | 5:01pm"
                Edate = "Friday November 18th | 4:59pm"
                Sby = "Monday November 7th | 11:00pm"
                SbH = "Tuesday November 8th | 2:00pm"
                Acab = "Thursday November 10th | 10:00am"
                Aadhoc = "Thursday November 10th | 5:00pm"
                NSD = "Friday December 2nd | 5:01pm"
                NED = "Friday December 9th | 4:59pm"
        if m == 12:
            if d == 2 or d == 3 or d == 4 or d == 5 or d == 6 or d == 7 or d == 8 or d == 9:
                Sdate = "Friday December 2nd | 5:01pm"
                Edate = "Friday December 9th | 4:59pm"
                Sby = "Monday November 28th | 11:00pm"
                SbH = "Tuesday November 29th | 2:00pm"
                Acab = "Thursday December 1st | 10:00am"
                Aadhoc = "Thursday December 1st | 5:00pm"
                NSD = "NA"
                NED = "NA"
            
    if t == "infrastructure":
        if m == 1:
            if d == 3 or d == 4 or d == 5 or d == 6 or d == 7:
                Sdate = "Monday January 3rd | 5:01pm"
                Edate = "Friday January 7th | 4:59pm"
                Sby = "Monday December 27th | 11:00pm"
                SbH = "Tuesday December 28nd | 2:00pm"
                Acab = "Thursday December 30th | 10:00am"
                Aadhoc = "Thursday December 30th | 5:00pm"
                NSD = "Friday January 7th | 5:01pm"
                NED = "Friday January 14th | 4:59pm"
            if d == 8 or d == 9 or d == 10 or d == 11 or d == 12 or d == 13 or d == 14:
                Sdate = "Friday January 7th | 5:01pm"
                Edate = "Friday January 14th | 4:59pm"
                Sby = "Monday January 3rd | 11:00pm"
                SbH = "Tuesday January 4th | 2:00pm"
                Acab = "Thursday January 6th | 10:00am"
                Aadhoc = "Thursday January 6th | 5:00pm"
                NSD = "Friday January 21st | 5:01pm"
                NED = "Friday January 28th | 4:59pm"
            if d == 21 or d == 22 or d == 23 or d == 24 or d == 25 or d == 26 or d == 27 or d == 28:
                Sdate = "Friday January 21st | 5:01pm"
                Edate = "Friday January 28th | 4:59pm"
                Sby = "Monday January 17th | 11:00pm"
                SbH = "Tuesday January 18th | 2:00pm"
                Acab = "Thursday January 20th | 10:00am"
                Aadhoc = "Thursday January 20th | 5:00pm"
                NSD = "Friday February 4th | 5:01pm"
                NED = "Friday February 11th | 4:59pm"
        if m == 2:
            if d == 4 or d == 5 or d == 6 or d == 7 or d == 8 or d == 9 or d == 10 or d == 11:
                Sdate = "Friday February 4st | 5:01pm"
                Edate = "Friday February 11th | 4:59pm"
                Sby = "Monday January 31st | 11:00pm"
                SbH = "Tuesday February 1st | 2:00pm"
                Acab = "Thursday February 3rd | 10:00am"
                Aadhoc = "Thursday February 3rd | 5:00pm"
                NSD = "Friday February 18th | 5:01pm"
                NED = "Friday February 25th | 4:59pm"
            if d == 18 or d == 19 or d == 20 or d == 21 or d == 22 or d == 23 or d == 24 or d == 25:
                Sdate = "Friday February 18th | 5:01pm"
                Edate = "Friday February 25th | 4:59pm"
                Sby = "Monday February 14st | 11:00pm"
                SbH = "Tuesday February 15th | 2:00pm"
                Acab = "Thursday February 17th | 10:00am"
                Aadhoc = "Thursday February 17th | 5:00pm"
                NSD = "Friday March 4th | 5:01pm"
                NED = "Friday March 11th | 4:59pm"
        if m == 3:
            if d == 4 or d == 5 or d == 6 or d == 7 or d == 8 or d == 9 or d == 10 or d == 11:
                Sdate = "Friday March 4th | 5:01pm"
                Edate = "Friday March 11th | 4:59pm"
                Sby = "Monday February 28th | 11:00pm"
                SbH = "Tuesday March 1st | 2:00pm"
                Acab = "Thursday March 3rd | 10:00am"
                Aadhoc = "Thursday March 3rd | 5:00pm"
                NSD = "Friday March 18th | 5:01pm"
                NED = "Friday March 25th | 4:59pm"
            if d == 18 or d == 19 or d == 20 or d == 21 or d == 22 or d == 23 or d == 24 or d == 25:
                Sdate = "Friday March 18th | 5:01pm"
                Edate = "Friday March 25th | 4:59pm"
                Sby = "Monday March 14th | 11:00pm"
                SbH = "Tuesday March 15th | 2:00pm"
                Acab = "Thursday March 17th | 10:00am"
                Aadhoc = "Thursday March 17th | 5:00pm"
                NSD = "Friday April 1st | 5:01pm"
                NED = "Friday April 8th | 4:59pm"
        if m == 4:
            if d == 1 or d == 2 or d == 3 or d == 4 or d == 5 or d == 6 or d == 7 or d == 8:
                Sdate = "Friday April 1st | 5:01pm"
                Edate = "Friday April 8th | 4:59pm"
                Sby = "Monday March 28th | 11:00pm"
                SbH = "Tuesday March 29th | 2:00pm"
                Acab = "Thursday March 31th | 10:00am"
                Aadhoc = "Thursday March 31th | 5:00pm"
                NSD = "Friday April 29th | 5:01pm"
                NED = "Friday May 6th | 4:59pm"
            if d == 29 or d == 30:
                Sdate = "Friday April 29th | 5:01pm"
                Edate = "Friday May 6th | 4:59pm"
                Sby = "Monday April 25th | 11:00pm"
                SbH = "Tuesday April 26th | 2:00pm"
                Acab = "Thursday April 28th | 10:00am"
                Aadhoc = "Thursday April 28th | 5:00pm"
                NSD = "Friday May 13th | 5:01pm"
                NED = "Friday May 20th | 4:59pm"
        if m == 5:
            if d == 1 or d == 2 or d == 3 or d == 4 or d == 5 or d == 6:
                Sdate = "Friday April 29th | 5:01pm"
                Edate = "Friday May 6th | 4:59pm"
                Sby = "Monday April 25th | 11:00pm"
                SbH = "Tuesday April 26th | 2:00pm"
                Acab = "Thursday April 28th | 10:00am"
                Aadhoc = "Thursday April 28th | 5:00pm"
                NSD = "Friday May 13th | 5:01pm"
                NED = "Friday May 20th | 4:59pm"
            if d == 13 or d == 14 or d == 15 or d == 16 or d == 17 or d == 18 or d == 19 or d == 20:
                Sdate = "Friday May 13th | 5:01pm"
                Edate = "Friday May 20th | 4:59pm"
                Sby = "Monday May 9th | 11:00pm"
                SbH = "Tuesday May 10th | 2:00pm"
                Acab = "Thursday May 12th | 10:00am"
                Aadhoc = "Thursday May 12th | 5:00pm"
                NSD = "Friday May 27th | 5:01pm"
                NED = "Friday June 3rd | 4:59pm"
            if d == 27 or d == 28 or d == 29 or d == 30 or d == 31:
                Sdate = "Friday May 27th | 5:01pm"
                Edate = "Friday June 3rd | 4:59pm"
                Sby = "Monday May 23rd | 11:00pm"
                SbH = "Tuesday May 24th | 2:00pm"
                Acab = "Thursday May 26th | 10:00am"
                Aadhoc = "Thursday May 26th | 5:00pm"
                NSD = "Friday June 10th | 5:01pm"
                NED = "Friday June 17th | 4:59pm"
        if m == 6:
            if d == 1 or d == 2 or d == 3:
                Sdate = "Friday May 27th | 5:01pm"
                Edate = "Friday June 3rd | 4:59pm"
                Sby = "Monday May 23rd | 11:00pm"
                SbH = "Tuesday May 24th | 2:00pm"
                Acab = "Thursday May 26th | 10:00am"
                Aadhoc = "Thursday May 26th | 5:00pm"
                NSD = "Friday June 10th | 5:01pm"
                NED = "Friday June 17th | 4:59pm"
            if d == 10 or d == 11 or d == 12 or d == 13 or d == 14 or d == 15 or d == 16 or d == 17:
                Sdate = "Friday June 10th | 5:01pm"
                Edate = "Friday June 17th | 4:59pm"
                Sby = "Monday June 6th | 11:00pm"
                SbH = "Tuesday June 7th | 2:00pm"
                Acab = "Thursday June 16th | 10:00am"
                Aadhoc = "Thursday June 16th | 5:00pm"
                NSD = "Friday June 24th | 5:01pm"
                NED = "Friday July 1st | 4:59pm"
            if d == 24 or d == 25 or d == 26 or d == 27 or d == 28 or d == 29 or d == 30:
                Sdate = "Friday June 24th | 5:01pm"
                Edate = "Friday July 1st | 4:59pm"
                Sby = "Monday June 20th | 11:00pm"
                SbH = "Tuesday June 21st | 2:00pm"
                Acab = "Thursday June 23rd | 10:00am"
                Aadhoc = "Thursday June 23rd | 5:00pm"
                NSD = "Friday July 8th | 5:01pm"
                NED = "Friday July 15th | 4:59pm"
        if m == 7:
            if d == 1:
                Sdate = "Friday June 24th | 5:01pm"
                Edate = "Friday July 1st | 4:59pm"
                Sby = "Monday June 20th | 11:00pm"
                SbH = "Tuesday June 21st | 2:00pm"
                Acab = "Thursday June 23rd | 10:00am"
                Aadhoc = "Thursday June 23rd | 5:00pm"
                NSD = "Friday July 8th | 5:01pm"
                NED = "Friday July 15th | 4:59pm"
            if d == 8 or d == 9 or d == 10 or d == 11 or d == 12 or d == 13 or d == 14 or d == 15:
                Sdate = "Friday July 8th | 5:01pm"
                Edate = "Friday July 15th | 4:59pm"
                Sby = "Monday July 4th | 11:00pm"
                SbH = "Tuesday July 5th | 2:00pm"
                Acab = "Thursday July 7th | 10:00am"
                Aadhoc = "Thursday July 7th | 5:00pm"
                NSD = "Friday July 22nd | 5:01pm"
                NED = "Friday July 29th | 4:59pm"
            if d == 22 or d == 23 or d == 24 or d == 25 or d == 26 or d == 27 or d == 28 or d == 29:
                Sdate = "Friday July 22nd | 5:01pm"
                Edate = "Friday July 29th | 4:59pm"
                Sby = "Monday July 18th | 11:00pm"
                SbH = "Tuesday July 19th | 2:00pm"
                Acab = "Thursday July 21st | 10:00am"
                Aadhoc = "Thursday July 21st | 5:00pm"
                NSD = "Friday August 5th | 5:01pm"
                NED = "Friday August 12th | 4:59pm"
        if m == 8:
            if d == 5 or d == 6 or d == 7 or d == 8 or d == 9 or d == 10 or d == 11 or d == 12:
                Sdate = "Friday August 5th | 5:01pm"
                Edate = "Friday August 12th | 4:59pm"
                Sby = "Monday August 1st | 11:00pm"
                SbH = "Tuesday August 2nd | 2:00pm"
                Acab = "Thursday August 4th | 10:00am"
                Aadhoc = "Thursday August 4th | 5:00pm"
                NSD = "Friday August 19th | 5:01pm"
                NED = "Friday August 26th | 4:59pm"
            if d == 19 or d == 20 or d == 21 or d == 22 or d == 23 or d == 24 or d == 25 or d == 26:
                Sdate = "Friday August 19th | 5:01pm"
                Edate = "Friday August 26th | 4:59pm"
                Sby = "Monday August 15th | 11:00pm"
                SbH = "Tuesday August 16th | 2:00pm"
                Acab = "Thursday August 18th | 10:00am"
                Aadhoc = "Thursday August 18th | 5:00pm"
                NSD = "Friday September 2nd | 5:01pm"
                NED = "Friday September 9th | 4:59pm"
        if m == 9:
            if d == 2 or d == 3 or d == 4 or d == 5 or d == 6 or d == 7 or d == 8 or d == 9:
                Sdate = "Friday September 2nd | 5:01pm"
                Edate = "Friday September 9th | 4:59pm"
                Sby = "Monday August 29th | 11:00pm"
                SbH = "Tuesday August 30th | 2:00pm"
                Acab = "Thursday September 1st | 10:00am"
                Aadhoc = "Thursday September 1st | 5:00pm"
                NSD = "Friday September 16th | 5:01pm"
                NED = "Friday September 23rd | 4:59pm"
            if d == 16 or d == 17 or d == 18 or d == 19 or d == 20 or d == 21 or d == 22 or d == 23:
                Sdate = "Friday September 16th | 5:01pm"
                Edate = "Friday September 23rd | 4:59pm"
                Sby = "Monday September 12th | 11:00pm"
                SbH = "Tuesday September 13th | 2:00pm"
                Acab = "Thursday September 15th | 10:00am"
                Aadhoc = "Thursday September 15th | 5:00pm"
                NSD = "Friday September 30th | 5:01pm"
                NED = "Friday October 5th | 4:59pm"
            if d == 30:
                Sdate = "Friday September 30th | 5:01pm"
                Edate = "Friday October 5th | 4:59pm"
                Sby = "Monday September 26th | 11:00pm"
                SbH = "Tuesday September 27th | 2:00pm"
                Acab = "Thursday September 29th | 10:00am"
                Aadhoc = "Thursday September 29th | 5:00pm"
                NSD = "Friday October 21st | 5:01pm"
                NED = "Friday October 28th | 4:59pm"
        if m == 10:
            if d == 1 or d == 2 or d == 3 or d == 4 or d == 5:
                Sdate = "Friday September 30th | 5:01pm"
                Edate = "Friday October 5th | 4:59pm"
                Sby = "Monday September 26th | 11:00pm"
                SbH = "Tuesday September 27th | 2:00pm"
                Acab = "Thursday September 29th | 10:00am"
                Aadhoc = "Thursday September 29th | 5:00pm"
                NSD = "Friday October 21st | 5:01pm"
                NED = "Friday October 28th | 4:59pm"
            if d == 21 or d == 22 or d == 23 or d == 24 or d == 25 or d == 26 or d == 27 or d == 28:
                Sdate = "Friday October 21st | 5:01pm"
                Edate = "Friday October 28th | 4:59pm"
                Sby = "Monday October 17th | 11:00pm"
                SbH = "Tuesday October 18th | 2:00pm"
                Acab = "Thursday October 20th | 10:00am"
                Aadhoc = "Thursday October 20th | 5:00pm"
                NSD = "Friday November 4th | 5:01pm"
                NED = "Friday November 11th | 4:59pm"
        if m == 11:
            if d == 4 or d == 5 or d == 6 or d == 7 or d == 8 or d == 9 or 10 == 4 or d == 11:
                Sdate = "Friday November 4th | 5:01pm"
                Edate = "Friday November 11th | 4:59pm"
                Sby = "Monday October 31st | 11:00pm"
                SbH = "Tuesday November 1st | 2:00pm"
                Acab = "Thursday November 3rd | 10:00am"
                Aadhoc = "Thursday November 3rd | 5:00pm"
                NSD = "Friday November 18th | 5:01pm"
                NED = "Friday November 23rd | 4:59pm"
            if d == 18 or d == 19 or d == 20 or d == 21 or d == 22 or d == 23:
                Sdate = "Friday November 18th | 5:01pm"
                Edate = "Friday November 23th | 4:59pm"
                Sby = "Monday November 14th | 11:00pm"
                SbH = "Tuesday November 15th | 2:00pm"
                Acab = "Thursday November 17th | 10:00am"
                Aadhoc = "Thursday November 17th | 5:00pm"
                NSD = "Friday December 9th | 5:01pm"
                NED = "Friday December 16th | 4:59pm"
        if m == 12:
            if d == 9 or d == 10 or d == 11 or d == 12 or d == 13 or d == 14 or d == 15 or d == 16:
                Sdate = "Friday December 9th | 5:01pm"
                Edate = "Friday December 16th | 4:59pm"
                Sby = "Monday December 5th | 11:00pm"
                SbH = "Tuesday December 6th | 2:00pm"
                Acab = "Thursday December 8th | 10:00am"
                Aadhoc = "Thursday December 8th | 5:00pm"
                NSD = "NA"
                NED = "NA"
                
    outputL.config(text="The closest " + t + " release week for a Normal Change will begin on " + Sdate + " and end on " + Edate
                    + ".\n\n Please ensure the following tasks are completed on time:\n\nSubmit the CRQ in Authorize state by: " + Sby + ".")
    outputM.config(text="NOTE:")
    outputN.config(text="If Monday is a statutory holiday, then submit by: " + SbH + ".")

    outputO.config(text="Attend CAB meeting (if required) on: " + Acab + ".\nAcquire AD-Hoc approval by: " + Aadhoc + ".")
    outputP.config(text="NOTE:")
    outputQ.config(text="If the approvals are not granted in time, the CRQ will be auto-rejected.")
    if m == 12:
        outputR.config(text="                           Implementation of the change can begin on: " + Sdate + ".\n                 Implementation of the change must be completed by: " + Edate + ".\n\n                         The next release will begin on the next week in January Year 2023.")
    else:
        outputR.config(text="Implementation of the change can begin on: " + Sdate + ".\nImplementation of the change must be completed by: " + Edate + ".\n\nThe next " + t + " week will begin on " + NSD + " and end on " + NED + ".")
        
#######################################################################################################################################################################################################################################################################################################################

def reenable():
    outputL.config(text="")
    outputM.config(text="")
    outputN.config(text="")
    outputO.config(text="")
    outputP.config(text="")
    outputQ.config(text="")
    outputR.config(text="")
    
    J1.config(command="", state=NORMAL, bg="#ffffff")
    J2.config(command="", state=NORMAL, bg="#ffffff")
    J3.config(command="", state=NORMAL, bg="#ffffff")
    J4.config(command="", state=NORMAL, bg="#ffffff")
    J4.config(command="", state=NORMAL, bg="#ffffff")
    J5.config(command="", state=NORMAL, bg="#ffffff")
    J6.config(command="", state=NORMAL, bg="#ffffff")
    J7.config(command="", state=NORMAL, bg="#ffffff")
    J8.config(command="", state=NORMAL, bg="#ffffff")
    J9.config(command="", state=NORMAL, bg="#ffffff")
    J10.config(command="", state=NORMAL, bg="#ffffff")
    J11.config(command="", state=NORMAL, bg="#ffffff")
    J12.config(command="", state=NORMAL, bg="#ffffff")
    J13.config(command="", state=NORMAL, bg="#ffffff")
    J14.config(command="", state=NORMAL, bg="#ffffff")
    J15.config(command="", state=NORMAL, bg="#ffffff")
    J16.config(command="", state=NORMAL, bg="#ffffff")
    J17.config(command="", state=NORMAL, bg="#ffffff")
    J18.config(command="", state=NORMAL, bg="#ffffff")
    J19.config(command="", state=NORMAL, bg="#ffffff")
    J20.config(command="", state=NORMAL, bg="#ffffff")
    J21.config(command="", state=NORMAL, bg="#ffffff")
    J22.config(command="", state=NORMAL, bg="#ffffff")
    J23.config(command="", state=NORMAL, bg="#ffffff")
    J24.config(command="", state=NORMAL, bg="#ffffff")
    J25.config(command="", state=NORMAL, bg="#ffffff")
    J26.config(command="", state=NORMAL, bg="#ffffff")
    J27.config(command="", state=NORMAL, bg="#ffffff")
    J28.config(command="", state=NORMAL, bg="#ffffff")
    J29.config(command="", state=NORMAL, bg="#ffffff")
    J30.config(command="", state=NORMAL, bg="#ffffff")
    J31.config(command="", state=NORMAL, bg="#ffffff")

    F1.config(command="", state=NORMAL, bg="#ffffff")
    F2.config(command="", state=NORMAL, bg="#ffffff")
    F3.config(command="", state=NORMAL, bg="#ffffff")
    F4.config(command="", state=NORMAL, bg="#ffffff")
    F4.config(command="", state=NORMAL, bg="#ffffff")
    F5.config(command="", state=NORMAL, bg="#ffffff")
    F6.config(command="", state=NORMAL, bg="#ffffff")
    F7.config(command="", state=NORMAL, bg="#ffffff")
    F8.config(command="", state=NORMAL, bg="#ffffff")
    F9.config(command="", state=NORMAL, bg="#ffffff")
    F10.config(command="", state=NORMAL, bg="#ffffff")
    F11.config(command="", state=NORMAL, bg="#ffffff")
    F12.config(command="", state=NORMAL, bg="#ffffff")
    F13.config(command="", state=NORMAL, bg="#ffffff")
    F14.config(command="", state=NORMAL, bg="#ffffff")
    F15.config(command="", state=NORMAL, bg="#ffffff")
    F16.config(command="", state=NORMAL, bg="#ffffff")
    F17.config(command="", state=NORMAL, bg="#ffffff")
    F18.config(command="", state=NORMAL, bg="#ffffff")
    F19.config(command="", state=NORMAL, bg="#ffffff")
    F20.config(command="", state=NORMAL, bg="#ffffff")
    F21.config(command="", state=NORMAL, bg="#ffffff")
    F22.config(command="", state=NORMAL, bg="#ffffff")
    F23.config(command="", state=NORMAL, bg="#ffffff")
    F24.config(command="", state=NORMAL, bg="#ffffff")
    F25.config(command="", state=NORMAL, bg="#ffffff")
    F26.config(command="", state=NORMAL, bg="#ffffff")
    F27.config(command="", state=NORMAL, bg="#ffffff")
    F28.config(command="", state=NORMAL, bg="#ffffff")

    M1.config(command="", state=NORMAL, bg="#ffffff")
    M2.config(command="", state=NORMAL, bg="#ffffff")
    M3.config(command="", state=NORMAL, bg="#ffffff")
    M4.config(command="", state=NORMAL, bg="#ffffff")
    M4.config(command="", state=NORMAL, bg="#ffffff")
    M5.config(command="", state=NORMAL, bg="#ffffff")
    M6.config(command="", state=NORMAL, bg="#ffffff")
    M7.config(command="", state=NORMAL, bg="#ffffff")
    M8.config(command="", state=NORMAL, bg="#ffffff")
    M9.config(command="", state=NORMAL, bg="#ffffff")
    M10.config(command="", state=NORMAL, bg="#ffffff")
    M11.config(command="", state=NORMAL, bg="#ffffff")
    M12.config(command="", state=NORMAL, bg="#ffffff")
    M13.config(command="", state=NORMAL, bg="#ffffff")
    M14.config(command="", state=NORMAL, bg="#ffffff")
    M15.config(command="", state=NORMAL, bg="#ffffff")
    M16.config(command="", state=NORMAL, bg="#ffffff")
    M17.config(command="", state=NORMAL, bg="#ffffff")
    M18.config(command="", state=NORMAL, bg="#ffffff")
    M19.config(command="", state=NORMAL, bg="#ffffff")
    M20.config(command="", state=NORMAL, bg="#ffffff")
    M21.config(command="", state=NORMAL, bg="#ffffff")
    M22.config(command="", state=NORMAL, bg="#ffffff")
    M23.config(command="", state=NORMAL, bg="#ffffff")
    M24.config(command="", state=NORMAL, bg="#ffffff")
    M25.config(command="", state=NORMAL, bg="#ffffff")
    M26.config(command="", state=NORMAL, bg="#ffffff")
    M27.config(command="", state=NORMAL, bg="#ffffff")
    M28.config(command="", state=NORMAL, bg="#ffffff")
    M29.config(command="", state=NORMAL, bg="#ffffff")
    M30.config(command="", state=NORMAL, bg="#ffffff")
    M31.config(command="", state=NORMAL, bg="#ffffff")

    A1.config(command="", state=NORMAL, bg="#ffffff")
    A2.config(command="", state=NORMAL, bg="#ffffff")
    A3.config(command="", state=NORMAL, bg="#ffffff")
    A4.config(command="", state=NORMAL, bg="#ffffff")
    A4.config(command="", state=NORMAL, bg="#ffffff")
    A5.config(command="", state=NORMAL, bg="#ffffff")
    A6.config(command="", state=NORMAL, bg="#ffffff")
    A7.config(command="", state=NORMAL, bg="#ffffff")
    A8.config(command="", state=NORMAL, bg="#ffffff")
    A9.config(command="", state=NORMAL, bg="#ffffff")
    A10.config(command="", state=NORMAL, bg="#ffffff")
    A11.config(command="", state=NORMAL, bg="#ffffff")
    A12.config(command="", state=NORMAL, bg="#ffffff")
    A13.config(command="", state=NORMAL, bg="#ffffff")
    A14.config(command="", state=NORMAL, bg="#ffffff")
    A15.config(command="", state=NORMAL, bg="#ffffff")
    A16.config(command="", state=NORMAL, bg="#ffffff")
    A17.config(command="", state=NORMAL, bg="#ffffff")
    A18.config(command="", state=NORMAL, bg="#ffffff")
    A19.config(command="", state=NORMAL, bg="#ffffff")
    A20.config(command="", state=NORMAL, bg="#ffffff")
    A21.config(command="", state=NORMAL, bg="#ffffff")
    A22.config(command="", state=NORMAL, bg="#ffffff")
    A23.config(command="", state=NORMAL, bg="#ffffff")
    A24.config(command="", state=NORMAL, bg="#ffffff")
    A25.config(command="", state=NORMAL, bg="#ffffff")
    A26.config(command="", state=NORMAL, bg="#ffffff")
    A27.config(command="", state=NORMAL, bg="#ffffff")
    A28.config(command="", state=NORMAL, bg="#ffffff")
    A29.config(command="", state=NORMAL, bg="#ffffff")
    A30.config(command="", state=NORMAL, bg="#ffffff")

    MA1.config(command="", state=NORMAL, bg="#ffffff")
    MA2.config(command="", state=NORMAL, bg="#ffffff")
    MA3.config(command="", state=NORMAL, bg="#ffffff")
    MA4.config(command="", state=NORMAL, bg="#ffffff")
    MA4.config(command="", state=NORMAL, bg="#ffffff")
    MA5.config(command="", state=NORMAL, bg="#ffffff")
    MA6.config(command="", state=NORMAL, bg="#ffffff")
    MA7.config(command="", state=NORMAL, bg="#ffffff")
    MA8.config(command="", state=NORMAL, bg="#ffffff")
    MA9.config(command="", state=NORMAL, bg="#ffffff")
    MA10.config(command="", state=NORMAL, bg="#ffffff")
    MA11.config(command="", state=NORMAL, bg="#ffffff")
    MA12.config(command="", state=NORMAL, bg="#ffffff")
    MA13.config(command="", state=NORMAL, bg="#ffffff")
    MA14.config(command="", state=NORMAL, bg="#ffffff")
    MA15.config(command="", state=NORMAL, bg="#ffffff")
    MA16.config(command="", state=NORMAL, bg="#ffffff")
    MA17.config(command="", state=NORMAL, bg="#ffffff")
    MA18.config(command="", state=NORMAL, bg="#ffffff")
    MA19.config(command="", state=NORMAL, bg="#ffffff")
    MA20.config(command="", state=NORMAL, bg="#ffffff")
    MA21.config(command="", state=NORMAL, bg="#ffffff")
    MA22.config(command="", state=NORMAL, bg="#ffffff")
    MA23.config(command="", state=NORMAL, bg="#ffffff")
    MA24.config(command="", state=NORMAL, bg="#ffffff")
    MA25.config(command="", state=NORMAL, bg="#ffffff")
    MA26.config(command="", state=NORMAL, bg="#ffffff")
    MA27.config(command="", state=NORMAL, bg="#ffffff")
    MA28.config(command="", state=NORMAL, bg="#ffffff")
    MA29.config(command="", state=NORMAL, bg="#ffffff")
    MA30.config(command="", state=NORMAL, bg="#ffffff")
    MA31.config(command="", state=NORMAL, bg="#ffffff")

    JU1.config(command="", state=NORMAL, bg="#ffffff")
    JU2.config(command="", state=NORMAL, bg="#ffffff")
    JU3.config(command="", state=NORMAL, bg="#ffffff")
    JU4.config(command="", state=NORMAL, bg="#ffffff")
    JU4.config(command="", state=NORMAL, bg="#ffffff")
    JU5.config(command="", state=NORMAL, bg="#ffffff")
    JU6.config(command="", state=NORMAL, bg="#ffffff")
    JU7.config(command="", state=NORMAL, bg="#ffffff")
    JU8.config(command="", state=NORMAL, bg="#ffffff")
    JU9.config(command="", state=NORMAL, bg="#ffffff")
    JU10.config(command="", state=NORMAL, bg="#ffffff")
    JU11.config(command="", state=NORMAL, bg="#ffffff")
    JU12.config(command="", state=NORMAL, bg="#ffffff")
    JU13.config(command="", state=NORMAL, bg="#ffffff")
    JU14.config(command="", state=NORMAL, bg="#ffffff")
    JU15.config(command="", state=NORMAL, bg="#ffffff")
    JU16.config(command="", state=NORMAL, bg="#ffffff")
    JU17.config(command="", state=NORMAL, bg="#ffffff")
    JU18.config(command="", state=NORMAL, bg="#ffffff")
    JU19.config(command="", state=NORMAL, bg="#ffffff")
    JU20.config(command="", state=NORMAL, bg="#ffffff")
    JU21.config(command="", state=NORMAL, bg="#ffffff")
    JU22.config(command="", state=NORMAL, bg="#ffffff")
    JU23.config(command="", state=NORMAL, bg="#ffffff")
    JU24.config(command="", state=NORMAL, bg="#ffffff")
    JU25.config(command="", state=NORMAL, bg="#ffffff")
    JU26.config(command="", state=NORMAL, bg="#ffffff")
    JU27.config(command="", state=NORMAL, bg="#ffffff")
    JU28.config(command="", state=NORMAL, bg="#ffffff")
    JU29.config(command="", state=NORMAL, bg="#ffffff")
    JU30.config(command="", state=NORMAL, bg="#ffffff")

    JUL1.config(command="", state=NORMAL, bg="#ffffff")
    JUL2.config(command="", state=NORMAL, bg="#ffffff")
    JUL3.config(command="", state=NORMAL, bg="#ffffff")
    JUL4.config(command="", state=NORMAL, bg="#ffffff")
    JUL4.config(command="", state=NORMAL, bg="#ffffff")
    JUL5.config(command="", state=NORMAL, bg="#ffffff")
    JUL6.config(command="", state=NORMAL, bg="#ffffff")
    JUL7.config(command="", state=NORMAL, bg="#ffffff")
    JUL8.config(command="", state=NORMAL, bg="#ffffff")
    JUL9.config(command="", state=NORMAL, bg="#ffffff")
    JUL10.config(command="", state=NORMAL, bg="#ffffff")
    JUL11.config(command="", state=NORMAL, bg="#ffffff")
    JUL12.config(command="", state=NORMAL, bg="#ffffff")
    JUL13.config(command="", state=NORMAL, bg="#ffffff")
    JUL14.config(command="", state=NORMAL, bg="#ffffff")
    JUL15.config(command="", state=NORMAL, bg="#ffffff")
    JUL16.config(command="", state=NORMAL, bg="#ffffff")
    JUL17.config(command="", state=NORMAL, bg="#ffffff")
    JUL18.config(command="", state=NORMAL, bg="#ffffff")
    JUL19.config(command="", state=NORMAL, bg="#ffffff")
    JUL20.config(command="", state=NORMAL, bg="#ffffff")
    JUL21.config(command="", state=NORMAL, bg="#ffffff")
    JUL22.config(command="", state=NORMAL, bg="#ffffff")
    JUL23.config(command="", state=NORMAL, bg="#ffffff")
    JUL24.config(command="", state=NORMAL, bg="#ffffff")
    JUL25.config(command="", state=NORMAL, bg="#ffffff")
    JUL26.config(command="", state=NORMAL, bg="#ffffff")
    JUL27.config(command="", state=NORMAL, bg="#ffffff")
    JUL28.config(command="", state=NORMAL, bg="#ffffff")
    JUL29.config(command="", state=NORMAL, bg="#ffffff")
    JUL30.config(command="", state=NORMAL, bg="#ffffff")
    JUL31.config(command="", state=NORMAL, bg="#ffffff")

    AU1.config(command="", state=NORMAL, bg="#ffffff")
    AU2.config(command="", state=NORMAL, bg="#ffffff")
    AU3.config(command="", state=NORMAL, bg="#ffffff")
    AU4.config(command="", state=NORMAL, bg="#ffffff")
    AU4.config(command="", state=NORMAL, bg="#ffffff")
    AU5.config(command="", state=NORMAL, bg="#ffffff")
    AU6.config(command="", state=NORMAL, bg="#ffffff")
    AU7.config(command="", state=NORMAL, bg="#ffffff")
    AU8.config(command="", state=NORMAL, bg="#ffffff")
    AU9.config(command="", state=NORMAL, bg="#ffffff")
    AU10.config(command="", state=NORMAL, bg="#ffffff")
    AU11.config(command="", state=NORMAL, bg="#ffffff")
    AU12.config(command="", state=NORMAL, bg="#ffffff")
    AU13.config(command="", state=NORMAL, bg="#ffffff")
    AU14.config(command="", state=NORMAL, bg="#ffffff")
    AU15.config(command="", state=NORMAL, bg="#ffffff")
    AU16.config(command="", state=NORMAL, bg="#ffffff")
    AU17.config(command="", state=NORMAL, bg="#ffffff")
    AU18.config(command="", state=NORMAL, bg="#ffffff")
    AU19.config(command="", state=NORMAL, bg="#ffffff")
    AU20.config(command="", state=NORMAL, bg="#ffffff")
    AU21.config(command="", state=NORMAL, bg="#ffffff")
    AU22.config(command="", state=NORMAL, bg="#ffffff")
    AU23.config(command="", state=NORMAL, bg="#ffffff")
    AU24.config(command="", state=NORMAL, bg="#ffffff")
    AU25.config(command="", state=NORMAL, bg="#ffffff")
    AU26.config(command="", state=NORMAL, bg="#ffffff")
    AU27.config(command="", state=NORMAL, bg="#ffffff")
    AU28.config(command="", state=NORMAL, bg="#ffffff")
    AU29.config(command="", state=NORMAL, bg="#ffffff")
    AU30.config(command="", state=NORMAL, bg="#ffffff")
    AU31.config(command="", state=NORMAL, bg="#ffffff")

    S1.config(command="", state=NORMAL, bg="#ffffff")
    S2.config(command="", state=NORMAL, bg="#ffffff")
    S3.config(command="", state=NORMAL, bg="#ffffff")
    S4.config(command="", state=NORMAL, bg="#ffffff")
    S4.config(command="", state=NORMAL, bg="#ffffff")
    S5.config(command="", state=NORMAL, bg="#ffffff")
    S6.config(command="", state=NORMAL, bg="#ffffff")
    S7.config(command="", state=NORMAL, bg="#ffffff")
    S8.config(command="", state=NORMAL, bg="#ffffff")
    S9.config(command="", state=NORMAL, bg="#ffffff")
    S10.config(command="", state=NORMAL, bg="#ffffff")
    S11.config(command="", state=NORMAL, bg="#ffffff")
    S12.config(command="", state=NORMAL, bg="#ffffff")
    S13.config(command="", state=NORMAL, bg="#ffffff")
    S14.config(command="", state=NORMAL, bg="#ffffff")
    S15.config(command="", state=NORMAL, bg="#ffffff")
    S16.config(command="", state=NORMAL, bg="#ffffff")
    S17.config(command="", state=NORMAL, bg="#ffffff")
    S18.config(command="", state=NORMAL, bg="#ffffff")
    S19.config(command="", state=NORMAL, bg="#ffffff")
    S20.config(command="", state=NORMAL, bg="#ffffff")
    S21.config(command="", state=NORMAL, bg="#ffffff")
    S22.config(command="", state=NORMAL, bg="#ffffff")
    S23.config(command="", state=NORMAL, bg="#ffffff")
    S24.config(command="", state=NORMAL, bg="#ffffff")
    S25.config(command="", state=NORMAL, bg="#ffffff")
    S26.config(command="", state=NORMAL, bg="#ffffff")
    S27.config(command="", state=NORMAL, bg="#ffffff")
    S28.config(command="", state=NORMAL, bg="#ffffff")
    S29.config(command="", state=NORMAL, bg="#ffffff")
    S30.config(command="", state=NORMAL, bg="#ffffff")

    O1.config(command="", state=NORMAL, bg="#ffffff")
    O2.config(command="", state=NORMAL, bg="#ffffff")
    O3.config(command="", state=NORMAL, bg="#ffffff")
    O4.config(command="", state=NORMAL, bg="#ffffff")
    O4.config(command="", state=NORMAL, bg="#ffffff")
    O5.config(command="", state=NORMAL, bg="#ffffff")
    O6.config(command="", state=NORMAL, bg="#ffffff")
    O7.config(command="", state=NORMAL, bg="#ffffff")
    O8.config(command="", state=NORMAL, bg="#ffffff")
    O9.config(command="", state=NORMAL, bg="#ffffff")
    O10.config(command="", state=NORMAL, bg="#ffffff")
    O11.config(command="", state=NORMAL, bg="#ffffff")
    O12.config(command="", state=NORMAL, bg="#ffffff")
    O13.config(command="", state=NORMAL, bg="#ffffff")
    O14.config(command="", state=NORMAL, bg="#ffffff")
    O15.config(command="", state=NORMAL, bg="#ffffff")
    O16.config(command="", state=NORMAL, bg="#ffffff")
    O17.config(command="", state=NORMAL, bg="#ffffff")
    O18.config(command="", state=NORMAL, bg="#ffffff")
    O19.config(command="", state=NORMAL, bg="#ffffff")
    O20.config(command="", state=NORMAL, bg="#ffffff")
    O21.config(command="", state=NORMAL, bg="#ffffff")
    O22.config(command="", state=NORMAL, bg="#ffffff")
    O23.config(command="", state=NORMAL, bg="#ffffff")
    O24.config(command="", state=NORMAL, bg="#ffffff")
    O25.config(command="", state=NORMAL, bg="#ffffff")
    O26.config(command="", state=NORMAL, bg="#ffffff")
    O27.config(command="", state=NORMAL, bg="#ffffff")
    O28.config(command="", state=NORMAL, bg="#ffffff")
    O29.config(command="", state=NORMAL, bg="#ffffff")
    O30.config(command="", state=NORMAL, bg="#ffffff")
    O31.config(command="", state=NORMAL, bg="#ffffff")

    N1.config(command="", state=NORMAL, bg="#ffffff")
    N2.config(command="", state=NORMAL, bg="#ffffff")
    N3.config(command="", state=NORMAL, bg="#ffffff")
    N4.config(command="", state=NORMAL, bg="#ffffff")
    N4.config(command="", state=NORMAL, bg="#ffffff")
    N5.config(command="", state=NORMAL, bg="#ffffff")
    N6.config(command="", state=NORMAL, bg="#ffffff")
    N7.config(command="", state=NORMAL, bg="#ffffff")
    N8.config(command="", state=NORMAL, bg="#ffffff")
    N9.config(command="", state=NORMAL, bg="#ffffff")
    N10.config(command="", state=NORMAL, bg="#ffffff")
    N11.config(command="", state=NORMAL, bg="#ffffff")
    N12.config(command="", state=NORMAL, bg="#ffffff")
    N13.config(command="", state=NORMAL, bg="#ffffff")
    N14.config(command="", state=NORMAL, bg="#ffffff")
    N15.config(command="", state=NORMAL, bg="#ffffff")
    N16.config(command="", state=NORMAL, bg="#ffffff")
    N17.config(command="", state=NORMAL, bg="#ffffff")
    N18.config(command="", state=NORMAL, bg="#ffffff")
    N19.config(command="", state=NORMAL, bg="#ffffff")
    N20.config(command="", state=NORMAL, bg="#ffffff")
    N21.config(command="", state=NORMAL, bg="#ffffff")
    N22.config(command="", state=NORMAL, bg="#ffffff")
    N23.config(command="", state=NORMAL, bg="#ffffff")
    N24.config(command="", state=NORMAL, bg="#ffffff")
    N25.config(command="", state=NORMAL, bg="#ffffff")
    N26.config(command="", state=NORMAL, bg="#ffffff")
    N27.config(command="", state=NORMAL, bg="#ffffff")
    N28.config(command="", state=NORMAL, bg="#ffffff")
    N29.config(command="", state=NORMAL, bg="#ffffff")
    N30.config(command="", state=NORMAL, bg="#ffffff")

    D1.config(command="", state=NORMAL, bg="#ffffff")
    D2.config(command="", state=NORMAL, bg="#ffffff")
    D3.config(command="", state=NORMAL, bg="#ffffff")
    D4.config(command="", state=NORMAL, bg="#ffffff")
    D4.config(command="", state=NORMAL, bg="#ffffff")
    D5.config(command="", state=NORMAL, bg="#ffffff")
    D6.config(command="", state=NORMAL, bg="#ffffff")
    D7.config(command="", state=NORMAL, bg="#ffffff")
    D8.config(command="", state=NORMAL, bg="#ffffff")
    D9.config(command="", state=NORMAL, bg="#ffffff")
    D10.config(command="", state=NORMAL, bg="#ffffff")
    D11.config(command="", state=NORMAL, bg="#ffffff")
    D12.config(command="", state=NORMAL, bg="#ffffff")
    D13.config(command="", state=NORMAL, bg="#ffffff")
    D14.config(command="", state=NORMAL, bg="#ffffff")
    D15.config(command="", state=NORMAL, bg="#ffffff")
    D16.config(command="", state=NORMAL, bg="#ffffff")
    D17.config(command="", state=NORMAL, bg="#ffffff")
    D18.config(command="", state=NORMAL, bg="#ffffff")
    D19.config(command="", state=NORMAL, bg="#ffffff")
    D20.config(command="", state=NORMAL, bg="#ffffff")
    D21.config(command="", state=NORMAL, bg="#ffffff")
    D22.config(command="", state=NORMAL, bg="#ffffff")
    D23.config(command="", state=NORMAL, bg="#ffffff")
    D24.config(command="", state=NORMAL, bg="#ffffff")
    D25.config(command="", state=NORMAL, bg="#ffffff")
    D26.config(command="", state=NORMAL, bg="#ffffff")
    D27.config(command="", state=NORMAL, bg="#ffffff")
    D28.config(command="", state=NORMAL, bg="#ffffff")
    D29.config(command="", state=NORMAL, bg="#ffffff")
    D30.config(command="", state=NORMAL, bg="#ffffff")
    D31.config(command="", state=NORMAL, bg="#ffffff")

#################################################################################################################################################################################################################################################################################
    
def application():
    reenable()
    applicationB.config(bg="#33FF66")
    infrastructureB.config(bg="light grey")
    
    J1.config(state=DISABLED, bg="red")
    J2.config(state=DISABLED, bg="red")
    J3.config(state=DISABLED, bg="red")
    J4.config(state=DISABLED, bg="red")
    J5.config(state=DISABLED, bg="red")
    J6.config(state=DISABLED, bg="red")
    J7.config(state=DISABLED, bg="red")
    J8.config(state=DISABLED, bg="red")
    J9.config(state=DISABLED, bg="red")
    J10.config(state=DISABLED, bg="red")
    J11.config(state=DISABLED, bg="red")
    J12.config(state=DISABLED, bg="red")
    J13.config(state=DISABLED, bg="red")
    J14.config(command=lambda:output(1, 14, "application"))
    J15.config(command=lambda:output(1, 15, "application"))
    J16.config(command=lambda:output(1, 16, "application"))
    J17.config(command=lambda:output(1, 17, "application"))
    J18.config(command=lambda:output(1, 18, "application"))
    J19.config(command=lambda:output(1, 19, "application"))
    J20.config(command=lambda:output(1, 20, "application"))
    J21.config(command=lambda:output(1, 21, "application"))
    J22.config(state=DISABLED, bg="red")
    J23.config(state=DISABLED, bg="red")
    J24.config(state=DISABLED, bg="red")
    J25.config(state=DISABLED, bg="red")
    J26.config(state=DISABLED, bg="red")
    J27.config(state=DISABLED, bg="red")
    J28.config(command=lambda:output(1, 28, "application"))
    J29.config(command=lambda:output(1, 29, "application"))
    J30.config(command=lambda:output(1, 30, "application"))
    J31.config(command=lambda:output(1, 31, "application"))

    F1.config(command=lambda:output(2, 1, "application"))
    F2.config(command=lambda:output(2, 2, "application"))
    F3.config(command=lambda:output(2, 3, "application"))
    F4.config(command=lambda:output(2, 4, "application"))
    F5.config(state=DISABLED, bg="red")
    F6.config(state=DISABLED, bg="red")
    F7.config(state=DISABLED, bg="red")
    F8.config(state=DISABLED, bg="red")
    F9.config(state=DISABLED, bg="red")
    F10.config(state=DISABLED, bg="red")
    F11.config(command=lambda:output(2, 11, "application"))
    F12.config(command=lambda:output(2, 12, "application"))
    F13.config(command=lambda:output(2, 13, "application"))
    F14.config(command=lambda:output(2, 14, "application"))
    F15.config(command=lambda:output(2, 15, "application"))
    F16.config(command=lambda:output(2, 16, "application"))
    F17.config(command=lambda:output(2, 17, "application"))
    F18.config(command=lambda:output(2, 18, "application"))
    F19.config(state=DISABLED, bg="red")
    F20.config(state=DISABLED, bg="red")
    F21.config(state=DISABLED, bg="red")
    F22.config(state=DISABLED, bg="red")
    F23.config(state=DISABLED, bg="red")
    F24.config(state=DISABLED, bg="red")
    F25.config(command=lambda:output(2, 25, "application"))
    F26.config(command=lambda:output(2, 26, "application"))
    F27.config(command=lambda:output(2, 27, "application"))
    F28.config(command=lambda:output(2, 28, "application"))

    M1.config(command=lambda:output(3, 1, "application"))
    M2.config(command=lambda:output(3, 2, "application"))
    M3.config(command=lambda:output(3, 3, "application"))
    M4.config(command=lambda:output(3, 4, "application"))
    M5.config(state=DISABLED, bg="red")
    M6.config(state=DISABLED, bg="red")
    M7.config(state=DISABLED, bg="red")
    M8.config(state=DISABLED, bg="red")
    M9.config(state=DISABLED, bg="red")
    M10.config(state=DISABLED, bg="red")
    M11.config(command=lambda:output(3, 11, "application"))
    M12.config(command=lambda:output(3, 12, "application"))
    M13.config(command=lambda:output(3, 13, "application"))
    M14.config(command=lambda:output(3, 14, "application"))
    M15.config(command=lambda:output(3, 15, "application"))
    M16.config(command=lambda:output(3, 16, "application"))
    M17.config(command=lambda:output(3, 17, "application"))
    M18.config(command=lambda:output(3, 18, "application"))
    M19.config(state=DISABLED, bg="red")
    M20.config(state=DISABLED, bg="red")
    M21.config(state=DISABLED, bg="red")
    M22.config(state=DISABLED, bg="red")
    M23.config(state=DISABLED, bg="red")
    M24.config(state=DISABLED, bg="red")
    M25.config(state=DISABLED, bg="red")
    M26.config(state=DISABLED, bg="red")
    M27.config(command=lambda:output(3, 27, "application"))
    M28.config(command=lambda:output(3, 28, "application"))
    M29.config(command=lambda:output(3, 29, "application"))
    M30.config(command=lambda:output(3, 30, "application"))
    M31.config(command=lambda:output(3, 31, "application"))

    A1.config(command=lambda:output(4, 1, "application"))
    A2.config(state=DISABLED, bg="red")
    A3.config(state=DISABLED, bg="red")
    A4.config(state=DISABLED, bg="red")
    A5.config(state=DISABLED, bg="red")
    A6.config(state=DISABLED, bg="red")
    A7.config(state=DISABLED, bg="red")
    A8.config(command=lambda:output(4, 8, "application"))
    A9.config(command=lambda:output(4, 9, "application"))
    A10.config(command=lambda:output(4, 10, "application"))
    A11.config(command=lambda:output(4, 11, "application"))
    A12.config(command=lambda:output(4, 12, "application"))
    A13.config(command=lambda:output(4, 12, "application"))
    A14.config(state=DISABLED, bg="red")
    A15.config(state=DISABLED, bg="red")
    A16.config(state=DISABLED, bg="red")
    A17.config(state=DISABLED, bg="red")
    A18.config(state=DISABLED, bg="red")
    A19.config(state=DISABLED, bg="red")
    A20.config(state=DISABLED, bg="red")
    A21.config(state=DISABLED, bg="red")
    A22.config(command=lambda:output(4, 22, "application"))
    A23.config(command=lambda:output(4, 23, "application"))
    A24.config(command=lambda:output(4, 24, "application"))
    A25.config(command=lambda:output(4, 25, "application"))
    A26.config(command=lambda:output(4, 26, "application"))
    A27.config(command=lambda:output(4, 27, "application"))
    A28.config(command=lambda:output(4, 28, "application"))
    A29.config(command=lambda:output(4, 29, "application"))
    A30.config(state=DISABLED, bg="red")

    MA1.config(state=DISABLED, bg="red")
    MA2.config(state=DISABLED, bg="red")
    MA3.config(state=DISABLED, bg="red")
    MA4.config(state=DISABLED, bg="red")
    MA5.config(state=DISABLED, bg="red")
    MA6.config(command=lambda:output(5, 6, "application"))
    MA7.config(command=lambda:output(5, 7, "application"))
    MA8.config(command=lambda:output(5, 8, "application"))
    MA9.config(command=lambda:output(5, 9, "application"))
    MA10.config(command=lambda:output(5, 10, "application"))
    MA11.config(command=lambda:output(5, 11, "application"))
    MA12.config(command=lambda:output(5, 12, "application"))
    MA13.config(command=lambda:output(5, 13, "application"))
    MA14.config(state=DISABLED, bg="red")
    MA15.config(state=DISABLED, bg="red")
    MA16.config(state=DISABLED, bg="red")
    MA17.config(state=DISABLED, bg="red")
    MA18.config(state=DISABLED, bg="red")
    MA19.config(state=DISABLED, bg="red")
    MA20.config(command=lambda:output(5, 20, "application"))
    MA21.config(command=lambda:output(5, 21, "application"))
    MA22.config(command=lambda:output(5, 22, "application"))
    MA23.config(command=lambda:output(5, 23, "application"))
    MA24.config(command=lambda:output(5, 24, "application"))
    MA25.config(command=lambda:output(5, 25, "application"))
    MA26.config(command=lambda:output(5, 26, "application"))
    MA27.config(command=lambda:output(5, 27, "application"))
    MA28.config(state=DISABLED, bg="red")
    MA29.config(state=DISABLED, bg="red")
    MA30.config(state=DISABLED, bg="red")
    MA31.config(state=DISABLED, bg="red")

    JU1.config(state=DISABLED, bg="red")
    JU2.config(state=DISABLED, bg="red")
    JU3.config(command=lambda:output(6, 3, "application"))
    JU4.config(command=lambda:output(6, 4, "application"))
    JU5.config(command=lambda:output(6, 5, "application"))
    JU6.config(command=lambda:output(6, 6, "application"))
    JU7.config(command=lambda:output(6, 7, "application"))
    JU8.config(command=lambda:output(6, 8, "application"))
    JU9.config(command=lambda:output(6, 9, "application"))
    JU10.config(command=lambda:output(6, 10, "application"))
    JU11.config(state=DISABLED, bg="red")
    JU12.config(state=DISABLED, bg="red")
    JU13.config(state=DISABLED, bg="red")
    JU14.config(state=DISABLED, bg="red")
    JU15.config(state=DISABLED, bg="red")
    JU16.config(state=DISABLED, bg="red")
    JU17.config(state=DISABLED, bg="red")
    JU18.config(state=DISABLED, bg="red")
    JU19.config(command=lambda:output(6, 19, "application"))
    JU20.config(command=lambda:output(6, 20, "application"))
    JU21.config(command=lambda:output(6, 21, "application"))
    JU22.config(command=lambda:output(6, 22, "application"))
    JU23.config(command=lambda:output(6, 23, "application"))
    JU24.config(command=lambda:output(6, 24, "application"))
    JU25.config(state=DISABLED, bg="red")
    JU26.config(state=DISABLED, bg="red")
    JU27.config(state=DISABLED, bg="red")
    JU28.config(state=DISABLED, bg="red")
    JU29.config(state=DISABLED, bg="red")
    JU30.config(state=DISABLED, bg="red")

    JUL1.config(command=lambda:output(7, 1, "application"))
    JUL2.config(command=lambda:output(7, 2, "application"))
    JUL3.config(command=lambda:output(7, 3, "application"))
    JUL4.config(command=lambda:output(7, 4, "application"))
    JUL5.config(command=lambda:output(7, 5, "application"))
    JUL6.config(command=lambda:output(7, 6, "application"))
    JUL7.config(command=lambda:output(7, 7, "application"))
    JUL8.config(command=lambda:output(7, 8, "application"))
    JUL9.config(state=DISABLED, bg="red")
    JUL10.config(state=DISABLED, bg="red")
    JUL11.config(state=DISABLED, bg="red")
    JUL12.config(state=DISABLED, bg="red")
    JUL13.config(state=DISABLED, bg="red")
    JUL14.config(state=DISABLED, bg="red")
    JUL15.config(command=lambda:output(7, 15, "application"))
    JUL16.config(command=lambda:output(7, 16, "application"))
    JUL17.config(command=lambda:output(7, 17, "application"))
    JUL18.config(command=lambda:output(7, 18, "application"))
    JUL19.config(command=lambda:output(7, 19, "application"))
    JUL20.config(command=lambda:output(7, 20, "application"))
    JUL21.config(command=lambda:output(7, 21, "application"))
    JUL22.config(command=lambda:output(7, 22, "application"))
    JUL23.config(state=DISABLED, bg="red")
    JUL24.config(state=DISABLED, bg="red")
    JUL25.config(state=DISABLED, bg="red")
    JUL26.config(state=DISABLED, bg="red")
    JUL27.config(state=DISABLED, bg="red")
    JUL28.config(state=DISABLED, bg="red")
    JUL29.config(command=lambda:output(7, 29, "application"))
    JUL30.config(command=lambda:output(7, 30, "application"))
    JUL31.config(command=lambda:output(7, 31, "application"))

    AU1.config(command=lambda:output(8, 1, "application"))
    AU2.config(command=lambda:output(8, 2, "application"))
    AU3.config(command=lambda:output(8, 3, "application"))
    AU4.config(command=lambda:output(8, 4, "application"))
    AU5.config(command=lambda:output(8, 5, "application"))
    AU6.config(state=DISABLED, bg="red")
    AU7.config(state=DISABLED, bg="red")
    AU8.config(state=DISABLED, bg="red")
    AU9.config(state=DISABLED, bg="red")
    AU10.config(state=DISABLED, bg="red")
    AU11.config(state=DISABLED, bg="red")
    AU12.config(command=lambda:output(8, 12, "application"))
    AU13.config(command=lambda:output(8, 13, "application"))
    AU14.config(command=lambda:output(8, 14, "application"))
    AU15.config(command=lambda:output(8, 15, "application"))
    AU16.config(command=lambda:output(8, 16, "application"))
    AU17.config(command=lambda:output(8, 17, "application"))
    AU18.config(command=lambda:output(8, 18, "application"))
    AU19.config(command=lambda:output(8, 19, "application"))
    AU20.config(state=DISABLED, bg="red")
    AU21.config(state=DISABLED, bg="red")
    AU22.config(state=DISABLED, bg="red")
    AU23.config(state=DISABLED, bg="red")
    AU24.config(state=DISABLED, bg="red")
    AU25.config(state=DISABLED, bg="red")
    AU26.config(command=lambda:output(8, 26, "application"))
    AU27.config(command=lambda:output(8, 27, "application"))
    AU28.config(command=lambda:output(8, 28, "application"))
    AU29.config(command=lambda:output(8, 29, "application"))
    AU30.config(command=lambda:output(8, 30, "application"))
    AU31.config(command=lambda:output(8, 31, "application"))

    S1.config(command=lambda:output(9, 1, "application"))
    S2.config(command=lambda:output(9, 2, "application"))
    S3.config(state=DISABLED, bg="red")
    S4.config(state=DISABLED, bg="red")
    S5.config(state=DISABLED, bg="red")
    S6.config(state=DISABLED, bg="red")
    S7.config(state=DISABLED, bg="red")
    S8.config(state=DISABLED, bg="red")
    S9.config(command=lambda:output(9, 9, "application"))
    S10.config(command=lambda:output(9, 10, "application"))
    S11.config(command=lambda:output(9, 11, "application"))
    S12.config(command=lambda:output(9, 12, "application"))
    S13.config(command=lambda:output(9, 13, "application"))
    S14.config(command=lambda:output(9, 14, "application"))
    S15.config(command=lambda:output(9, 15, "application"))
    S16.config(command=lambda:output(9, 16, "application"))
    S17.config(state=DISABLED, bg="red")
    S18.config(state=DISABLED, bg="red")
    S19.config(state=DISABLED, bg="red")
    S20.config(state=DISABLED, bg="red")
    S21.config(state=DISABLED, bg="red")
    S22.config(state=DISABLED, bg="red")
    S23.config(command=lambda:output(9, 23, "application"))
    S24.config(command=lambda:output(9, 24, "application"))
    S25.config(command=lambda:output(9, 25, "application"))
    S26.config(command=lambda:output(9, 26, "application"))
    S27.config(command=lambda:output(9, 27, "application"))
    S28.config(command=lambda:output(9, 28, "application"))
    S29.config(command=lambda:output(9, 29, "application"))
    S30.config(command=lambda:output(9, 30, "application"))

    O1.config(state=DISABLED, bg="red")
    O2.config(state=DISABLED, bg="red")
    O3.config(state=DISABLED, bg="red")
    O4.config(state=DISABLED, bg="red")
    O5.config(state=DISABLED, bg="red")
    O6.config(state=DISABLED, bg="red")
    O7.config(state=DISABLED, bg="red")
    O8.config(state=DISABLED, bg="red")
    O9.config(state=DISABLED, bg="red")
    O10.config(state=DISABLED, bg="red")
    O11.config(state=DISABLED, bg="red")
    O12.config(state=DISABLED, bg="red")
    O13.config(state=DISABLED, bg="red")
    O14.config(command=lambda:output(10, 14, "application"))
    O15.config(command=lambda:output(10, 15, "application"))
    O16.config(command=lambda:output(10, 16, "application"))
    O17.config(command=lambda:output(10, 15, "application"))
    O18.config(command=lambda:output(10, 15, "application"))
    O19.config(command=lambda:output(10, 15, "application"))
    O20.config(command=lambda:output(10, 15, "application"))
    O21.config(command=lambda:output(10, 15, "application"))
    O22.config(state=DISABLED, bg="red")
    O23.config(state=DISABLED, bg="red")
    O24.config(state=DISABLED, bg="red")
    O25.config(state=DISABLED, bg="red")
    O26.config(state=DISABLED, bg="red")
    O27.config(state=DISABLED, bg="red")
    O28.config(command=lambda:output(10, 28, "application"))
    O29.config(command=lambda:output(10, 29, "application"))
    O30.config(command=lambda:output(10, 30, "application"))
    O31.config(command=lambda:output(10, 31, "application"))

    N1.config(command=lambda:output(11, 1, "application"))
    N2.config(command=lambda:output(11, 2, "application"))
    N3.config(command=lambda:output(11, 3, "application"))
    N4.config(command=lambda:output(11, 4, "application"))
    N5.config(state=DISABLED, bg="red")
    N6.config(state=DISABLED, bg="red")
    N7.config(state=DISABLED, bg="red")
    N8.config(state=DISABLED, bg="red")
    N9.config(state=DISABLED, bg="red")
    N10.config(state=DISABLED, bg="red")
    N11.config(command=lambda:output(11, 11, "application"))
    N12.config(command=lambda:output(11, 12, "application"))
    N13.config(command=lambda:output(11, 13, "application"))
    N14.config(command=lambda:output(11, 14, "application"))
    N15.config(command=lambda:output(11, 15, "application"))
    N16.config(command=lambda:output(11, 16, "application"))
    N17.config(command=lambda:output(11, 17, "application"))
    N18.config(command=lambda:output(11, 18, "application"))
    N19.config(state=DISABLED, bg="red")
    N20.config(state=DISABLED, bg="red")
    N21.config(state=DISABLED, bg="red")
    N22.config(state=DISABLED, bg="red")
    N23.config(state=DISABLED, bg="red")
    N24.config(state=DISABLED, bg="red")
    N25.config(state=DISABLED, bg="red")
    N26.config(state=DISABLED, bg="red")
    N27.config(state=DISABLED, bg="red")
    N28.config(state=DISABLED, bg="red")
    N29.config(state=DISABLED, bg="red")
    N30.config(state=DISABLED, bg="red")

    D1.config(state=DISABLED, bg="red")
    D2.config(command=lambda:output(12, 2, "application"))
    D3.config(command=lambda:output(12, 3, "application"))
    D4.config(command=lambda:output(12, 4, "application"))
    D5.config(command=lambda:output(12, 5, "application"))
    D6.config(command=lambda:output(12, 6, "application"))
    D7.config(command=lambda:output(12, 7, "application"))
    D8.config(command=lambda:output(12, 8, "application"))
    D9.config(command=lambda:output(12, 9, "application"))
    D10.config(state=DISABLED, bg="red")
    D11.config(state=DISABLED, bg="red")
    D12.config(state=DISABLED, bg="red")
    D13.config(state=DISABLED, bg="red")
    D14.config(state=DISABLED, bg="red")
    D15.config(state=DISABLED, bg="red")
    D16.config(state=DISABLED, bg="red")
    D17.config(state=DISABLED, bg="red")
    D18.config(state=DISABLED, bg="red")
    D19.config(state=DISABLED, bg="red")
    D20.config(state=DISABLED, bg="red")
    D21.config(state=DISABLED, bg="red")
    D22.config(state=DISABLED, bg="red")
    D23.config(state=DISABLED, bg="red")
    D24.config(state=DISABLED, bg="red")
    D25.config(state=DISABLED, bg="red")
    D26.config(state=DISABLED, bg="red")
    D27.config(state=DISABLED, bg="red")
    D28.config(state=DISABLED, bg="red")
    D29.config(state=DISABLED, bg="red")
    D30.config(state=DISABLED, bg="red")
    D31.config(state=DISABLED, bg="red")
    
    dateCheck("a")
    
def infrastructure():
    reenable()
    infrastructureB.config(bg="#C39BD3")
    applicationB.config(bg="light grey")

    J1.config(state=DISABLED, bg="red")
    J2.config(state=DISABLED, bg="red")
    J3.config(command=lambda:output(1, 3, "infrastructure"))
    J4.config(command=lambda:output(1, 4, "infrastructure"))
    J5.config(command=lambda:output(1, 5, "infrastructure"))
    J6.config(command=lambda:output(1, 6, "infrastructure"))
    J7.config(command=lambda:output(1, 7, "infrastructure"))
    J8.config(command=lambda:output(1, 8, "infrastructure"))
    J9.config(command=lambda:output(1, 9, "infrastructure"))
    J10.config(command=lambda:output(1, 10, "infrastructure"))
    J11.config(command=lambda:output(1, 11, "infrastructure"))
    J12.config(command=lambda:output(1, 12, "infrastructure"))
    J13.config(command=lambda:output(1, 13, "infrastructure"))
    J14.config(command=lambda:output(1, 14, "infrastructure"))
    J15.config(state=DISABLED, bg="red")
    J16.config(state=DISABLED, bg="red")
    J17.config(state=DISABLED, bg="red")
    J18.config(state=DISABLED, bg="red")
    J19.config(state=DISABLED, bg="red")
    J20.config(state=DISABLED, bg="red")
    J21.config(command=lambda:output(1, 21, "infrastructure"))
    J22.config(command=lambda:output(1, 22, "infrastructure"))
    J23.config(command=lambda:output(1, 23, "infrastructure"))
    J24.config(command=lambda:output(1, 24, "infrastructure"))
    J25.config(command=lambda:output(1, 25, "infrastructure"))
    J26.config(command=lambda:output(1, 26, "infrastructure"))
    J27.config(command=lambda:output(1, 27, "infrastructure"))
    J28.config(command=lambda:output(1, 28, "infrastructure"))
    J29.config(state=DISABLED, bg="red")
    J30.config(state=DISABLED, bg="red")
    J31.config(state=DISABLED, bg="red")

    F1.config(state=DISABLED, bg="red")
    F2.config(state=DISABLED, bg="red")
    F3.config(state=DISABLED, bg="red")
    F4.config(command=lambda:output(2, 4, "infrastructure"))
    F5.config(command=lambda:output(2, 5, "infrastructure"))
    F6.config(command=lambda:output(2, 6, "infrastructure"))
    F7.config(command=lambda:output(2, 7, "infrastructure"))
    F8.config(command=lambda:output(2, 8, "infrastructure"))
    F9.config(command=lambda:output(2, 9, "infrastructure"))
    F10.config(command=lambda:output(2, 10, "infrastructure"))
    F11.config(command=lambda:output(2, 11, "infrastructure"))
    F12.config(state=DISABLED, bg="red")
    F13.config(state=DISABLED, bg="red")
    F14.config(state=DISABLED, bg="red")
    F15.config(state=DISABLED, bg="red")
    F16.config(state=DISABLED, bg="red")
    F17.config(state=DISABLED, bg="red")
    F18.config(command=lambda:output(2, 18, "infrastructure"))
    F19.config(command=lambda:output(2, 19, "infrastructure"))
    F20.config(command=lambda:output(2, 20, "infrastructure"))
    F21.config(command=lambda:output(2, 21, "infrastructure"))
    F22.config(command=lambda:output(2, 22, "infrastructure"))
    F23.config(command=lambda:output(2, 23, "infrastructure"))
    F24.config(command=lambda:output(2, 24, "infrastructure"))
    F25.config(command=lambda:output(2, 25, "infrastructure"))
    F26.config(state=DISABLED, bg="red")
    F27.config(state=DISABLED, bg="red")
    F28.config(state=DISABLED, bg="red")

    M1.config(state=DISABLED, bg="red")
    M2.config(state=DISABLED, bg="red")
    M3.config(state=DISABLED, bg="red")
    M4.config(command=lambda:output(3, 4, "infrastructure"))
    M5.config(command=lambda:output(3, 5, "infrastructure"))
    M6.config(command=lambda:output(3, 6, "infrastructure"))
    M7.config(command=lambda:output(3, 7, "infrastructure"))
    M8.config(command=lambda:output(3, 8, "infrastructure"))
    M9.config(command=lambda:output(3, 9, "infrastructure"))
    M10.config(command=lambda:output(3, 10, "infrastructure"))
    M11.config(command=lambda:output(3, 11, "infrastructure"))
    M12.config(state=DISABLED, bg="red")
    M13.config(state=DISABLED, bg="red")
    M14.config(state=DISABLED, bg="red")
    M15.config(state=DISABLED, bg="red")
    M16.config(state=DISABLED, bg="red")
    M17.config(state=DISABLED, bg="red")
    M18.config(command=lambda:output(3, 18, "infrastructure"))
    M19.config(command=lambda:output(3, 19, "infrastructure"))
    M20.config(command=lambda:output(3, 20, "infrastructure"))
    M21.config(command=lambda:output(3, 21, "infrastructure"))
    M22.config(command=lambda:output(3, 22, "infrastructure"))
    M23.config(command=lambda:output(3, 23, "infrastructure"))
    M24.config(command=lambda:output(3, 24, "infrastructure"))
    M25.config(command=lambda:output(3, 25, "infrastructure"))
    M26.config(state=DISABLED, bg="red")
    M27.config(state=DISABLED, bg="red")
    M28.config(state=DISABLED, bg="red")
    M29.config(state=DISABLED, bg="red")
    M30.config(state=DISABLED, bg="red")
    M31.config(state=DISABLED, bg="red")

    A1.config(command=lambda:output(4, 1, "infrastructure"))
    A2.config(command=lambda:output(4, 2, "infrastructure"))
    A3.config(command=lambda:output(4, 3, "infrastructure"))
    A4.config(command=lambda:output(4, 4, "infrastructure"))
    A5.config(command=lambda:output(4, 5, "infrastructure"))
    A6.config(command=lambda:output(4, 6, "infrastructure"))
    A7.config(command=lambda:output(4, 7, "infrastructure"))
    A8.config(command=lambda:output(4, 8, "infrastructure"))
    A9.config(state=DISABLED, bg="red")
    A10.config(state=DISABLED, bg="red")
    A11.config(state=DISABLED, bg="red")
    A12.config(state=DISABLED, bg="red")
    A13.config(state=DISABLED, bg="red")
    A14.config(state=DISABLED, bg="red")
    A15.config(state=DISABLED, bg="red")
    A16.config(state=DISABLED, bg="red")
    A17.config(state=DISABLED, bg="red")
    A18.config(state=DISABLED, bg="red")
    A19.config(state=DISABLED, bg="red")
    A20.config(state=DISABLED, bg="red")
    A21.config(state=DISABLED, bg="red")
    A22.config(state=DISABLED, bg="red")
    A23.config(state=DISABLED, bg="red")
    A24.config(state=DISABLED, bg="red")
    A25.config(state=DISABLED, bg="red")
    A26.config(state=DISABLED, bg="red")
    A27.config(state=DISABLED, bg="red")
    A28.config(state=DISABLED, bg="red")
    A29.config(command=lambda:output(4, 29, "infrastructure"))
    A30.config(command=lambda:output(4, 30, "infrastructure"))

    MA1.config(command=lambda:output(5, 1, "infrastructure"))
    MA2.config(command=lambda:output(5, 2, "infrastructure"))
    MA3.config(command=lambda:output(5, 3, "infrastructure"))
    MA4.config(command=lambda:output(5, 4, "infrastructure"))
    MA5.config(command=lambda:output(5, 5, "infrastructure"))
    MA6.config(command=lambda:output(5, 6, "infrastructure"))
    MA7.config(state=DISABLED, bg="red")
    MA8.config(state=DISABLED, bg="red")
    MA9.config(state=DISABLED, bg="red")
    MA10.config(state=DISABLED, bg="red")
    MA11.config(state=DISABLED, bg="red")
    MA12.config(state=DISABLED, bg="red")
    MA13.config(command=lambda:output(5, 13, "infrastructure"))
    MA14.config(command=lambda:output(5, 14, "infrastructure"))
    MA15.config(command=lambda:output(5, 15, "infrastructure"))
    MA16.config(command=lambda:output(5, 16, "infrastructure"))
    MA17.config(command=lambda:output(5, 17, "infrastructure"))
    MA18.config(command=lambda:output(5, 18, "infrastructure"))
    MA19.config(command=lambda:output(5, 19, "infrastructure"))
    MA20.config(command=lambda:output(5, 20, "infrastructure"))
    MA21.config(state=DISABLED, bg="red")
    MA22.config(state=DISABLED, bg="red")
    MA23.config(state=DISABLED, bg="red")
    MA24.config(state=DISABLED, bg="red")
    MA25.config(state=DISABLED, bg="red")
    MA26.config(state=DISABLED, bg="red")
    MA27.config(command=lambda:output(5, 27, "infrastructure"))
    MA28.config(command=lambda:output(5, 28, "infrastructure"))
    MA29.config(command=lambda:output(5, 29, "infrastructure"))
    MA30.config(command=lambda:output(5, 30, "infrastructure"))
    MA31.config(command=lambda:output(5, 31, "infrastructure"))

    JU1.config(command=lambda:output(6, 1, "infrastructure"))
    JU2.config(command=lambda:output(6, 2, "infrastructure"))
    JU3.config(command=lambda:output(6, 3, "infrastructure"))
    JU4.config(state=DISABLED, bg="red")
    JU5.config(state=DISABLED, bg="red")
    JU6.config(state=DISABLED, bg="red")
    JU7.config(state=DISABLED, bg="red")
    JU8.config(state=DISABLED, bg="red")
    JU9.config(state=DISABLED, bg="red")
    JU10.config(command=lambda:output(6, 10, "infrastructure"))
    JU11.config(command=lambda:output(6, 11, "infrastructure"))
    JU12.config(command=lambda:output(6, 12, "infrastructure"))
    JU13.config(command=lambda:output(6, 13, "infrastructure"))
    JU14.config(command=lambda:output(6, 14, "infrastructure"))
    JU15.config(command=lambda:output(6, 15, "infrastructure"))
    JU16.config(command=lambda:output(6, 16, "infrastructure"))
    JU17.config(command=lambda:output(6, 17, "infrastructure"))
    JU18.config(state=DISABLED, bg="red")
    JU19.config(state=DISABLED, bg="red")
    JU20.config(state=DISABLED, bg="red")
    JU21.config(state=DISABLED, bg="red")
    JU22.config(state=DISABLED, bg="red")
    JU23.config(state=DISABLED, bg="red")
    JU24.config(command=lambda:output(6, 24, "infrastructure"))
    JU25.config(command=lambda:output(6, 25, "infrastructure"))
    JU26.config(command=lambda:output(6, 26, "infrastructure"))
    JU27.config(command=lambda:output(6, 27, "infrastructure"))
    JU28.config(command=lambda:output(6, 28, "infrastructure"))
    JU29.config(command=lambda:output(6, 29, "infrastructure"))
    JU30.config(command=lambda:output(6, 30, "infrastructure"))

    JUL1.config(command=lambda:output(7, 1, "infrastructure"))
    JUL2.config(state=DISABLED, bg="red")
    JUL3.config(state=DISABLED, bg="red")
    JUL4.config(state=DISABLED, bg="red")
    JUL5.config(state=DISABLED, bg="red")
    JUL6.config(state=DISABLED, bg="red")
    JUL7.config(state=DISABLED, bg="red")
    JUL8.config(command=lambda:output(7, 8, "infrastructure"))
    JUL9.config(command=lambda:output(7, 9, "infrastructure"))
    JUL10.config(command=lambda:output(7, 10, "infrastructure"))
    JUL11.config(command=lambda:output(7, 11, "infrastructure"))
    JUL12.config(command=lambda:output(7, 12, "infrastructure"))
    JUL13.config(command=lambda:output(7, 13, "infrastructure"))
    JUL14.config(command=lambda:output(7, 14, "infrastructure"))
    JUL15.config(command=lambda:output(7, 15, "infrastructure"))
    JUL16.config(state=DISABLED, bg="red")
    JUL17.config(state=DISABLED, bg="red")
    JUL18.config(state=DISABLED, bg="red")
    JUL19.config(state=DISABLED, bg="red")
    JUL20.config(state=DISABLED, bg="red")
    JUL21.config(state=DISABLED, bg="red")
    JUL22.config(command=lambda:output(7, 22, "infrastructure"))
    JUL23.config(command=lambda:output(7, 23, "infrastructure"))
    JUL24.config(command=lambda:output(7, 24, "infrastructure"))
    JUL25.config(command=lambda:output(7, 25, "infrastructure"))
    JUL26.config(command=lambda:output(7, 26, "infrastructure"))
    JUL27.config(command=lambda:output(7, 27, "infrastructure"))
    JUL28.config(command=lambda:output(7, 28, "infrastructure"))
    JUL29.config(command=lambda:output(7, 29, "infrastructure"))
    JUL30.config(state=DISABLED, bg="red")
    JUL31.config(state=DISABLED, bg="red")

    AU1.config(state=DISABLED, bg="red")
    AU2.config(state=DISABLED, bg="red")
    AU3.config(state=DISABLED, bg="red")
    AU4.config(state=DISABLED, bg="red")
    AU5.config(command=lambda:output(8, 5, "infrastructure"))
    AU6.config(command=lambda:output(8, 6, "infrastructure"))
    AU7.config(command=lambda:output(8, 7, "infrastructure"))
    AU8.config(command=lambda:output(8, 8, "infrastructure"))
    AU9.config(command=lambda:output(8, 9, "infrastructure"))
    AU10.config(command=lambda:output(8, 10, "infrastructure"))
    AU11.config(command=lambda:output(8, 11, "infrastructure"))
    AU12.config(command=lambda:output(8, 12, "infrastructure"))
    AU13.config(state=DISABLED, bg="red")
    AU14.config(state=DISABLED, bg="red")
    AU15.config(state=DISABLED, bg="red")
    AU16.config(state=DISABLED, bg="red")
    AU17.config(state=DISABLED, bg="red")
    AU18.config(state=DISABLED, bg="red")
    AU19.config(command=lambda:output(8, 19, "infrastructure"))
    AU20.config(command=lambda:output(8, 20, "infrastructure"))
    AU21.config(command=lambda:output(8, 21, "infrastructure"))
    AU22.config(command=lambda:output(8, 22, "infrastructure"))
    AU23.config(command=lambda:output(8, 23, "infrastructure"))
    AU24.config(command=lambda:output(8, 24, "infrastructure"))
    AU25.config(command=lambda:output(8, 25, "infrastructure"))
    AU26.config(command=lambda:output(8, 26, "infrastructure"))
    AU27.config(state=DISABLED, bg="red")
    AU28.config(state=DISABLED, bg="red")
    AU29.config(state=DISABLED, bg="red")
    AU30.config(state=DISABLED, bg="red")
    AU31.config(state=DISABLED, bg="red")

    S1.config(state=DISABLED, bg="red")
    S2.config(command=lambda:output(9, 2, "infrastructure"))
    S3.config(command=lambda:output(9, 3, "infrastructure"))
    S4.config(command=lambda:output(9, 4, "infrastructure"))
    S5.config(command=lambda:output(9, 5, "infrastructure"))
    S6.config(command=lambda:output(9, 6, "infrastructure"))
    S7.config(command=lambda:output(9, 7, "infrastructure"))
    S8.config(command=lambda:output(9, 8, "infrastructure"))
    S9.config(command=lambda:output(9, 9, "infrastructure"))
    S10.config(state=DISABLED, bg="red")
    S11.config(state=DISABLED, bg="red")
    S12.config(state=DISABLED, bg="red")
    S13.config(state=DISABLED, bg="red")
    S14.config(state=DISABLED, bg="red")
    S15.config(state=DISABLED, bg="red")
    S16.config(command=lambda:output(9, 16, "infrastructure"))
    S17.config(command=lambda:output(9, 17, "infrastructure"))
    S18.config(command=lambda:output(9, 18, "infrastructure"))
    S19.config(command=lambda:output(9, 19, "infrastructure"))
    S20.config(command=lambda:output(9, 20, "infrastructure"))
    S21.config(command=lambda:output(9, 21, "infrastructure"))
    S22.config(command=lambda:output(9, 22, "infrastructure"))
    S23.config(command=lambda:output(9, 23, "infrastructure"))
    S24.config(state=DISABLED, bg="red")
    S25.config(state=DISABLED, bg="red")
    S26.config(state=DISABLED, bg="red")
    S27.config(state=DISABLED, bg="red")
    S28.config(state=DISABLED, bg="red")
    S29.config(state=DISABLED, bg="red")
    S30.config(command=lambda:output(9, 30, "infrastructure"))

    O1.config(command=lambda:output(10, 1, "infrastructure"))
    O2.config(command=lambda:output(10, 2, "infrastructure"))
    O3.config(command=lambda:output(10, 3, "infrastructure"))
    O4.config(command=lambda:output(10, 4, "infrastructure"))
    O5.config(command=lambda:output(10, 5, "infrastructure"))
    O6.config(state=DISABLED, bg="red")
    O7.config(state=DISABLED, bg="red")
    O8.config(state=DISABLED, bg="red")
    O9.config(state=DISABLED, bg="red")
    O10.config(state=DISABLED, bg="red")
    O11.config(state=DISABLED, bg="red")
    O12.config(state=DISABLED, bg="red")
    O13.config(state=DISABLED, bg="red")
    O14.config(state=DISABLED, bg="red")
    O15.config(state=DISABLED, bg="red")
    O16.config(state=DISABLED, bg="red")
    O17.config(state=DISABLED, bg="red")
    O18.config(state=DISABLED, bg="red")
    O19.config(state=DISABLED, bg="red")
    O20.config(state=DISABLED, bg="red")
    O21.config(command=lambda:output(10, 21, "infrastructure"))
    O22.config(command=lambda:output(10, 22, "infrastructure"))
    O23.config(command=lambda:output(10, 23, "infrastructure"))
    O24.config(command=lambda:output(10, 24, "infrastructure"))
    O25.config(command=lambda:output(10, 25, "infrastructure"))
    O26.config(command=lambda:output(10, 26, "infrastructure"))
    O27.config(command=lambda:output(10, 27, "infrastructure"))
    O28.config(command=lambda:output(10, 28, "infrastructure"))
    O29.config(state=DISABLED, bg="red")
    O30.config(state=DISABLED, bg="red")
    O31.config(state=DISABLED, bg="red")

    N1.config(state=DISABLED, bg="red")
    N2.config(state=DISABLED, bg="red")
    N3.config(state=DISABLED, bg="red")
    N4.config(command=lambda:output(11, 4, "infrastructure"))
    N5.config(command=lambda:output(11, 5, "infrastructure"))
    N6.config(command=lambda:output(11, 6, "infrastructure"))
    N7.config(command=lambda:output(11, 7, "infrastructure"))
    N8.config(command=lambda:output(11, 8, "infrastructure"))
    N9.config(command=lambda:output(11, 9, "infrastructure"))
    N10.config(command=lambda:output(11, 10, "infrastructure"))
    N11.config(command=lambda:output(11, 11, "infrastructure"))
    N12.config(state=DISABLED, bg="red")
    N13.config(state=DISABLED, bg="red")
    N14.config(state=DISABLED, bg="red")
    N15.config(state=DISABLED, bg="red")
    N16.config(state=DISABLED, bg="red")
    N17.config(state=DISABLED, bg="red")
    N18.config(command=lambda:output(11, 18, "infrastructure"))
    N19.config(command=lambda:output(11, 19, "infrastructure"))
    N20.config(command=lambda:output(11, 20, "infrastructure"))
    N21.config(command=lambda:output(11, 21, "infrastructure"))
    N22.config(command=lambda:output(11, 22, "infrastructure"))
    N23.config(command=lambda:output(11, 23, "infrastructure"))
    N24.config(state=DISABLED, bg="red")
    N25.config(state=DISABLED, bg="red")
    N26.config(state=DISABLED, bg="red")
    N27.config(state=DISABLED, bg="red")
    N28.config(state=DISABLED, bg="red")
    N29.config(state=DISABLED, bg="red")
    N30.config(state=DISABLED, bg="red")

    D1.config(state=DISABLED, bg="red")
    D2.config(state=DISABLED, bg="red")
    D3.config(state=DISABLED, bg="red")
    D4.config(state=DISABLED, bg="red")
    D5.config(state=DISABLED, bg="red")
    D6.config(state=DISABLED, bg="red")
    D7.config(state=DISABLED, bg="red")
    D8.config(state=DISABLED, bg="red")
    D9.config(command=lambda:output(12, 9, "infrastructure"))
    D10.config(command=lambda:output(12, 10, "infrastructure"))
    D11.config(command=lambda:output(12, 11, "infrastructure"))
    D12.config(command=lambda:output(12, 12, "infrastructure"))
    D13.config(command=lambda:output(12, 13, "infrastructure"))
    D14.config(command=lambda:output(12, 14, "infrastructure"))
    D15.config(command=lambda:output(12, 15, "infrastructure"))
    D16.config(command=lambda:output(12, 16, "infrastructure"))
    D17.config(state=DISABLED, bg="red")
    D18.config(state=DISABLED, bg="red")
    D19.config(state=DISABLED, bg="red")
    D20.config(state=DISABLED, bg="red")
    D21.config(state=DISABLED, bg="red")
    D22.config(state=DISABLED, bg="red")
    D23.config(state=DISABLED, bg="red")
    D24.config(state=DISABLED, bg="red")
    D25.config(state=DISABLED, bg="red")
    D26.config(state=DISABLED, bg="red")
    D27.config(state=DISABLED, bg="red")
    D28.config(state=DISABLED, bg="red")
    D29.config(state=DISABLED, bg="red")
    D30.config(state=DISABLED, bg="red")
    D31.config(state=DISABLED, bg="red")
    
    dateCheck("i")

############################################################################################################################################################################################################################################################################

root = Tk()

############################################################################################################################################################################################################################################################################HARRIOSN ROSE +44 (0) 79235053239

outputL = Label(root, bg="#FFFFFF", font=("Times", 16))
outputM = Label(root, bg="#FFFFFF", font=("Times", 16, "bold"))
outputN = Label(root, bg="#FFFFFF", font=("Times", 12))
outputO = Label(root, bg="#FFFFFF", font=("Times", 16))
outputP = Label(root, bg="#FFFFFF", font=("Times", 16, "bold"))
outputQ = Label(root, bg="#FFFFFF", font=("Times", 12))
outputR = Label(root, bg="#FFFFFF", font=("Times", 16))

Ljan = Label(root, text="January", bg="#FFFFFF", font=("Times", 16))
Lfeb = Label(root, text="February", bg="#FFFFFF", font=("Times", 16))
Lmar = Label(root, text="March", bg="#FFFFFF", font=("Times", 16))
Lapr = Label(root, text="April", bg="#FFFFFF", font=("Times", 16))
Lmay = Label(root, text="May", bg="#FFFFFF", font=("Times", 16))
Ljun = Label(root, text="June", bg="#FFFFFF", font=("Times", 16))
Ljul = Label(root, text="July", bg="#FFFFFF", font=("Times", 16))
Laug = Label(root, text="August", bg="#FFFFFF", font=("Times", 16))
Lsep = Label(root, text="September", bg="#FFFFFF", font=("Times", 16))
Loct = Label(root, text="October", bg="#FFFFFF", font=("Times", 16))
Lnov = Label(root, text="November", bg="#FFFFFF", font=("Times", 16))
Ldec = Label(root, text="December", bg="#FFFFFF", font=("Times", 16))
Ljan.place(x=190, y=75)
Lfeb.place(x=190, y=285)
Lmar.place(x=190, y=485)
Lapr.place(x=700, y=75)
Lmay.place(x=700, y=285)
Ljun.place(x=700, y=485)
Ljul.place(x=1190, y=75)
Laug.place(x=1190, y=285)
Lsep.place(x=1190, y=485)
Loct.place(x=1690, y=75)
Lnov.place(x=1690, y=285)
Ldec.place(x=1690, y=485)

############################################################################################################################################################################################################################################################################

Loblaws = PhotoImage(file="logo.png")

############################################################################################################################################################################################################################################################################

LogoL = Label(root, image=Loblaws, bg="#FFFFFF")
RL = Label(root, text="Press your release type to continue: ", bg="#FFFFFF", font=("Times"))
LogoL.place(x=0, y=948)
RL.place(x=1450, y=775)

applicationB = Button(root, command=application, text="Application Release",  height=7, width=40, bg="light grey")
infrastructureB = Button(root, command=infrastructure, text="Infrastructure Release",  height=7, width=40, bg="light grey")

J1 = Button(root, state=DISABLED, text="1",  height=1, width=4, bg="red")
J2 = Button(root, state=DISABLED, text="2",  height=1, width=4, bg="red")
J3 = Button(root, state=DISABLED, text="3",  height=1, width=4, bg="red")
J4 = Button(root, state=DISABLED, text="4",  height=1, width=4, bg="red")
J5 = Button(root, state=DISABLED, text="5",  height=1, width=4, bg="red")
J6 = Button(root, state=DISABLED, text="6",  height=1, width=4, bg="red")
J7 = Button(root, state=DISABLED, text="7",  height=1, width=4, bg="red")
J8 = Button(root, state=DISABLED, text="8",  height=1, width=4, bg="red")
J9 = Button(root, state=DISABLED, text="9",  height=1, width=4, bg="red")
J10 = Button(root, state=DISABLED, text="10",  height=1, width=4, bg="red")
J11 = Button(root, state=DISABLED, text="11",  height=1, width=4, bg="red")
J12 = Button(root, state=DISABLED, text="12",  height=1, width=4, bg="red")
J13 = Button(root, state=DISABLED, text="13",  height=1, width=4, bg="red")
J14 = Button(root, state=DISABLED, text="14",  height=1, width=4, bg="red")
J15 = Button(root, state=DISABLED, text="15",  height=1, width=4, bg="red")
J16 = Button(root, state=DISABLED, text="16",  height=1, width=4, bg="red")
J17 = Button(root, state=DISABLED, text="17",  height=1, width=4, bg="red")
J18 = Button(root, state=DISABLED, text="18",  height=1, width=4, bg="red")
J19 = Button(root, state=DISABLED, text="19",  height=1, width=4, bg="red")
J20 = Button(root, state=DISABLED, text="20",  height=1, width=4, bg="red")
J21 = Button(root, state=DISABLED, text="21",  height=1, width=4, bg="red")
J22 = Button(root, state=DISABLED, text="22",  height=1, width=4, bg="red")
J23 = Button(root, state=DISABLED, text="23",  height=1, width=4, bg="red")
J24 = Button(root, state=DISABLED, text="24",  height=1, width=4, bg="red")
J25 = Button(root, state=DISABLED, text="25",  height=1, width=4, bg="red")
J26 = Button(root, state=DISABLED, text="26",  height=1, width=4, bg="red")
J27 = Button(root, state=DISABLED, text="27",  height=1, width=4, bg="red")
J28 = Button(root, state=DISABLED, text="28",  height=1, width=4, bg="red")
J29 = Button(root, state=DISABLED, text="29",  height=1, width=4, bg="red")
J30 = Button(root, state=DISABLED, text="30",  height=1, width=4, bg="red")
J31 = Button(root, state=DISABLED, text="31",  height=1, width=4, bg="red")

F1 = Button(root, state=DISABLED, text="1",  height=1, width=4, bg="red")
F2 = Button(root, state=DISABLED, text="2",  height=1, width=4, bg="red")
F3 = Button(root, state=DISABLED, text="3",  height=1, width=4, bg="red")
F4 = Button(root, state=DISABLED, text="4",  height=1, width=4, bg="red")
F5 = Button(root, state=DISABLED, text="5",  height=1, width=4, bg="red")
F6 = Button(root, state=DISABLED, text="6",  height=1, width=4, bg="red")
F7 = Button(root, state=DISABLED, text="7",  height=1, width=4, bg="red")
F8 = Button(root, state=DISABLED, text="8",  height=1, width=4, bg="red")
F9 = Button(root, state=DISABLED, text="9",  height=1, width=4, bg="red")
F10 = Button(root, state=DISABLED, text="10",  height=1, width=4, bg="red")
F11 = Button(root, state=DISABLED, text="11",  height=1, width=4, bg="red")
F12 = Button(root, state=DISABLED, text="12",  height=1, width=4, bg="red")
F13 = Button(root, state=DISABLED, text="13",  height=1, width=4, bg="red")
F14 = Button(root, state=DISABLED, text="14",  height=1, width=4, bg="red")
F15 = Button(root, state=DISABLED, text="15",  height=1, width=4, bg="red")
F16 = Button(root, state=DISABLED, text="16",  height=1, width=4, bg="red")
F17 = Button(root, state=DISABLED, text="17",  height=1, width=4, bg="red")
F18 = Button(root, state=DISABLED, text="18",  height=1, width=4, bg="red")
F19 = Button(root, state=DISABLED, text="19",  height=1, width=4, bg="red")
F20 = Button(root, state=DISABLED, text="20",  height=1, width=4, bg="red")
F21 = Button(root, state=DISABLED, text="21",  height=1, width=4, bg="red")
F22 = Button(root, state=DISABLED, text="22",  height=1, width=4, bg="red")
F23 = Button(root, state=DISABLED, text="23",  height=1, width=4, bg="red")
F24 = Button(root, state=DISABLED, text="24",  height=1, width=4, bg="red")
F25 = Button(root, state=DISABLED, text="25",  height=1, width=4, bg="red")
F26 = Button(root, state=DISABLED, text="26",  height=1, width=4, bg="red")
F27 = Button(root, state=DISABLED, text="27",  height=1, width=4, bg="red")
F28 = Button(root, state=DISABLED, text="28",  height=1, width=4, bg="red")

M1 = Button(root, state=DISABLED, text="1",  height=1, width=4, bg="red")
M2 = Button(root, state=DISABLED, text="2",  height=1, width=4, bg="red")
M3 = Button(root, state=DISABLED, text="3",  height=1, width=4, bg="red")
M4 = Button(root, state=DISABLED, text="4",  height=1, width=4, bg="red")
M5 = Button(root, state=DISABLED, text="5",  height=1, width=4, bg="red")
M6 = Button(root, state=DISABLED, text="6",  height=1, width=4, bg="red")
M7 = Button(root, state=DISABLED, text="7",  height=1, width=4, bg="red")
M8 = Button(root, state=DISABLED, text="8",  height=1, width=4, bg="red")
M9 = Button(root, state=DISABLED, text="9",  height=1, width=4, bg="red")
M10 = Button(root, state=DISABLED, text="10",  height=1, width=4, bg="red")
M11 = Button(root, state=DISABLED, text="11",  height=1, width=4, bg="red")
M12 = Button(root, state=DISABLED, text="12",  height=1, width=4, bg="red")
M13 = Button(root, state=DISABLED, text="13",  height=1, width=4, bg="red")
M14 = Button(root, state=DISABLED, text="14",  height=1, width=4, bg="red")
M15 = Button(root, state=DISABLED, text="15",  height=1, width=4, bg="red")
M16 = Button(root, state=DISABLED, text="16",  height=1, width=4, bg="red")
M17 = Button(root, state=DISABLED, text="17",  height=1, width=4, bg="red")
M18 = Button(root, state=DISABLED, text="18",  height=1, width=4, bg="red")
M19 = Button(root, state=DISABLED, text="19",  height=1, width=4, bg="red")
M20 = Button(root, state=DISABLED, text="20",  height=1, width=4, bg="red")
M21 = Button(root, state=DISABLED, text="21",  height=1, width=4, bg="red")
M22 = Button(root, state=DISABLED, text="22",  height=1, width=4, bg="red")
M23 = Button(root, state=DISABLED, text="23",  height=1, width=4, bg="red")
M24 = Button(root, state=DISABLED, text="24",  height=1, width=4, bg="red")
M25 = Button(root, state=DISABLED, text="25",  height=1, width=4, bg="red")
M26 = Button(root, state=DISABLED, text="26",  height=1, width=4, bg="red")
M27 = Button(root, state=DISABLED, text="27",  height=1, width=4, bg="red")
M28 = Button(root, state=DISABLED, text="28",  height=1, width=4, bg="red")
M29 = Button(root, state=DISABLED, text="29",  height=1, width=4, bg="red")
M30 = Button(root, state=DISABLED, text="30",  height=1, width=4, bg="red")
M31 = Button(root, state=DISABLED, text="31",  height=1, width=4, bg="red")

A1 = Button(root, state=DISABLED, text="1",  height=1, width=4, bg="red")
A2 = Button(root, state=DISABLED, text="2",  height=1, width=4, bg="red")
A3 = Button(root, state=DISABLED, text="3",  height=1, width=4, bg="red")
A4 = Button(root, state=DISABLED, text="4",  height=1, width=4, bg="red")
A5 = Button(root, state=DISABLED, text="5",  height=1, width=4, bg="red")
A6 = Button(root, state=DISABLED, text="6",  height=1, width=4, bg="red")
A7 = Button(root, state=DISABLED, text="7",  height=1, width=4, bg="red")
A8 = Button(root, state=DISABLED, text="8",  height=1, width=4, bg="red")
A9 = Button(root, state=DISABLED, text="9",  height=1, width=4, bg="red")
A10 = Button(root, state=DISABLED, text="10",  height=1, width=4, bg="red")
A11 = Button(root, state=DISABLED, text="11",  height=1, width=4, bg="red")
A12 = Button(root, state=DISABLED, text="12",  height=1, width=4, bg="red")
A13 = Button(root, state=DISABLED, text="13",  height=1, width=4, bg="red")
A14 = Button(root, state=DISABLED, text="14",  height=1, width=4, bg="red")
A15 = Button(root, state=DISABLED, text="15",  height=1, width=4, bg="red")
A16 = Button(root, state=DISABLED, text="16",  height=1, width=4, bg="red")
A17 = Button(root, state=DISABLED, text="17",  height=1, width=4, bg="red")
A18 = Button(root, state=DISABLED, text="18",  height=1, width=4, bg="red")
A19 = Button(root, state=DISABLED, text="19",  height=1, width=4, bg="red")
A20 = Button(root, state=DISABLED, text="20",  height=1, width=4, bg="red")
A21 = Button(root, state=DISABLED, text="21",  height=1, width=4, bg="red")
A22 = Button(root, state=DISABLED, text="22",  height=1, width=4, bg="red")
A23 = Button(root, state=DISABLED, text="23",  height=1, width=4, bg="red")
A24 = Button(root, state=DISABLED, text="24",  height=1, width=4, bg="red")
A25 = Button(root, state=DISABLED, text="25",  height=1, width=4, bg="red")
A26 = Button(root, state=DISABLED, text="26",  height=1, width=4, bg="red")
A27 = Button(root, state=DISABLED, text="27",  height=1, width=4, bg="red")
A28 = Button(root, state=DISABLED, text="28",  height=1, width=4, bg="red")
A29 = Button(root, state=DISABLED, text="29",  height=1, width=4, bg="red")
A30 = Button(root, state=DISABLED, text="30",  height=1, width=4, bg="red")

MA1 = Button(root, state=DISABLED, text="1",  height=1, width=4, bg="red")
MA2 = Button(root, state=DISABLED, text="2",  height=1, width=4, bg="red")
MA3 = Button(root, state=DISABLED, text="3",  height=1, width=4, bg="red")
MA4 = Button(root, state=DISABLED, text="4",  height=1, width=4, bg="red")
MA5 = Button(root, state=DISABLED, text="5",  height=1, width=4, bg="red")
MA6 = Button(root, state=DISABLED, text="6",  height=1, width=4, bg="red")
MA7 = Button(root, state=DISABLED, text="7",  height=1, width=4, bg="red")
MA8 = Button(root, state=DISABLED, text="8",  height=1, width=4, bg="red")
MA9 = Button(root, state=DISABLED, text="9",  height=1, width=4, bg="red")
MA10 = Button(root, state=DISABLED, text="10",  height=1, width=4, bg="red")
MA11 = Button(root, state=DISABLED, text="11",  height=1, width=4, bg="red")
MA12 = Button(root, state=DISABLED, text="12",  height=1, width=4, bg="red")
MA13 = Button(root, state=DISABLED, text="13",  height=1, width=4, bg="red")
MA14 = Button(root, state=DISABLED, text="14",  height=1, width=4, bg="red")
MA15 = Button(root, state=DISABLED, text="15",  height=1, width=4, bg="red")
MA16 = Button(root, state=DISABLED, text="16",  height=1, width=4, bg="red")
MA17 = Button(root, state=DISABLED, text="17",  height=1, width=4, bg="red")
MA18 = Button(root, state=DISABLED, text="18",  height=1, width=4, bg="red")
MA19 = Button(root, state=DISABLED, text="19",  height=1, width=4, bg="red")
MA20 = Button(root, state=DISABLED, text="20",  height=1, width=4, bg="red")
MA21 = Button(root, state=DISABLED, text="21",  height=1, width=4, bg="red")
MA22 = Button(root, state=DISABLED, text="22",  height=1, width=4, bg="red")
MA23 = Button(root, state=DISABLED, text="23",  height=1, width=4, bg="red")
MA24 = Button(root, state=DISABLED, text="24",  height=1, width=4, bg="red")
MA25 = Button(root, state=DISABLED, text="25",  height=1, width=4, bg="red")
MA26 = Button(root, state=DISABLED, text="26",  height=1, width=4, bg="red")
MA27 = Button(root, state=DISABLED, text="27",  height=1, width=4, bg="red")
MA28 = Button(root, state=DISABLED, text="28",  height=1, width=4, bg="red")
MA29 = Button(root, state=DISABLED, text="29",  height=1, width=4, bg="red")
MA30 = Button(root, state=DISABLED, text="30",  height=1, width=4, bg="red")
MA31 = Button(root, state=DISABLED, text="31",  height=1, width=4, bg="red")

JU1 = Button(root, state=DISABLED, text="1",  height=1, width=4, bg="red")
JU2 = Button(root, state=DISABLED, text="2",  height=1, width=4, bg="red")
JU3 = Button(root, state=DISABLED, text="3",  height=1, width=4, bg="red")
JU4 = Button(root, state=DISABLED, text="4",  height=1, width=4, bg="red")
JU5 = Button(root, state=DISABLED, text="5",  height=1, width=4, bg="red")
JU6 = Button(root, state=DISABLED, text="6",  height=1, width=4, bg="red")
JU7 = Button(root, state=DISABLED, text="7",  height=1, width=4, bg="red")
JU8 = Button(root, state=DISABLED, text="8",  height=1, width=4, bg="red")
JU9 = Button(root, state=DISABLED, text="9",  height=1, width=4, bg="red")
JU10 = Button(root, state=DISABLED, text="10",  height=1, width=4, bg="red")
JU11 = Button(root, state=DISABLED, text="11",  height=1, width=4, bg="red")
JU12 = Button(root, state=DISABLED, text="12",  height=1, width=4, bg="red")
JU13 = Button(root, state=DISABLED, text="13",  height=1, width=4, bg="red")
JU14 = Button(root, state=DISABLED, text="14",  height=1, width=4, bg="red")
JU15 = Button(root, state=DISABLED, text="15",  height=1, width=4, bg="red")
JU16 = Button(root, state=DISABLED, text="16",  height=1, width=4, bg="red")
JU17 = Button(root, state=DISABLED, text="17",  height=1, width=4, bg="red")
JU18 = Button(root, state=DISABLED, text="18",  height=1, width=4, bg="red")
JU19 = Button(root, state=DISABLED, text="19",  height=1, width=4, bg="red")
JU20 = Button(root, state=DISABLED, text="20",  height=1, width=4, bg="red")
JU21 = Button(root, state=DISABLED, text="21",  height=1, width=4, bg="red")
JU22 = Button(root, state=DISABLED, text="22",  height=1, width=4, bg="red")
JU23 = Button(root, state=DISABLED, text="23",  height=1, width=4, bg="red")
JU24 = Button(root, state=DISABLED, text="24",  height=1, width=4, bg="red")
JU25 = Button(root, state=DISABLED, text="25",  height=1, width=4, bg="red")
JU26 = Button(root, state=DISABLED, text="26",  height=1, width=4, bg="red")
JU27 = Button(root, state=DISABLED, text="27",  height=1, width=4, bg="red")
JU28 = Button(root, state=DISABLED, text="28",  height=1, width=4, bg="red")
JU29 = Button(root, state=DISABLED, text="29",  height=1, width=4, bg="red")
JU30 = Button(root, state=DISABLED, text="30",  height=1, width=4, bg="red")

JUL1 = Button(root, state=DISABLED, text="1",  height=1, width=4, bg="red")
JUL2 = Button(root, state=DISABLED, text="2",  height=1, width=4, bg="red")
JUL3 = Button(root, state=DISABLED, text="3",  height=1, width=4, bg="red")
JUL4 = Button(root, state=DISABLED, text="4",  height=1, width=4, bg="red")
JUL5 = Button(root, state=DISABLED, text="5",  height=1, width=4, bg="red")
JUL6 = Button(root, state=DISABLED, text="6",  height=1, width=4, bg="red")
JUL7 = Button(root, state=DISABLED, text="7",  height=1, width=4, bg="red")
JUL8 = Button(root, state=DISABLED, text="8",  height=1, width=4, bg="red")
JUL9 = Button(root, state=DISABLED, text="9",  height=1, width=4, bg="red")
JUL10 = Button(root, state=DISABLED, text="10",  height=1, width=4, bg="red")
JUL11 = Button(root, state=DISABLED, text="11",  height=1, width=4, bg="red")
JUL12 = Button(root, state=DISABLED, text="12",  height=1, width=4, bg="red")
JUL13 = Button(root, state=DISABLED, text="13",  height=1, width=4, bg="red")
JUL14 = Button(root, state=DISABLED, text="14",  height=1, width=4, bg="red")
JUL15 = Button(root, state=DISABLED, text="15",  height=1, width=4, bg="red")
JUL16 = Button(root, state=DISABLED, text="16",  height=1, width=4, bg="red")
JUL17 = Button(root, state=DISABLED, text="17",  height=1, width=4, bg="red")
JUL18 = Button(root, state=DISABLED, text="18",  height=1, width=4, bg="red")
JUL19 = Button(root, state=DISABLED, text="19",  height=1, width=4, bg="red")
JUL20 = Button(root, state=DISABLED, text="20",  height=1, width=4, bg="red")
JUL21 = Button(root, state=DISABLED, text="21",  height=1, width=4, bg="red")
JUL22 = Button(root, state=DISABLED, text="22",  height=1, width=4, bg="red")
JUL23 = Button(root, state=DISABLED, text="23",  height=1, width=4, bg="red")
JUL24 = Button(root, state=DISABLED, text="24",  height=1, width=4, bg="red")
JUL25 = Button(root, state=DISABLED, text="25",  height=1, width=4, bg="red")
JUL26 = Button(root, state=DISABLED, text="26",  height=1, width=4, bg="red")
JUL27 = Button(root, state=DISABLED, text="27",  height=1, width=4, bg="red")
JUL28 = Button(root, state=DISABLED, text="28",  height=1, width=4, bg="red")
JUL29 = Button(root, state=DISABLED, text="29",  height=1, width=4, bg="red")
JUL30 = Button(root, state=DISABLED, text="30",  height=1, width=4, bg="red")
JUL31 = Button(root, state=DISABLED, text="31",  height=1, width=4, bg="red")

AU1 = Button(root, state=DISABLED, text="1",  height=1, width=4, bg="red")
AU2 = Button(root, state=DISABLED, text="2",  height=1, width=4, bg="red")
AU3 = Button(root, state=DISABLED, text="3",  height=1, width=4, bg="red")
AU4 = Button(root, state=DISABLED, text="4",  height=1, width=4, bg="red")
AU5 = Button(root, state=DISABLED, text="5",  height=1, width=4, bg="red")
AU6 = Button(root, state=DISABLED, text="6",  height=1, width=4, bg="red")
AU7 = Button(root, state=DISABLED, text="7",  height=1, width=4, bg="red")
AU8 = Button(root, state=DISABLED, text="8",  height=1, width=4, bg="red")
AU9 = Button(root, state=DISABLED, text="9",  height=1, width=4, bg="red")
AU10 = Button(root, state=DISABLED, text="10",  height=1, width=4, bg="red")
AU11 = Button(root, state=DISABLED, text="11",  height=1, width=4, bg="red")
AU12 = Button(root, state=DISABLED, text="12",  height=1, width=4, bg="red")
AU13 = Button(root, state=DISABLED, text="13",  height=1, width=4, bg="red")
AU14 = Button(root, state=DISABLED, text="14",  height=1, width=4, bg="red")
AU15 = Button(root, state=DISABLED, text="15",  height=1, width=4, bg="red")
AU16 = Button(root, state=DISABLED, text="16",  height=1, width=4, bg="red")
AU17 = Button(root, state=DISABLED, text="17",  height=1, width=4, bg="red")
AU18 = Button(root, state=DISABLED, text="18",  height=1, width=4, bg="red")
AU19 = Button(root, state=DISABLED, text="19",  height=1, width=4, bg="red")
AU20 = Button(root, state=DISABLED, text="20",  height=1, width=4, bg="red")
AU21 = Button(root, state=DISABLED, text="21",  height=1, width=4, bg="red")
AU22 = Button(root, state=DISABLED, text="22",  height=1, width=4, bg="red")
AU23 = Button(root, state=DISABLED, text="23",  height=1, width=4, bg="red")
AU24 = Button(root, state=DISABLED, text="24",  height=1, width=4, bg="red")
AU25 = Button(root, state=DISABLED, text="25",  height=1, width=4, bg="red")
AU26 = Button(root, state=DISABLED, text="26",  height=1, width=4, bg="red")
AU27 = Button(root, state=DISABLED, text="27",  height=1, width=4, bg="red")
AU28 = Button(root, state=DISABLED, text="28",  height=1, width=4, bg="red")
AU29 = Button(root, state=DISABLED, text="29",  height=1, width=4, bg="red")
AU30 = Button(root, state=DISABLED, text="30",  height=1, width=4, bg="red")
AU31 = Button(root, state=DISABLED, text="31",  height=1, width=4, bg="red")

S1 = Button(root, state=DISABLED, text="1",  height=1, width=4, bg="red")
S2 = Button(root, state=DISABLED, text="2",  height=1, width=4, bg="red")
S3 = Button(root, state=DISABLED, text="3",  height=1, width=4, bg="red")
S4 = Button(root, state=DISABLED, text="4",  height=1, width=4, bg="red")
S5 = Button(root, state=DISABLED, text="5",  height=1, width=4, bg="red")
S6 = Button(root, state=DISABLED, text="6",  height=1, width=4, bg="red")
S7 = Button(root, state=DISABLED, text="7",  height=1, width=4, bg="red")
S8 = Button(root, state=DISABLED, text="8",  height=1, width=4, bg="red")
S9 = Button(root, state=DISABLED, text="9",  height=1, width=4, bg="red")
S10 = Button(root, state=DISABLED, text="10",  height=1, width=4, bg="red")
S11 = Button(root, state=DISABLED, text="11",  height=1, width=4, bg="red")
S12 = Button(root, state=DISABLED, text="12",  height=1, width=4, bg="red")
S13 = Button(root, state=DISABLED, text="13",  height=1, width=4, bg="red")
S14 = Button(root, state=DISABLED, text="14",  height=1, width=4, bg="red")
S15 = Button(root, state=DISABLED, text="15",  height=1, width=4, bg="red")
S16 = Button(root, state=DISABLED, text="16",  height=1, width=4, bg="red")
S17 = Button(root, state=DISABLED, text="17",  height=1, width=4, bg="red")
S18 = Button(root, state=DISABLED, text="18",  height=1, width=4, bg="red")
S19 = Button(root, state=DISABLED, text="19",  height=1, width=4, bg="red")
S20 = Button(root, state=DISABLED, text="20",  height=1, width=4, bg="red")
S21 = Button(root, state=DISABLED, text="21",  height=1, width=4, bg="red")
S22 = Button(root, state=DISABLED, text="22",  height=1, width=4, bg="red")
S23 = Button(root, state=DISABLED, text="23",  height=1, width=4, bg="red")
S24 = Button(root, state=DISABLED, text="24",  height=1, width=4, bg="red")
S25 = Button(root, state=DISABLED, text="25",  height=1, width=4, bg="red")
S26 = Button(root, state=DISABLED, text="26",  height=1, width=4, bg="red")
S27 = Button(root, state=DISABLED, text="27",  height=1, width=4, bg="red")
S28 = Button(root, state=DISABLED, text="28",  height=1, width=4, bg="red")
S29 = Button(root, state=DISABLED, text="29",  height=1, width=4, bg="red")
S30 = Button(root, state=DISABLED, text="30",  height=1, width=4, bg="red")

O1 = Button(root, state=DISABLED, text="1",  height=1, width=4, bg="red")
O2 = Button(root, state=DISABLED, text="2",  height=1, width=4, bg="red")
O3 = Button(root, state=DISABLED, text="3",  height=1, width=4, bg="red")
O4 = Button(root, state=DISABLED, text="4",  height=1, width=4, bg="red")
O5 = Button(root, state=DISABLED, text="5",  height=1, width=4, bg="red")
O6 = Button(root, state=DISABLED, text="6",  height=1, width=4, bg="red")
O7 = Button(root, state=DISABLED, text="7",  height=1, width=4, bg="red")
O8 = Button(root, state=DISABLED, text="8",  height=1, width=4, bg="red")
O9 = Button(root, state=DISABLED, text="9",  height=1, width=4, bg="red")
O10 = Button(root, state=DISABLED, text="10",  height=1, width=4, bg="red")
O11 = Button(root, state=DISABLED, text="11",  height=1, width=4, bg="red")
O12 = Button(root, state=DISABLED, text="12",  height=1, width=4, bg="red")
O13 = Button(root, state=DISABLED, text="13",  height=1, width=4, bg="red")
O14 = Button(root, state=DISABLED, text="14",  height=1, width=4, bg="red")
O15 = Button(root, state=DISABLED, text="15",  height=1, width=4, bg="red")
O16 = Button(root, state=DISABLED, text="16",  height=1, width=4, bg="red")
O17 = Button(root, state=DISABLED, text="17",  height=1, width=4, bg="red")
O18 = Button(root, state=DISABLED, text="18",  height=1, width=4, bg="red")
O19 = Button(root, state=DISABLED, text="19",  height=1, width=4, bg="red")
O20 = Button(root, state=DISABLED, text="20",  height=1, width=4, bg="red")
O21 = Button(root, state=DISABLED, text="21",  height=1, width=4, bg="red")
O22 = Button(root, state=DISABLED, text="22",  height=1, width=4, bg="red")
O23 = Button(root, state=DISABLED, text="23",  height=1, width=4, bg="red")
O24 = Button(root, state=DISABLED, text="24",  height=1, width=4, bg="red")
O25 = Button(root, state=DISABLED, text="25",  height=1, width=4, bg="red")
O26 = Button(root, state=DISABLED, text="26",  height=1, width=4, bg="red")
O27 = Button(root, state=DISABLED, text="27",  height=1, width=4, bg="red")
O28 = Button(root, state=DISABLED, text="28",  height=1, width=4, bg="red")
O29 = Button(root, state=DISABLED, text="29",  height=1, width=4, bg="red")
O30 = Button(root, state=DISABLED, text="30",  height=1, width=4, bg="red")
O31 = Button(root, state=DISABLED, text="31",  height=1, width=4, bg="red")

N1 = Button(root, state=DISABLED, text="1",  height=1, width=4, bg="red")
N2 = Button(root, state=DISABLED, text="2",  height=1, width=4, bg="red")
N3 = Button(root, state=DISABLED, text="3",  height=1, width=4, bg="red")
N4 = Button(root, state=DISABLED, text="4",  height=1, width=4, bg="red")
N5 = Button(root, state=DISABLED, text="5",  height=1, width=4, bg="red")
N6 = Button(root, state=DISABLED, text="6",  height=1, width=4, bg="red")
N7 = Button(root, state=DISABLED, text="7",  height=1, width=4, bg="red")
N8 = Button(root, state=DISABLED, text="8",  height=1, width=4, bg="red")
N9 = Button(root, state=DISABLED, text="9",  height=1, width=4, bg="red")
N10 = Button(root, state=DISABLED, text="10",  height=1, width=4, bg="red")
N11 = Button(root, state=DISABLED, text="11",  height=1, width=4, bg="red")
N12 = Button(root, state=DISABLED, text="12",  height=1, width=4, bg="red")
N13 = Button(root, state=DISABLED, text="13",  height=1, width=4, bg="red")
N14 = Button(root, state=DISABLED, text="14",  height=1, width=4, bg="red")
N15 = Button(root, state=DISABLED, text="15",  height=1, width=4, bg="red")
N16 = Button(root, state=DISABLED, text="16",  height=1, width=4, bg="red")
N17 = Button(root, state=DISABLED, text="17",  height=1, width=4, bg="red")
N18 = Button(root, state=DISABLED, text="18",  height=1, width=4, bg="red")
N19 = Button(root, state=DISABLED, text="19",  height=1, width=4, bg="red")
N20 = Button(root, state=DISABLED, text="20",  height=1, width=4, bg="red")
N21 = Button(root, state=DISABLED, text="21",  height=1, width=4, bg="red")
N22 = Button(root, state=DISABLED, text="22",  height=1, width=4, bg="red")
N23 = Button(root, state=DISABLED, text="23",  height=1, width=4, bg="red")
N24 = Button(root, state=DISABLED, text="24",  height=1, width=4, bg="red")
N25 = Button(root, state=DISABLED, text="25",  height=1, width=4, bg="red")
N26 = Button(root, state=DISABLED, text="26",  height=1, width=4, bg="red")
N27 = Button(root, state=DISABLED, text="27",  height=1, width=4, bg="red")
N28 = Button(root, state=DISABLED, text="28",  height=1, width=4, bg="red")
N29 = Button(root, state=DISABLED, text="29",  height=1, width=4, bg="red")
N30 = Button(root, state=DISABLED, text="30",  height=1, width=4, bg="red")

D1 = Button(root, state=DISABLED, text="1",  height=1, width=4, bg="red")
D2 = Button(root, state=DISABLED, text="2",  height=1, width=4, bg="red")
D3 = Button(root, state=DISABLED, text="3",  height=1, width=4, bg="red")
D4 = Button(root, state=DISABLED, text="4",  height=1, width=4, bg="red")
D5 = Button(root, state=DISABLED, text="5",  height=1, width=4, bg="red")
D6 = Button(root, state=DISABLED, text="6",  height=1, width=4, bg="red")
D7 = Button(root, state=DISABLED, text="7",  height=1, width=4, bg="red")
D8 = Button(root, state=DISABLED, text="8",  height=1, width=4, bg="red")
D9 = Button(root, state=DISABLED, text="9",  height=1, width=4, bg="red")
D10 = Button(root, state=DISABLED, text="10",  height=1, width=4, bg="red")
D11 = Button(root, state=DISABLED, text="11",  height=1, width=4, bg="red")
D12 = Button(root, state=DISABLED, text="12",  height=1, width=4, bg="red")
D13 = Button(root, state=DISABLED, text="13",  height=1, width=4, bg="red")
D14 = Button(root, state=DISABLED, text="14",  height=1, width=4, bg="red")
D15 = Button(root, state=DISABLED, text="15",  height=1, width=4, bg="red")
D16 = Button(root, state=DISABLED, text="16",  height=1, width=4, bg="red")
D17 = Button(root, state=DISABLED, text="17",  height=1, width=4, bg="red")
D18 = Button(root, state=DISABLED, text="18",  height=1, width=4, bg="red")
D19 = Button(root, state=DISABLED, text="19",  height=1, width=4, bg="red")
D20 = Button(root, state=DISABLED, text="20",  height=1, width=4, bg="red")
D21 = Button(root, state=DISABLED, text="21",  height=1, width=4, bg="red")
D22 = Button(root, state=DISABLED, text="22",  height=1, width=4, bg="red")
D23 = Button(root, state=DISABLED, text="23",  height=1, width=4, bg="red")
D24 = Button(root, state=DISABLED, text="24",  height=1, width=4, bg="red")
D25 = Button(root, state=DISABLED, text="25",  height=1, width=4, bg="red")
D26 = Button(root, state=DISABLED, text="26",  height=1, width=4, bg="red")
D27 = Button(root, state=DISABLED, text="27",  height=1, width=4, bg="red")
D28 = Button(root, state=DISABLED, text="28",  height=1, width=4, bg="red")
D29 = Button(root, state=DISABLED, text="29",  height=1, width=4, bg="red")
D30 = Button(root, state=DISABLED, text="30",  height=1, width=4, bg="red")
D31 = Button(root, state=DISABLED, text="31",  height=1, width=4, bg="red")

XButton = Button(root,command=close, text="X",  height=1, width=4, bg="orange")

######################################################################################################################################################################################################################################################################

outputL.place(x=50, y=700)
outputM.place(x=365, y=825)
outputN.place(x=440, y=827)
outputO.place(x=332, y=850)
outputP.place(x=390, y=900)
outputQ.place(x=460, y=902)
outputR.place(x=200, y=940)

applicationB.place(x=1250, y=850)
infrastructureB.place(x=1585, y=850)

XButton.place(x=1853, y=0)

J1.place(x=316, y=102)
J2.place(x=88, y=128)
J3.place(x=126, y=128)
J4.place(x=164, y=128)
J5.place(x=202, y=128)
J6.place(x=240, y=128)
J7.place(x=278, y=128)
J8.place(x=316, y=128)
J9.place(x=88, y=154)
J10.place(x=126, y=154)
J11.place(x=164, y=154)
J12.place(x=202, y=154)
J13.place(x=240, y=154)
J14.place(x=278, y=154)
J15.place(x=316, y=154)
J16.place(x=88, y=180)
J17.place(x=126, y=180)
J18.place(x=164, y=180)
J19.place(x=202, y=180)
J20.place(x=240, y=180)
J21.place(x=278, y=180)
J22.place(x=316, y=180)
J23.place(x=88, y=206)
J24.place(x=126, y=206)
J25.place(x=164, y=206)
J26.place(x=202, y=206)
J27.place(x=240, y=206)
J28.place(x=278, y=206)
J29.place(x=316, y=206)
J30.place(x=88, y=232)
J31.place(x=126, y=232)

F1.place(x=164, y=332)
F2.place(x=202, y=332)
F3.place(x=240, y=332)
F4.place(x=278, y=332)
F5.place(x=316, y=332)
F6.place(x=88, y=358)
F7.place(x=126, y=358)
F8.place(x=164, y=358)
F9.place(x=202, y=358)
F10.place(x=240, y=358)
F11.place(x=278, y=358)
F12.place(x=316, y=358)
F13.place(x=88, y=384)
F14.place(x=126, y=384)
F15.place(x=164, y=384)
F16.place(x=202, y=384)
F17.place(x=240, y=384)
F18.place(x=278, y=384)
F19.place(x=316, y=384)
F20.place(x=88, y=410)
F21.place(x=126, y=410)
F22.place(x=164, y=410)
F23.place(x=202, y=410)
F24.place(x=240, y=410)
F25.place(x=278, y=410)
F26.place(x=316, y=410)
F27.place(x=88, y=436)
F28.place(x=126, y=436)

M1.place(x=164, y=536)
M2.place(x=202, y=536)
M3.place(x=240, y=536)
M4.place(x=278, y=536)
M5.place(x=316, y=536)
M6.place(x=88, y=562)
M7.place(x=126, y=562)
M8.place(x=164, y=562)
M9.place(x=202, y=562)
M10.place(x=240, y=562)
M11.place(x=278, y=562)
M12.place(x=316, y=562)
M13.place(x=88, y=588)
M14.place(x=126, y=588)
M15.place(x=164, y=588)
M16.place(x=202, y=588)
M17.place(x=240, y=588)
M18.place(x=278, y=588)
M19.place(x=316, y=588)
M20.place(x=88, y=614)
M21.place(x=126, y=614)
M22.place(x=164, y=614)
M23.place(x=202, y=614)
M24.place(x=240, y=614)
M25.place(x=278, y=614)
M26.place(x=316, y=614)
M27.place(x=88, y=640)
M28.place(x=126, y=640)
M29.place(x=164, y=640)
M30.place(x=202, y=640)
M31.place(x=240, y=640)

A1.place(x=778, y=102)
A2.place(x=816, y=102)
A3.place(x=588, y=128)
A4.place(x=626, y=128)
A5.place(x=664, y=128)
A6.place(x=702, y=128)
A7.place(x=740, y=128)
A8.place(x=778, y=128)
A9.place(x=816, y=128)
A10.place(x=588, y=154)
A11.place(x=626, y=154)
A12.place(x=664, y=154)
A13.place(x=702, y=154)
A14.place(x=740, y=154)
A15.place(x=778, y=154)
A16.place(x=816, y=154)
A17.place(x=588, y=180)
A18.place(x=626, y=180)
A19.place(x=664, y=180)
A20.place(x=702, y=180)
A21.place(x=740, y=180)
A22.place(x=778, y=180)
A23.place(x=816, y=180)
A24.place(x=588, y=206)
A25.place(x=626, y=206)
A26.place(x=664, y=206)
A27.place(x=702, y=206)
A28.place(x=740, y=206)
A29.place(x=778, y=206)
A30.place(x=816, y=206)

MA1.place(x=588, y=332)
MA2.place(x=626, y=332)
MA3.place(x=664, y=332)
MA4.place(x=702, y=332)
MA5.place(x=740, y=332)
MA6.place(x=778, y=332)
MA7.place(x=816, y=332)
MA8.place(x=588, y=358)
MA9.place(x=626, y=358)
MA10.place(x=664, y=358)
MA11.place(x=702, y=358)
MA12.place(x=740, y=358)
MA13.place(x=778, y=358)
MA14.place(x=816, y=358)
MA15.place(x=588, y=384)
MA16.place(x=626, y=384)
MA17.place(x=664, y=384)
MA18.place(x=702, y=384)
MA19.place(x=740, y=384)
MA20.place(x=778, y=384)
MA21.place(x=816, y=384)
MA22.place(x=588, y=410)
MA23.place(x=626, y=410)
MA24.place(x=664, y=410)
MA25.place(x=702, y=410)
MA26.place(x=740, y=410)
MA27.place(x=778, y=410)
MA28.place(x=816, y=410)
MA29.place(x=588, y=436)
MA30.place(x=626, y=436)
MA31.place(x=664, y=436)

JU1.place(x=702, y=536)
JU2.place(x=740, y=536)
JU3.place(x=778, y=536)
JU4.place(x=816, y=536)
JU5.place(x=588, y=562)
JU6.place(x=626, y=562)
JU7.place(x=664, y=562)
JU8.place(x=702, y=562)
JU9.place(x=740, y=562)
JU10.place(x=778, y=562)
JU11.place(x=816, y=562)
JU12.place(x=588, y=588)
JU13.place(x=626, y=588)
JU14.place(x=664, y=588)
JU15.place(x=702, y=588)
JU16.place(x=740, y=588)
JU17.place(x=778, y=588)
JU18.place(x=816, y=588)
JU19.place(x=588, y=614)
JU20.place(x=626, y=614)
JU21.place(x=664, y=614)
JU22.place(x=702, y=614)
JU23.place(x=740, y=614)
JU24.place(x=778, y=614)
JU25.place(x=816, y=614)
JU26.place(x=588, y=640)
JU27.place(x=626, y=640)
JU28.place(x=664, y=640)
JU29.place(x=702, y=640)
JU30.place(x=740, y=640)

JUL1.place(x=1278, y=102)
JUL2.place(x=1316, y=102)
JUL3.place(x=1088, y=128)
JUL4.place(x=1126, y=128)
JUL5.place(x=1164, y=128)
JUL6.place(x=1202, y=128)
JUL7.place(x=1240, y=128)
JUL8.place(x=1278, y=128)
JUL9.place(x=1316, y=128)
JUL10.place(x=1088, y=154)
JUL11.place(x=1126, y=154)
JUL12.place(x=1164, y=154)
JUL13.place(x=1202, y=154)
JUL14.place(x=1240, y=154)
JUL15.place(x=1278, y=154)
JUL16.place(x=1316, y=154)
JUL17.place(x=1088, y=180)
JUL18.place(x=1126, y=180)
JUL19.place(x=1164, y=180)
JUL20.place(x=1202, y=180)
JUL21.place(x=1240, y=180)
JUL22.place(x=1278, y=180)
JUL23.place(x=1316, y=180)
JUL24.place(x=1088, y=206)
JUL25.place(x=1126, y=206)
JUL26.place(x=1164, y=206)
JUL27.place(x=1202, y=206)
JUL28.place(x=1240, y=206)
JUL29.place(x=1278, y=206)
JUL30.place(x=1316, y=206)
JUL31.place(x=1088, y=232)

AU1.place(x=1126, y=332)
AU2.place(x=1164, y=332)
AU3.place(x=1202, y=332)
AU4.place(x=1240, y=332)
AU5.place(x=1278, y=332)
AU6.place(x=1316, y=332)
AU7.place(x=1088, y=358)
AU8.place(x=1126, y=358)
AU9.place(x=1164, y=358)
AU10.place(x=1202, y=358)
AU11.place(x=1240, y=358)
AU12.place(x=1278, y=358)
AU13.place(x=1316, y=358)
AU14.place(x=1088, y=384)
AU15.place(x=1126, y=384)
AU16.place(x=1164, y=384)
AU17.place(x=1202, y=384)
AU18.place(x=1240, y=384)
AU19.place(x=1278, y=384)
AU20.place(x=1316, y=384)
AU21.place(x=1088, y=410)
AU22.place(x=1126, y=410)
AU23.place(x=1164, y=410)
AU24.place(x=1202, y=410)
AU25.place(x=1240, y=410)
AU26.place(x=1278, y=410)
AU27.place(x=1316, y=410)
AU28.place(x=1088, y=436)
AU29.place(x=1126, y=436)
AU30.place(x=1164, y=436)
AU31.place(x=1202, y=436)

S1.place(x=1240, y=536)
S2.place(x=1278, y=536)
S3.place(x=1316, y=536)
S4.place(x=1088, y=562)
S5.place(x=1126, y=562)
S6.place(x=1164, y=562)
S7.place(x=1202, y=562)
S8.place(x=1240, y=562)
S9.place(x=1278, y=562)
S10.place(x=1316, y=562)
S11.place(x=1088, y=588)
S12.place(x=1126, y=588)
S13.place(x=1164, y=588)
S14.place(x=1202, y=588)
S15.place(x=1240, y=588)
S16.place(x=1278, y=588)
S17.place(x=1316, y=588)
S18.place(x=1088, y=614)
S19.place(x=1126, y=614)
S20.place(x=1164, y=614)
S21.place(x=1202, y=614)
S22.place(x=1240, y=614)
S23.place(x=1278, y=614)
S24.place(x=1316, y=614)
S25.place(x=1088, y=640)
S26.place(x=1126, y=640)
S27.place(x=1164, y=640)
S28.place(x=1202, y=640)
S29.place(x=1240, y=640)
S30.place(x=1278, y=640)

O1.place(x=1816, y=102)
O2.place(x=1588, y=128)
O3.place(x=1626, y=128)
O4.place(x=1664, y=128)
O5.place(x=1702, y=128)
O6.place(x=1740, y=128)
O7.place(x=1778, y=128)
O8.place(x=1816, y=128)
O9.place(x=1588, y=154)
O10.place(x=1626, y=154)
O11.place(x=1664, y=154)
O12.place(x=1702, y=154)
O13.place(x=1740, y=154)
O14.place(x=1778, y=154)
O15.place(x=1816, y=154)
O16.place(x=1588, y=180)
O17.place(x=1626, y=180)
O18.place(x=1664, y=180)
O19.place(x=1702, y=180)
O20.place(x=1740, y=180)
O21.place(x=1778, y=180)
O22.place(x=1816, y=180)
O23.place(x=1588, y=206)
O24.place(x=1626, y=206)
O25.place(x=1664, y=206)
O26.place(x=1702, y=206)
O27.place(x=1740, y=206)
O28.place(x=1778, y=206)
O29.place(x=1816, y=206)
O30.place(x=1588, y=232)
O31.place(x=1626, y=232)

N1.place(x=1664, y=332)
N2.place(x=1702, y=332)
N3.place(x=1740, y=332)
N4.place(x=1778, y=332)
N5.place(x=1816, y=332)
N6.place(x=1588, y=358)
N7.place(x=1626, y=358)
N8.place(x=1664, y=358)
N9.place(x=1702, y=358)
N10.place(x=1740, y=358)
N11.place(x=1778, y=358)
N12.place(x=1816, y=358)
N13.place(x=1588, y=384)
N14.place(x=1626, y=384)
N15.place(x=1664, y=384)
N16.place(x=1702, y=384)
N17.place(x=1740, y=384)
N18.place(x=1778, y=384)
N19.place(x=1816, y=384)
N20.place(x=1588, y=410)
N21.place(x=1626, y=410)
N22.place(x=1664, y=410)
N23.place(x=1702, y=410)
N24.place(x=1740, y=410)
N25.place(x=1778, y=410)
N26.place(x=1816, y=410)
N27.place(x=1588, y=436)
N28.place(x=1626, y=436)
N29.place(x=1664, y=436)
N30.place(x=1702, y=436)

D1.place(x=1740, y=536)
D2.place(x=1778, y=536)
D3.place(x=1816, y=536)
D4.place(x=1588, y=562)
D5.place(x=1626, y=562)
D6.place(x=1664, y=562)
D7.place(x=1702, y=562)
D8.place(x=1740, y=562)
D9.place(x=1778, y=562)
D10.place(x=1816, y=562)
D11.place(x=1588, y=588)
D12.place(x=1626, y=588)
D13.place(x=1664, y=588)
D14.place(x=1702, y=588)
D15.place(x=1740, y=588)
D16.place(x=1778, y=588)
D17.place(x=1816, y=588)
D18.place(x=1588, y=614)
D19.place(x=1626, y=614)
D20.place(x=1664, y=614)
D21.place(x=1702, y=614)
D22.place(x=1740, y=614)
D23.place(x=1778, y=614)
D24.place(x=1816, y=614)
D25.place(x=1588, y=640)
D26.place(x=1626, y=640)
D27.place(x=1664, y=640)
D28.place(x=1702, y=640)
D29.place(x=1740, y=640)
D30.place(x=1778, y=640)
D31.place(x=1816, y=640)

######################################################################################################################################################################################################################################################################################

root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("Release Calculator")
root.configure(bg="white", highlightthickness=15, highlightcolor= "black")
root.mainloop()
