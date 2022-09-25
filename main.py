print("Welcome")
print("Make sure file is shared with 'anyone with the link' can view or better")
print("Choose an option")
print('1. Uploaded File')
print('2. Google Docs')
print('3. Google Slides')
print('4. Google Sheets')

in1 = input('Choose(1-4): ')

if in1 == '1':
    link = input('Shared link: ')
    id = link.replace("https://drive.google.com/file/d/", "").split("/")[0]
    download_link = "https://drive.google.com/uc?export=download&" + id
    print(f"Download Link: {download_link}")
    print("Bye")
    exit()

if in1 == '2':
    print('Download As')
    print('1. .docx')
    print('2. .pdf')
    print('3. .txt')
    print('4. .html')
    in2 = input('Choose(1-4): ')

    if in2 == '1':
        link = input('Shared link: ')
        id = link.replace("https://docs.google.com/document/d/", "").split("/")[0]
        download_link = "https://docs.google.com/document/d/" + id + "/export?format=doc"
        print(f"Download Link: {download_link}")
        print("Bye")
        exit()

    if in2 == '2':
        link = input('Shared link: ')
        id = link.replace("https://docs.google.com/document/d/", "").split("/")[0]
        download_link = "https://docs.google.com/document/d/" + id + "/export?format=pdf"
        print(f"Download Link: {download_link}")
        print("Bye")
        exit()

    if in2 == '3':
        link = input('Shared link: ')
        id = link.replace("https://docs.google.com/document/d/", "").split("/")[0]
        download_link = "https://docs.google.com/document/d/" + id + "/export?format=txt"
        print(f"Download Link: {download_link}")
        print("Bye")
        exit()

    if in2 == '4':
        link = input('Shared link: ')
        id = link.replace("https://docs.google.com/document/d/", "").split("/")[0]
        download_link = "https://docs.google.com/document/d/" + id + "/export?format=html"
        print(f"Download Link: {download_link}")
        print("Bye")
        exit()

if in1 == '3':
    print('Download As')
    print('1. .pptx')
    print('2. .pdf')
    in2 = input('Choose(1-2): ')
    
    if in2 == '1':
        link = input('Shared link: ')
        id = link.replace("https://docs.google.com/presentation/d/", "").split("/")[0]
        download_link = "https://docs.google.com/presentation/d/" + id + "/export/pptx"
        print(f"Download Link: {download_link}")
        print("Bye")
        exit()

    if in2 == '2':
        link = input('Shared link: ')
        id = link.replace("https://docs.google.com/presentation/d/", "").split("/")[0]
        download_link = "https://docs.google.com/presentation/d/" + id + "/export/pdf"
        print(f"Download Link: {download_link}")
        print("Bye")
        exit()

if in1 == '4':
    print('Download As')
    print('1. .xlsx')
    print('2. .pdf')
    in2 = input('Choose(1-2): ')

    if in2 == '1':
        link = input('Shared link: ')
        id = link.replace("https://docs.google.com/spreadsheets/d/", "").split("/")[0]
        download_link = "https://docs.google.com/spreadsheets/d/" + id + "/export?format=xlsx"
        print(f"Download Link: {download_link}")
        print("Bye")
        exit()
    
    if in2 == '2':
        link = input('Shared link: ')
        id = link.replace("https://docs.google.com/spreadsheets/d/", "").split("/")[0]
        download_link = "https://docs.google.com/spreadsheets/d/" + id + "/export?format=pdf"
        print(f"Download Link: {download_link}")
        print("Bye")
        exit()
