// Copyright (c) 2023.
const skipLink: Element = document.querySelector('[data-skip-link="true"]')

// If the skip link is not found, do nothing.
// Else, iterate each skip link and add event listeners.
skipLinks.forEach(function (skipLink): void {
    // Show the skip link when it is focused.
    skipLink.addEventListener('focus', function (): void {
        skipLink.removeAttribute('hidden')
    })
    // Hide the skip link when it is blurred/looses focus & tabbing stops
    skipLink.addEventListener('blur', function (): void {
        skipLink.setAttribute('hidden', 'until-found')
    })
})
