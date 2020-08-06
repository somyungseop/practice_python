#data_type(list)
#리스트는 []를 씌워 만듭니다.
#리스트는 어떠한 자료형도 포함시킬 수 있습니다.
#리스트로 문자열 자료형과 같이 인덱싱,슬라이싱,더하거나 곱하는 연산가능합니다.
#문자열과 같이 길이 구하기 가능합니다.
#리스트의 수정은 리스트 값을 인덱싱한 후에 "= 바꾸는값"의 방법으로 바꿉니다.
#del 함수를 이용해 리스트의 요소를 삭제할 수 있습니다. ex) "del 객체(인덱싱으로 한번에 여러개 삭제 가능)"

#list_function
#변수.함수(값)의 방법으로 사용한다.

a = ["append","sort","reverse","index","insert","remove","pop","count","extend"]
for listcode in a:
    if listcode in ["append"]:
        print("%s는 리스트에 요소를 추가합니다." %listcode)    #a.append(x)
    elif listcode in ["sort"]:
        print("%s는 리스트의 요소들을 순서대로 정렬합니다." %listcode)    #a.sort()
    elif listcode in ["reverse"]:
        print("%s는 처음 리스트 그대로의 상태를 역순으로 정렬합니다." %listcode)    #a.reverse()  
    elif listcode in ["index"]:
        print("%s는 리스트 내에 특정 값의 위치를 알려줍니다.존재하지 않을 경우 에러가 발생합니다." %listcode)    #a.index(x)  
    elif listcode in ["insert"]:
        print("%s는 지정위치에 특정값을 삽입합니다.(앞,뒤)=앞의 위치에 뒤의 값을 삽입" %listcode)    #a.insert(x,y)
    elif listcode in ["remove"]:
        print("%s는 첫번째로 나오는 특정값을 삭제합니다." %listcode)    #a.remove(x) 반복하면 계속 x값이 지워진다.
    elif listcode in ["pop"]:
        print("%s는 리스트의 마지막 요소를 뽑아내고 리스트에선 삭제합니다." %listcode)    #a.pop()
    elif listcode in ["count"]:
        print("%s는 리스트안에 특정 값의 갯수를 알려줍니다." %listcode)    #a.count(x)   
    else:
        print("%s는 값에 리스트만 올 수 있으며 리스트 요소를 리스트에 더합니다." %listcode)    #a.extend([list])    
                                                                                          #append는 리스트 그자체를 요소로 더하고 extend는 리스트의 요소를 더한다.                         

print("="*50)    #리스트 자료형 종료

#data_type(tuple)