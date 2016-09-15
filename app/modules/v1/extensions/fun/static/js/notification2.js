var client = null;
$(document).ready(function() {
  if (typeof $.mobile === 'object') {
  	$.mobile.linkBindingEnabled = false;
  	$.mobile.ajaxEnabled = false;
  	$.mobile.hashListeningEnabled = false;
  }
  $('.collapsable').hide();
  $('.permalink').bind('click', function() {
    if ($(this).parents('td').length > 0) {
      $(this).closest('tr').find('.collapsable').toggle();
    } else {
      $(this).closest('div').find('.collapsable').toggle();
    }

    return false;
  });

  var minutes = 5;
  var seconds = minutes * 60;
  var counter = setInterval(function() {
    if (seconds > 0) {
      seconds--;
      var mins = Math.floor(seconds / 60);
      var secs = seconds - (mins * 60);
      if (mins < 10)
        mins = '0' + mins;
      if (secs < 10)
        secs = '0' + secs;
      $('.timer').html(mins + ':' + secs);
    } else {
      seconds = minutes * 60;
      $.notificationcenter.newAlert('This alert has been pushed via ' + minutes + ' minute timer', 'invite');
    }
  }, 1000);

  var date = new Date();
  $('body').notificationcenter({
    notification_offset: 50,
    types:[
      {
        type: 'sticky',
        img: 'fa fa-clock-o',
        imgtype: 'class',
        display_time: 0
      },
      {
        type: 'fontawesome',
        img: 'fa fa-bullseye',
        imgtype: 'class',
        type_max_display: 2,
        alert_hidden_sound: 'sounds/Basso'
      },
      {
        type: 'invite',
        img: '//raw.githubusercontent.com/TheSin-/notificationcenter/master/img/invite.png',
        bgcolor: '#3366ff'
      },
      {
        type: 'todo',
        img: '//raw.githubusercontent.com/TheSin-/notificationcenter/master/img/clipboard.png',
        bgcolor: '#fff',
        color: '#000'
      },
      {
        type: 'gift',
        img: '//raw.githubusercontent.com/TheSin-/notificationcenter/master/img/gift.png',
        bgcolor: '#eb5d49',
        truncate_message: 50
      },
      {
        type: 'calendar',
        img: '//raw.githubusercontent.com/TheSin-/notificationcenter/master/img/calendar.png',
        bgcolor: '#2767a8'
      },
      {
        type: 'system',
        img: '//raw.githubusercontent.com/TheSin-/notificationcenter/master/img/settings.png',
        type_max_display: 10
      }
    ],
    default_notifs:[
      {
        type: 'system',
        values:[{
          text: {
            text: 'This is an example, I have a callback click me to see it.',
            title: 'Callback'
          },
          time: date.getTime()/1000,
          callback: function(notif) {
            $.notificationcenter.alert(notif.text, notif.type);
          },
          new: true
        }]
      }
    ],
    alert_hidden_sound: 'sounds/Purr',
    store_callback: function(notifs) {
      console.log(JSON.stringify(notifs));
    }
  });

  $('.slideit').on('click', function() {
    $.notificationcenter.slide();
  });

  $('.notif').on('click', function() {
    if ($(this).attr('data-type') == 'snooze')
      $.notificationcenter.alert('New alert by button click, with a callback action.', 'sticky', function(notif) { setTimeout( function() { $.notificationcenter.alert(notif.text, notif.type, notif.callback, 'snooze'); }, 1 * 60 * 1000); }, 'snooze');
    else
      $.notificationcenter.newAlert({'text':'New alert by button click.', 'title':$(this).attr('data-type')}, $(this).attr('data-type'));
  });

  var ajax_options = 'examples/object.json';
  var ajax_checkTime = 5 * 60 * 1000; // 5 minutes
  $('.ajax').on('click', function() {
    if (!$('.ajax').hasClass('disabled')) {
      $.notificationcenter.ajax(ajax_options, ajax_checkTime);
      $('.ajax').addClass('disabled');
    }
  });
});
