/**
 * Created by zhaojm on 15/11/2016.
 */
import article_service from '../../services/article_service'
import category_service from '../../services/category_service'

import $ from 'jQuery'

class ArticleDetailController {

    constructor() {
        let article_id = $('#article_id').val();
        article_service.get_article(article_id).then((article)=> {
            $('#title').text(article.title);
            $('#content').text(article.content);
            $('#author').text(article.author.username);
            $('#category').text(article.category);
            $('#tags').text(article.tags);
            $('#create_time').text(article.create_time);
            $('#update_time').text(article.update_time);
        }).catch((errmsg)=> {
            console.log(errmsg);
        });


        $('#article_edit_btn').click(() => {
            location.href = "/admin/article/edit/" + article_id;
        });
        $('#article_remove_btn').click(() => {
            article_service.remove_article(article_id).then((result)=> {
                location.href = "/admin/article/list";
            }).catch((errmsg)=> {
                console.log(errmsg);
            });
        });




    }
}

export default ArticleDetailController