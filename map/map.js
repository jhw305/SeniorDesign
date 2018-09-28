// Constants
var delta = 5 ;
var default_side_length = 10 ;

// Stored user triangle
var current_user_x = 0 ;
var current_user_y = 0 ;
var current_user_theta = 0 ;
var user_exists = false ;

// Stored points
var mypoints = [ ] ;

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

// From degrees to radians
function deg_to_rad( theta_in_degrees ) {
	return ( Math.PI / 180.0 ) * theta_in_degrees ;
}

// Draw triangle centered at ( user_x , user_y )
function plot_user( user_x , user_y , theta_in_degrees , color , side_length ) {
	var canvas = document.getElementById( "themap" ) ;
	var mycontext = canvas.getContext( "2d" ) ;
	// Calculate each corner of the triangle
	// Get the position of each vertex before rotation
	A = new Array( 2 ) ;
	A[ 0 ] = new Array( 1 ) ;
	A[ 1 ] = new Array( 1 ) ; A[ 0 ][ 0 ] = user_x - ( ( Math.sqrt( 3.0 ) / 2.0 ) * side_length ) ;
	A[ 1 ][ 0 ] = user_y - ( side_length / 4.0 ) ;
	B = new Array( 2 ) ;
	B[ 0 ] = new Array( 1 ) ;
	B[ 1 ] = new Array( 1 ) ;
	B[ 0 ][ 0 ] = user_x + ( ( Math.sqrt( 3.0 ) / 2.0 ) * side_length ) ;
	B[ 1 ][ 0 ] = user_y - ( side_length / 4.0 ) ;
	C = new Array( 2 ) ;
	C[ 0 ] = new Array( 1 ) ;
	C[ 1 ] = new Array( 1 ) ;
	C[ 0 ][ 0 ] = user_x ;
	C[ 1 ][ 0 ] = user_y + ( side_length / 4.0 ) ;
	// Get the rotation matrix
	T = new Array( 2 ) ;
	T[ 0 ] = new Array( 2 ) ;
	T[ 1 ] = new Array( 2 ) ;
	T[ 0 ][ 0 ] = Math.cos( deg_to_rad( theta_in_degrees ) ) ;
	T[ 0 ][ 1 ] = -1 * Math.sin( deg_to_rad( theta_in_degrees ) ) ;
	T[ 1 ][ 0 ] = Math.sin( deg_to_rad( theta_in_degrees ) ) ;
	T[ 1 ][ 1 ] = Math.cos( deg_to_rad( theta_in_degrees ) ) ;
	// Perform rotation
	final_A = mat_mult( T , A ) ;
	final_B = mat_mult( T , B ) ;
	final_C = mat_mult( T , C ) ;
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

function plot_all_current_points( ) {
	var pt_cnt = 0 ;
	for ( pt_cnt = 0 ; pt_cnt < mypoints.length ; pt_cnt++ ) {
		plot_point( mypoints[ pt_cnt ][ 0 ] , mypoints[ pt_cnt ][ 1 ] ) ;
	}
}

// Only for testing
function _plot( ) {
	var x = parseInt( document.getElementById( "x_item" ).value ) ;
	var y = parseInt( document.getElementById( "y_item" ).value ) ;
	plot_point( x , y ) ;
	mypoints.push( [ x , y ] ) ;
}

function _plot_user( ) {
	var x = parseInt( document.getElementById( "x_user" ).value ) ;
	var y = parseInt( document.getElementById( "y_user" ).value ) ;
	var theta = parseInt( document.getElementById( "theta_user" ).value ) ;
	// Clear the current user arrow
	if ( user_exists == true ) {
		plot_user( current_user_x , current_user_y , current_user_theta , 'white' , default_side_length + delta ) ;
	} else {
		user_exists = true ;
	}
	// Redraw the points/map in case it got cleared when the user moved
	plot_all_current_points( ) ;
	// Plot user's triangle
	plot_user( x , y , theta , 'red' , default_side_length ) ;
	// Set global vars
	current_user_x = x ;
	current_user_y = y ;
	current_user_theta = theta ;
}
