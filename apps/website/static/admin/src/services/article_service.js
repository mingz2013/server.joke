/**
 * Created by zhaojm on 13/11/2016.
 */


import ajax_promise from '../api/ajax_promise'


class ArticleService {
    constructor() {

    }

    get_article_list() {
        return ajax_promise({
            type: "GET",
            url: "/api/article/list"
        })
    }

    remove_article(article_id) {
        return ajax_promise({
            type: "DELETE",
            url: "/api/article/remove/" + article_id
        })
    }

    add_article(article) {

        return ajax_promise({
            type: "POST",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(article),
            dataType: "json",
            url: "/api/article/add"
        })
    }

    get_article(article_id) {
        return ajax_promise({
            type: "GET",
            url: "/api/article/detail/" + article_id
        })
    }

    update_article(article) {
        return ajax_promise({
            type: "PUT",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(article),
            dataType: "json",
            url: "/api/article/update"
        })
    }


    get_author_list() {
        user_api.get_user_list().then((data) => {
            //通过拿到的数据渲染页面
            console.log(data);

            if (data.retcode == 0) {
                console.log("get success..");
                //location.href = "/admin/article/list";
                var user_list = data.result;

                var html_str = '';

                user_list.forEach(({_id, username}, index) => {
                    html_str += '<option value="' + _id + '">' + username + '</option>'
                });
                $('#user_id').html(html_str);

            } else {
                console.log("error retcode...");
                Promise.reject(data.errmsg);
            }
        }).catch(function (errmsg) {
            //获取数据失败时的处理逻辑
            console.log(errmsg)
        })
    }
}

let article_service = new ArticleService();
export default article_service;
