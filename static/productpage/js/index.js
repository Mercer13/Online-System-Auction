$(document).ready(function(){
var data,ownerName;
var users,currentUser;
//get all user information 
function getusers()
{
$.ajax({url: "rest/users/?format=json", success: function(result){
    users= result;
    console.log(result);
    
    

 },complete:function()
 {
    //do nothing 
 },
 
 });
} 
    
   
//get products  
function getproductinfo()
{
    $.ajax({url: "/product/rest/products/?id=&itemname=&owner=&status=0&buyer=", success: function(result){
        data= result;
        console.log(result);
        $('#users').html('');
        

    },complete:function()
    {
        refresh();
        printResult();
        if(data.length==0)
        {
            $("#products-list").html("")
            $("#products-list").append('<h1>There are currently no products</h1>');
        }
    },
    
    });

}

//function to change owner from url to name
function refresh()
{
   for(var key in data)
   {
        for(var x in users)
        {
            if(data[key].owner == users[x].url)
            {
                data[key].owner = users[x].username
            }
        } 
   }
    
}
// Append products to html
function printResult()
{

    $('#product').html('');
    for(var key in data)
    {
          

          $("#products-list").append('<div class="col-xs-6 col-lg-4" style=""><div class="card " style="width:250x;"><img class="card-img-top " style=" object-fit: cover;width:250px;margin:0 auto;" src="'+data[key].image+'" alt="Card image"><div class="card-body"><h4 class="card-title">'+data[key].itemname +'</h4><p class="card-text">'+data[key].description +'</p><a href ="'+data[key].id+'/'+'">GO BITCH!</a></div></div></div>');
    }
}
    getusers();
    getproductinfo();
    // setInterval(getproductinfo, 5000);
    // setInterval(getusers,15000);
});