/**
 * Created by zhaojm on 15/11/2016.
 */
import user_service from '../../services/user_service'

import $ from 'jQuery'


class UserEditController {
    constructor() {
        let user_id = $('#user_id').val();


        user_service.get_user(user_id).then((user)=> {

            $('#username').val(user.username);
            $('#email').val(user.email);
            $('#mobile').val(user.mobile);
            $('#sex').val(user.sex);
            $('#permission').val(user.permission);
            $('#create_time').val(user.create_time);

        }).catch((errmsg) => {
            console.log(errmsg)
        });

        $('#change_password_btn').click(()=> {
            $('#change_password_box').toggle();
        });

        $('#change_password_btn_2').click(()=> {
            let old_password = $('#old_password').val();
            let new_password = $('#new_password').val();
            let new_password_2 = $('#new_password_2').val();

        });

        $('#user_edit_btn').click(() => {
            let user = {
                "_id": $('#user_id').val(),
                "username": $('#username').val(),
                "password": $('#password').val(),
                "email": $('#email').val(),
                "mobile": $('#mobile').val(),
                "sex": $('#sex').val(),
                "permission": $('#permission').val(),
            };

            user_service.update_user(user).then((result)=> {
                location.href = "/admin/user/detail/" + user_id;
            }).catch((errmsg) => {
                console.log(errmsg)
            });
        });

    }
}

export default UserEditController;