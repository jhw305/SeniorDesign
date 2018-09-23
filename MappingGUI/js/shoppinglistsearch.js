var script = document.createElement('script');
script.src = 'jquery.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);


class listItem{
    constructor(name, currentQuantity, neededQuantity, price){
        this.name = name;
        this.currentQuantity = currentQuantity;
        this.neededQuantity = neededQuantity;
        this.price = price;
    }

    get getCostNeeded( ) {
        return this.neededQuantity * this.price;
    }
    
    get getCurrentCost( ){
        return this.currentQuantity * this.price;
    }
}

let storeInventory = [];

storeInventory.push( new listItem( "Apples", 0, 1, 3.26 ) );
storeInventory.push( new listItem( "Oranges", 0, 1, .87) );
storeInventory.push( new listItem( "Bananas", 0, 1, 4.51 ) );
storeInventory.push( new listItem( "Pears", 0, 1, 2.29) );
storeInventory.push( new listItem( "Grapes", 0, 1, 4.75 ) );

generateTable( storeInventory );

$( '#totalMoneySpent' ).html( getTotal( storeInventory ) );

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
                if( newValue < 1 || isNaN( newValue ) ){
                    alert("Please enter a valid quantity.");
                }
                else{
                    storeInventory[row].neededQuantity = newValue;
                    $( '#totalMoneySpent' ).html( getTotal( storeInventory ) );
                }
            }
            else{
                storeInventory[row].neededQuantity = '1';
                $( '#totalMoneySpent' ).html( getTotal( storeInventory ) );
            }
            change = true;
        }
        
        if(change){
            $( this ).toggleClass( "selected notChanged" );
            $( this ).html( generateRow( storeInventory, this.closest('tr').rowIndex ) );
        }
    }
});


/*
Takes the current shopping list and generates the table upon entering the page.
If the table is empty, an empty string will be returned
*/
function generateTable( storeInventory ){

    let tableValue = "";

    if ( storeInventory.length != 0 ){
        for(let i = 0; i < storeInventory.length; i++){
            $('#storeInventory > tbody:last-child').append(
                "<tr id='" + storeInventory[i].name + "' class='notChanged'>" + 
                    "<td>" + storeInventory[i].name + "</td>" + 
                    "<td>" + storeInventory[i].neededQuantity + "</td>" + 
                    "<td>$" + storeInventory[i].getCostNeeded + "</td>" + 
                "</tr");
        }
    }
}

/*
Takes a row and re generates the correct table value
*/
function generateRow( storeInventory, i ){

    return ("<td>" + storeInventory[i].name + "</td>" + 
                    "<td>" + storeInventory[i].neededQuantity + "</td>" + 
                    "<td>$" + parseFloat( storeInventory[i].getCostNeeded ).toFixed( 2 ) + "</td>");
                
}

/*
returns a string of the total that is currently in the cart and
total to be purchased
*/
function getTotal( storeInventory ) {
    
    let i = 0;
    let total = 0;

    for( i = 0; i < storeInventory.length ; i++ ){
        total += storeInventory[i].getCostNeeded;
    }

    total = parseFloat( total ).toFixed( 2 ); 

    return ('Total: $' + total );

}

// filters list with user input to search bar
$( "#textinput" ).on("keyup", function() {
    var value = $(this).val().toUpperCase();
    $( "tbody tr" ).each(function() {
        if($(this).attr("id").toUpperCase().search(value) > -1) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
});
