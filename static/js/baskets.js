window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {

        let t_href = event.target;
        console.log(t_href.name);
        console.log(t_href.value);

        $.ajax({
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data) {
                $('.basket_list').html(data.result)
            },
        });
        Event.preventDefault();
    })

}