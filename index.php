<?php

    session_start();

?>

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
    <div class="container content-center">
        <form enctype='multipart/form-data' method="post" class='link-form'>
            <label for="video_link">Вставьте ссылку на видео:</label>
            <input type="text" name="video_link" id="video_link" required >
            <label for="video_frame">Укажите количество кадров:</label>
            <input type="text" name="video_frame" id="video_frame" required >
            <input type="submit" value="Отправить" class="form_submit" user_id="<?php echo session_id() ?>">
        </form>
    </div>
    <footer>
        <div class="footer-line">
            <div class="container" style="justify-content: center;">
            <p>Разработано студентами группы МБД2131 МТУСИ</p>
            </div>
        </div>
    </footer>
    <svg class="footer-path" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 250">
            <linearGradient id="0" x1="0.74" y1="0.06" x2="0.26" y2="0.94">
            <stop offset="0%" stop-color="#cfecd0"/>
            <stop offset="7%" stop-color="#c4e9c6"/>
            <stop offset="14%" stop-color="#bae6bd"/>
            <stop offset="21%" stop-color="#b5e1b9"/>
            <stop offset="28%" stop-color="#afdcb4"/>
            <stop offset="35%" stop-color="#aad7b0"/>
            <stop offset="49%" stop-color="#a0cea7"/>
            <stop offset="55.86%" stop-color="#9fccb3"/>
            <stop offset="62.71%" stop-color="#9dcabb"/>
            <stop offset="69.57%" stop-color="#9bc9c1"/>
            <stop offset="76.43%" stop-color="#99c7c7"/>
            <stop offset="83.29%" stop-color="#97c6ce"/>
            <stop offset="97%" stop-color="#9ec0db"/>
            </linearGradient>
            <path id="waveline" fill="url(#0)" fill-opacity="1" d="M0,64L48,96C96,128,192,192,288,213.3C384,235,480,213,576,176C672,139,768,85,864,53.3C960,21,1056,11,1152,21.3C1248,32,1344,64,1392,80L1440,96L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
    </svg>

    <div class="overlay">
        <div class="loader-container">
            <div class="loader" id="loader-6">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
            <div class="loader-text">
                Видео загружается
            </div>
        </div>
    </div>
</body>
</html>