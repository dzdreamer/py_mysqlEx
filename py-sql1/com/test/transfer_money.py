# -*- coding: UTF-8 -*-  
'''
Created on 2017年5月28日 @author: Administrator
'''

if _name_=="_main_":
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]
    
    conn = MySQLdb.Connect(host='127.0.0.1',user='root',passwd='bsker',port=3306,db='pysql')
    
    tr_money = TransferMoney(conn)
    
    try:
        tr_money.transfer(source_acctid,target_acctid,money)
    except Exception as e:
        print "Oops,there is a problem!!"+ str(e)
    finally:
        conn.close()