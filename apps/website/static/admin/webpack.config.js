/**
 * Created by zhaojm on 13/11/2016.
 */
var path = require('path');
var webpack = require('webpack');
var ROOT_PATH = path.resolve(__dirname);

module.exports = {

    entry: [path.resolve(ROOT_PATH, 'src/index.js')],

    output: {
        path: path.resolve(ROOT_PATH, 'dist'),
        filename: 'bundle.js'
    },

    resolve: {
        extensions: ['', '.js', '.jsx']
    },

    module: {
        loaders: [
            {
                test: /\.js|jsx$/,
                exclude: /node_modules/,
                loader: "babel",
                query: {
                    presets: ['es2015']
                }
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader'
            },
            {
                test: /\.(png|jpg)$/,
                loader: 'url-loader?limit=8192'
            },
            {
                test: /\.scss$/,
                loader: "style!css!sass"
            }
        ]
    }
};
