let li = document.getElementsByTagName('li');

function change(id) {
    // 定位当前点击的 li ，并改变其 class 和其子元素 a 的 class
    let select = document.getElementById(id);
    select.className = "li1 li2";
    select.firstChild.className = "a1 a2";
    for (let i = 0; i < li.length; i++) {
        if (li[i].id !== id) {
            li[i].className = "li1";
            li[i].firstChild.className = "a1";
        }
    }
    select = '';
}

function iframeShow(src) {  // 获取当前 iframe 显示页面的链接地址，并改变相应的 li 和 a 标签的 class
    /* src 的值在 html 中传递时不能直接传递当前 iframe 的 src 属性，
       而应该是使用 this.contentWindow.location.href 来传递 iframe 当前显示页面的链接地址 */
    // console.log("iframe src:");
    // console.log(src);
    let iframe = document.getElementsByClassName('show')[0];
    for (let i = 0; i < li.length; i++) {
        if (li[i].firstChild.href == src) {
            // 判断 iframe 当前显示的页面链接 src 与选中的 a 中的 href 是否相同
            li[i].className = 'li1 li2';
            li[i].firstChild.className = 'a1 a2';
        } else {
            li[i].className = 'li1';
            li[i].firstChild.className = 'a1';
        }
    }
}

