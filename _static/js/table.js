$(window).on('load', function () {

    let tile_click_order = js_vars.tile_click_order;
    let opt_click_order = js_vars.opt_click_order;

    $('.choice-tile').each(function(idx){
        let row_len = $(this).siblings().length;
        let x = idx % row_len;
        let y = Math.floor(idx / row_len);
       $(this).attr("x", x);
       $(this).attr("y", y);
    });

    $('.choice-rad').click(function(){
        let c = $(this).val();
        $('#choice').val(c);

        // Send click information
        opt_click_order += 1;
        liveSend({'func': 'option-click',
                        'seq': opt_click_order,
                        'option': c,
                        });

    });

    $('.cover').click(function(){
        $('.n-cell').css('visibility', 'hidden');
        $('.cover').css('background-color', 'black');

        $(this).css('background-color', 'white');
        $(this).children('.n-cell').css('visibility', 'visible');

        // Send results
        tile_click_order += 1;
        let td = $(this).parents('td');
        let x = td.attr('x');
        let y = td.attr('y');
        liveSend({'func': 'tile-click',
                        'seq': tile_click_order,
                        'x': x, 'y': y});
    });
});