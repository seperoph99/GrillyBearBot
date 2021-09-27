	// Toggle Mode
    $( ".inner-switch" ).on("click", function() {
        if( $( ".header" ).hasClass( "dark" )) {
          $( ".header" ).removeClass( "dark" );
          $( ".inner-switch" ).text( "OFF" );
        } else {
          $( ".header" ).addClass( "dark" );
          $( ".inner-switch" ).text( "ON" );
        }
    });