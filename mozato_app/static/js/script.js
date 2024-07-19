$('#user_m').click(function(e){
    e.preventDefault()
    $('#subMenu').slideToggle();
})


// user-profile popup
$('#user-pro').click(function(e){
    e.preventDefault()
    $('.user-profile').show();
})

$('.cross-user-profile').click(function(){
    $('.user-profile').hide();
})





let scrollConatiner = document.querySelector(".food_theme_under");
let backbtn = document.getElementById("backbtn");
let nextbtn = document.getElementById("nextbtn");

// scrollConatiner.addEventListener("wheel", (e) => {
//     e.preventDefault();
//     scrollConatiner.scrollLeft += e.deltaY;
//     scrollConatiner.computedStyleMap.scrollBehavior = "auto";
// });

nextbtn.addEventListener("click", ()=>{
    scrollConatiner.style.scrollBehavior = "smooth";
    scrollConatiner.scrollLeft += 400;
});

backbtn.addEventListener("click", ()=>{
    scrollConatiner.style.scrollBehavior = "smooth";
    scrollConatiner.scrollLeft -= 400;
});


// brand scroll
let scrollConatiner_1 = document.querySelector(".brand_img");
let backbtn_1 = document.getElementById("backbtn_1");
let nextbtn_1 = document.getElementById("nextbtn_1");

nextbtn_1.addEventListener("click", ()=>{
    scrollConatiner_1.style.scrollBehavior = "smooth";
    scrollConatiner_1.scrollLeft += 400;
});

backbtn_1.addEventListener("click", ()=>{
    scrollConatiner_1.style.scrollBehavior = "smooth";
    scrollConatiner_1.scrollLeft -= 400;
});


