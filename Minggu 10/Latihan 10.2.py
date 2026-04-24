def soalSederhana(fileName):
    print("PERTANYAAN")

    with open(fileName, "r") as file:
        for line in file:
            if "||" in line:
                lineTemp = line.strip().split("||")
                pertanyaan = lineTemp[0].strip()
                jawabanAsli = lineTemp[1].strip()

                print(pertanyaan)
                jawabanUser = input("Jawab: ").strip()

                if jawabanUser.lower() == jawabanAsli.lower():
                    print("Jawaban benar!\n")
                else:
                    print("Jawaban salah!\n")

#Test Case
soalSederhana('Minggu 10/soal.txt')