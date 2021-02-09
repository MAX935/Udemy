##while True:
##    try:
##        x = int(input('Input x:'))
##        print(x / 2)
##    except ValueError:
##        print('You have to input int')
##    else:
##        print('Nice, you have got a result!')
##        break
##    finally:
##        print('Finally block')




def divide(x,y):
        try:
            print(x / y)
        except TypeError:
            print('Input the value type int!')
        except ZeroDivisionError:
            print('The parameter y can\'t be a null!')
        else:
            print('You\'ve got a great result!')
        finally:
            print('finally block')



divide(3,'6')