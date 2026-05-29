def gap_ichidagi_sozlar_soni(text):
    sozlar = text.split()
    return len(sozlar)

text = "Gap ichidagi so'zlar sonini aniqlang"
print(gap_ichidagi_sozlar_soni(text))
