# Проект Face_Definition

API на Flask для распознавания лиц на изображении. 

# Запуск
Клонировать репозиторий. Запустить проект используя Docker Compose командой:
+ docker-compose up  
  
 
    
# Инструкция
Реализованно два эндпоинта.  

**Первый эндпоинт** осуществляет получение изображений из вне, анализирует наличие лиц на нем, сохраняет изображение на диск, информация о ключевых точках на лице и путь к изображению сохраняется в БД SQLite.  

**Получает изображение(разрешённый формат jpeg)**  

**Возвращает:** информацию об окаймляющем прямоугольнике (bounding box) и координатах пяти лицевых точек для каждого лица на изображении.  

**Второй эндпоинт** позволяет понять были в истории запросы с такими же лицами.  

**Получает изображение(разрешённый формат jpeg)**  

**Возвращает:** количество лиц на переданном изображении и количество совпадений лиц на этом изображении с
лицами уже ранее просмотренными этим сервисом.
  

  
# Примеры 
Первый эндпоинт: 
+ curl -F 'file=@path/to/image/' http://0.0.0.0:8000/image_analysis
    + ответ: {
    "face_0": {
        "rectangle_points": {
            "left": 63,
            "top": 99,
            "right": 384,
            "bottom": 420
        },
        "points": [
            [
                310,
                200
            ],
            [
                260,
                204
            ],
            [
                133,
                200
            ],
            [
                186,
                204
            ],
            [
                224,
                286
            ]
        ]
    }
}
      
Второй эндпоинт:
+ curl -F 'file=@/path/to/image/' http://0.0.0.0:8000/face_verification  
  + ответ: {"face_in_image": 1, "verification_face": 3}  
      

      
# Инструменты
+ [DLib](http://dlib.net/)
+ [Flask](https://flask.palletsprojects.com/)
+ [SQLite](https://www.sqlite.org/)
+ [Python](https://www.python.org/)
+ [Docker](https://www.docker.com/)
+ [Docker Compose](https://docs.docker.com/compose/)
