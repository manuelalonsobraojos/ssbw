$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip();

  $( ".ButtonIncrementLikes" ).click(function() {
    id_visit = $(this).attr('data-id-visit');
    groupClickIncrementLikes(id_visit)
  });

  $( ".ButtonDecrementLikes" ).click(function() {
    id_visit = $(this).attr('data-id-visit');
    groupClickDecrementLikes(id_visit)
  });

});

/**
 * Método en el que se incrementa el numero de likes
 */
function groupClickIncrementLikes(id) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: url_increment_likes,
        data: {'id': id, 'csrfmiddlewaretoken': csrftoken,},
        success: function (data) {
            $("#NumberLikes-"+id).text(data.likes);
        }
    });
}

/**
 * Método en el que se decrementa el numero de likes
 */
function groupClickDecrementLikes(id) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: url_decrement_likes,
        data: {'id': id, 'csrfmiddlewaretoken': csrftoken,},
        success: function (data) {
            $("#NumberLikes-"+id).text(data.likes);
        }
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
