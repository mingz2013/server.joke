/**
 * Created by zhaojm on 15/11/2016.
 */
import joke_service from '../../services/joke_service'
import category_service from '../../services/category_service'
import tag_service from '../../services/tag_service'
import user_service from '../../services/user_service'

import $ from 'jQuery'

class ArticleAddController {

    constructor() {
        this.get_user_list();
        this.get_category_list();
        this.get_tag_list();

        $('#article_add_btn').click(() => {

            let tag_input_list = $("input[type=checkbox][name=tag]:checked");
            console.log(tag_input_list);
            let tag_list = [];

            tag_input_list.each((index, tag_input)=> {
                //tag_list += tag_input.value + ",";
                tag_list.push(tag_input.value);
            });

            let article = {
                "user_id": $('#user_id').val(),
                "title": $('#title').val(),
                "content": $('#content').val(),
                "category": $("input[name='category']:checked").val(),
                "tags": tag_list,
                "status": $('#status').val()
            };
            console.log(article);
            article_service.add_article(article).then((article_id)=> {
                location.href = "/admin/article/detail/" + article_id;
            }).catch((errmsg)=> {
                console.log(errmsg);
            });

        });

        $('#category_add_switch').click(() => {
            $('#category_add_box').toggle();
        });

        $('#category_add_btn').click(() => {
            let title = $('#category_add').val();
            let category = {
                "title": title
            };
            category_service.add_category(category).then((result)=> {
                this.get_category_list();
                $('#category_add_box').toggle();
            }).catch((errmsg)=> {
                console.log(errmsg);
            });
        });


        $('#tag_add_switch').click(() => {
            $('#tag_add_box').toggle();
        });

        $('#tag_add_btn').click(() => {
            let title = $('#tag_add').val();
            let tag = {
                "title": title
            };
            tag_service.add_tag(tag).then((result)=> {
                this.get_tag_list();
                $('#tag_add_box').toggle();
            }).catch((errmsg)=> {
                console.log(errmsg);
            });
        });

    }

    get_user_list() {
        user_service.get_user_list().then((user_list)=> {
            let html_str = '';

            user_list.forEach(({_id, username}, index) => {
                html_str += '<option value="' + _id + '">' + username + '</option>'
            });

            $('#user_id').html(html_str);

        }).catch((errmsg)=> {
            console.log(errmsg);
        });
    }

    get_category_list() {
        category_service.get_category_list().then((category_list)=> {
            let html_str = '';

            category_list.forEach(({title}, index) => {
                html_str += '<input type="radio" name="category" value="' + title + '"/>' + title
            });

            $('#category').html(html_str);
        }).catch((errmsg)=> {
            console.log(errmsg);
        });
    }

    get_tag_list() {
        tag_service.get_tag_list().then((tag_list)=> {
            let html_str = '';

            tag_list.forEach(({title}, index) => {
                html_str += '<input type="checkbox" name="tag" value="' + title + '"/>' + title
            });

            $('#tag_box').html(html_str);
        }).catch((errmsg)=> {
            console.log(errmsg);
        });
    }
}

export default ArticleAddController;