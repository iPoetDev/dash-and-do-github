/** @type {import("tailwindcss").Config} */
module.exports = {
    content: {
        relative: true,
        files: [
            './templates/index.html', // main index file & entrpoint
            './apps/**/templates/**/*.{html,js}',
            './templates/*.{html,js}',
            './templates/**/*.{html,js}',
            './static/**/*.{html,css,js}',
            './staticfiles/**/*.{html,css,js}',
        ],
    },
    theme: {
        container: {
            center: true,
        },
        fontFamily: {
            sans: ['Inter', 'sans-serif'],
            serif: ['Inter', 'sans-serif'],
        },
        extend: {},
    },
    plugins: [require('tailwindcss-owl')],
}
