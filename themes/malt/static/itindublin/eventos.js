function getEventsMeetup(api_service){
    var groups_meetup = [];
    $('#groups_meetup input[name="g_meetup"]').each(function() {
        groups_meetup.push(($(this).val()));
    });

    $.get(api_service+"/events_meetup", { "groups_meetup": JSON.stringify(groups_meetup)},
        function(data, status){
            $('#events_meetup').html(data.html);
    });
}
