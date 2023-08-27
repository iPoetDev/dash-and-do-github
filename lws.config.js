module.exports = {
    // Base
    directory: '.',
    port: 8004,
    hostname: '127.0.0.1',
    // Static Files
    static: [
        {
            index: 'page.html',
            maxage: 0,
        },
    ],
    // Observability
    logFormat: 'stats',
}
