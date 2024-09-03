$(document).ready(function() {
    function add_or_del_good(event) {
        event.preventDefault(); 

        var id_of_good = $(this).find('button').data('good-id'); 
        var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const button = $(this).find('button');

        var form = $(this);
        var goodElement;

        if (button.hasClass('btn_del_good_cart')) {
            goodElement = form.closest('.good_in_cart');
        }

        $.ajax({
            url: form.attr('action'),
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': csrftoken,
                'id_of_good': id_of_good
            },
            success: function(response) {
                $('.cart_quantity').text(response.quantity_sum);
                if (button.hasClass('btn_del_good_cart')) {
                    goodElement.remove();
                    $('.result_price_cart_n').text(response.result_price);
                    $('.result_quantity_cart_n').text(response.quantity_sum);
                } else if (button.hasClass('in_basket_b')) {
                    if (response.is_alredy_in_cart != 'В корзину') {
                        button.text('Уже в корзине');
                        button.append('<img class="button_image" src="/static/images/double-tick.png">');
                        button.addClass('already_in_cart');
                    } else {
                        button.text('В корзину');
                        button.removeClass('already_in_cart');
                    }
                }
            },
            error: function() {
                alert("Произошла ошибка, попробуйте позже");
            }
        });
    }
    
    $('form.form_button').submit(add_or_del_good);
    $('form.form_del_good_cart').submit(add_or_del_good)
});

$(document).ready(function() {
    $(".good_quantity").on("input", function() {

        var id_of_good = $(this).data('good-id'); 
        var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        var quantity = $(this).val();
        var new_price_el = $(this).closest('.good_in_cart').find('.good_price_cart');


        $.ajax({
            url: 'cart_change_quality/' + id_of_good + '/' + quantity + '/',
            type: 'POST',
            data: {
                'id_of_good': id_of_good,
                'csrfmiddlewaretoken': csrftoken,
                'quantity': quantity
            },
            success: function(response) {
                $('.cart_quantity').text(response.quantity_sum);
                $('.result_quantity_cart_n').text(response.quantity_sum);
                var new_price = parseFloat(response.new_price)
                if (Number.isInteger(new_price)) {
                    new_price = new_price.toString();  
                } else {
                    new_price = new_price.toFixed(2).replace(/\.?0+$/, '');
                }
                new_price_el.text(new_price.replace('.',',') + ' руб.');
                $('.result_price_cart_n').text(response.result_price);
            },
            error: function(response) {
                alert("Произошла ошибка, попробуйте позже: " + response.responseJSON.error);
            }
        });
    });
});


window.onpageshow = function(event) {
    if (event.persisted) {
        window.location.reload();
    }
};

function show_hide_sort_menu(){
    var sortContainer = document.querySelector('.sort_by_wr');
    sortContainer.classList.toggle('open');
}

window.addEventListener('click', function(event) {
    var sortContainer = document.querySelector('.sort');
    var sortContainer_ins = document.querySelector('.sort_by_wr');
    if (!sortContainer.contains(event.target)) {
        sortContainer_ins.classList.remove('open');
    }
});

function lazyLoad() {
    $('.lazy_img').each(function() {
        if ($(this).offset().top < $(window).scrollTop() + $(window).height()) {
            const src = $(this).data('src');
            if (src) {
                $(this).attr('src', src);
                $(this).removeAttr('data-src');
            }
        }
    });
}

$(document).ready(function() {
    lazyLoad(); 
    $(window).on('scroll', lazyLoad);
});

