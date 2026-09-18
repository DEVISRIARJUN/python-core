# 9. Implement a class incorrectly first:
# • Attendance stored in a list
# • Exposed directly so any outside code can modify it
# Then redesign properly:
# • Make attendance private
# • Provide controlled methods for marking attendance only


# class Attendence:
#     def __init__(self,name):
#         self.name=name
#         self.attendence=[] 
#     def attend(self,day):
#         self.attendence.append(day)
# a = Attendence("arjun")
# a.attend("monday")
# a.attend("tuesday")
# print(a.attendence)
# a.attendence.append("wednesday")
# print(a.attendence)




class Attendence:
    def __init__(self,name):
        self.name = name
        self.__attendence = []
    def attend(self,day):
        self.__attendence.append(day)
    def show_attendence(self):
        print(self.__attendence)
a= Attendence("Arjun")
a.attend("Monday")
a.attend("Tuesday")
a.show_attendence()
a.__attendence.append("wednesdya")
a.show_attendence()



