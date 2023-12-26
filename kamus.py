meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "GW": "Kata untuk menyatakan diri sendiri",
            }
            
for i in range (3):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    if word in meme_dict.keys():
        print('artinya:')
        print(meme_dict[word])
    else:
        print('maaf kata belum ada atau di update')
