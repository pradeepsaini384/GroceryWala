import mysql.connector
import random

# conn = mysql.connector.connect(host = "134.119.205.13",user= "wingogam_admin",password ="iAJ#D=Btre9O",database="wingogam_blog")
conn = mysql.connector.connect(host = "localhost",user= "root",password ="",database="juhacks")
cursor = conn.cursor()

def email_auth(email):
    done = 1
    cursor.execute("""SELECT * FROM `email_subs` WHERE `email` LIKE '{}' """.format(email))
    popular = cursor.fetchall()
    if len(popular)>0:
        return done
    else:
        cursor.execute("""INSERT INTO `email_subs` (`email`) VALUES('{}')""".format(email))
        conn.commit()
        done = 0
        return done
    
def authentication(email,password):
    cursor.execute("""SELECT * FROM `user` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users = cursor.fetchall()
    return users

def registration(name,email,password):
    cursor.execute("""INSERT INTO `user` (`name`,`email`,`password`) VALUES ('{}','{}','{}')""".format(name,email,password))
    conn.commit()
    done = 1
    return done

    
def shop_bakery():
    cursor.execute("""SELECT * FROM `bakery` """)
    users = cursor.fetchall()
    return users
def dairy_data():
    cursor.execute("""SELECT * FROM `dairy_prod` """)
    users = cursor.fetchall()
    return users
def grocey_data():
    cursor.execute("""SELECT * FROM `bakery` """)
    users = cursor.fetchall()
    return users


def popular_prods():
        cursor.execute("""SELECT * FROM `bakery` WHERE `sub_category` LIKE 'popular' """)
        users = cursor.fetchall()
        
        return users
def dairy_prods():
        cursor.execute("""SELECT * FROM `bakery` WHERE `sub_category` LIKE 'daily' """)
        users = cursor.fetchall()
        
        return users
def fresh_vegi():
        cursor.execute("""SELECT * FROM `fresh_veg` """)
        users = cursor.fetchall()
        
        return users



def add_produc(title,price,p_price,Category,sub_Category,img_path):
    lst = ['g','r','o','c','1','2','3','4']
    id = ''
    for i in lst:
        id = id + str(random.choice(lst))
    vendor_name = 'pradeep'
    if Category=='Vegetables':
        print('enter')
        cursor.execute("""INSERT INTO `fresh_veg` (`p_id`,`p_name`,`vendor_name`,`price`,`category`,`sub_category`,`img_path`,`offer_price`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')""".format(id,title,vendor_name,price,Category,sub_Category,img_path,p_price))
        conn.commit()
        done = 1
        return done