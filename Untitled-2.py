
'''
print("mostafa ")
sum = 1
min=3
print(sum + min) 
if(100>=90): 
    print("good")
  
else :
    print ("not good") 


print(f"{sum} me this is sum ")

x="mostafa"
z= "tarawneh"
print(f"{x} {z} king odf people ")
#############################################
# ----------------- IF Statment----------------

if False :
    print("the if is true")
    print("this is code block ")

answer = "correct"
if answer == "correct" :
    print("this is correct answer ")
    
password = 50 
if password ==50 :
    print("the login process sucess")    

password = 100

if password != 50 :
    print("this is uncorrect pass")    

ava= True

if ava :
    print("this is available")

if not ava :
    print("this person not available")    

num = 99
if num >=100 :
    print("the num bigger than 100")    
else :
    print("the num less than 100")

hour = 9 
if hour > 12 :
    print("good evening")    
elif hour < 12 :
    print ("good morning")

#-------------Complex Diction----------------#

age = 17 
is_promit = True
if age >= 18 and is_promit :
    print ("he can drive")
elif age < 18 or not is_promit :
    print("he cant drive ")
    
else :
    print("go out")

#------------------------- self assgin ----------------

name = "mostafa"
name = name + " Tarawneh" 
name = name +" is he a king "
print (name) 
###############
num = 1
num =num +1 
num = num +4 
print(num)
num += 1
print(f"new num  {num}")
num -= 5
print(f"new num  {num}") 
###########################lOOPS ######################3

#while False :
 #   print("the bloinare mostafa") 

keep_print = True 
 
#while keep_print == True :
 #   print ("hello one time")
  #  keep_print = False 
#print ("the while is stoped ")    
n= 1
#while keep_print == True :
 #   if n <= 10 :
  #      print (n)
   #     n += 1
        
    #else :
     #   print (f"this is a print {n} times")
k=0
this = True
#while this :
 #   print(k)
  #  k += 1
   # if k >20 :
    #    this = False
counter = 1

#while counter < 4 :
 #   print(counter)
  #  counter += 1            
#while counter < 55 : 
    #print(counter)
    #counter+=5
###################3 FOR LOOPS ##############

#for i in range (5):
 #   print("mostafa")
#for i in range(5) :
 #   print("round : ")
  #  print(i)
#line = ""   
#for i in range (3) :
 #     line = line + "*"
  #    print (line)         

###################LIST###############
'''
'''
my_first_list = ["mostafa","abed","tarawneh"]
print (my_first_list)
print (my_first_list[0])
print (my_first_list[1])
print (my_first_list[2])
my_first_list[2] = "king"
print(my_first_list)'''
'''
todo=[1,10,15]
todo.append(55)
print (todo)'''

'''
king =["abdulaah ", "ali", "hussan"]

king.append("saddam")

print(king)
'''
'''
todo = ["mostafa","abed","tarawneh"]
todo.append("mones")
todo.insert(0,"arrrhab")#لاضافة عنصر في همكان معين 
print(todo)

todo.pop() #لحذف اخر عنصر من ال اليست 
print(todo)'''
'''
todo=[55,22,44,77,66,8520]
todo.append("king")
todo.insert(2,"ti2")
print(todo)
removed=todo.pop(1)
print(todo)
print(removed)
print(todo[1])
'''

'''
#for i in todo :
 #   print (i)
print(len(todo)) #هاذا بتعرف كم في عنصر داخل الليست '''

#todo =[1,5,445,8,9]
''' 
max_num = max(todo)
min_num = min(todo)
print(max_num,min_num)'''
#todo.sort() #للترتيب العناصر داخل الليست من اللاقل الى الاعلى 
#print(todo)
#print(sum(todo))
######################## compain two datalist#################3
'''todo2=[5,6,6,67]
all_list = todo+todo2
print(all_list)

todo3=[444,5,6,68,"mostafa",mostafa"]
print(all_list+todo3)
'''
'''todo3=[444,5,6,68,"mostafa","mostafa"]
print(todo3.count("mostafa")) # هاذي الداله تبين كم مره تكرر العنصر في الليست 
print(68 in todo3) #هاذي تبين اذا كان العنصر موجود ضمن الليست '''

############################################

#names = "mostafa abedessalam tarawneh"########
#new_name_list= names.split()                 #
#new_name_list= names.split(",")              # تستخدم لتحويل النص العادي الى ليست 
#print(new_name_list)##########################
'''my_name = "mostafa al qatawneh"
new_name=my_name.replace("qatawneh","tarawneh")#تستخدم لتبديل بين الكلمات داخل السترنق
print(my_name)
print(new_name)'''
################################### function###########################
'''
def greet_user () :
    print("hello user")
    print("hello mostafa")


def cal_sum () :
    n =[1,2,3,4,5,6,78,9]
    print(sum(n))
    

greet_user()    
cal_sum()

def printo_stars () :
    print("******************")
printo_stars()

def greet_your_name(name):
    print("hello "+name)

greet_your_name("mostafa")

def cal_sum_two(n):
    sum = n / 2
    print(sum)  

cal_sum_two(10)'''
##################### return value in function ###############3   
'''
def add_10(n):
    end= n+10
    return end
 
r = add_10(5)
print(r)


def add_10_2(n):# هذه الفنكشن ترجع none  لانه ما في ريترن وبالعاده كل الفن هيك
    end= n+10
    print(end)
 
print(add_10_2(8))

def user_signup (user):
    user_status = user + " sign up sucess"
    return user_status

print(user_signup("mostafa"))

def pound2Kg(weight): #---> this convert from pound to Kg
    rs = weight * 0.45359237 
    rs2 =  f"{rs} <---this is your weight in Kg"
    return rs2

print(pound2Kg(180))

def Kg2pound (num):#---> this convert from Kg to Pound
    #Pounds = Kilograms * 2.20462262
    p= num * 2.20462262
    p2 = f"{p} <----- this is your weight in pound "
    return p2 


print(Kg2pound(88))


###### multible parameter #######

def add_team_player(firstname,secendname): #--->this add team 
    plname=print ("this is your team name " + firstname +" "+secendname)
    return plname

print(add_team_player("mostafa","tarawneh"))'''

################ variable and function scope ###################### 
'''
def mos(nam):
    like = nam +10# this is a local scope that we cant use it out side function 
    print(like)

mos(50)

k = 10 
def king (m):
    m+=k # here we use a variable "k" as a global var 
    print (m)
    
king(8)


def low_batt (level) :
    if level <= 20 :
        print(f"the battery level is {level} low ")


def show_name_online (list) :
    print(f"this is online users : {list}")

m=["mostafa ahmed ali"]
show_name_online(m)

def person_info(list):
    print(f"your info : {list}")

person_info(m)

def pr_star(numstar):
    counter=1
    while counter <=numstar :
        print("*")
        counter+=1
        
pr_star(5)

def display_progress(file):
    for i in range(file) :
        print(f"downloading file {i} of {file}")        

display_progress(9)    

def list_price (list):
    for p in list :
        print(p)    
        
lsit=[55,47,99]
list_price(lsit)       

def pla_track (musics):
    for music in musics :
        print (music)
        print("------")
music=["kazzem","ahmed","omr"]

pla_track(music)


def p():
    if True :
        print("hige")
    else :
        print("no")
'''

######## Tuples , Dictionaries ########
'''
mostafa_data = ("mostafa",1999) # this is a tuple data that let you to group different pices of data belongs togother
print(mostafa_data)

list=[("mostafa",1999),"ahmed", "ali"]
print(list)

#التيوبل مفيدا جدا لانه بتسمح النا نرجع من اليست اكثر من قيمه وكمان مثلها مثل الليست بس الفرق انه اتيبول ما بتعدل على القيمه 
def show_ls(L):
    
    print(f"this is all ls : {L}")

list = [("mostafa",1999,"canda","imgration","alkarak",17,"nov"),("someone",2002,2,"tripple maker")]

show_ls(list[0])

def analyze_profit(gains,expanses):
    profit = gains-expanses
    after_taxes = 0.85 * profit
    above_mean = profit > 1000
    return profit,after_taxes,above_mean

insight=analyze_profit(500,1000) 

print(f"this is profit {insight[0]}")
print(f"this is after taxes {insight[1]}")
print(f"this is above_mean {insight[2]}") '''

################### creating dictionaries ###############


    

 