    // Function to show or hide the scroll-up button based on scroll position
    window.onscroll = function() {
        scrollFunction();
    };

    function scrollFunction() {
        var scrollBtn = document.querySelector('.scroll-up-btn');
        if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
            scrollBtn.style.display = "block";
        } else {
            scrollBtn.style.display = "none";
        }
    }

    // Function to scroll to the top when the button is clicked
    function scrollToTop() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    }



    document.addEventListener('DOMContentLoaded', function () {
        var profileOpenBtn = document.getElementById('profile-open-btn');
        var profileDiv = document.getElementById('profile-div');
    
        profileOpenBtn.addEventListener('click', function (event) {
            event.stopPropagation();
            profileDiv.style.display = (profileDiv.style.display === 'block') ? 'none' : 'block';
        });
    
        document.addEventListener('click', function (event) {
            var targetElement = event.target;
            if (profileDiv.style.display === 'block' && !profileDiv.contains(targetElement)) {
                profileDiv.style.display = 'none';
            }
        });
    });


    document.addEventListener('DOMContentLoaded', function () {
        var postEditOpenBtn = document.getElementById('post-edit-btn');
        var postEdit = document.getElementById('post-edit');
    
        postEditOpenBtn.addEventListener('click', function (event) {
            event.stopPropagation();
            postEdit.style.display = (postEdit.style.display === 'block') ? 'none' : 'block';
        });
    
        document.addEventListener('click', function (event) {
            var targetElement = event.target;
            if (postEdit.style.display === 'block' && !postEdit.contains(targetElement)) {
                postEdit.style.display = 'none';
            }
        });
    });



const menuBtn = document.getElementById('menu-btn')
const aside = document.getElementById('aside')
const main = document.getElementById('main')

menuBtn.addEventListener('click', ()=>{
    aside.classList.toggle('width-20')
    aside.classList.toggle('width-0')
    main.classList.toggle('margin-20')
})