
import datetime

start = ['3', '4', '5', '6']


def date_validation(aasta, kuu, kp):
    isValidDate = True
    try:
        datetime.datetime(int(aasta), int(kuu), int(kp))
    except ValueError:
        isValidDate = False
    if isValidDate == False:
        return False


def if_validation(ik):
    check_summ = (1 * int(ik[0]) + 2 * int(ik[1]) + 3 * int(ik[2]) + 4 * int(ik[3]) + 5 * int(ik[4]) + 6 * int(
        ik[5]) + 7 * int(ik[6]) + 8 * int(ik[7]) + 9 * int(ik[8]) + 1 * int(ik[9])) % 11
    # print(check_summ, int(ik[10]))
    if check_summ != int(ik[10]):
        return False
    else:
        # print("ok!")
        return True


def ikood(ik):
    # print(ik)
    global aasta
    # print(ik)
    # try:
    ik = str(ik)
    if len(ik) != 11:
        return False
        # print("Vale pikkus!")
    if ik[0] not in start:
        return False
        # print("Vale isikukood!")
    if ik[0] in ['3', '4']:
        aasta = '19' + ik[1] + ik[2]
        # print(aasta)
    if ik[0] in ['5', '6']:
        aasta = '20' + ik[1] + ik[2]

    kuu = ik[3] + ik[4]
    # print(kuu)
    kp = ik[5] + ik[6]
    # print(kp)
    if if_validation(ik):
        date_validation(aasta, kuu, kp)
        return True


    # except Exception as e:
    #     print(f"Sisestasite vale isikukood - Error:     {e}")

# print(ikood('38410103729'))