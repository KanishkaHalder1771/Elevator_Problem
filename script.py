print("Enter initial Elevator Positions:")
ele_pos = list(map(int, input().split()))

if max(ele_pos)>10 or min(ele_pos)<1:
    print("Endter floor between 0 and 10")
    exit
if len(ele_pos) != 3:
    print("Enter 3 elevator positions")
    exit

print("Enter User Positions:")
user_pos = list(map(int, input().split()))

if max(user_pos)>10 or min(user_pos)<1:
    print("Endter floor between 0 and 10")
    exit

upp_bd = [-1,-1,-1]
lwr_bd = [-1,-1,-1]
wait_time = [0,0,0]

def get_wait_time(upp,lwr,pos):
    return (upp-lwr + min(upp-pos, pos-lwr))

ele_pos =  list(dict.fromkeys(ele_pos))
user_pos = list(dict.fromkeys(user_pos))

ele_pos = sorted(ele_pos,reverse=True)
user_pos = sorted(user_pos,reverse=True)

upp_bd[0] = max(ele_pos[0],user_pos[0])
lwr_bd[0] = ele_pos[0]

upp_bd[1] = max(ele_pos[0]-1,ele_pos[1])
lwr_bd[1] = min(ele_pos[2]+1, ele_pos[1])

upp_bd[2] = ele_pos[2]
lwr_bd[2] = min(ele_pos[-1],user_pos[-1])

for i in range(len(ele_pos)):
    wait_time[i] = get_wait_time(upp_bd[i],lwr_bd[i],ele_pos[i])


mid_list = user_pos[user_pos.index(upp_bd[1]):user_pos.index(lwr_bd[1])+1]



while(True):
    if wait_time[1] <= wait_time[0] or wait_time[1]<=wait_time[2]:
        break
    
    w_t = max(wait_time)
    up_time =100
    down_time = 100
    if(upp_bd[1]!=ele_pos[1]):
        w_t_middle = get_wait_time(mid_list[1],lwr_bd[1],ele_pos[1])
        w_t_top = get_wait_time(upp_bd[0],mid_list[0],ele_pos[2])
        up_time = max(w_t_middle,w_t_top)

    if(lwr_bd[1]!=ele_pos[1]):
        w_t_middle = get_wait_time(upp_bd[1],mid_list[-2],ele_pos[1])
        w_t_btm = get_wait_time(mid_list[-1],lwr_bd[2],ele_pos[2])
        down_time = max(w_t_middle,w_t_btm)
    
    if down_time<=up_time and down_time<w_t:
        lwr_bd[1] = mid_list[-2]
        upp_bd[2] = mid_list[-1]
        wait_time[1] = get_wait_time(upp_bd[1],lwr_bd[1],ele_pos[1])
        wait_time[2] = get_wait_time(upp_bd[2],lwr_bd[2],ele_pos[2])
        mid_list = mid_list[:-1]
    elif up_time<down_time and up_time<w_t:
        upp_bd[1] = mid_list[1]
        lwr_bd[0] = mid_list[0]
        wait_time[1] = get_wait_time(upp_bd[1],lwr_bd[1],ele_pos[1])
        wait_time[0] = get_wait_time(upp_bd[0],lwr_bd[0],ele_pos[0])
        mid_list = mid_list[1:]
    else:
        break
    print(upp_bd,lwr_bd,wait_time)

end_pos = [-1,-1,-1]

def get_end_pos(upp,lwr,pos):
    if(upp-pos >= pos - lwr):
        return upp
    else:
        return lwr

for i in range(len(ele_pos)):
    end_pos[i] = get_end_pos(upp_bd[i],lwr_bd[i],ele_pos[i])
print("Maximum wait time:", max(wait_time))
print("End postitions of top, middle and bottom elevators are:", end_pos)