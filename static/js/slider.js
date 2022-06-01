const weather_slider = document.querySelector('.slider-container');
const currency_slider = document.querySelector('.slider-container-currency');

// Swiper main-slider settings //
let slider = new Swiper (weather_slider, {
    centeredSlides: true,
    slidesPerView: 'auto',
    spaceBetween: 50,
    simulateTouch: true,
    touchRatio: 1,
    touchAngle: 45,
    grabCursor: true,
    loop: true,
    freeMode: true,
    autoplay: {
        delay: 3000,
        stopOnLastSlide: false,
        disableOnInteraction: false
    },
    speed: 800,
    effect: 'cube',
    cubeEffect: {
        slideShadows: true,
        shadow: true,
        shadowOffset: 20,
        shadowScale: 0.94,
    },
    // effect: 'flip',
    // flipEffect: {
    //     slideShadows: true,
    //     limitRotation: true,
    // },
});

let slider_currency = new Swiper (currency_slider, {
    centeredSlides: false,
    slidesPerView: 3,
    spaceBetween: 50,
    loop: true,
    grabCursor: true,
    speed: 800,
    autoplay: {
        delay: 1000,
        stopOnLastSlide: false,
        disableOnInteraction: false
    },
});
