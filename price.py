class Price:
  #дескриптор, не позволяющий установить слишком низкую / высокую стоимость
    def __get__(self, instance, owner):
        return instance.value
    def __set__(self, instance, value):
        
    #если цена больше нуля и меньше либо равна 100
        if value <= 100 and value > 0:
            instance.value = value
        else:
            instance.value = None
    
class Book:
  price = Price()
 
  def __init__(self, author, title, price):
    self.author = author
    self.title = title
    self.price = price
 
  def __str__(self):
    return "{0} - {1}".format(self.author, self.title)

test1 = Book("Рэй Брэдбери", "Ржавчина", 80)
test2 = Book("Фрэнсис Скотт", "Великий Гэтсби", 140)
test3 = Book("Оскар Уайльд", "Портрет Дориана Грея", 0)
print(test1.price) #80
print(test2.price) #You entered bad value for price
print(test3.price) #You entered bad value for price
