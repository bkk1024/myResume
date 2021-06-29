// 左右切换轮播器的 js 代码，整体思路就是通过 index 这个变量来改变显示的 图片和点
// changeMarginLeft() 函数就是改变第一个 ul 中的所有 li 的 marginLeft 的值形成左右切换的效果

let box = document.getElementsByClassName('box')[0];  // 定位轮播器父盒子 box
let boxLi = box.getElementsByTagName('li');  // 定位 box 中的所有的 li 标签
let prev = document.getElementsByClassName('prev')[0],
    next = document.getElementsByClassName('next')[0];  // 定位 上一张 和 下一张 按钮
let time = 0;  // 定时器时间参数
let point = document.getElementsByClassName('point')[0];  // 定位轮播器小点父盒子 point
let pointLi = point.getElementsByTagName('li');  // 定位 point 中的所有 li 标签
var index = 0;  // 表示哪个图片、小点在显示

function cleanIndex(name) {
    for (let i = 0; i < name.length; i++) {
        name[i].className = '';
    }
}

function changeMarginLeft() {
    cleanIndex(pointLi);
    boxLi[0].style.marginLeft = -721*index + 'px';
    boxLi[1].style.marginLeft = -721*(index - 1) + 'px';
    boxLi[2].style.marginLeft = -721*(index - 2) + 'px';
    boxLi[3].style.marginLeft = -721*(index - 3) + 'px';
    boxLi[4].style.marginLeft = -721*(index - 4) + 'px';
    pointLi[index].className = 'select';
}

function goPrev() {
    if (index == 0) {
        index = pointLi.length - 1;
    } else {
        index--;
    }
    changeMarginLeft();
}

function goNext() {
    if (index == pointLi.length - 1) {
        index = 0;
    } else {
        index++;
    }
    changeMarginLeft();
}

prev.addEventListener('click', function() {
    goPrev();
    time = 0;
});

next.addEventListener('click', function() {
    goNext();
    time = 0;
});

for (let i = 0; i < boxLi.length; i++) {
    pointLi[i].addEventListener('click', function() {
        let pointLiIndex = this.getAttribute('data-index');
        // HTML5 可以通过 data-XXX 来定义一个属性存放数据，在 js 中通过 this.getAttribute('data-XXX'); 方法获取该数据
        index = pointLiIndex - 1;
        goNext();
        time = 0;
    });
}

// 重复执行定时器，设定每 3s 执行一次 goIndex() 函数
var show = setInterval(function(){
    time++;
    if (time == 30) {
        goNext();
        time = 0;
    }
}, 100);