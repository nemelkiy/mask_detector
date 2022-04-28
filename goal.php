<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Добро пожаловать в Mask Detector от группы разработчиков МБД2131 МТУСИ</title>

    <link rel="stylesheet" href="front/css/main.css">
    <link rel="stylesheet" href="front/css/owl.carousel.min.css">
    <link rel="stylesheet" href="front/css/owl.theme.default.min.css">
    <link rel="stylesheet" href="front/css/media.css">

    <script src="front/js/jquery-3.6.0.min.js"></script>
    <script src="front/js/owl.carousel.min.js"></script>
    <script src="front/js/common.js"></script>

</head>
<body>
    <?include('front/core/header.php')?>
    <h1>Цели приложения:</h1>
    <div class="container index-container">
        <div class="index-container__text">
            <p>Список целей:</p>
            <ul>
                <li>Командная разработка приложения по поиску масок на лицах</li>
                <li>Обучение методам взаимной работы внутри Docker</li>
                <li>Изучение принципов работы нейросетей для дальнейшей их проектировки и обучения</li>
                <li>Разработка приложения</li>
            </ul>
            <p>Принцип работы:</p>
            <ul>
                <li>Загрузка видео через GUI</li>
                <li>Разделение видео на кадры</li>
                <li>Постановка кадров в очередь на передачу в нейросеть и последующая передача</li>
                <li>Обработка нейросетью изображений, фильтрация лиц без масок</li>
                <li>Собранные изображения без масок собираются в очередь и передаются в GUI</li>
                <li>Выдача результата в GUI</li>
            </ul>
            <p>Языки программирования и компоненты в проекте:</p>
            <p>Языки:</p>
            <ul>
                <li>Python для нейросети</li>
                <li>PHP для разработки GUI</li>
            </ul>
            <p>Компоненты:</p>
            <ul>
                <li>Nginx</li>
                <li>RabbitMq</li>
                <li>Redis</li>
            </ul>
        </div>
    </div>
    <footer>
        <div class="footer-line">
            <div class="container" style="justify-content: center;">
            <p>Разработано студентами группы МБД2131 МТУСИ</p>
            </div>
        </div>
    </footer>
</body>
</html>