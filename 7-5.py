# def profile(name, age, lang1,lang2,lang3,lang4,lang5):
#     print("이름: {0}\t나이 : {1}\t".format(name,age),end =" " )
#     print(lang1,lang2,lang3,lang4,lang5)

def profile(name, age, *language):
    print("이름: {0}\t나이 : {1}\t".format(name,age),end =" " )#,end =" "<밑문장을 계속출력한다는뜻 c#의writeline의뜻
    for lang in language:
        print(lang,end=" ")
        print()
    

profile("유재석",20,"python","java","c#","c++","c","js")
profile("김태호",25,"kotlin","swift")