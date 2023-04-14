#!/usr/bin/node

class rectangle {

    constructor(w, h) {
        if (w == undefined || h == undefined)
            return NULL

        this.width = w;
        this.height = h;
    }

}

module.exports = { rectangle }