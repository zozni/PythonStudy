import time

input("엔터를 누르고 20초를 셉니다.")
start = time.time()

input("again press the enter key after 20sec.")
end = time.time()

et = end - start
print ("real time:" , et, "sec")
print ("difference:", abs(et - 20), "sec")
