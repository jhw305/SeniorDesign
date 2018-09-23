var script = document.createElement('script');
script.src = 'jquery.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);


class listItem{
    constructor(name, currentQuatity, neededQuatity, price){
        this.name = name;
        this.currentQuatity = currentQuatity;
        this.neededQuatity = neededQuatity;
        this.price = price;
    }

    get getCostNeeded( ) {
        return this.neededQuatity * this.price;
    }
    
    get getCurrentCost( ){
        return this.currentQuatity * this.price;
    }
}

let shoppingList = [];

shoppingList.push( new listItem( "Apples", 3, 4, 3.26 ) );
shoppingList.push( new listItem( "Oranges", 0, 5, .87) );
shoppingList.push( new listItem( "Bananas", 1, 4, 4.51 ) );
shoppingList.push( new listItem( "Pears", 3, 7, 2.29) );
shoppingList.push( new listItem( "Grapes", 0, 1, 4.75 ) );
shoppingList.push( new listItem( "Apples", 3, 4, 3.26 ) );
shoppingList.push( new listItem( "Oranges", 0, 5, .87) );
shoppingList.push( new listItem( "Bananas", 1, 4, 4.51 ) );
shoppingList.push( new listItem( "Pears", 3, 7, 2.29) );
shoppingList.push( new listItem( "Grapes", 0, 1, 4.75 ) );
shoppingList.push( new listItem( "Apples", 3, 4, 3.26 ) );
shoppingList.push( new listItem( "Oranges", 0, 5, .87) );
shoppingList.push( new listItem( "Bananas", 1, 4, 4.51 ) );
shoppingList.push( new listItem( "Pears", 3, 7, 2.29) );
shoppingList.push( new listItem( "Grapes", 0, 1, 4.75 ) );
shoppingList.push( new listItem( "Apples", 3, 4, 3.26 ) );
shoppingList.push( new listItem( "Oranges", 0, 5, .87) );
shoppingList.push( new listItem( "Bananas", 1, 4, 4.51 ) );
shoppingList.push( new listItem( "Pears", 3, 7, 2.29) );
shoppingList.push( new listItem( "Grapes", 0, 1, 4.75 ) );

generateTable( shoppingList );

$( '#totalMoneySpent' ).html( getTotal( shoppingList ) );


/*
if an item is clicked inside the list, this will toggle between the edit state and the 
normal state. Does some error checking to ensure that the user changes to a valid value.
*/
$( "tbody tr" ).click( function ( e ) {
    if( $( this ).hasClass( 'notChanged' ) ){
        $( this ).toggleClass( "selected notChanged" );
        $( this ).html(
            "<td id='back'>Back</td>" + 
            "<td id='value' type='text'><input class='textCenter textSmall editQuantityButtons' style='width: 80px;' placeholder='0'></td>"+
            "<td id='submit'>Change Quantity</td>"
            );
    }
    else{
        
        let change = false;
        let row = this;

        if( ( $(e.target).get(0).id ) == 'back'){
            change = true;
        }
        else if( ( $(e.target).get(0).id ) == 'submit'){
            let newValue = $( this ).find(":input").val();
            let row = this.closest('tr').rowIndex ;
            if( newValue != ''){
                if( newValue > shoppingList[row].neededQuatity || newValue < 0 || isNaN( newValue ) ){
                    alert("Please enter a valid quantity.");
                }
                else{
                    shoppingList[row].currentQuatity = newValue;
                    $( '#totalMoneySpent' ).html( getTotal( shoppingList ) );
                }
            }
            else{
                shoppingList[row].currentQuatity = '0';
                $( '#totalMoneySpent' ).html( getTotal( shoppingList ) );
            }
            change = true;
        }
        
        if(change){
            $( this ).toggleClass( "selected notChanged" );
            $( this ).html( generateRow( shoppingList, this.closest('tr').rowIndex ) );
        }
    }
});


/*
Takes the current shopping list and generates the table upon entering the page.
If the table is empty, an empty string will be returned
*/
function generateTable( shoppingList ){

    let tableValue = "";

    if ( shoppingList.length != 0 ){
        for(let i = 0; i < shoppingList.length; i++){
            $('#shoppingList > tbody:last-child').append(
                "<tr id='" + shoppingList[i].name + "' class='notChanged textSmall'>" + 
                    "<td>" + shoppingList[i].name + "</td>" + 
                    "<td>" + shoppingList[i].currentQuatity + " / " + shoppingList[i].neededQuatity + "</td>" + 
                    "<td>$" + parseFloat( shoppingList[i].getCurrentCost ).toFixed( 2 ) + "/" + parseFloat( shoppingList[i].getCostNeeded ).toFixed( 2 ) + "</td>" + 
                "</tr");
        }
    }
}

/*
Takes a row and re generates the correct table value
*/
function generateRow( shoppingList, i ){

    return ("<td>" + shoppingList[i].name + "</td>" + 
                    "<td>" + shoppingList[i].currentQuatity + " / " + shoppingList[i].neededQuatity + "</td>" + 
                    "<td>$" + parseFloat( shoppingList[i].getCurrentCost ).toFixed( 2 ) + "/" + parseFloat( shoppingList[i].getCostNeeded ).toFixed( 2 ) + "</td>");
                
}


/*
returns a string of the total that is currently in the cart and
total to be purchased
*/
function getTotal( shoppingList ) {
    
    let i = 0;
    let subtotal = 0, total = 0;

    for( i = 0; i < shoppingList.length ; i++ ){

        subtotal += shoppingList[i].getCurrentCost;
        total += shoppingList[i].getCostNeeded;
    }

    subtotal = parseFloat( subtotal ).toFixed( 2 ); 
    total = parseFloat( total ).toFixed( 2 ); 

    return ('$' + subtotal + " / " + '$' + total );

}

