$('#inputField').keyup(function(e) {
    if ($('#inputField').val() === '') {
        $('#buttonField').attr('disabled', true);
    } else {
        $('#buttonField').attr('disabled', false);
    }
});