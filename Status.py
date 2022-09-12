Status=input("Staus Code:")
match int (Status):
    case 200:
        print("Ok")
    case 404:
        print("Not Found")
    case 500:
        print("Server Eror")
    case _:
        print("Others")

