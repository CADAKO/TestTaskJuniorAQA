## Тестовое задание на позицию Junior AQA

### Тесты для проверки ссылок навигации по сайту effective-mobile.ru

Тесты находятся в файле tests/test_main_page_navigation.py

Использована параметризация и Allure отчет

Для локального запуска тестов необходимо в терминале 
в корневой папке проекта собрать Docker образ и запустить его:
>docker build -t effective-mobile-tests:latest .
> 
>docker run -v ./allure_results:/app/allure_results effective-mobile-tests:latest tests/test_main_page_navigation.py --alluredir allure_results

Для просмотра Allure отчета необходим установленный ACL и команда:

>allure generate allure_results --clean && allure open
