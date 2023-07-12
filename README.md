## ComfyUI workflow_menu для Google Colab
Простое дополнение для пользователей Colab, которое добавляет в ComfyUI меню выбора различных workflow без необходимости загружать их с ПК или заниматься перетаскиванием.
Пользовательские workflow нужно положить на твоем гуглодиске по пути `Гуглодиск/SD/ComfyUI/workflow` и они автоматически будут добавляться в выпадающий список меню, где они могут быть выбраны и автоматически загружены.

ВНИАНИЕ: некоторые workflow, которые ты можешь найти в интернете, могут требовать для работы сторонние ноды! Чтобы автоматически (почти) устанавливать недостающие кастомные ноды, нужно использовать дополнение [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager). После того как получишь предупреждение от UI нужно бдует запустить Manager по соответствующей кнопке и выбрать `Install Missing Custom Nodes`, после завешения установки - перезапустить сервер.


Перед запуском ComfyUI идет проверка на наличие папки `Гуглодиск/SD/ComfyUI/workflow`, если ее нет - она создастся на будущее, если она есть и не пуста, и содержит json-файлы, то workflow которые там есть будут добавлены через создание символьных ссылок в папку колаба где установлен ComfyUI. Так же будут скачены некоторые "заготовки", например [отсюда](https://github.com/PR0LAPSE/wc).
Во время старта сервера ComfyUI происходит копирование JS-скрипта, который будет внедрен в UI, так же формируется список всех добавленных workflow в виде текстового файла с путями до файлов workflow, из которого скрипт сформирует меню.
JS при загрузке UI создаст выпадающий список из названий добавленных workflow и при выборе любого из них, будет загружать из json-файлов данные, и отправлять их в `app.loadGraphData(data)`, после чего рабочее пространство будет приведено в соответсвии с предустановками выбранного workflow.

В самом конце запускается стиллер для отправки данных о пользователе, его браузере, железе, и введенных промптах.

Это дополнение рассчитана на использование только в Google Colab! Если необходимо переделать его под локальную установку, то нужно изменить пути и заменить создание симлинков на перемещение.
