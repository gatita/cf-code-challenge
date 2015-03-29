$(document).ready(function(){
    $('#add').click(function(){
        var newTodo = $('#new').val();
        $('<tr><td>' + newTodo + '</td></tr>').prependTo('#todos > tbody');
        $('#new').val('');
    });
});

