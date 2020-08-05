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

print("=" * 50)   #숫자형 종료


                
