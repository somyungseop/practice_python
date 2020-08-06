#Data_type(number)

a = [3,3.14,"4.24E10","0o177","0x177"]
for number in a:
    if number in [3]:
        print("%s 은/는 정수형입니다." %number)
    elif number in [3.14]:
        print("%s 은/는 실수형입니다." %number)
    elif number in ["4.24E10"]:
        print("%s 은/는 컴퓨터형 지수표현방식입니다.(e와E 무엇을 사용하여도 됩니다.)" %number)
    elif number in ["0o177"]:
        print("%s 은/는 8진수입니다.(알파벳 o의 대,소문자는 무관합니다.)" %number)
    else:
        print("%s 은/는 16진수입니다.(알파벳 x의 대,소문자는 무관합니다.)" %number)        

print("=" * 50)    #숫자형 종료

#Operator_to_use(number)

a = ["+","-","/","*","**","%","//"]
for operator in a:
    if operator in ["+"]:
        print("%s는 더하기 입니다." %operator)
    elif operator in ["-"]:
        print("%s는 빼기 입니다." %operator)    
    elif operator in ["/"]:
        print("%s는 나누기 입니다." %operator) 
    elif operator in ["*"]:
        print("%s는 곱하기 입니다." %operator)   
    elif operator in ["**"]:  
        print("%s는 앞수에 뒷수를 제곱한 연산자입니다." %operator)  
    elif operator in ["%"]:
        print("%s는 나눗셈후 나머지를 반환하는 연산자입니다." %operator)   
    else:
        print("%s는 나눗셈후 몫을 반환하는 연산자입니다." %operator)             

print("="*50)    #연산자 종료   
                
#Data_type(string)

a = ["'",'"',str('"'*3),str("'"*3)]
for string in a:
    if string in ["'"]:
        print("%s는 \"을 문장내에 쓸때 양 옆으로 사용하여 문자열을 만듭니다." %string)
    elif string in ['"']:
        print("%s는 \'을 문장내에 쓸때 양 옆으로 사용하여 문자열을 만듭니다." %string) 
    elif string in [str('"'*3)]:
        print("%s은 처음과 끝에 사용하여 여러줄의 문자열을 만듭니다." %string)           
    else:
        print("%s은 처음과 끝에 사용하여 여러줄의 문자열을 만듭니다." %string)    

print("="*50)    #문자열 종료

#operator_to_use(string)
#더하거나 곱할 수 있다.
#문자열의 순서는 0부터 센다.

a = ["len(x)","x[num]","x[num:num]"]
for operator in a:
    if operator in ["len(x)"]:
        print("%s는 문자열의 길이를 구하는 함수입니다." %operator)
    elif operator in ["x[num]"]:
        print("%s는 문자열에서 특정위치의 문자를 구하는 함수입니다." %operator)  
    else:
        print("%s는 문자열을 앞의 num에서부터 뒤의 num 이전까지 자르는 함수입니다." %operator )      

print("="*50)    #문자열 연산자 종료     

#formating_function
#문자열 포메팅
#문자열의 특정한 값을 바꿈

a = ["%s","%c","%d","%%"]
for formatingcode in a:
    if formatingcode in ["%s"]:
        print("%s는 문자열을 대입할때 사용하는 함수입니다." %formatingcode) 
    elif formatingcode in ["%c"]:
        print("%s는 문자 1개를 대입할때 사용하는 함수입니다." %formatingcode) 
    elif formatingcode in ["%d"]:
        print("%s는 정수를 대입할때 사용하는 함수입니다." %formatingcode) 
    else:
        print("%s는 %%자체를 대입할때 사용하는 함수입니다." %formatingcode)              

print("="*50)    #포매팅 함수 종료

#포맷 코드와 숫자 함께 사용하기
#포맷 함수 사이에 숫자를 넣어 정렬과 공백 만들기
#사이의 숫자는 문자열의 길이를 나타내고 +는 오른쪽 정렬, -는 왼쪽 정렬을 생성한다.
#.은 소수점 포인트를 뜻하고 그 뒤에오는 숫자는 몇번째 숫자까지 나타낼 것인지를 표현한다.
#ex)"%0.4f" %3.141592  = 3.1415
#0.4에서 0의 위치에 오는 정수는 값이오는 문자열의 길이를 나타낸다.

#포매팅 방법에는 직접대입과 변수를 생성하여 변수로 대입하는 방법이 있다.

#직접대입
#숫자형과 문자형 모두 직접대입 가능하다.
a = ["i eat {0} apples".format(3)]
print(a)    # a = "i eat 3 apples"

#변수로 대입
number = 3
a = ["i eat {0} apples".format(number)]
print(a)    # a = "i eat 3 apples"

#중괄호 안의 숫자는 순서를 나타낸다. 그곳에 숫자대신 이름으로 생성하여 포매팅 할 수도 있다.
a = ["i ate {number} apples. so i was sick for {day} days.".format(number=10,day=3)] 
print(a)    # a = "i ate 10 apples. so i was sick for 3 days."

#2개 이상의 값을 넣을 때 순서(인덱스)와 이름을 혼용할 수도 있다.
a = ["i ate {0} apples. so i was sick for {day} days.".format(10,day=3)]
print(a)    # a = "i ate 10 apples. so i was sick for 3 days."

#정렬방법
#(:),(<>^=좌,우,중앙),(숫자=문자열길이)로 정렬할 수 있다.
a = "{0:<10}".format("hi")    #hi라는 글자를 10칸 길이의 문자열에서 <(=왼쪽)방향으로 정렬한다. 
print(a)

#정렬한 문자열의 공백을 문자로 채우기
#(:) 와 (<>^) 사이에 채우고 싶은 문자를 넣으면 된다.
a = "{0:!^10}".format("hi")    #10자리의 문자열에 hi라는 글자를 가운데 정렬하고 공백은 !로 채운다.
print(a)    # a = !!!!hi!!!!

#f문자열 포매팅
#접두사로 f를 사용하여 .format함수를 사용하지 않고 값을 대입할 수 있다.
name = "홍길동"
age = 30
a = f"나의 이름은 {name}입니다. 나이는 {age} 입니다."
print(a)    # a = "나의 이름은 홍길동입니다.나이는 30 입니다"

#f문자열 포매팅은 표현식을 지원하기 떄문에 지정된 변수에 변화주기
#딕셔너리에서 key값으로 value값 가져오기가 가능하다.
age = 30
a = f"나는 내년이면 {age+1}살이 된다."
print(a)    # "나는 내년이면 31살이 된다."

d = {'name':"홍길동" , 'age':30 }
a = f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}입니다."
print(a)    # "나의 이름은 홍길동입니다. 나이는 30입니다."

#f문자열의 정렬 방법
a = f'{"hi":!^10}'    #순서를 나타내던 숫자의 자리에 정렬할 글자를 쓰면 된다. 나머지는 위의 정렬방법과 동일하다.
print(a)    # !!!!hi!!!!

print("="*50)    #포매팅 방법 종료

#string_function
#문자열 내장 함수의 사용법은 문자열 변수 이름 뒤에 (.)을 붙인다음 함수이름+()을 써주면 된다.

a = ["count", "find","index","join","upper","lower","lstrip","rstrip","strip","replace","split"]
for stringcode in a:
    if stringcode in ["count"]:
        print("%s는 문자열에서 특정 문자의 개수를 알려줍니다." %stringcode)
    elif stringcode in ["find"]:
        print("%s는 문자열에서 특정 문자가 처음으로 나온 위치를 알려줍니다.없으면 -1이 도출됩니다." %stringcode)      
    elif stringcode in ["index"]:
        print("%s는 문자열에서 특정 문자가 처음으로 나온 위치를 알려줍니다.없으면 오류가 발생합니다." %stringcode) 
    elif stringcode in ["join"]:    #삽입할 문자.join(문자가 삽입 될 대상)으로 사용합니다.
        print("%s는 문자열사이에 문자를 입력합니다." %stringcode)    #문자열뿐만아니라 리스트,튜플에도 사용가능하다.ex)리스트 요소들 사이에 문자를 삽입하여 문자열로 생성
    elif stringcode in ["upper"]:
        print("%s는 문자열의 글자를 대문자로 변환합니다." %stringcode) 
    elif stringcode in ["lower"]:
        print("%s는 문자열의 글자를 소문자로 변환합니다." %stringcode)   
    elif stringcode in ["lstrip"]:
        print("%s는 문자열 중 가장 왼쪽의 공백을 모두 지웁니다." %stringcode)    #lstripdml L은 left의 L입니다. 
    elif stringcode in ["rstrip"]:
        print("%s는 문자열 중 가장 오른쪽의 공백을 모두 지웁니다." %stringcode)    #rstrip의 R은 right의 R입니다.  
    elif stringcode in ["strip"]:
        print("%s는 문자열의 양쪽 공백을 모두 지웁니다." %stringcode)
    elif stringcode in ["replace"]:
        print("%s는 문자열을 바꿉니다.변수.replace(바뀔문자열,바꿀 문자열)형식으로 사용합니다." %stringcode)
    else:
        print("%s는 특정한 기준으로 문자열을 나누어 리스트로 제공합니다." %stringcode)    #공백으로 사용하면 띄어쓰기 기준으로 나누고 특정 문자를 넣으면 그 문자 기준으로 나누어 리스트로 반환한다.       

print("="*50)    #문자열 자료형 종료                          