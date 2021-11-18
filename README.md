# SiteWork
Файл "db_initialize_script" создает базу данных и таблицы со связями.

Файл "db_fill_script" заполняет таблицы базы данных нужными данными.

Файл main, запускать именно его для тестирования, непосредственно модели для взаимодействия с базой данных, http methods(GET, PUT, POST, DELETE(реализованы, но DELETE нет возможности проверить, насколько я понял пока не появятся записи в History, потому что он не может удалить того чего нет, а history не успел реализовать, хотя есть идеи как, через PUT сделать это)

В данной работе я успел реализовать: базу данных, ее наполнение, модели для взаимодействия с бд через SQLAlchemy, http методы(GET, PUT, POST, DELETE[смотреть выше почему не смог доделать DELETE]).

В данной работе я не успел реализовать: авторизацию (соответственно взаимодействие с определенными запросами относительно авторизации, так как на данный момент спустя много просмотренных видеороликов\сайтов\документации так и не понял как это реализовать без frontend, а только через backend), историю измения товаров(хотя есть идеи как бы я мог сделать это через PUT метод product), также не до конца понял как выводить с помощью GET постранично разбитый список из 10 товаров.

Тестировал запросы через программу HTTPMaster, GET тестируется довольно просто, созданием запроса GET по ссылке, которую я сделал для GET в работе, POST также по ссылке, а вот PUT и DELETE, необходимо добавить после ссылки, ID товара или категории которую необходимо удалить\изменить. Все тестировал с помощью JSON формата.

Наброски регистрации и логина, я прикрепил в файле AUTH + UserLogin, то, что на данный момент я успел найти и адаптировать, 
