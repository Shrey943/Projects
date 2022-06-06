// Python - MySQL connector

import mysql.connector as m
con=m.connect(host="localhost",user="root",passwd="shrey",database="shrey")
if con.is_connected():
    print("Welcome to Electronic store")
def display():

                st="select * from store"
                cursor=con.cursor()
                cursor.execute(st)

                data=cursor.fetchall()
                for x in data:
                                print (x)
                

def updation():
                
                cursor=con.cursor()
                n=int(input("Enter product id to be updated"))
                c=input("Enter new product name")
                r=input("Enter new product brand")
                x=int(input("Enter new product quantity"))


                st="update store set p_id={},p_name={},brand={},quantity={} where p_id={}".format(n,c,r,x,n)
                cursor.execute(st)
                con.commit()
                print("Product updated successfully")
                
def searching():

                n=input("Enter product id")
                st="select * from store where p_id=%s"%(n,)
                cursor=con.cursor()
                cursor.execute(st)
                data=cursor.fetchall()
                for x in data:
                    print(x)

    
def insertion():


                cursor=con.cursor()
                n=int(input("Enter product id"))
                c=input("Enter product name")
                v=input("Enter product brand")
                b=int(input("Enter product quantity"))

                st="insert into store values({},{},{},{})".format(n,c,v,b)
                cursor.execute(st)
                con.commit()
                print("Product inserted successfully")
    
def deletion():
                
                cursor=con.cursor()
                n=input("Enter product id for deletion")
                

                st="delete from store where p_id={}".format(n)
                cursor.execute(st)
                con.commit()
                print("Product deleted successfully")
ch='Y'
while ch=='Y':
                print("""Press 1 to Display list of products
Press 2 for Insertion
Press 3 for Updation
Press 4 for Searching
Press 5 for Deletion""")
                choice=int(input("Enter Choice"))
                if choice==1:
                                display()
                elif choice==2:
                                insertion()
                elif choice==3:
                                updation()
                elif choice==4:
                                searching()
                elif choice==5:
                                deletion()
                else:
                            print("invalid Choice")
                ch1=input("Do you want to continue?(y/n)")
                ch  =ch1.upper()

                
