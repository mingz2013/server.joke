/**
 * Created by zhaojm on 16/11/2016.
 */
import $ from 'jQuery'
import login_service from '../services/login_service'

class LoginController {

    constructor() {

        $('#login_btn').click(()=> {
            let username = $('#username').val();
            let passsword = $('#password').val();

            let user = {
                "username": username,
                "password": passsword
            };

            login_service.login(user).then((result)=> {
                location.href = "/admin/";
            }).catch((errmsg)=> {
                console.log(errmsg);
            });


        });

    }


}

export default LoginController;