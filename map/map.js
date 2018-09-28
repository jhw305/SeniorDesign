// TODO Some kind of layering capability so that the user, items, and the map can be in different layers?
// TODO Hmmmm... a more general clearing capability?
// TODO This really should be object-oriented in some way...

// Background image
var bground_img_src = "map.jpg"

function set_bground( ) {
	var canvas = document.getElementById( "themap" ) ;
	var mycontext = canvas.getContext( "2d" ) ;
	var bground_img = new Image( ) ;
	bground_img.src = bground_img_src ;
	mycontext.drawImage( bground_img , 0 , 0 ) ;
	// From https://stackoverflow.com/questions/23104582/scaling-an-image-to-fit-on-canvas
	mycontext.drawImage( bground_img , 0 , 0 , bground_img.width , bground_img.height , 0 , 0 , canvas.width , canvas.height ) ;
}
set_bground( ) ;

// Constants
var delta = 5 ;
var default_side_length = 30 ;
var default_height = 25 ;

// Stored user triangle
var current_user_x = 0 ;
var current_user_y = 0 ;
var current_user_theta = 0 ;
var user_exists = false ;

// Stored points
var mypoints = [ ] ;
var last_plotted_point_x = 0 ;
var last_plotted_point_y = 0 ;
var at_least_one_point = false ;

// Available to programmers
// Taken from https://stackoverflow.com/questions/7812514/drawing-a-dot-on-html5-canvas
function plot_point( center_x , center_y ) {
	var canvas = document.getElementById( "themap" ) ;
	var mycontext = canvas.getContext( "2d" ) ;
	var radius = 5 ;
	var angle_start = 0 ;
	var angle_end = 2 * Math.PI ;
	var ctr_clockwise = true ;
	mycontext.beginPath( ) ;
	mycontext.arc( center_x , center_y , radius , angle_start , angle_end , ctr_clockwise ) ;
	mycontext.fillStyle = 'blue' ;
	mycontext.fill( ) ;
	mycontext.strokeStyle = 'blue' ;
	mycontext.stroke( ) ;
}

// Matrix multiplication
// A,B - arrays of arrays
// TODO: Error checking possible?
function mat_mult( A , B ) {
	var A_row_cnt = 0 ;
	var B_col_cnt = 0 ;
	var B_row_cnt = 0 ;
	var C = new Array( A.length ) ;
	for ( A_row_cnt = 0 ; A_row_cnt < A.length ; A_row_cnt++ ) {
		var row_in_C = new Array( B[ 0 ].length ) ;
		for ( B_col_cnt = 0 ; B_col_cnt < B[ 0 ].length ; B_col_cnt++ ) {
			var mysum = 0 ;
			for ( B_row_cnt = 0 ; B_row_cnt < B.length ; B_row_cnt++ ) {
				mysum += A[ A_row_cnt ][ B_row_cnt ] * B[ B_row_cnt ][ B_col_cnt ] ;
			}
			row_in_C[ B_col_cnt ] = mysum ;
		}
		C[ A_row_cnt ] = row_in_C ;
	}
	return C ;
}

// TODO: Error checking - must be same size
function mat_add( A , B ) {
	var C = [ ] ;
	var ab_row_cnt = 0 ;
	var ab_col_cnt = 0 ;
	for ( ab_row_cnt = 0 ; ab_row_cnt < A.length ; ab_row_cnt++ ) {
		row_in_C = [ ] ;
		for ( ab_col_cnt = 0 ; ab_col_cnt < A[ 0 ].length ; ab_col_cnt++ ) {
			row_in_C.push( A[ ab_row_cnt ][ ab_col_cnt ] + B[ ab_row_cnt ][ ab_col_cnt ] ) ;
		}
		C.push( row_in_C ) ;
	}
	return C ;
}

function scalar_mult( c , A ) {
	var B = [ ] ;
	var a_row_cnt = 0 ;
	var a_col_cnt = 0 ;
	for ( a_row_cnt = 0 ; a_row_cnt < A.length ; a_row_cnt++ ) {
		var B_row = [ ] ;
		for ( a_col_cnt = 0 ; a_col_cnt < A[ 0 ].length ; a_col_cnt++ ) {
			B_row.push( c * A[ a_row_cnt ][ a_col_cnt ] ) ;
		}
		B.push( B_row ) ;
	}
	return B ;
}

// TODO: Error checking - must be same size
function mat_sub( A , B ) {
	return mat_add( A , scalar_mult( -1 , B ) ) ;
}

// From degrees to radians
function deg_to_rad( theta_in_degrees ) {
	return ( Math.PI / 180.0 ) * theta_in_degrees ;
}

// Draw triangle centered at ( user_x , user_y )
function plot_user( user_x , user_y , theta_in_degrees , color , side_length , height ) {
	var canvas = document.getElementById( "themap" ) ;
	var mycontext = canvas.getContext( "2d" ) ;
	var center = [ [ user_x ] , [ user_y ] ] ;
	// Calculate each corner of the triangle
	// Get the position of each vertex before rotation
	A = new Array( 2 ) ;
	A[ 0 ] = new Array( 1 ) ;
	A[ 1 ] = new Array( 1 ) ;
	A[ 0 ][ 0 ] = user_x - Math.sqrt( ( side_length * side_length ) - ( height * height ) ) ;
	A[ 1 ][ 0 ] = user_y - ( height / 2.0 ) ;
	B = new Array( 2 ) ;
	B[ 0 ] = new Array( 1 ) ;
	B[ 1 ] = new Array( 1 ) ;
	B[ 0 ][ 0 ] = user_x + Math.sqrt( ( side_length * side_length ) - ( height * height ) ) ;
	B[ 1 ][ 0 ] = user_y - ( height / 2.0 ) ;
	C = new Array( 2 ) ;
	C[ 0 ] = new Array( 1 ) ;
	C[ 1 ] = new Array( 1 ) ;
	C[ 0 ][ 0 ] = user_x ;
	C[ 1 ][ 0 ] = user_y + ( height / 2.0 ) ;
	// Get the rotation matrix
	T = new Array( 2 ) ;
	T[ 0 ] = new Array( 2 ) ;
	T[ 1 ] = new Array( 2 ) ;
	T[ 0 ][ 0 ] = Math.cos( deg_to_rad( theta_in_degrees ) ) ;
	T[ 0 ][ 1 ] = -1 * Math.sin( deg_to_rad( theta_in_degrees ) ) ;
	T[ 1 ][ 0 ] = Math.sin( deg_to_rad( theta_in_degrees ) ) ;
	T[ 1 ][ 1 ] = Math.cos( deg_to_rad( theta_in_degrees ) ) ;
	// 1) Move origin to center of triangle
	// 2) Perform rotation
	// 3) Shift origin back to original position
	final_A = mat_add( mat_mult( T , mat_sub( A , center ) ) , center ) ;
	final_B = mat_add( mat_mult( T , mat_sub( B , center ) ) , center ) ;
	final_C = mat_add( mat_mult( T , mat_sub( C , center ) ) , center ) ;
	// Draw triangle
	mycontext.beginPath( ) ;
	mycontext.moveTo( final_A[ 0 ][ 0 ] , final_A[ 1 ][ 0 ] ) ;
	mycontext.lineTo( final_B[ 0 ][ 0 ] , final_B[ 1 ][ 0 ] ) ;
	mycontext.lineTo( final_C[ 0 ][ 0 ] , final_C[ 1 ][ 0 ] ) ;
	mycontext.lineTo( final_A[ 0 ][ 0 ] , final_A[ 1 ][ 0 ] ) ;
	mycontext.fillStyle = color ;
	mycontext.fill( ) ;
	mycontext.strokeStyle = color ;
	mycontext.stroke( ) ;
}

// Draw a line from last point plotted to the point provided
function draw_line( x , y ) {
	var canvas = document.getElementById( "themap" ) ;
	var mycontext = canvas.getContext( "2d" ) ;
	mycontext.beginPath( ) ;
	mycontext.moveTo( last_plotted_point_x , last_plotted_point_y ) ;
	mycontext.lineTo( x , y ) ;
	mycontext.strokeStyle = 'blue' ;
	mycontext.stroke( ) ;
}

// Add another item point to the map
// push is optional arg. Determines whether to push to mypoints.
function next_point( x , y , push ) {
	plot_point( x , y ) ;
	if ( typeof( push ) === 'undefined' || push == true ) {
		mypoints.push( [ x , y ] ) ;
	}
	if ( at_least_one_point == false ) {
		at_least_one_point = true ;
	} else {
		draw_line( x , y ) ;
	}
	last_plotted_point_x = x ;
	last_plotted_point_y = y ;
}

function plot_all_points( ) {
	at_least_one_point = false ;
	var point_ctr = 0 ;
	for ( point_ctr = 0 ; point_ctr < mypoints.length ; point_ctr++ ) {
		next_point( mypoints[ point_ctr ][ 0 ] , mypoints[ point_ctr ][ 1 ] , false ) ;
	}
}

// Only for testing
function _plot( ) {
	var x = parseInt( document.getElementById( "x_item" ).value ) ;
	var y = parseInt( document.getElementById( "y_item" ).value ) ;
	next_point( x , y ) ;
}

function _plot_user( ) {
	var x = parseInt( document.getElementById( "x_user" ).value ) ;
	var y = parseInt( document.getElementById( "y_user" ).value ) ;
	var theta = parseInt( document.getElementById( "theta_user" ).value ) ;
	// Clear the current user arrow
	if ( user_exists == true ) {
		plot_user( current_user_x , current_user_y , current_user_theta , 'white' , default_side_length + delta , default_height + delta ) ;
	} else {
		user_exists = true ;
	}
	// Redraw the points/map in case it got cleared when the user moved
	set_bground( ) ;
	plot_all_points( ) ;
	// Plot user's triangle
	plot_user( x , y , theta , 'red' , default_side_length , default_height ) ;
	// Set global vars
	current_user_x = x ;
	current_user_y = y ;
	current_user_theta = theta ;
}
