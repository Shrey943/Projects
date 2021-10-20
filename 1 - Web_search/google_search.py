# Please install following 2 packages in cmd prompt / command line

#pip install beautifulsoup4

#pip install google

try:
    from googlesearch import search

except ImportError:
    print("No module named 'google' found")

# to search
a="Y"
while a=="Y":
    query = input("Enter your query :  ")

    try:
        for i in search(query, tld="com", num=10, stop=10, pause=2):
            print("\n",i)
    except:
       print("Something went wrong, please check your internet connection!")

    b=input("\n Do you want to continue? (Y/N) : ")
    b=b.upper()

    while b!="N" and b!="Y":
        c = input("Enter  only between Y or N: ")
        b = c.upper()

    else:
        if  b=="N":
            break
        elif b=="Y":
            continue







