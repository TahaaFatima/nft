$(document).ready(function(){
    $('.list').click(function(){
        const value = $(this).attr('data-filter');

        if (value == 'all'){
            $('.all').show('1000');
        }

        else{
            $('.all').filter('.' + value).show('1000');
            $('.all').not('.' + value).hide('1000');
        }
    })
    $('.list').click(function(){
        $(this).addClass('active').siblings().removeClass('active')
    })
})

// AOS.init();