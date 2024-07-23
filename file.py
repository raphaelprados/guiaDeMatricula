
# importing required modules 
from pypdf import PdfReader 
  
# creating a pdf reader object 
reader = PdfReader('HistoricoAcademico.pdf') 
  
# getting a specific page from the pdf file 
page = []
text = ""
for i in range(1, len(reader.pages)):
    page.append(reader.pages[i]) 
    text += page[i-1].extract_text()

start = text.find("TIPO")
end = text.find("IVE - INGRESSO POR VESTIBULAR")
text = text[start + 5:end]

while(text.find("Ministério da Educação") != -1 and text.find("Pg. ") != -1):
    cabecalho_start = text.find("Ministério da Educação")
    cabecalho_end = text.find("Pg. ") + 10
    text = text[:cabecalho_start] + "\n" + text[cabecalho_end:]
    # print("C_st: ", cabecalho_start, "C_end:", cabecalho_end, "Total: ", len(text))

semestres = []
substrings = text.split("\n")

for i in range(0, len(substrings) - 1):
    if(substrings[i][0] == "2"):
        semestres.append([substrings[i], []])
    elif(substrings[i][0] == "0"):
        info_pos = substrings[i][3].find("AP") if substrings[i].find("AP") != -1 else substrings[i].find("RP")
        final_string = substrings[i][:substrings[i].rfind(" ")] + " - " + substrings[i][info_pos - 4:]
        semestres[-1][1].append({"disciplina": final_string, "prof": substrings[i+1]})

for i in range(0, len(semestres)):
    print(semestres[i][0])
    for j in range(0, len(semestres[i][1])):
        print(semestres[i][1][j])

