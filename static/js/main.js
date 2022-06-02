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

// filter for currencies //
document.querySelector('#filter-currencies').oninput = function () {
    let val = this.value.trim();
    let filterPlatformItems = document.querySelectorAll('.filter-currencies li');
    if (val !== '') {
        filterPlatformItems.forEach(function (elem) {
            if (elem.innerText.toLowerCase().search(val.toLowerCase()) === -1) {
                elem.classList.add('hide');
            }
            else {
              elem.classList.remove('hide');
            }
        });
    }
    else {
        filterPlatformItems.forEach(function (elem) {
            elem.classList.remove('hide');
        });
    }
}
