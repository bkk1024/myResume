function change(id) {
    // 定位当前点击的 li ，并改变其 class 和其子元素 a 的 class
    let select = document.getElementById(id);
    select.className = "li1 li2";
    select.firstChild.className = "a1 a2";
    // 获取到其他的 li ，改变其 class 和其子元素 a 的 class 为初始样式
    let other = document.getElementsByTagName('li');
    for (let i = 0; i < other.length; i++) {
        if (other[i].id !== id) {
            other[i].className = "li1";
            other[i].firstChild.className = "a1";
        }
    }
}
