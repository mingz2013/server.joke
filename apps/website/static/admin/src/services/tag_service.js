/**
 * Created by zhaojm on 15/11/2016.
 */

import ajax_promise from '../api/ajax_promise'


class TagService {
    constructor() {
    }

    add_tag(tag) {
        return ajax_promise({
            type: "POST",
            data: tag,
            url: "/api/tag/add"
        })
    }

    get_tag_list() {
        return ajax_promise({
            type: "GET",
            url: "/api/tag/list"
        })
    }


}

let tag_service = new TagService();

export default tag_service;