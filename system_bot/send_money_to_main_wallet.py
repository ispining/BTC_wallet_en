import datetime

import iluxaMod as ilm
from config import *


brokens = []
while True:
    database = ilm.postgreSQL_connect(
        user="postgres",
        password="armageddon",
        database="anonym_wallet",
        host="illyashost.ddns.net"
    )
    #database.init_DB(stages=True, sub=True, staff=True, settings=True, balance=True)
    db = database.db
    sql = database.sql
    glob_wif = database.settings("global_wif")
    pw = PayedWifs()
    print(Wallet(glob_wif).get_balance("usd"))
    for wif_info in pw.get():
        wif, user_id, amount = (wif_info[0], wif_info[1], wif_info[2])
        try:
            print(datetime.datetime.now())
            print(f"[+] Detected new payment ({str(amount)}$)")
            w = Wallet(wif)
            tr_id = w.send(Wallet(glob_wif).get_address(), int(round(float(amount))/2), "usd", Wallet(glob_wif).get_address())
            print(tr_id)
            if tr_id.split(" ")[0].lower() != "Balance is less then mount for send".split(" ")[0].lower():
                print(f"[+] {str(amount)}$ sended to global_wallet")
                pw.wif = wif
                pw.remove()

        except:
            if wif not in brokens:
                brokens.append(wif)
            else:
                brokens.remove(wif)
                pw.wif = wif
                pw.remove()


        print()






