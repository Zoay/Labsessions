$(document).ready(function() {

    var $form = $('#srch');
    var doSubmit = function() {
        $.post('php_search.php',
            {
                qq: $form.val()
            }, function(data, textStatus, xhr) {
                var persons = $.parseJSON(data);
                var output = "";

                $.each(persons, function(index, person) {
                    output += '<div>' + person.firstname + ' <strong><em>' + person.lastname + '</em></strong></div>';
                });
                $('#result').html(output);
            });
    }

    $form.on('keydown', doSubmit);

});