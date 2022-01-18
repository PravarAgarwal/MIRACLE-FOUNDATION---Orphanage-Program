print(".............................................................INDEX........................................................")
print()
print()
print()
print(" 1. ABOUT")
print(" 2. ADOPTION CRITERION")
print(" 3. FUNDS")
print(" 4. STUDENTS INFO.")
print(" 5. WORKERS INFO.")


ans = str(input("Start the program? (y/n): "))
if ans == 'n':
    exit()
print (end='\n')

print ('                 MIRACLE FOUNDATION          ')
print ('                   New Delhi - 91            ')
print (end='\n')


print ('''Impossible is just an opinion 
                          -Paulo Coehlo
                          ''')

print ('''We know the very best thing for a child is to be part of a loving
family—it’s where they thrive. That’s why everything we do is
designed to accomplish just that.

Our goal is a loving family and the end of institutionalized care for every
child. Period. We believe that, together, we can change the way we care for
children and help to get them into stable, loving, nurturing environments.
We believe in them, in you and in Miracles. We believe in a world that
listens closely to children and gives them a voice.

Miracle Foundation is a Delhi-based non-profit that
brings life-changing care to orphaned and vulnerable children. And that’s
just the beginning. By 2040, we fully intend to be out of business. Why?
Because we know that together we can achieve miracles. We can transition
every institutionalized child into a loving family in our lifetime.

These children deserve the very best. A way out of their past of abandonment
and a way forward into their bright future. We believe in partnerships, and
with generous gifts from people like you, we can make their dream of living
with a family a reality. Sound impossible? Thankfully, that’s just an opinion.''')

#Adoption Criteria

print ('''In the heart of every child is a hunger for home.
Not just for food and a place to sleep, but for safety and
community. Most importantly: for love. At the Miracle Foundation,
we are much more than a home for unwanted Indian orphans.

But it's always a wonderful sight to see the eyes of a kid
glitter with joy when they have, afer such unfairness, someone
to call as their parents.
''')
adop = str(input('Do you want to know about the adoption eligibility? (y/n) :'))
if adop == 'n':
    pass
elif adop == 'y':
    print ('''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

In India, the adoption process is monitored by Central Adoption
Resource Authority (CARA) which is the nodal agency to monitor and
regulate in-country and intra-country adoption and is a part of
Ministry of women and child care. Following are the basic conditions
which need to be satisfied by the adopting parents in order to be
eligible to adopt a child:

1) A child in India can be adopted by an Indian citizen, NRI
or a foreign citizen. The procedure of adoption is different for
all three.

2) Any person is eligible to adopt irrespective of their gender
or marital status.

3) In case a couple is adopting a child, they should have completed
at least two years of stable marriage and should have a joint
consensus for adoption of the child.

4) The age difference between the child and the adoptive parents
should not be less than 25 years.
''')

adopt = str(input("Are you willing to adopt a child? (y/n): "))
if adopt == 'y':
    print ('''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Congratulations! You're on your way to a good step in life.

Your interest shows that you are really ecstatic for the
adoption, but in reality, there are certain procedures and
guidelines that need to be followed in order to adopt a
child. Let's know if you're ready or not...
''')

    kil = 0
    crit1 = str(input('Are you a male/female or non-binary? (m/f/n) : '))

    if crit1 == 'm' or crit1 == 'M' or crit1 == 'f' or crit1 == 'F' or crit1 == 'n' or crit1 == 'N':
                kil=kil+1
    else :
            True
            
    crit2 = int(input('What is your age? :'))
    if crit2 >= 25:
                kil+=1
    else:
            True
        
    crit3 = int(input('How long has your marriage been?'))
    if crit3 >= 3:
                kil+=1
    else:
            True
    if kil == 3:
        print('You are eligible to adopt a child :)')
    else:
        print('sorry you are not eligible to adpot a child')
else :
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        

a=float(input("If you want to help us by your donations please enter the amount,Enter 0 to skip:"))
e=0
f=0
s=0
if a <= 100 :
    f=a
    e=s=0
elif a >= 100 and a < 1000 :
    e=(1/2)*a
    f=a-e
    s=0
elif a >= 1000 and a < 5000 :
    e=(1/2)*a
    f=(3/8)*a
    s=(1/8)*a
elif a >= 5000 and a <= 10000 :
    e=(3/4)*a
    f=(1/8)*a
    s=f
else :
    e=(3/4)*a
    f=(1/8)*a
    s=f
print("Thank You for your kindness and selflesness :)")
print ("We ensure transparency in our processes and that's \n we want you to know how your donations help us:- ")
print("Education: Rs",e,"\nFood and Lifestyle: Rs",f,"\nInfrastructural Building",s)
    



#WORKERS AND STUDENTS INFO:

import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="pravar",database="orphanage")
if mycon.is_connected():
    print("CONNECTION ESTABLISHED WITH MYSQL")
cursor =mycon.cursor()
st = "insert into students(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(1,'RAMU',5,'M','2014-05-11')
cursor.execute(st)
st1="insert into students(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(2,'SHAMU',8,'M','2011-12-13')
cursor.execute(st1)
st2="insert into students(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(3,'HARI',11,'M','2008-01-02')
cursor.execute(st)
st3="insert into students(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(4,'KISHAN',12,'M','2007-07-07')
cursor.execute(st3)
st4="insert into students(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(5,'OM',4,'M','2015-04-30')
cursor.execute(st4)
st5="insert into students(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(6 ,'TIMMY',9,'M','2010-07-23')
cursor.execute(st5)
st6="insert into students(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(7,'RADHA',11,'F','2008-08-21')
cursor.execute(st6)
st7="insert into students(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(8,'GEETA',16,'F','2003-02-20')
cursor.execute(st7)
st8="insert into students(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(9,'RANJANA',14,'F','2005-06-06')
cursor.execute(st8)
st9="insert into students(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(10,'SWAPNIL',7,'F','2012-03-29')
cursor.execute(st9)
st10="insert into students(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(11,'RENU',2,'F','2017-07-31')
cursor.execute(st10)
st11="insert into students(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(12,'APARNA',5,'F','2014-05-15')
cursor.execute(st11)


w = "insert into workers(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(1,'KAMLA',25,'F','1996-05-16')
cursor.execute(w)
w1 = "insert into workers(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(2,'JAYA',30,'F','1989-08-11')
cursor.execute(w1)
w2 = "insert into workers(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(3,'SUSHMA',27,'F','1992-09-19')
cursor.execute(w2)
w3 = "insert into workers(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(4,'FATHIMA',35,'F','1984-03-30')
cursor.execute(w3)
w4 = "insert into workers(s_no,name,age,gender,DOB)values({},'{}','{}','{}','{}')".format(5,'RAJU',24,'M','1995-07-14')
cursor.execute(w4)

mycon.commit()

print()

p=str(input("are you first time using this programme ? (y,n)"))
if p =="n":
    cursor.execute("delete from students limit 12")
    cursor.execute("delete from workers limit 5")
    mycon.commit()
else:
    pass
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print()

b=str(input("Do you want to know about our WORKERS ?(y,n)"))
if b=='y' or b=='Y':
    cursor.execute("select * from workers")
    data = cursor.fetchall()
    count = cursor.rowcount

    print("total number of rows : ",count)
    print()
    for row in data:
        print(row)
else:
    pass
print()
c=str(input("Do you want to know about our STUDENTS ?(y,n)"))
if c=="y" or c=="Y":
     cursor.execute("select * from students")
     data = cursor.fetchall()
     count = cursor.rowcount

     print("total number of rows : ",count)
     print()
     for row in data:
         print(row)
else:
    pass
