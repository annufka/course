class Price:
  #дескриптор, не позволяющий установить слишком низкую / высокую стоимость
  def __get__(self, instance, owner):
    #если цена больше нуля и меньше либо равна 100
    if instance.value <= 100 and instance.value > 0:
      return instance.value
    #иначе вернем сообщение
    else:
      return "You entered bad value for price"
  def __set__(self, instance, value):
    instance.value = value
    

class Book:
  price = Price()
 
  def __init__(self, author, title, price):
    self.author = author
    self.title = title
    self.price = price
 
  def __str__(self):
    return "{0} - {1}".format(self.author, self.title)

test1 = Book("Рэй Брэдбери", "Ржавчина", 80)
test2 = Book("Фрэнсис Скотт", "The Great Gatsby", 140)
print(test1.price)
print(test2.price)
