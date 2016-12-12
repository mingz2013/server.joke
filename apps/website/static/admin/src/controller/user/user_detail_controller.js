/**
 * Created by zhaojm on 15/11/2016.
 */

import user_service from '../../services/user_service'

import $ from 'jQuery'


class UserDetailController {
    constructor() {
        let user_id = $('#user_id').val();

        user_service.get_user(user_id).then((user) => {

            $('#username').text(user.username);
            $('#email').text(user.email);
            $('#mobile').text(user.mobile);
            $('#sex').text(user.sex);
            $('#permission').text(user.permission);
            $('#create_time').text(user.create_time);

        }).catch((errmsg) => {
            console.log(errmsg);
        });

        $('#user_edit_btn').click(() => {
            location.href = "/admin/user/edit/" + user_id;
        });

        $('#user_remove_btn').click(() => {
            user_service.remove_user(user_id).then((result) => {
                location.href = "/admin/user/list";

            }).catch((errmsg) => {
                console.log(errmsg);
            });

        });


    }
}

export default UserDetailController;