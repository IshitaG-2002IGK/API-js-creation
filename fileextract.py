def main():
    file=open("file.txt","r")
    lines=file.readlines()
    file.close()
    for line in lines:
        line=line.strip()
        print(line)

main()
 
