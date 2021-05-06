let i = 0;
const srcs = ["/static/img/slider1/group1.png", "/static/img/slider1/group2.png", "/static/img/slider1/group3.png", "/static/img/slider1/group4.png", "/static/img/slider1/group5.png"];
function toggle(){
    $('.slider').animate({'opacity':'0'},600,function(){
        $(this).attr("src", srcs[i]);
        $(this).animate({'opacity':'1'},600);
    });
    i++;
    if(i==4){
        i=0;
    }
}

function test(){
    // alert($(this));
    $(this).css('background-color', 'red');
}
setInterval(toggle, 4000);
