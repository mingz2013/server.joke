/**
 * Created by zhaojm on 13/11/2016.
 */


import ajax_promise from '../api/ajax_promise'


class UserService {
    constructor() {
    }

    get_user_list() {
        return ajax_promise({
            type: "GET",
            url: "/api/user/list"
        });
    };

    remove_user(user_id) {
        return ajax_promise({
            type: "DELETE",
            url: "/api/user/remove/" + user_id
        });
    }

    add_user(user) {
        return ajax_promise({
            type: "POST",
            data: user,
            url: "/api/user/add"
        });
    }


    get_user(user_id) {
        return ajax_promise({
            type: "GET",
            url: "/api/user/detail/" + user_id
        });
    }

    update_user(user) {
        return ajax_promise({
            type: "PUT",
            data: user,
            url: "/api/user/update"
        });
    }
}

let user_service = new UserService();
export default user_service;
