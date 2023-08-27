/** @type {import("tailwindcss").Config} */
module.exports = {
    content: [
        "./apps/**/templates/**/*.{html,js}",
        "./templates/*.{html,js}",
        "./templates/**/*.{html,js}",
        "./static/**/*.{html,css,js}",
        "./staticfiles/**/*.{html,css,js}"
    ],
    theme: {
        extend: {}
    },
    plugins: []
};
