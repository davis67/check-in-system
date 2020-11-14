'use strict'
const {
    VueLoaderPlugin
} = require('vue-loader')
const {
    join
} = require('path');
module.exports = {
    mode: 'development',
    entry: [
        './assets/js/main.js'
    ],
    module: {
        rules: [{
            test: /\.vue$/,
            use: 'vue-loader'
        }]
    },
    resolve: {
        alias: {
            vue: 'vue/dist/vue.js'
        },
    },
    output: {
        path: join(__dirname, 'static/js'),
        filename: 'app.min.js'
    },
    plugins: [
        new VueLoaderPlugin()
    ]
}