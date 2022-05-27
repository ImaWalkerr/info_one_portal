// Swiper main-slider settings //

let slider = new Swiper ('.slider-container', {
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
        delay: 1500,
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

let slider_currency = new Swiper ('.slider-container-currency', {
    centeredSlides: false,
    slidesPerView: 3,
    spaceBetween: 50,
    loop: true,
    autoplay: {
        delay: 1000,
        stopOnLastSlide: false,
        disableOnInteraction: false
    },
});
