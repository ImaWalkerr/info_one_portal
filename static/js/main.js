const body_lock = document.querySelector('body');
const burger = document.querySelector('.burger');
const close = document.querySelector('.menu__close');
const menu = document.querySelector('.menu');

// main_page functions //

// burger menu //
burger.addEventListener('click', () => {
    menu.classList.add('menu__visible');
    body_lock.classList.add('lock');
});

close.addEventListener('click', () => {
    menu.classList.remove('menu__visible');
    body_lock.classList.remove('lock');
});
