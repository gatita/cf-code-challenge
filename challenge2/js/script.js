$(document).ready(function(){
    $('#add').click(function(){
        var newTodo = $('#new').val();
        $('#todos > tbody:first').append('<tr><td>' + newTodo + '</td></tr>');
    });
});

