/**
 * Created by zhaojm on 15/11/2016.
 */

import $ from 'jQuery'

let ajax_promise = (params) => {
    return new Promise((resolve, reject) => {
        $.ajax(params).then((data) => {
            console.log(data);
            if (data.retcode == 0) {
                resolve(data.result)
            } else {
                Promise.reject(data.errmsg);
            }
        }, reject);
    })
};

export default ajax_promise;