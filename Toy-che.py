import time
import os


str1 = """
                                       $$$$$$$$
                                $$$$$$$$$$$$$$$$$$
                             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                          $$$$$$$$$$$$$$$$ $      $$$$$$$$$$$$$$$$$$$
                        $$$$$$$$$$$               $$ $$$$$$$$$$$$$$$$$$
                       $$$$$$$$ $$$                    $$$$$$$$$$$$$$$$$
             $$$$$$$  $$$$$$$                   $$$$$  $$$$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$        $          $$$$$$$  $$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$      $$$$$$$       $$$$$$$  $$$$$$$$$$$$$$$$$$
     $$$$$$$$$$$$$$$$$$$$$$     $$$$$$$$        $$$$$   $$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$      $$$$$$$     $$$        $$$$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$$$$$$$$$$$$$        $                  $$$$$$$$$$$$$$$$$$ 
  $$$$$$$$$$$$$$$$$$$$$$$$$$                   $      $$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$                      $$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$            $$$$$ $$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$$$$$$$$$$$$$$ $$ $$ $  $$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$   $ $$$$$$$    $$ $$$$$$$$$$$$
     $$$$$$$$$$$$$$$$$$$$$   $$$$$$$$      $ $$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$     $$$$$$$$$$    $  $$$$$ $$$$$$$
              $$$          $$$$ $$$$  $$ $ $$$$$ $$$$$
                            $$$$ $$$  $   $ $$ $$$$ $$
                            $$$$$$$     $ $ $$$$$$$$$$$
                             $$$$$$ $$$  $ $$$$$$$$$$$$
                               $$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$
                              $$$$$$$$$$$$$$$$$$$$$ $$$$
                            $$$$$$$$$$$$$$$$ $$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""

str2 = """
                                       $$$$$$$$
                                $$$$$$$$$$$$$$$$$$
                             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                          $$$$$$$$$$$$$$$$ $      $$$$$$$$$$$$$$$$$$$
                        $$$$$$$$$$$               $$ $$$$$$$$$$$$$$$$$$
                       $$$$$$$$ $$$                    $$$$$$$$$$$$$$$$$
                   $  $$$$$$$                   $$$$$  $$$$$$$$$$$$$$$$$$
               $$$$$$$$$$$$$                   $$$$$$$  $$$$$$$$$$$$$$$$$
             $$$$$$$$$$$$$$    $$$$$$$$        $$$$$$$  $$$$$$$$$$$$$$$$$$
           $$$$$$$$$$$$$$$$     $$$$$$$$        $$$$$   $$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$                             $$$$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$       $$                  $$$$$$$$$$$$$$$$$$ 
        $$$$$$$$$$$$$$$$$$$$         $$$              $$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$          $$$$$$      $$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$$$                  $$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$$ $$ $$ $  $$$$$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$   $ $$$$$$$    $$ $$$$$$$$$$$$
           $$$$$$$$$$$$$$$   $$$$$$$$      $ $$$$$$$$$$$$$$
              $$$$$$$$$     $$$$$$$$$$    $  $$$$$ $$$$$$$
                    $$$    $$$$ $$$$  $$ $ $$$$$ $$$$$
                            $$$$ $$$  $   $ $$ $$$$ $$
                            $$$$$$$     $ $ $$$$$$$$$$$
                             $$$$$$ $$$  $ $$$$$$$$$$$$
                               $$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$
                              $$$$$$$$$$$$$$$$$$$$$ $$$$
                            $$$$$$$$$$$$$$$$ $$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
str3 = """
"Первое домашнее задание завершено"
"""

# цикл 1
# первый кадр
# очистка окна терминала
os.system('cls')
# выводим сообщение
print(str1, end='\r')
# засыпаем на 1 секунду
time.sleep(1)

# второй кадр
os.system('cls')
print(str2, end='\r')
time.sleep(1)

# цикл 2
os.system('cls')
print(str1, end='\r')
time.sleep(1)
os.system('cls')
print(str2, end='\r')
time.sleep(1)
# цикл 3
os.system('cls')
print(str1, end='\r')
time.sleep(1)
os.system('cls')
print(str2, end='\r')
time.sleep(1)
# цикл 4
os.system('cls')
print(str1, end='\r')
time.sleep(1)
os.system('cls')
print(str2, end='\r')
time.sleep(5)
os.system('cls')
print(str3, end='\r')
