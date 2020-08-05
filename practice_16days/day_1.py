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
for Operator in a:
    if Operator in ["+"]:
        print("%s는 더하기 입니다." %Operator)
    elif Operator in ["-"]:
        print("%s는 빼기 입니다." %Operator)    
    elif Operator in ["/"]:
        print("%s는 나누기 입니다." %Operator) 
    elif Operator in ["*"]:
        print("%s는 곱하기 입니다." %Operator)   
    elif Operator in ["**"]:  
        print("%s는 앞수에 뒷수를 제곱한 연산자입니다." %Operator)  
    elif Operator in ["%"]:
        print("%s는 나눗셈후 나머지를 반환하는 연산자입니다." %Operator)   
    else:
        print("%s는 나눗셈후 몫을 반환하는 엽산자입니다." %Operator)             

print("="*50)    #연산자 종료   
                
#Data_type(string)

a = "'",'"',str('"'*3),str("'"*3)
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