a = input("File name: ").split(".")

a1 = a[0].lower().strip()
a2 = a[len(a)-1].lower().strip()

match a2:
    case "gif":
        print("image/" + a2)
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/" + a2)
    case "pdf":
        print("application/" + a2)
    case "txt":
        print("text/" + a1)
    case "zip":
        print("application/" + a2)
    case _:
        print("application/octet-stream")