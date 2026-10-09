#  Create a class Transaction with a method process() that uses try, except, and finally blocks to ensure a cleanup message is always printed.




# class Transation:
#     def process(self,s):
#         try:
#             s = int(s)
#         except ValueError as e:
#             print(e)
#         finally:
#             print("The process updated sucessfully")
# t = Transation()
# t.process("arjun")



class Transaction:
    def process(self, s):
        try:
            s = int(s)
            print("Transaction processed")
        except ValueError as e:
            print("Transaction failed:", e)
        finally:
            print("Cleanup completed")

t = Transaction()
t.process("arjun")
