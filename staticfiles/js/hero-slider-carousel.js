// Copyright (c) 2023.

// External Javascript File

/**
 * Shows a specific slide in the slider.
 *
 * @param {number} slideIndex - The index of the slide to show.
 * @return {undefined} This function does not return anything.
 */
function showSlide(slideIndex) {
    const slides = document.querySelectorAll('.slider-item')
    slides[slideIndex].classList.add('block')
    slides[slideIndex].classList.remove('hidden')
}

/**
 * Hides a specific slide in the slider.
 *
 * @param {number} slideIndex - The index of the slide to hide.
 * @return {void}
 */
function hideSlide(slideIndex) {
    const slides = document.querySelectorAll('.slider-item')
    slides[slideIndex].classList.add('hidden')
    slides[slideIndex].classList.remove('block')
}

/**
 * Activates the indicator at the specified index.
 *
 * @param {number} indicatorIndex - The index of the indicator to activate.
 */
function activateIndicator(indicatorIndex) {
    const indicators = document.querySelectorAll('.indicator')
    indicators[indicatorIndex].classList.add('active')
}

/**
 * Deactivates an indicator by removing the 'active' class from the specified indicator element.
 *
 * @param {number} indicatorIndex - The index of the indicator element to deactivate.
 */
function deactivateIndicator(indicatorIndex) {
    const indicators = document.querySelectorAll('.indicator')
    indicators[indicatorIndex].classList.remove('active')
}

/**
 * Updates the slide at the given index.
 *
 * @param {number} slideIndex - The index of the slide to update.
 * @return {undefined} This function does not return a value.
 */
function updateSlide(slideIndex) {
    const slides = document.querySelectorAll('.slider-item')
    slides.forEach((slide, index) => {
        if (index === slideIndex) {
            showSlide(index)
            activateIndicator(index)
        } else {
            hideSlide(index)
            deactivateIndicator(index)
        }
    })
}

/**
 * Attaches click events to the indicators.
 *
 * @param {Element[]} indicators - Array of indicator elements.
 * @return {void} This function does not return a value.
 */
function attachIndicatorClickEvents() {
    const indicators = document.querySelectorAll('.indicator')
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            updateSlide(index)
        })
    })
}

/**
 * Attaches click events to the slider controls.
 *
 * @param {type} paramName - description of parameter
 * @return {type} description of return value
 */
function attachControlClickEvents() {
    const slides = document.querySelectorAll('.slider-item')
    document.querySelector('.slider-control-next').addEventListener('click', () => {
        activeSlideIndex = (activeSlideIndex + 1) % slides.length
        updateSlide(activeSlideIndex)
    })
    document.querySelector('.slider-control-prev').addEventListener('click', () => {
        activeSlideIndex = (activeSlideIndex - 1 + slides.length) % slides.length
        updateSlide(activeSlideIndex)
    })
}

/**
 * Generates a random index for a slide in the slider.
 *
 * @return {number} The randomly generated slide index.
 */
//function getRandomSlideIndex() {
//    const slides = document.querySelectorAll(".slider-item");
//    return Math.floor(Math.random() * slides.length);
//}
// let activeSlideIndex = getRandomSlideIndex();

let activeSlideIndex = 0
attachIndicatorClickEvents()
attachControlClickEvents()
updateSlide(activeSlideIndex)
