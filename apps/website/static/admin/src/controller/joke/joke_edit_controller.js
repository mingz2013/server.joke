/**
 * Created by zhaojm on 15/11/2016.
 */
import article_service from '../../services/article_service'
import category_service from '../../services/category_service'

import $ from 'jQuery'

class ArticleEditController {

    constructor() {
        let article_id = $('#article_id').val();

        article_service.get_article(article_id).then((article)=> {
            $('#title').val(article.title);
            $('#content').val(article.content);
            $('#author').val(article.author);
            $('#category').val(article.category);
            $('#tags').val(article.tags);
            $('#create_time').val(article.create_time);
            $('#update_time').val(article.update_time);
        }).catch((errmsg)=> {
            console.log(errmsg);
        });


        $('#article_edit_btn').click(() => {


            let article = {
                "_id": article_id,
                "title": $('#title').val(),
                "content": $('#content').val(),
                "author": $('#author').val(),
                "category": $('#category').val(),
                "tags": $('#tags').val(),
                "create_time": $('#create_time').val(),
                "update_time": $('#update_time').val(),
            };

            article_service.update_article(article).then((result)=> {
                location.href = "/admin/article/detail/" + article_id;
            }).catch((errmsg)=> {
                console.log(errmsg);
            });
        });

    }
}

export default ArticleEditController