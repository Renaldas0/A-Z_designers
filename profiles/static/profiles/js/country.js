/* Sets the colour of country input placeholder to grey and if a country is selected to black */

let countrySelected = $('#id_default_country');
if (!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
}

$('#id_default_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});