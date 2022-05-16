alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " " ]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]

sentence1 = alphabet[-5]+alphabet[4]+alphabet[-1]+alphabet[0]+alphabet[-10]+alphabet[4]+alphabet[-1]+alphabet[-9]+alphabet[10]+alphabet[7]+alphabet[-7]+alphabet[-1]+alphabet[11]+alphabet[8]+alphabet[10]+alphabet[4]+alphabet[11]+alphabet[8]+alphabet[-13]+alphabet[-14]
sentence2 = alphabet[7]+alphabet[0]+alphabet[2]+alphabet[10]+alphabet[-1]+alphabet[-3]+alphabet[-13]+alphabet[-7]+alphabet[-10]+alphabet[-1]+alphabet[11]+alphabet[8]+alphabet[5]+alphabet[4]
sentence3 = alphabet[12]+alphabet[-3]+alphabet[-1]+alphabet[13]+alphabet[0]+alphabet[12]+alphabet[4]+alphabet[-1]+alphabet[8]+alphabet[-9]+alphabet[-1]+alphabet[9]+alphabet[4]+alphabet[14]+alphabet[13]+alphabet[-1]+alphabet[9]+alphabet[8]+alphabet[-3]+alphabet[-7]+alphabet[13]

birthday = number[1] + number[9] + number[9] + number[9] + number[0] + number[8] + number[1] + number[4]
phone = number[0] + number[1] + number[0] + number[10] + number[8] + number[7] + number[5] + number[8] + number[10] + number[8] + number[3] + number[4] + number[7]
id = number[2] + number[0] + number[1] + number[8] + number[1] + number[4] + number[1] + number[1] + number[3]
print(sentence1)
print(sentence2)
print(sentence3)
print("제 생일은 " + birthday + "입니다.")
print("제 전화번호는 " + phone + "입니다.")
print("제 학번은 " + id + "입니다.")