#!/usr/bin/node

class Rectangle {

    constructor(w, h) {
        if (w == undefined || h == undefined)
            return NULL

        this.width = w;
        this.height = h;
    }

}

module.exports = Rectangle