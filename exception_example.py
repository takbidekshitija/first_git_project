import traceback
class MyExcept:

    a = 10
    b = 20
    L = [1, 2 , 3]
    def my_function(self):
        try:
            print("Hello")
            # this will execute Exception block
            print(10/0)
            # This will execute Exception block
            print(h)
            # program raise error
            print(self.L[10])
            # raising manually error
            # raise IndexError("This is my custom index error")
        except (IndexError,ZeroDivisionError) as e:
            print("this common handler for index and ZeroDiv")
            print(e)
            print(traceback.format_exc())      # to find where error is occurred.
        except NameError as e:
            print("This is name error")
        except Exception as e:
            print("This is general block for error.")
        else:
            # this block will get executed only when there is no error
            print("this is else block")

        finally:
            # This block act as resource releaser
            print("This block will get executed every time whether "
                  "error occurred or not.")

if __name__ == "__main__":
    obj = MyExcept()
    obj.my_function()


