$(document).ready(function(){
    var groups_meetup = [];
    $('#groups_meetup input[name="g_meetup"]').each(function() {
        groups_meetup.push(($(this).val()));
    });

    $.get("http://127.0.0.1:5000/api/v1/events_meetup", { "groups_meetup": JSON.stringify(groups_meetup)},
        function(data, status){
            $('#events_meetup').html(data.html);
    });
});
//$('#groups_meetup input[name="g_meetup"]').val()