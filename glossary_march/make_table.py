with open('defs.txt', 'r') as f:
    def_lines = f.readlines()
    
    
with open('collocation_defs.txt', 'r') as f:
    collocations_defs = f.readlines()
    
    
with open("Glossary_ZhelyapovAK.md", 'w') as f:
    f.write("|#|Collocation|Definition|\n|:----:|:----|:-----|\n")

    for i in range(len(def_lines)):
        def_data = def_lines[i].split(':')
        f.write("|" + str(i + 1) + ".|" + def_data[0] + "|" + def_data[1][1:-1] + "|\n")

    f.write ("\n\n")
    
    for i in range(len(def_lines)):
        f.write("### " + str(i + 1) + ". Word: " + def_lines[i].split(':')[0] + '\n')
        print(str(i + 1) + ". Word: " + def_lines[i].split(':')[0])
        f.write("|#|Collocation|Definition|\n|:----:|:----|:-----|\n")
        
        for k in range(5):
            line = collocations_defs[i * 5 + k].split(':')
            f.write("|" + str(k + 1) + ".|" + line[0] + '|' + line[1][1:-1] + '|\n')
        