/**
 * Created by zhaojm on 15/11/2016.
 */

import ajax_promise from '../api/ajax_promise'


class CategoryService {
    constructor() {
    }

    add_category(category) {
        return ajax_promise({
            type: "POST",
            data: category,
            url: "/api/category/add"
        })
    }

    get_category_list() {
        return ajax_promise({
            type: "GET",
            url: "/api/category/list"
        })
    }


}

let category_service = new CategoryService();

export default category_service;