$(document).ready(function(){
    $('#add').click(function(){
        addRow();
    });
    $('#new').keydown(function(e) {
        if (e.keyCode == 13) {
            addRow();
        }
    });
});

function addRow() {
    if ($('#new').val() != '') {
        var newTodo = $('#new').val();
        $("<tr><td>" + newTodo + '</td></tr>').prependTo('#todos > tbody');
        $('#new').val('');
        $('#todos td').click(function(){
            $(this).remove();
        });
    }
};


