  $(function() {
    $( ".dialog" ).click(function(){        
        $('#dialog').html($(this).html());
        $('#dialog').dialog();
    });
  });