from random import randint
# import matplotlib.pyplot as plt
ganhou = 0
ganhous =[]
for x in range (1281):
    a = randint(1,3)
    # if(a==1):
    #     # print("Escolheu 1")
    #     # print("Abrindo porta 3")
        
    # if(a == 2):
    #     # print("Escolheu 2")
    #     # print("Abrindo porta 1")
    # if(a == 3):
    #     # print("Escolheu 3")
    #     # print("Abrindo porta 1")

    trocar = 1
    if(trocar == 1):
        if( a == 1):
            b = 2
        if( a == 2):
            b = 1
        if (a == 3):
            b = 2
    else:
        b = a

    if( b == 2 ):
        # print("ganhou!!!!!")
        ganhou+=1
    
    if(x == 1):
        print(ganhou,x)
        ganhous.append(ganhou*100/1)
    if(x == 2):
        ganhous.append(ganhou*100/2)
    if(x == 3):
        ganhous.append(ganhou*100/3)
    if(x == 4):
        ganhous.append(ganhou*100/4)
    if(x == 5):
        ganhous.append(ganhou*100/5)
    if(x == 6):
        ganhous.append(ganhou*100/6)
    if(x == 7):
        ganhous.append(ganhou*100/7)
    if(x == 8):
        ganhous.append(ganhou*100/8)
    if(x == 9):
        ganhous.append(ganhou*100/9)
    if(x == 10):
        ganhous.append(ganhou*100/10)
    if(x==20):
        ganhous.append(ganhou*100/20)
    if(x==40):
        ganhous.append(ganhou*100/40)
    if(x == 80):
        ganhous.append(ganhou*100/80)
    if(x == 160):
        ganhous.append(ganhou*100/160)
    if(x == 320):
        ganhous.append(ganhou*100/320)
    if(x == 640):
        ganhous.append(ganhou*100/640)
    if(x == 1280):
        ganhous.append(ganhou*100/1280)
labels = [10,20,40,80,160,320,640,1280]
print(ganhous)
# plt.plot(labels, ganhous)
# plt.show()