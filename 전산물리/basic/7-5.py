def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이: {1}\t".format(name, age), end= " ") #end= " " : 줄 바꾸지 말란 뜻
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "swift", " ", " ", " ")

def protile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "Java", "C", "C++", "C#", "Javascript")
protile("김태호", 25, "Katlin", "Swift")