import fun
import local

print ("Witaj w aplikacji librus")

fun.log()

'''
ADMINISTRATOR
'''
if (fun.user_type() == "admin"):
    print("Dodawanie ucznia ")
    fun.add_student()
