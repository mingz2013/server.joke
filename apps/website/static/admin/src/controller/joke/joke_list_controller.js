/**
 * Created by zhaojm on 15/11/2016.
 */
import article_service from '../../services/article_service'
import category_service from '../../services/category_service'

import $ from 'jQuery'

class ArticleListController {

    constructor() {


        article_service.get_article_list().then((article_list)=> {
            let html_str = '<table><tr><td>index</td><td>title</td><td>author</td></tr>';

            article_list.forEach(({_id, title, author}, index) => {

                html_str += '<tr>' +
                    '<td>' + index + '</td>' +
                    '<td><a href="/admin/article/detail/' + _id + '">' + title + '</a></td>' +
                    '<td>' + author + '</td>' +
                    '<td><a href="/admin/article/edit/' + _id + '">edit</a></td>' +
                    '<td><a href="javascript:void(0);" onclick="window.controller.remove_article(\'' + _id + '\')">remove</a></td>' +
                    '</tr>';
            });

            html_str += '</table>';

            $('#article_list').html(html_str);
        }).catch((errmsg)=> {
            console.log(errmsg);
        });


        //$('#article_detail_btn').click(() => {
        //    location.href = "/admin/article/detail/" + $('#article_id').val();
        //});
        //
        //$('#article_edit_btn').click(() => {
        //    location.href = "/admin/article/edit/" + $('#article_id').val();
        //});
        //$('#article_remove_btn').click(() => {
        //    article_service.remove_article($('#article_id').val());
        //});


    }


    remove_article(article_id) {
        article_service.remove_article(article_id).then((result)=> {
            location.href = "/admin/article/list";
        }).catch((errmsg)=> {
            console.log(errmsg);
        });
    }


}

export default ArticleListController