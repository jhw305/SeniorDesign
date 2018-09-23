var script = document.createElement('script');
script.src = 'jquery.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);


class storeLocation {

    constructor(name, img, distance){
        this.name = name;
        this.img = img;
        this.distance = distance;
    }

}

let storeLocationList = [];

storeLocationList.push(new storeLocation("Ralphs", "../img/Ralphs.jpg", 2.1));
storeLocationList.push(new storeLocation("Albertsons", "../img/Albertsons.jpg", 4.20));
storeLocationList.push(new storeLocation("Costco", "../img/Costco.jpg", 6.9));
storeLocationList.push(new storeLocation("Ralphs", "../img/Ralphs.jpg", 2.1));
storeLocationList.push(new storeLocation("Albertsons", "../img/Albertsons.jpg", 4.20));
storeLocationList.push(new storeLocation("Costco", "../img/Costco.jpg", 6.9));
storeLocationList.push(new storeLocation("Ralphs", "../img/Ralphs.jpg", 2.1));
storeLocationList.push(new storeLocation("Albertsons", "../img/Albertsons.jpg", 4.20));
storeLocationList.push(new storeLocation("Costco", "../img/Costco.jpg", 6.9));
storeLocationList.push(new storeLocation("Ralphs", "../img/Ralphs.jpg", 2.1));
storeLocationList.push(new storeLocation("Albertsons", "../img/Albertsons.jpg", 4.20));
storeLocationList.push(new storeLocation("Costco", "../img/Costco.jpg", 6.9));
storeLocationList.push(new storeLocation("Ralphs", "../img/Ralphs.jpg", 2.1));
storeLocationList.push(new storeLocation("Albertsons", "../img/Albertsons.jpg", 4.20));
storeLocationList.push(new storeLocation("Costco", "../img/Costco.jpg", 6.9));
storeLocationList.push(new storeLocation("Ralphs", "../img/Ralphs.jpg", 2.1));
storeLocationList.push(new storeLocation("Albertsons", "../img/Albertsons.jpg", 4.20));
storeLocationList.push(new storeLocation("Costco", "../img/Costco.jpg", 6.9));


generateTable(storeLocationList);

let testing = false;

$( "tbody tr" ).click( function ( e ) {
    if( $( this ).hasClass( 'notChanged' ) ){
        $( this ).toggleClass( "selected notChanged" );
        $( this ).html(
            "<td id='maps'> <img class='icon' id='gog' src='../img/googleMaps.png'></td>" + 
            "<td id='shoppingList'><img class='icon' id='shop' src='../img/shoppingList.png'></td>"
            );
    }
    else{
        
        let shoppingList = false;
        let gMaps = false;
        let row = this;

        if( ( $(e.target).get(0).id ) == 'maps' || $(e.target).get(0).id == 'gog' ){
            console.log($(e.target).get(0));
            gMaps = true;
        }
        else if( ( $(e.target).get(0).id ) == 'shoppingList' || $(e.target).get(0).id == 'shop'){
            shoppingList = true;
        }
        
        if(gMaps){
            window.location.href ="https://www.google.com/maps/dir/University+of+California+Irvine,+Irvine,+CA+92697/Subway+Restaurants,+Dupont+Drive,+Irvine,+CA/@33.6568265,-117.8750852,14z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x80dcde0e2592bf91:0x79fbc5d0b6dab7ec!2m2!1d-117.8442962!2d33.6404952!1m5!1m1!1s0x80dcde601839f29b:0x9e955d830b092c02!2m2!1d-117.8519685!2d33.669089";
            return
        
        }

        if(shoppingList){
            window.location.href ="shoppinglist.html";
            return
        
        }
    }
});



function generateTable( storeLocationList ){

    let tableValue = "";

    if ( storeLocationList.length != 0 ){
        for(let i = 0; i < storeLocationList.length; i++){
            $('#storeLocationList > tbody:last-child').append(
                "<tr id='" + storeLocationList[i].name + "' class='notChanged'>" + 
                    "<td>" + "<img class='resize' src = '" + storeLocationList[i].img + "'>" + "</td>" + 
                    "<td>" + storeLocationList[i].name  + ' - ' + storeLocationList[i].distance + "mi" +"</td>" + 
                "</tr");
        }
    }
}

function generateRow( storeLocationList, i ){
    return ("<td>" + "<img class='resize' src = '" + storeLocationList[i].img + "'>" + "</td>" + 
                    "<td>" + storeLocationList[i].name + ' - ' + storeLocationList[i].distance + "mi" + "</td>");
                
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
