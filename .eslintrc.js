// Copyright (c) 2023.

module.exports = {
    root: true,
    extends: ['standard', 'prettier'],
    rules: {
        'vue/html-self-closing': [
            'error',
            {
                html: {
                    void: 'never',
                    normal: 'always',
                    component: 'always',
                },
                svg: 'always',
                math: 'always',
            },
        ],
    },
}
