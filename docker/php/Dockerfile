FROM php:7.3-fpm


RUN cat /etc/issue
# Install modules
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libicu-dev \
        libmcrypt-dev \
        libcurl4-gnutls-dev \
        libvpx-dev \
        libjpeg-dev \
        libpng-dev \
        libxpm-dev \
        zlib1g-dev \
        libfreetype6-dev \
        libxml2-dev \
        libexpat1-dev \
        libbz2-dev \
        libgmp3-dev \
        libldap2-dev \
        unixodbc-dev \
        libsqlite3-dev \
        libaspell-dev \
        libsnmp-dev \
        libpcre3-dev \
        libtidy-dev \
        libzip-dev \
        libpq-dev \
         libfreetype6-dev \
         libjpeg62-turbo-dev \

        curl \
        libonig-dev \
        git \
        wget \
            --no-install-recommends




RUN docker-php-ext-install zip intl mbstring  pdo_mysql mbstring exif \
    && docker-php-ext-configure gd \
    && docker-php-ext-install gd

RUN pecl install -o -f  mcrypt-1.0.4 \
    && docker-php-ext-enable mcrypt

RUN pecl install -o -f xdebug \
    && rm -rf /tmp/pear

RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli

RUN docker-php-ext-configure gd \
        --with-freetype-dir=/usr/lib/x86_64-linux-gnu/ \
        --with-jpeg-dir=/usr/lib/x86_64-linux-gnu/ \
        --with-xpm-dir=/usr/lib/x86_64-linux-gnu/ \
            && docker-php-ext-install -j "$(nproc)" gd


RUN apt-get update && apt-get install -y libbz2-dev

RUN docker-php-ext-install bz2

RUN pecl install -o -f xdebug \
    && rm -rf /tmp/pear

RUN curl -sS https://getcomposer.org/installer | php

COPY ./php.ini /usr/local/etc/php/
COPY ./www.conf /usr/local/etc/php/


# sendmail config
RUN groupadd -g 124 postfix && \
    groupadd -g 125 postdrop && \
useradd -u 116 -g 124 postfix

RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
    postfix \
    bsd-mailx

CMD echo test mail | mail logachev.iv@koleso.ru


RUN apt-get purge -y g++ \
    && apt-get autoremove -y \
    && rm -r /var/lib/apt/lists/* \
    && rm -rf /tmp/*


RUN usermod -u 1000 www-data

VOLUME /root/.composer
WORKDIR /app

EXPOSE 9000
CMD ["php-fpm"]
