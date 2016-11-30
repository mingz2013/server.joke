/**
 * Created by zhaojm on 16/11/2016.
 */


import ajax_promise from '../api/ajax_promise'


class LoginService {
    constructor() {
    }

    login(data) {
        return ajax_promise({
            type: "POST",
            data: data,
            url: "/api/user/login"
        });
    };

}

let login_service = new LoginService();
export default login_service;
