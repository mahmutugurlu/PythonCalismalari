#Pflichtaufgabe: Listenoperationen mit Slicing
highscore = [12, 45, 7, 89, 34, 56, 23, 78, 91, 5]

neu_score = highscore[:3] #Listenin ilk 3 elemanını alır.[başlangıç:bitiş] formatında:başlangıç boş → 0’dan başlab itiş = 3 → 3. index dahil değil
                            #👉 Yani index 0,1,2 alınır.
print(neu_score)



end_score = highscore[-3:] #Listenin son 3 elemanını alır.
print(end_score)



list_score = highscore[3:] #3. index’ten başlayıp sona kadar alır
print(list_score)

neu_score1 = highscore[::2] # Her 2 elemandan birini alır, başlangıç:bitiş:adım], adım = 2 → 2’şer atla
print(neu_score1)
#neu_score2 = highscore[1::2]


highscore.reverse() #ters döndürür
print(highscore)

highscore.reverse()
print(highscore)

neu_score2=highscore[2:7] #index 2 dahil , index 7 dahil değil
print(neu_score2)
