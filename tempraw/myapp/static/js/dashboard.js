chosenText = $('#testInput').val();
var testVar = [];

function TestFunc(testVar){
chosenText = $('#testInput').val();
testVar = [chosenText, 1];
alert('Sending your test variable: '+testVar);
return testVar
}

$(document).ready( function () {
  $('#testInput').attr('placeholder', 'Type text to send...');

  $('#testBtn').click(function(event){
    testVar = TestFunc(testVar)
    $.ajax({
      data: JSON.stringify({
        'trigger': 'test',
        'sentTerm': '{{sentTerm}}',
        'testVar': testVar
      }),
      type: 'POST',
      url: '/ajaxhandle',
      contentType: 'application/json',
      dataType: 'json',
    })
    .done(function(response){
      window.location= response.url;
    });
    event.preventDefault();
  });

});

$(function () {
  $('[data-toggle="popover"]').popover()
})

$('.popover-dismiss').popover({
  trigger: 'focus'
})
